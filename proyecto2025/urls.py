"""
URL configuration for proyecto2025 project.
... (el resto de los comentarios) ...
"""
from django.contrib import admin
from django.urls import path, include
from users import urls

# ¡Añade VistaProtegida a esta línea!
from users.views import welcome, about, VistaProtegida 

from django.contrib.auth.views import LoginView, LogoutView

# --- IMPORTS PARA JWT ---
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# ------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- RUTAS DE JWT ---
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # ¡Añade esta nueva ruta protegida!
    path('api/protegida/', VistaProtegida.as_view(), name='vista_protegida'),
    # ------------------

    # --- Tus rutas existentes ---
    path('users/', include(urls)),
    path('',
         LoginView.as_view(template_name="base.html"),
         name="login"
         ),
    path('logout/',
         LogoutView.as_view(),
         name="logout"
         ),
    path('about/', about, name="about" ),
]
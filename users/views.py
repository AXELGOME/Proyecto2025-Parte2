from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from users.models import Product
from django.urls import reverse_lazy
from .forms import ProductForm


# Create your views here.

def test_view(request):
    return HttpResponse("<h1>¡Hola! Esta es una vista de prueba.</h1>")


def home(request):
    user = request.user
    context = {
        'title': 'Proyecto 2025',
        'message': 'Bienvenido al proyecto de prueba'
    }
    return render(request, 'home.html', context)

def welcome(request):
    return render(request, "base.html")

def about(request):
    context ={
        "products": Product.objects.filter(
            is_active=True
        )
    }
    return render(
        request,
        "about.html",
        context=context
    )

def create_product(request):
    if request.method == "GET":
        return render(
            request,
            "product/create.html",
        )
    else:
        product = Product()
        product.name = request.POST['name_product']
        product.stock = request.POST['stock_product']
        product.save()
        return redirect(reverse_lazy("about"))


def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("about")  
    else:
        form = ProductForm(instance=product)
    return render(request, "product/update.html", {"form": form})



def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        return redirect("about")
    return render(request, "product/delete.html", {"product": product})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class VistaProtegida(APIView):
    permission_classes = [IsAuthenticated] # ¡Esta línea es la clave!

    def get(self, request):
        return Response({
            'message': '¡Acceso autorizado!',
            'user': request.user.username,
            'email': request.user.email
        })
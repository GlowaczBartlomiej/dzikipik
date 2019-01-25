from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.checks import messages
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.shortcuts import render
from django.views import View


from main.models import Post, Image


class IndexView(View):

    def get(self, request):
        return render(request, "index.html")


class BlogView(View):

    def get(self, request):
        posts = Post.objects.all()
        return render(request, "blog.html", {"posts": posts})


class GalleryView(View):

    def get(self, request):
        images = Image.objects.all()
        return render(request, "gallery.html", {"images": images})


class PricingView(View):

    def get(self, request):
        return render(request, "pricing.html")


class ContactView(View):

    def get(self, request):
        return render(request, "contact.html")


class LoginView(View):

    def post(self, request):
        email = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "index.html")


class RegisterView(View):

    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("psw")
        password2 = request.POST.get("psw-repeat")
        info = "Niepoprawny adres email i/lub hasło"
        if password == password2:
            try:
                new_user = User.objects.create_user(username=email, email=email, password=password)
                new_user.save()
            except IntegrityError:
                info = "Użytkownik już istnieje"
                return render(request, "register.html", {"info": info})
            return redirect("/")
        return render(request, "register.html", {"info": info})


class SessionView(View):

    def get(self, request):
        return render(request, "session.html")


class PostView(View):

    def get(self, request, id):
        post = Post.objects.get(id=id)
        return render(request, "post.html", {"post":post})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("/")

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views import View


from main.models import Post


class IndexView(View):

    def get(self, request):
        return render(request, "index.html")


class BlogView(View):

    def get(self, request):
        posts = Post.objects.all()
        return render(request, "blog.html", {"posts": posts})


class GalleryView(View):

    def get(self, request):
        return render(request, "gallery.html")


class PricingView(View):

    def get(self, request):
        return render(request, "pricing.html")


class ContactView(View):

    def get(self, request):
        return render(request, "contact.html")


class LoginView(View):

    def post(self, request):
        email = request.POST.get("defaultForm-email")
        password = request.POST.get("defaultForm-pass")
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
        if password == password2:
            new_user = User.objects.create_user(username=email, email=email, password=password)
            new_user.save()
            return render(request, "register.html")


class SessionView(View):

    def get(self, request):
        return render(request, "session.html")

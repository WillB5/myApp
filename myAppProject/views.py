from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from myAppProject.models import Upload, User
from django.shortcuts import render, redirect

# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        if User.objects.filter(username=request.POST['username']).exists():
            user = User.objects.get(username=request.POST['username'])
            if user.password == request.POST['password']:
                request.session["username"] = user.username
                return redirect('/home/')
            else:
                return render(request, 'login.html', {"message": "Invalid Login"})
        else:
            return render(request, 'login.html', {"message": "Invalid Login"})


class Register(View):
    def get(self, request):
        return render(request, "register.html", {})

    def post(self, request):
        userName = request.POST['username']
        passWord = request.POST['password']
        if User.objects.filter(username=userName).exists():
            return render(request, 'register.html', {"message": "Username already exists"})
        else:
            User.objects.create(username=userName, password=passWord)
            request.session["username"] = userName
            return redirect('/')


class makePost(CreateView):
    model = Upload
    template_name = 'post.html'
    fields = 'owner', 'image', 'desc'


class Home(View):
    def get(self, request):
        Owner = request.session.get('username')
        libraryList = list(Upload.objects.all())
        return render(request, "home.html", {'library': libraryList})

class Profile(View):
    def get(self, request):
        Owner = request.session.get('username')
        profileName = Owner
        libraryList = list(Upload.objects.filter(owner=User.objects.get(username=Owner)))
        return render(request, 'profile.html', {'library': libraryList, 'profile': profileName})


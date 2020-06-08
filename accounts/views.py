from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import CreateView,View,TemplateView
from accounts.forms import RegisterForm,UserForm,LoginForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from accounts.models import User
# Create your views here.


class Homepage(TemplateView):
    template_name = 'accounts/index.html'

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.admin = True
        user.is_active = True
        user.is_superuser = True
        user.staff= True
        user.status = 'V'
        user.save()
        return redirect('admin/login/?next=/admin/')

class RequestView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/request.html'
    success_url = 'login/'
    

class LoginView(FormView):
    def get(self,request):
        form = LoginForm()
        return render(request, 'accounts/login.html', context = {'form':form})

    def post(self,request):
        username = request.POST['email']
        password = request.POST['password']
        form = LoginForm(request.POST)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('login/')
=======

# Create your views here.


def index(request):
    return render(request, 'accounts/index.html')
>>>>>>> de971c457c57b32399128ec0900d27bd168bb331

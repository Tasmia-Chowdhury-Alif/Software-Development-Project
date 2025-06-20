from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

# Create your views here.
class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        # in logout view the request Must be Post
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('login')

class UserProfileUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance= request.user)
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request):
        form = UserUpdateForm(data= request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
        return render(request, self.template_name, {'form' : form})
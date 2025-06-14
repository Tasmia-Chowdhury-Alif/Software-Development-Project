from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, DepositForm
from django.contrib.auth import login
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse_lazy


def send_email(user, amount, subject, message_template):
    message = render_to_string(message_template, context={
        'user' : user, 
        'amount' : amount,
    })
    email = EmailMultiAlternatives(subject, to=[user.email])
    email.attach_alternative(message, "text/html")
    email.send()


# Create your views here.
class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('profile')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'files': self.request.FILES
        })
        return kwargs

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        messages.success(self.request, f"{user.username} Registered Successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "Registration Form"
        return context
    
    

class UserLoginView(LoginView):
    template_name = 'accounts/registration.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["title"] = "Login Form"
        return context
    

class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')


def profile(request):
    return render(request, 'accounts/profile.html')


class DepositView(FormView):
    form_class = DepositForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = self.request.user
        profile = user.profile
        amount = form.cleaned_data.get('amount')

        
        profile.balance += amount
        profile.save(
            update_fields = ['balance']
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )

        send_email(user, amount, "Deposit Message", 'accounts/deposit_email.html')

        return super().form_valid(form)
    
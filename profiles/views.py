from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView
# Create your views here.

from .forms import RegisterForm
from diseases.models import Item
from patients.models import PatientsInfo

User = get_user_model()

def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        qs = Profile.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            profile = qs.first()
            if not profile.actibated:
                user_=profile.user
                user_.is_activate = True
                user_.save()
                profile.activated=True
                profile.activation_key=None
                profile.save()
                return  redirect("/login")
    return redirect("/login")



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect("/logout")
        return super(RegisterView,self).dispatch(*args, **kwargs)


class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)
    
    def get_context_data(self,*args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        user =context['user']
        query = self.request.GET.get('q')
        items_exists = Item.objects.filter(user=user).exists()
        qs = PatientsInfo.objects.filter(owner=user)
        if query:
            qs = qs.search(query)
        # if items_exists and qs.exists():
        if items_exists or qs.exists():
            context['information'] = qs
        return context
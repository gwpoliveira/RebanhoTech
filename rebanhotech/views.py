from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from cadastro_animais.models import Animal
from genealogia.models import Genealogia
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['cadastro_animais'] = Animal.objects.all()[:10]
            context['genealogia'] = Genealogia.objects.all()[:10]
        except Animal.DoesNotExist:
            context['cadastro_animais'] = None
        except Genealogia.DoesNotExist:
            context['genealogia'] = None

        return context
    
class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.object)
        return response
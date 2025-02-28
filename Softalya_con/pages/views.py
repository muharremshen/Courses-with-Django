from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course
from django.views.generic.edit import FormView
from . forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class IndexView (TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['total_course']= Course.objects.filter(available=True).count()
        return context
    
#def index(request):
#    return render(request, 'index.html')


class AboutView (TemplateView):
    template_name = 'about.html'

class ContactView (SuccessMessageMixin,FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message= "We received your request"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

#def about(request):
#    return render(request, 'about.html')
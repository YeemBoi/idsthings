from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic

from .models import User, Year, Entry, Comment

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'tracken/home.html'

class AboutView(generic.TemplateView):
    template_name = 'tracken/about.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('tracken:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(redirect_field_name='tracken:progress')
def progressTracker(request):
    year = get_object_or_404(Year, student=get_user(request))
    context = {
        'entryList': year.entry_set.order_by('work_date'),
        'year': year.id,
    }
    return render(request, 'tracken/progress.html', context)

class NewEntryView(generic.CreateView, LoginRequiredMixin):
    model = Entry
    template_name = 'tracken/new-entry.html'
    fields = ['hours', 'goal', 'accomplishments']
    def form_valid(self, form):
        year = get_object_or_404(Year, pk=self.kwargs['year'])
        form.instance.year = year
        return super(NewEntryView, self).form_valid(form)

class EntryView(generic.DetailView, LoginRequiredMixin):
    model = Entry
    template_name = 'tracken/entry.html'

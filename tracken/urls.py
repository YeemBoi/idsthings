from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'tracken'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('progress/', views.progressTracker, name='progress'),
    path('new-entry/<int:year>/', views.NewEntryView.as_view(), name='new-entry'),
    path('entry/<int:pk>/', views.EntryView.as_view(), name='entry'),
    path('edit-goal/<int:pk>', views.EditGoalView.as_view(), name='edit-goal')
    #path('login/', auth_views.LoginView.as_view(template_name='tracken/login.html'), name='login'),
    #path('password-reset', auth_views.PasswordResetView.as_view(), name='password_reset')
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
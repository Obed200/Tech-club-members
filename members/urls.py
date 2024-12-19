from django.urls import path
from . import views

# gpt suggestions
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),

    path('members/login_user/', views.login_user, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    
    path('members/logout/', views.logout_user, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Optional: Sign-Up Page
    path('signup/', views.signup, name='signup'),
]
# gpt suggestions
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

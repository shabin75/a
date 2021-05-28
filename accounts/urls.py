from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('', views.indexView, name="index"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    # path('login/',LoginView.as_view(),name="login_url"),
    # path('register/', views.registerView, name="register_url"),
    # path('home/',home.as_view(next_page='dashboard'),name="home_url"),
    path('dashboard/home/', views.home, name="home_url"),
    # path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout"),
    path('test/', views.test, name='test'),
    path('password_reset', PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('login/', views.login_view, name='login_url'),
    path('logout', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register_url')

]

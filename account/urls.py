from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    path('login/', views.AccountLogin.as_view(), name='login'),
    path('logout/', views.AccountLogout.as_view(), name='logout'),
    path('password_reset/', views.AccountPasswordReset.as_view(), name='pwdreset'),
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/',
        views.AccountPasswordConfirm.as_view(), name='password_reset_confirm'
        ),
    path('password_reset/password_reset_email_confirm/',
        TemplateView.as_view(template_name="account/user/reset_status.html"), name='password_reset_done'
        ),
    path('password_reset_complete/',
        TemplateView.as_view(template_name="account/user/reset_status.html"), name="password_reset_complete"
        ),
    # User dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.edit_details, name='edit_details'),
    path('profile/delete_user/', views.delete_user, name='delete_user'),
    path('profile/delete_confirm/',
        TemplateView.as_view(template_name="account/user/delete_confirm.html"), name='delete_confirmation'
        ),
]

from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.account_register, name="register"),
    path("activate/<slug:uidb64>/<slug:token>/", views.account_activate, name="activate"),
    path("login/", views.AccountLogin.as_view(), name="login"),
    path("logout/", views.AccountLogout.as_view(), name="logout"),
    path("password_reset/", views.AccountPasswordReset.as_view(), name="pwdreset"),
    path(
        "password_reset_confirm/<slug:uidb64>/<slug:token>/",
        views.AccountPasswordConfirm.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/password_reset_email_confirm/",
        TemplateView.as_view(template_name="account/password_reset/reset_status.html"),
        name="password_reset_done",
    ),
    path(
        "password_reset_complete/",
        TemplateView.as_view(template_name="account/password_reset/reset_status.html"),
        name="password_reset_complete",
    ),
    # User dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/edit/", views.edit_details, name="edit_details"),
    path("profile/delete_user/", views.delete_user, name="delete_user"),
    path(
        "profile/delete_confirm/",
        TemplateView.as_view(template_name="account/dashboard/delete_confirm.html"),
        name="delete_confirmation",
    ),
    path("addresses/", views.view_address, name="addresses"),
    path("add_address/", views.add_address, name="add_address"),
    path("addresses/edit/<slug:id>/", views.edit_address, name="edit_address"),
    path("addresses/delete/<slug:id>/", views.delete_address, name="delete_address"),
    path("addresses/set_default/<slug:id>/", views.set_default, name="set_default"),
    # Wishlist
    path("wishlist/", views.wishlist, name="wishlist"),
    path("wishlist/add_to_wishlist/<int:id>/", views.add_to_wishlist, name="user_wishlist"),
]

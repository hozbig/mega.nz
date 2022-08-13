from django.contrib.auth import views
from django.urls import path

from .forms import UserLoginForm
from .views import (get_activation_token, register_new_user,
                    send_activation_email)

app_name = "account"
urlpatterns = [
	path("register/", register_new_user, name="register"),

	path("send-activation-email/<str:email>/", send_activation_email, name="send"),
	path("recive-activation-token/<uidb64>/<token>/", get_activation_token, name="get_token"),

	path('login/', views.LoginView.as_view(
		authentication_form = UserLoginForm
	), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),

	# path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
	# path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

	# path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
	# path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	# path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	# path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

from django.contrib.auth.views import PasswordResetView
from django.urls import path, include


urlpatterns = [

    path('password_reset/',
         PasswordResetView.as_view(html_email_template_name='emails/password_reset_email.html'),
         name='password_reset'),
    path('', include('django.contrib.auth.urls'))

]

from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$',
        auth_views.login,
        name='login'),

    url(r'^logout/$',
        auth_views.logout,
        {'next_page': '/'},
        name='logout'),

    url(r'^password_change/$',
        auth_views.password_change,
        name='password_change'),

    url(r'^password_change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),

    url(r'^password_reset/$',
        auth_views.password_reset,
        {'html_email_template_name': 'emails/password_reset_email.html'},
        name='admin_password_reset'),

    url(r'^password_reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),

    url(r'^reset/(?P<token>.+)-(?P<uidb64>[0-9A-Za-z]+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),

    url(r'^reset/done/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
]

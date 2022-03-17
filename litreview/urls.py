"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView
#from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import authentication.views
import reviewsapp.views

# path('logout/', LogoutView.as_view(), name='logout'),

# path('password/change/', PasswordChangeView.as_view(
#         template_name='authentication/password_change_form.html'),
#     name='password_change'),
# path('password/change/done/', PasswordChangeDoneView.as_view(
#         template_name='authentication/password_change_done.html'),
#     name='password_change_done'),

# path('password/reset/', PasswordResetView.as_view(),
#     name='password_reset'),
# path('password/reset/confirm/', PasswordResetConfirmView.as_view(),
#     name='password_reset_confirm'),
# path('password/reset/complete/', PasswordResetCompleteView.as_view(),
#     name='password_reset_complete'),
# path('password/reset/done', PasswordResetDoneView.as_view(),
#     name='password_reset_done'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('logout/', authentication.views.UserLogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),

    
    path('home/', reviewsapp.views.home, name='home'),

    path('ticket/create/', reviewsapp.views.ticket_create, name='ticket-create'),
    path('ticket/<int:ticket_id>/delete/', reviewsapp.views.ticket_delete, name='ticket-delete'),
    path('ticket/<int:ticket_id>/update/', reviewsapp.views.ticket_update, name='ticket-update'),

    path('review/create/', reviewsapp.views.review_create, name='review-create'),
    path('review/ticket-<int:ticket_id>/create/', reviewsapp.views.review_create, name='review-create'),
    path('review/<int:review_id>/delete/', reviewsapp.views.review_delete, name='review-delete'),
    path('review/<int:review_id>/update/', reviewsapp.views.review_update, name='review-update'),

    path('follow/', reviewsapp.views.follow, name='follow'),
    path('follow/<int:follow_user_id>/delete/', reviewsapp.views.follow_delete, name='follow-delete'),

    path('post/', reviewsapp.views.post, name='post'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
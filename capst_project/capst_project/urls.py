from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from lostfound_app import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from lostfound_app import views as viewOperations

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^home/$', views.post, name='post'),
    re_path(r'^uploaded/$', views.upload_image_view, name='upload_image_view'),
    re_path(r'^board/$', views.board_images, name='board_images'),
    re_path(r'^board/search/$', views.search_document, name='search_document'),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # re_path(r'^claim/$', views.image_details, name='image_details'),
    path('image_details/<int:id>/', views.image_details, name='image_details'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    
    re_path(r'^reset/$', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ), name='password_reset'),
    
    re_path(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),
            name='password_reset_done'),
    
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    #         name='password_reset_confirm'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    re_path(r'^reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
            name='password_reset_complete'),
    
    re_path(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    re_path(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
    
    path('delete_image/<int:id>/', viewOperations.delete_image, name='delete_image'),
    path('update_image/<int:id>/', viewOperations.update_image, name='update_image')
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
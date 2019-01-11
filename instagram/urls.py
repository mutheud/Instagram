from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostLikeToggle
else:
#    DATABASES = {
#        'default': dj_database_url.config(
#            default=config('DATABASE_URL')
#        )
#    }
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

urlpatterns=[
   url(r'^$',views.welcome,name = 'welcome'),
   url(r'^profile',views.new_profile,name = 'new_profile'),
   url(r'^profile/(\d+)',views.profile,name ='profile'),
   url(r'^search/', views.search_results, name='search_results'),
   url(r'^comment/(?P<image_id>\d+)', views.one_image, name='comment'),
   url(r'^(?P<image_id>[\w-]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),
   
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
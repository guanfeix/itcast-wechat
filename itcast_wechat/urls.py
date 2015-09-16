"""itcast_wechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^wechat/', 'wechat.views.index', name = 'index'),
	url(r'^create_menu/', 'wechat.views.create_menu', name = 'create_menu'),
	url(r'^user_info/', 'wechat.views.user_info', name = 'user_info'),
	url(r'^register/', 'wechat.views.register', name = 'register'),
	url(r'^academyInfo/(?P<academyinfo_name_slug>[\w\-]+)/$', 'wechat.views.academyInfo', name = 'academyInfo'),
	url(r'^student/(?P<student_name_slug>[\w\-]+)/$', 'wechat.views.student', name = "student"),
	url(r'^courseList/(?P<course_name_slug>[\w\-]+)/$', 'wechat.views.courseList', name = "courseList"),
	url(r'^topic/', 'wechat.views.topic', name = "topic"),
	url(r'^help/', 'wechat.views.help', name = "help"),
	url(r'^about/', 'wechat.views.about', name = "about"),
	
	url(r'^userPost/', 'wechat.views.userPost', name = 'userPost'),
	url(r'^ajaxTest/', 'wechat.views.ajaxTest', name = 'ajaxTest'),
	
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
	url(r'^static/(?P<path>.*)$','django.views.static.serve',{ 'document_root': settings.STATIC_PATH }),
]
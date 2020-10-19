"""fproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url
from fApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.PostListView.as_view(),name='list'),
    path('<int:pk>/detail',views.Post_detail_view,name='detail'),
    #path('<int:pk>/detail/',views.PostDetailView.as_view(),name='detail'),
    #url(r'^comment/$',views.Commentview,name='add_comment'),
    path('like/<int:pk>',views.ListView ,name='like_post'),
    #url(r'^(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='detail'),
    #path('<int:pk>/comment/',views.AddCommentview.as_view(),name='add_comment'),
     path('oauth/', include('social_django.urls', namespace='social')), ## from 'social_media_auth)
]
#(?P<pk>[0-9]+)/
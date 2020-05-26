"""typeieda URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from blog.views import (IndexView, CategoryView, TagView,
                        PostDetailView, SearchView, post_detail, AuthorView
                        )

from config.views import (LinkListView,)

from comment.views import CommentView

from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap

from config.views import links
from .customer_site import custom_site
from blog.apis import post_list, PostList

from rest_framework.routers import DefaultRouter
from blog.apis import PostViewSet, CategoryViewSet

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas.coreapi import AutoSchema

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url('^tag/(?P<tag_id>\d+).html$', TagView.as_view(),name='tag-list'),
    #url(r'^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
 #   url(r'^links/$', links, name='links'),
    url(r'super_admin/', admin.site.urls, name='super-admin'),
    url(r'admin/', custom_site.urls, name='admin'),
    url(r'about/', TemplateView.as_view(template_name='about.html')),
    url(r'^search/$', SearchView.as_view() , name='search'),
    url(r'^author/(?P<owner_id>\d+)$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts':PostSitemap}}),
    #url(r'^api/post/', PostList.as_view(), name='post-list'),
    url(r'^api/post/(?P<post_id>\d+)', post_list, name='post-list'),
 #   url(r'^api/(?P<post_id>\d+)', include(router.urls)),
#    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),


]

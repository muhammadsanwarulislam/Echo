"""echo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from authentication import views as authentication_views
from core import views as core_views
from search import views as search_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'core/cover.html'},name='login'),
    url(r'^signup/$', authentication_views.signup, name='signup'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^feeds/', include('feeds.urls')),
    url(r'^settings/', include('core.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^messages/', include('messenger.urls')),
    url(r'^notifications/', include('activities.urls')),
    url(r'^search/', search_views.search, name='search'),
    url(r'^network/', search_views.search, name='network'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# from django.conf import settings
# from django.conf.urls import include
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView

# from authentication import views as authentication_views
# from core import views as core_views
# from search import views as search_views

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('', core_views.home, name='home'),
#     path('login', auth_views.login,
#          {'template_name': 'core/cover.html'}, name='login'),
#     path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),
#     path('signup/', authentication_views.signup, name='signup'),

#     path('feeds/', include('bootcamp.feeds.urls')),
#     path('settings/', include('bootcamp.core.urls')),
#     path('articles/', include('bootcamp.articles.urls')),
#     path('messages/', include('bootcamp.messenger.urls')),
#     path('questions/', include('bootcamp.questions.urls')),
#     path('notifications/', include('bootcamp.activities.urls')),

#     path('search/', search_views.search, name='search'),
#     path('network/', core_views.network, name='network'),

#     # path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),

#     path('<str:username>/', core_views.profile, name='profile'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

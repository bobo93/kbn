from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    #oferty
    url(r'^offer/details/(?P<pk>[0-9]+)/$', views.offer_details, name='odder_details'),
    url(r'^wyszukaj/$', views.wyszukaj, name='wyszukaj'),
    url(r'^wyniki/$', views.wyniki, name='wyniki'),

#koszyk
    url(r'^bucket_add/(?P<pk>[0-9]+)/(?P<un>[0-9a-zA-Z]+)/$', views.bucket_add, name='bucket_add'),
    url(r'^bucket/$', views.bucket, name='bucket'),
    url(r'^bucket/(?P<un>[0-9a-zA-Z]+)/$', views.bucket, name='bucket1'),
    url(r'^bucket_delete/(?P<pk>[0-9]+)/(?P<un>[0-9a-zA-Z]+)/$', views.bucket_delete, name='bucket_delete'),
#logowianie i rejestracja
     url(r'^accounts/login/$',  views.login),
    url(r'^accounts/auth$',  views.auth_view),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/invalid/$', views.invalid_login),
     url(r'^accounts/register/$',views.register_user),
    url(r'^accounts/register_success/$', views.register_success),


#formularz

url(r'^form/new/$', views.form_new, name='form_new'),


]

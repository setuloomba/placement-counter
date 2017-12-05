from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'tpcprocess'


urlpatterns = [

    # localhost/
    url(r'^$', views.login_user, name='login'),

    # /logout/
    url(r'^logout/$', views.logout_user, name='logout_user'),

    # /key/register_stu/
    url(r'^(?P<key>[0-1])/register_stu$', views.register_stu, name='register_stu'),

    # /submit_eligi/
    url(r'^submit_eligi/$', views.submit_eligi, name='submit_eligi'),

    # /comp_list/
    url(r'^comp_list/$', views.comp_list, name='comp_list'),

    # /apply/id
    url(r'^apply/(?P<company_id>[0-9]+)/$', views.apply, name='apply'),

    # /candi_list/
    url(r'^candi_list/$', views.candi_list, name='candi_list'),

    # /filter_list/
    url(r'^filter_candi/$', views.filter_candi, name='filter_candi'),

]

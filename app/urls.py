from django.conf.urls import url
from . import views
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    url(r'^api-auth-token/', rest_framework_views.obtain_auth_token),
    url(r'^v1/reimbursement/$', views.reimbursement_list, name='reimbursement_list'),
    url(r'^v1/reimbursement/(?P<pk>[0-9]+)$', views.reimbursement_detail, name='reimbursement_detail'),
    url(r'^v1/pending/$', views.pending_reimbursement, name='pending_reimbursement'),
]
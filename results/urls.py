from django.conf.urls import url

from . import views

app_name = 'results'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /consequence/5/
    url(r'^(?P<consequence_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /consequence/5/context/
    url(r'^(?P<consequence_id>[0-9]+)/context/$', views.context, name='context'),
    # ex: /results/mitigationindex/
    url(r'mitigationindex', views.mitigationindex, name='mitigationindex'),
    # ex: /consequence/5/mitigation/
    url(r'^(?P<consequence_id>[0-9]+)/mitigation/$', views.mitigation, name='mitigation'),
    # ex: /results/consequencelist/
    url(r'consequencelist', views.consequencelist, name='consequencelist'),
    # ex: /missinginfo/5/missingdetail/
    url(r'^(?P<missinginfo_id>[0-9]+)/missingdetail/$', views.missingdetail, name='missingdetail'),
    # ex: /missinginfo/5/manuallyaccept/
    url(r'^(?P<missinginfo_id>[0-9]+)/manuallyaccept/$', views.manuallyaccept, name='manuallyaccept'),
    # ex: /missinginfo/5/manualcommentsdetail/
    url(r'^(?P<missinginfo_id>[0-9]+)/manualcommentsdetail/$', views.manualcommentsdetail, name='manualcommentsdetail'),
    # ex: /missinginfo/5/addingdata/
    url(r'^(?P<missinginfo_id>[0-9]+)/addingdata/$', views.addingdata, name='addingdata'),
    # ex: /missinginfo/5/manualaddeddetail/
    url(r'^(?P<missinginfo_id>[0-9]+)/manualaddeddetail/$', views.manualaddeddetail, name='manualaddeddetail'),

]

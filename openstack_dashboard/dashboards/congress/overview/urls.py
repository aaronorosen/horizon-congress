from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from openstack_dashboard.dashboards.congress.overview import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^\?tab=overview_tabs_tab$',
        views.IndexView.as_view(), name='overview_tabs'),
)

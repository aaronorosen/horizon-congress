from horizon import views
from openstack_dashboard.dashboards.congress.overview \
    import tabs as congress_tabs


class IndexView(views.APIView):
    # A very simple class-based view...
    tab_group_class = congress_tabs.OverviewTabs
    template_name = 'congress/overview/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context

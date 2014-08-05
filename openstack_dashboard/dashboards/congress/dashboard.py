from django.utils.translation import ugettext_lazy as _

import horizon

class Policy(horizon.PanelGroup):
    slug = "policy"
    name = _("Policy")
    panels = ('overview',)

class Congress(horizon.Dashboard):
    name = _("Congress")
    slug = "congress"
    panels = (Policy,)  # Add your panels here.
    default_panel = 'overview'  # Specify the slug of the dashboard's default panel.


horizon.register(Congress)

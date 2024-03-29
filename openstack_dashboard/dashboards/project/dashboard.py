# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.utils.translation import ugettext_lazy as _

import horizon


class BasePanels(horizon.PanelGroup):
    slug = "compute"
    name = _("Compute")
    panels = ('overview',
              'instances',
              'volumes',
              'images',
              'access_and_security',)


class NetworkPanels(horizon.PanelGroup):
    slug = "network"
    name = _("Network")
    panels = ('network_topology',
              'networks',
              'routers',
              'loadbalancers',
              'firewalls',
              'vpn',)


class ObjectStorePanels(horizon.PanelGroup):
    slug = "object_store"
    name = _("Object Store")
    panels = ('containers',)


class OrchestrationPanels(horizon.PanelGroup):
    name = _("Orchestration")
    slug = "orchestration"
    panels = ('stacks',)


class DatabasePanels(horizon.PanelGroup):
    name = _("Database")
    slug = "database"
    panels = ('databases',
              'database_backups',)


class DataProcessingPanels(horizon.PanelGroup):
    name = _("Data Processing")
    slug = "data_processing"
    panels = ('data_processing.data_plugins',
              'data_processing.data_image_registry',
              'data_processing.nodegroup_templates',
              'data_processing.cluster_templates',
              'data_processing.clusters',
              'data_processing.data_sources',
              'data_processing.job_binaries',
              'data_processing.jobs',
              'data_processing.job_executions', )


class Project(horizon.Dashboard):
    name = _("Project")
    slug = "project"
    panels = (
        BasePanels,
        NetworkPanels,
        ObjectStorePanels,
        OrchestrationPanels,
        DatabasePanels,
        DataProcessingPanels,)
    default_panel = 'overview'
    supports_tenants = True


horizon.register(Project)

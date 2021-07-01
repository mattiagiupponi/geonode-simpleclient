# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2020 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
from django.apps import AppConfig as BaseAppConfig
import os


def run_setup_hooks(*args, **kwargs):
    from geonode.urls import urlpatterns
    from django.conf import settings
    from django.conf.urls import url, include

    LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
    settings.TEMPLATES[0]["DIRS"].insert(0, os.path.join(LOCAL_ROOT, "templates"))

    urlpatterns += [
        url(r'^', include('simpleapp_adapter.simpleapp.api.urls')),
    ]


class AppConfig(BaseAppConfig):

    name = "simpleapp_adapter"
    label = "simpleapp_adapter"

    def ready(self):
        run_setup_hooks()
        super(AppConfig, self).ready()
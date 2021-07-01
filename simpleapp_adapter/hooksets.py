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

from geonode.client.hooksets import BaseHookSet

from django import template

register = template.Library()

class SimpleAppHookset(BaseHookSet):

    # Layers
    def layer_detail_template(self, context=None):
        return 'simpleapp/layer_detail.html'

    def layer_new_template(self, context=None):
        return 'simpleapp/layer_detail.html'

    def layer_view_template(self, context=None):
        return 'simpleapp/layer_detail.html'

    def layer_update_template(self, context=None):
        return 'simpleapp/layer_detail.html'

    def layer_embed_template(self, context=None):
        return 'simpleapp/layer_embed.html'

    def layer_download_template(self, context=None):
        return 'simpleapp/layer_detail.html'

    def layer_style_edit_template(self, context=None):
        return 'simpleapp/layer_style_edit.html'

    # Maps
    def map_detail_template(self, context=None):
        return 'simpleapp/map_detail.html'

    def map_new_template(self, context=None):
        return 'simpleapp/map_new.html'

    def map_view_template(self, context=None):
        return 'simpleapp/map_view.html'

    def map_edit_template(self, context=None):
        return 'simpleapp/map_edit.html'

    def map_embed_template(self, context=None):
        return 'simpleapp/map_embed.html'

    # GeoApps
    def geoapp_list_template(self, context=None):
        return 'simpleapp/app_list.html'

    def geoapp_new_template(self, context=None):
        return 'simpleapp/app_new.html'

    def geoapp_view_template(self, context=None):
        return 'simpleapp/app_view.html'

    def geoapp_edit_template(self, context=None):
        return 'simpleapp/app_edit.html'

    def geoapp_update_template(self, context=None):
        return 'simpleapp/app_update.html'

    def geoapp_embed_template(self, context=None):
        return 'simpleapp/app_embed.html'

    def geoapp_download_template(self, context=None):
        return 'simpleapp/app_download.html'

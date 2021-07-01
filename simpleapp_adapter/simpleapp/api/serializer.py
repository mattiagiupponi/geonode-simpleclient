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
import logging

from geonode.geoapps.api.serializers import GeoAppSerializer

from ..models import SimpleApp

logger = logging.getLogger(__name__)


class SimpleAppSerializer(GeoAppSerializer):

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(SimpleAppSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = SimpleApp
        name = 'simpleapp'
        view_name = 'simpleapp-list'
        fields = (
            'pk', 'uuid', 'app_type',
            'zoom', 'projection', 'center_x', 'center_y',
            'urlsuffix', 'data'
        )

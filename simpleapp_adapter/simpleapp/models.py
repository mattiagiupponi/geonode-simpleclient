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

from django.db import models
from geonode.geoapps.models import GeoApp
from django.conf import settings

# Create your models here.
class SimpleApp(GeoApp):
     
    app_type = models.CharField(
        '%s Type' % settings.GEONODE_APPS_NAME,
        db_column='simpleapp_app_type',
        default='simpleapp',
        max_length=255)


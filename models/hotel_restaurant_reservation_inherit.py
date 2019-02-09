# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services PVT. LTD.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# ---------------------------------------------------------------------------

import time
import datetime
import urllib2
from odoo.exceptions import except_orm, ValidationError
from odoo.tools import misc, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import models, fields, api, _
from odoo import workflow
from decimal import Decimal
import logging
_logger = logging.getLogger(__name__)

class hotel_restaurant_reservation_inherit(models.Model):

	_name = 'hotel.restaurant.reservation'
	_inherit = 'hotel.restaurant.reservation'

	tiempo_mesa = fields.Integer('Duracion (min)', default=30)

	@api.onchange('tiempo_mesa')
	def tiempo_mesa_change(self):
		if self.start_date:
			
		duracion_mesa= datetime.datetime.strptime(self.start_date, DEFAULT_SERVER_DATETIME_FORMAT)
			duracion=self.tiempo_mesa
			self.end_date=duracion_mesa+datetime.timedelta(minutes=duracion)
   		

	@api.onchange('start_date')
	def start_date_change(self):
		if self.tiempo_mesa:
			
			duracion_mesa= datetime.datetime.strptime(self.start_date, DEFAULT_SERVER_DATETIME_FORMAT)
			duracion=self.tiempo_mesa
			self.end_date=duracion_mesa+datetime.timedelta(minutes=duracion)
   		

	
	   
		

hotel_restaurant_reservation_inherit()


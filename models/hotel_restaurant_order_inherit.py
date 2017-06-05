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

class hotel_restaurant_order_inherit(models.Model):

	_name = 'hotel.restaurant.order'

	_inherit = 'hotel.restaurant.order'

	
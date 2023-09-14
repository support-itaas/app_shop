# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import uuid

from itertools import groupby
from datetime import datetime, timedelta
from werkzeug.urls import url_encode

from odoo import api, fields, models, _
from odoo.exceptions import UserError, AccessError
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

from odoo.tools.misc import formatLang

# from odoo.addons import decimal_precision as dp


class SaleOrder_inherit(models.Model):
    _inherit = "sale.order"
    # _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _description = "Quotation"
    _order = 'date_order desc, id desc'


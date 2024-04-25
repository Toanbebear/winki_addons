import json
from datetime import datetime, date, timedelta
import requests
import pytz
from dateutil.relativedelta import relativedelta
from odoo import fields, api, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = 'product.template'


    type_detailed_gym = fields.Selection(
        [('may_tap_pilates', 'Máy tập Pilates'), ('phu_kien', 'Phụ Kiện'), ('gym', 'Máy tập gym'), ('may_chay_bo', 'Máy chạy bộ')], string="Loại sản phẩm",  tracking=True)


import json
import logging
from datetime import date, timedelta, datetime
from itertools import groupby
from lxml import etree
from odoo.tools import float_is_zero, float_compare
from odoo import fields, api, models, _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)

class CtvLead(models.Model):
    _inherit = 'crm.lead'

    check_country = fields.Boolean('check country', compute='_check_country', store=False)

    @api.depends('country_id', 'brand_id')
    def _check_country(self):
        for record in self:
            record.check_country = False
            if record.brand_id.code == 'DA' and record.country_id.code == 'VN':
                record.check_country = True
            else:
                record.check_country = False

class CrmStage(models.Model):
    _inherit = 'crm.stage'
    crm_type_id = fields.Many2many('crm.type', 'stage_type_crm_ref', 'stage', 'type_crm', string='Type crm')
    crm_stage_insight_id = fields.Integer('Insight stage id')

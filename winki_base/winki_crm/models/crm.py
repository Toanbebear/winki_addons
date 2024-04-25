import json
from datetime import datetime, date, timedelta
import requests
import pytz
from dateutil.relativedelta import relativedelta
from odoo import fields, api, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools.translate import _


class CRM(models.Model):
    _inherit = 'crm.lead'

    date = fields.Date('Ngày ghi nhận', tracking=True)
    name = fields.Char('Mã', default='New')
    name_lead = fields.Char('Mã', default='New')
    status_classification = fields.Selection(
        [('follow', 'Follow'), ('potential', 'Tiềm năng'), ('success', 'Thành công'), ('no_success', 'Không thành công'), ('super_potential', 'Siêu tiềm năng')], string="Phân loại", tracking=True)
    # type_setup = fields.Selection(
    #     [('gym_basic', 'Gym gia đình'), ('gym_family', 'Gym gia đình'), ('gym_pilates', 'Winki Pilates'), ('logisstic', 'GetGo Logisstics'), ('sport', 'Sport247')], string="Dự án kinh doanh", tracking=True )
    type_gym = fields.Selection(
        [('gym', "Gym"), ('pilates', 'Pilates')], string='Loại hình', tracking=True)
    exchange_content = fields.Text(string='Nội dung trao đổi')
    evaluate = fields.Char(string='Đánh giá')
    acreage = fields.Float(string='Diện tích')
    career = fields.Char(string='Nghề nghiệp')
    ground = fields.Char(string='Mặt bằng')
    customer_classify = fields.Selection(
        [('hot', 'Nóng'), ('cold', 'Lạnh'), ('warm', 'Ấm')], string="Trạng thái khách hàng",  tracking=True)
    mo_hinh = fields.Selection(
        [('kinh_doanh', 'Kinh Doanh'), ('gia_dinh', 'Gia Đình')], string="Mô hình",  tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            sequence = self.env['ir.sequence'].next_by_code('crm.lead')
            vals['name'] = sequence
        record = super(CRM, self).create(vals)
        return record

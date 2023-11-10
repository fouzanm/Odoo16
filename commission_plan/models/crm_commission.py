# -*- coding: utf-8 -*-
import datetime
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Commission(models.Model):
    """This is used to set commission  and its type."""
    _name = 'crm.commission'
    _description = 'CRM Commission'

    name = fields.Char(string="Commission Plan")
    active = fields.Boolean(copy=False, help="to set plan is active or not.",
                            default=True)
    start_date = fields.Date(default=datetime.date.today(),
                             help="to select Commission plan start date")
    end_date = fields.Date(
        default=datetime.date.today() + relativedelta(months=3),
        help="to select Commission plan end date")
    type = fields.Selection(selection=[('product_wise', 'Product Wise'),
                                       ('revenue_wise', 'Revenue Wise')],
                            required=True,
                            help="to select Commission type")
    productwise_ids = fields.One2many('commission.productwise',
                                      'commission_id')
    revenuewise_ids = fields.One2many('commission.revenuewise',
                                      'commission_id')
    revenue_type = fields.Selection(selection=[('straight', 'Straight'),
                                               ('graduated', 'Graduated')],
                                    default='',
                                    help="to select Revenue wise type")

    @api.constrains('revenuewise_ids', 'revenue_type')
    def validation_revenuewise(self):
        """This is used to set limit to add rules in Straight type."""
        if self.revenue_type == 'straight':
            if len(self.revenuewise_ids) > 1:
                raise ValidationError("Only 1 entry is possible.")

    @api.constrains('start_date', 'end_date')
    def validation_expire_date(self):
        """This is used to set validity of date in Commission plan."""
        today = datetime.date.today()
        if self.end_date:
            if self.end_date < today or self.start_date > today:
                self.active = False
            elif self.start_date:
                if self.start_date > self.end_date:
                    raise ValidationError("Start date must be before End date")

    @api.onchange('type')
    def _onchange_type(self):
        if self.type == 'product_wise':
            self.revenue_type = False

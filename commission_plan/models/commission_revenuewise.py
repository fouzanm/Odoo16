# -*- coding: utf-8 -*-
from odoo import fields, models


class CommissionRevenueWise(models.Model):
    """This is used to set revenue wise commission type."""
    _name = 'commission.revenuewise'
    _description = 'Commission Plan Revenue Wise'

    sequence = fields.Integer(string="Sequence")
    from_amount = fields.Float(string="From Amount",
                               help="to select Commission plan from amount.")
    to_amount = fields.Float(string="To Amount",
                             help="to select Commission plan to amount.")
    rate = fields.Float(string="rate in %",
                        help="to select Commission plan percentage.")
    commission_id = fields.Many2one('crm.commission')
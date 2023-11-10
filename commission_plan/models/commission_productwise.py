# -*- coding: utf-8 -*-
from odoo import fields, models


class CommissionProductWise(models.Model):
    """This is used to set product wise commission type."""
    _name = 'commission.productwise'
    _description = 'Commission Plan Product wise'

    product_category_id = fields.Many2one('product.category',
                                          help="to select Product category.")
    product_id = fields.Many2one('product.product',
                                 domain="[('categ_id', '=', "
                                        "product_category_id)]",
                                 help="to select Product.")
    rate = fields.Float(string="Rate in %",
                        help="to select Commission percentage.")
    max_amount = fields.Float(string="Maximum Commission Amount",
                              help= "to set a limit of Commission amount.")
    commission_id = fields.Many2one('crm.commission')

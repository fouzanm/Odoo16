# -*- coding: utf-8 -*-
from odoo import fields, models


class BestPriceWizard(models.TransientModel):
    """to add supplier view in wizard"""
    _name = 'best.price.wizard'
    _description = 'Best Price Wizard'

    supplier_ids = fields.Many2many('supplier.info')

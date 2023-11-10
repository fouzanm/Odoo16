# -*- coding: utf-8 -*-
from odoo import api, models


class SaleOrder(models.Model):
    """to set default tolerance in sale order line"""
    _inherit = 'sale.order'
    _description = 'Sale order'

    @api.onchange('partner_id', 'order_line')
    def _onchange_partner_id(self):
        """to set default tolerance in sale order line"""
        for record in self.order_line:
            if self.partner_id.tolerance and not record.tolerance:
                record.tolerance = self.partner_id.tolerance

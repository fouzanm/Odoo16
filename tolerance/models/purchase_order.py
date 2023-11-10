# -*- coding: utf-8 -*-
from odoo import api, models


class PurchaseOrder(models.Model):
    """to set default tolerance in purchase order line"""
    _inherit = 'purchase.order'
    _description = 'Purchase Order'

    @api.onchange('partner_id', 'order_line')
    def _onchange_partner_id(self):
        """to set default tolerance in purchase order line"""
        for record in self.order_line:
            if self.partner_id.tolerance and not record.tolerance:
                record.tolerance = self.partner_id.tolerance

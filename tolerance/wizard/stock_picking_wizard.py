# -*- coding: utf-8 -*-
from odoo import fields, models


class StockPickingWizard(models.TransientModel):
    """to create wizard for warning"""
    _name = 'stock.picking.wizard'
    _description = 'Stock Picking Wizard'

    message = fields.Text(string="Warning message", readonly=True)

    def accept_transfer(self):
        """button action in wizard to confirm transfer"""
        record_id = self.env.context
        stock_picking_id = self.env['stock.picking'].browse(
            record_id['record_id'])
        stock_picking_id.force_accept = True
        stock_picking_id._action_done()

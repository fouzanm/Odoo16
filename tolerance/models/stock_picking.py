# -*- coding: utf-8 -*-
from odoo import fields, models


class StockPicking(models.Model):
    """to set tolerance rule"""
    _inherit = 'stock.picking'
    _description = 'Stock picking'

    force_accept = fields.Boolean(default=False)

    def button_validate(self):
        """button action to validate transfer"""
        for record in self.move_ids:
            if self.sale_id:
                tolerance = record.sale_line_id.tolerance
                quantity = record.sale_line_id.product_uom_qty
            else:
                tolerance = record.purchase_line_id.tolerance
                quantity = record.purchase_line_id.product_uom_qty
            min_qty = quantity - tolerance
            max_qty = quantity + tolerance
            if (min_qty > record.quantity_done or
                    record.quantity_done > max_qty)\
                    and self.force_accept is False:
                wizard = self.env['stock.picking.wizard'].create({
                    'message': f"The Done quantity of the product "
                               f"'{record.product_id.name}' is outside the"
                               f" allowed Tolerance range.\n "
                               f"Do you want to continue?",
                })
                return {
                    'name': 'Warning',
                    'type': 'ir.actions.act_window',
                    'res_model': 'stock.picking.wizard',
                    'res_id': wizard.id,
                    'view_mode': 'form',
                    'view_type': 'form',
                    'target': 'new',
                    'context': {
                        'record_id': self.id
                    }}
        return super(StockPicking, self).button_validate()

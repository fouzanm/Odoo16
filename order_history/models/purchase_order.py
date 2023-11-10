from odoo import fields, models


class PurchaseOrder(models.Model):
    """to inherit purchase order"""
    _inherit = 'purchase.order'
    _description = 'Purchase order'

    order_history_id = fields.Many2one('order.history')

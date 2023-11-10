# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    """This is used to set commission type in Quotation."""
    _inherit = 'sale.order'
    _description = 'Sale order'

    commission_plan_id = fields.Many2one('crm.commission',
                                         readonly=True)
    res_users_id = fields.Many2one('res.users')
    commission = fields.Float(string="Commission Amount", readonly=True,
                              compute='_compute_commission', store=True)

    @api.depends('commission_plan_id', 'order_line')
    def _compute_commission(self):
        """This is used to calculate commission."""
        total = 0
        commission = 0
        plan = False
        if self.team_id.commission_plan_id:
            plan = self.team_id.commission_plan_id
        elif self.user_id.commission_plan_id:
            plan = self.user_id.commission_plan_id
        self.commission_plan_id = plan
        if plan:
            for record in self.order_line:
                total += record.price_subtotal
                if plan.type == 'product_wise':
                    for rec in plan.productwise_ids:
                        rate = 0
                        if rec.product_id.id == record.product_id.id:
                            rate += rec.rate * record.price_subtotal / 100
                            if rec.max_amount and rate > rec.max_amount:
                                commission += rec.max_amount
                            else:
                                commission += rate
                elif plan.revenue_type == 'straight':
                    rate = plan.revenuewise_ids.rate
                    from_amount = plan.revenuewise_ids.from_amount
                    to_amount = plan.revenuewise_ids.to_amount
                    amount = total
                    if total >= from_amount:
                        if total > to_amount:
                            amount = to_amount
                        commission = amount * rate / 100
            if plan.revenue_type == 'graduated':
                amount = total
                for rec in plan.revenuewise_ids:
                    if total > rec.from_amount:
                        if total > rec.to_amount:
                            difference = rec.to_amount - rec.from_amount
                            rate = difference * rec.rate / 100
                            amount -= difference
                            commission += rate
                        else:
                            rate = amount * rec.rate / 100
                            commission += rate
        self.commission = commission

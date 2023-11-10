# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    """to add field in POS Settings"""
    _inherit = 'res.config.settings'

    pos_categ_discount = fields.Boolean(related="pos_config_id"
                                                ".pos_categ_discount",
                                        string="Limit Category Discount",
                                        help="This Category will be used as"
                                             " maximum discount limit.",
                                        readonly=False)
    pos_categ_ids = fields.Many2many(related="pos_config_id.pos_categ_ids",
                                     readonly=False)
    discount_limit = fields.Float(related="pos_config_id.discount_limit",
                                  string="Max Discount Limit",
                                  readonly=False, default=100.0)
    @api.constrains('pos_categ_discount')
    def _set_pos_categ_ids(self):
        if not self.pos_categ_discount:
            self.pos_categ_ids = False

# -*- coding: utf-8 -*-
from odoo import models


class PosSession(models.Model):
    """to load field in POS"""
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        """add field in pos session"""
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('quality_rating')
        return result

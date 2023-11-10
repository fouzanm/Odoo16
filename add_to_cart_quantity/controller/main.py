# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSale(WebsiteSale):

    @http.route(['/shop'], type="http", auth="public")
    def shop(self, page=0, category=None, search='', min_price=0.0,
             max_price=0.0, ppg=False, **post):
        result = super(WebsiteSale, self).shop(page=0, category=None, search='',
                                               min_price=0.0, max_price=0.0,
                                               ppg=False, **post)
        show_quantity = request.env['ir.config_parameter'].sudo().get_param(
            'show_quantity')
        result.qcontext['show_quantity'] = show_quantity
        return request.render("website_sale.products", result.qcontext)

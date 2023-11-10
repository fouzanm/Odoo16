# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MostViewedProducts(http.Controller):
    """to return most viewed products"""
    @http.route(['/most_viewed_products'], type="json", auth="public")
    def viewed_products(self):
        viewed_products = request.env['website.track'].sudo().search([
                    ('product_id', '!=', False)
                ])
        viewed_products = [{'id': record.id, 'name': record.name,
                            'view_count': viewed_products.search_count([
                                ('product_id', '=', record.id)]),
                            'template_id': record.product_tmpl_id.id,
                            'image': record.image_1920}
                           for record in viewed_products.mapped('product_id')]
        viewed_products = sorted(viewed_products, key=lambda x: x['view_count'],
                                 reverse=True)[:16]
        return viewed_products

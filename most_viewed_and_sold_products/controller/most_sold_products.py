# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MostSoldProducts(http.Controller):
    """to return most sold products"""
    @http.route(['/most_sold_products'], type="json", auth="public")
    def sold_products(self):
        sold_products = request.env['product.product'].sudo().search([]).sorted(
            key=lambda x: x.sales_count, reverse=True)
        sold_products = [{'id': record.id, 'name': record.name,
                          'sales_count': record.sales_count,
                          'template_id': record.product_tmpl_id.id,
                          'image': record.image_1920
                          } for record in sold_products[:16]]
        return sold_products

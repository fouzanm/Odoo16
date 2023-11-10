# -*- coding: utf-8 -*-
import datetime

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo import _, http, fields
from odoo.http import request


class PortalAccount(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        return_count = request.env['product.return'].sudo().search_count([])
        values['return_count'] = return_count
        return values

    @http.route(route=['/my/return'], type='http', auth="user", website=True)
    def portal_my_return_orders(self):
        order = request.env['product.return'].sudo().search([])
        order = [{'name': record.name,
                  'customer': record.partner_id.name,
                  'date': record.date,
                  'order': record.order_id.name,
                  'status': record.status} for record in order]
        return request.render("website_product_return.portal_my_return_orders",
                              {'return_orders': order,
                               'page_name': 'return_orders'})

    @http.route(route=['/my/orders/<int:order_id>'], type='http', auth="user",
                website=True)
    def portal_order_page(self, order_id, *args):
        response = super().portal_order_page(order_id, *args)
        return_order = request.env['product.return'].sudo().search([
            ('order_id', '=', response.qcontext['sale_order'].id)])
        response.qcontext['return_order'] = True if return_order else False
        return response

    @http.route(['/order/return/<model("sale.order"):sale_order>'], type='http',
                auth="user", website=True)
    def action_create_return_order(self, sale_order):
        today = datetime.date.today()
        reason = request.env['return.reason'].sudo().search([])
        return request.render("website_product_return.return_order_form",
                              {'sale_order': sale_order, 'today': today,
                               'reason': reason})

    @http.route(['/return/create'], type='http', auth="public",
                website=True)
    def action_submit_return_order(self, **kw):
        if kw.get('reason') == 'Other':
            reason = request.env['return.reason'].create({
                'name': kw.get('other_reason')}).id
        else:
            reason = kw.get('reason')
        order = []
        for i in range(len(kw)):
            if kw.get(str(i)):
                order_line = request.env['sale.order.line'].sudo().browse(
                    int(kw.get(str(i))))
                returned_qty = kw.get(f'quantity[{kw.get(str(i))}]')
                stock_move = request.env['stock.move'].sudo().search([
                    ('sale_line_id', '=', order_line.id)
                ])
                order.append({'product_id': order_line.product_id,
                              'quantity': order_line.product_uom_qty,
                              'returned_qty': returned_qty,
                              'location_id': stock_move.location_dest_id,
                              'location_dest_id': stock_move.location_id})
        request.env['product.return'].sudo().create({
            'order_id': kw.get('order'),
            'date': kw.get('create_date'),
            'reason_id': reason,
            'order_line_ids': [fields.Command.create({
                'product_id': record['product_id'].id,
                'quantity': record['returned_qty'],
                'location_id': record['location_id'].id,
                'location_dest_id': record['location_dest_id'].id
            }) for record in order]})
        return request.redirect(f'/my/orders/{kw.get("order")}')

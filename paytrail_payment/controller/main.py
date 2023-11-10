# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class PaytrailPaymentGatewayController(http.Controller):
    _return_url = '/payment/paytrail/return'
    @http.route(_return_url,type='http', auth='public', methods=['GET'],
                csrf=False, save_session=False)
    def paytrail_return_from_checkout(self, **data):
        tx_sudo = request.env['payment.transaction'].sudo()._get_tx_from_notification_data(
            'paytrail', data
        )
        status = data.get('checkout-status')
        if status == 'ok':
            tx_sudo._set_done()
        elif status == 'fail':
            tx_sudo._set_canceled()
        return request.redirect('/payment/status')

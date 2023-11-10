import hashlib
import hmac
import uuid
import datetime
import requests
from werkzeug import urls
from odoo import _, models
from odoo.addons.payment import utils as payment_utils
import json
from odoo.exceptions import ValidationError


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    @staticmethod
    def compute_sha256_hash(message: str, secret: str):

        hash = hmac.new(secret.encode(), message.encode(),
                        digestmod=hashlib.sha256)
        return hash.hexdigest()

    @staticmethod
    def calculate_hmac(self, secret: str, headers: dict, payload: str = ''):
        data = []
        for key, value in headers.items():
            if key.startswith('checkout-'):
                data.append('{key}:{value}'.format(key=key, value=value))
        data.append(payload)
        return self.compute_sha256_hash('\n'.join(data), secret)

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'paytrail':
            return res
        converted_amount = payment_utils.to_minor_currency_units(
            self.amount, self.currency_id)
        base_url = 'https://2411-202-56-252-130.ngrok-free.app/'
        order = self.sale_order_ids
        order_line = self.env['sale.order.line'].search([
            ('order_id', '=', order.id)
        ])
        items = [{
            'unitPrice': payment_utils.to_minor_currency_units(
                record.price_reduce_taxinc, self.currency_id),
            'units': record.product_uom_qty,
            'vatPercentage': 0,
            'productCode': record.name_short,
            'stamp': str(uuid.uuid4()),
        } for record in order_line]
        payload = {
            'stamp': str(uuid.uuid4()),
            'reference': self.reference,
            'amount': converted_amount,
            'currency': "EUR",
            # 'currency': self.currency_id.name,
            'language': self.partner_lang[:2].upper(),
            'items': items,
            'customer': {
                'email': self.partner_id.email_normalized,
            },
            'redirectUrls': {
                'success': urls.url_join(base_url,
                                         'payment/paytrail/return'),
                'cancel': urls.url_join(base_url,
                                        'payment/paytrail/return'),
            },
            'callbackUrls': {
                'success': urls.url_join(base_url,
                                         'payment/paytrail/return'),
                'cancel': urls.url_join(base_url,
                                        'payment/paytrail/return'),
            }
        }
        secret = self.provider_id.paytrail_secret_key
        headers = {
            "checkout-account": self.provider_id.paytrail_merchant_identifier,
            "checkout-algorithm": "sha256",
            "checkout-method": "POST",
            "checkout-nonce": self.reference,
            "checkout-timestamp": datetime.datetime.utcnow().strftime(
                "%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}
        payload = json.dumps(payload)
        hmac_signature = self.calculate_hmac(self, secret, headers, payload)
        headers['signature'] = hmac_signature
        headers['content-type'] = 'application/json; charset=utf-8'
        url = 'https://services.paytrail.com/payments/'
        response = requests.post(url, headers=headers, data=payload)
        response_data = json.loads(response.text)
        api_url = response_data['href']
        return {'api_url': api_url}

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        tx = super()._get_tx_from_notification_data(provider_code,
                                                    notification_data)
        if provider_code != 'paytrail' or len(tx) == 1:
            return tx
        reference = notification_data.get('checkout-reference')
        if not reference:
            raise ValidationError(
                "Paytrail: " + _("Received data with missing reference %(ref)s",
                                 ref=reference)
            )
        tx = self.search([('reference', '=', reference),
                          ('provider_code', '=', 'paytrail')])
        if not tx:
            raise ValidationError(
                "Paytrail: " + _("No transaction found matching reference %s.",
                                 reference)
            )
        return tx

# -*- coding: utf-8 -*-
from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('paytrail', "Paytrail")],
        ondelete={'paytrail': 'set default'}
    )
    paytrail_merchant_identifier = fields.Char(
        string="Paytrail Merchant Identifier",
        required_if_provider='paytrail',
    )
    paytrail_secret_key = fields.Char(
        string="Paytrail Secret Key",
        required_if_provider='paytrail',
    )

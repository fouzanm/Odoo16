# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectTask(models.Model):
    """to add field in Project Task"""
    _inherit = 'project.task'
    _description = 'Project Task'

    product_id = fields.Many2one('product.product')

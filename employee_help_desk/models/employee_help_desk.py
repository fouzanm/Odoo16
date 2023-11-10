# -*- coding: utf-8 -*-
import datetime

from odoo import fields, models


class EmployeeHelpDesk(models.Model):
    """to create help desk for employees"""
    _name = 'employee.help.desk'

    name = fields.Char(string="Ticket")
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee',
                                  required=True)
    manager_id = fields.Many2one(comodel_name='hr.employee',
                                 string="Assigned to", readonly=False,
                                 related='employee_id.parent_id', required=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company',
                                 default=lambda self: self.env.company,
                                 required=True)
    issue_id = fields.Many2one(comodel_name='help.desk.issue', string="Type",
                               help='Select issue type.', required=True)
    issue = fields.Text(string="Issue", help='Describe your issue')
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    issued_date = fields.Date(default=datetime.date.today(),
                              string="Date issued")
    state = fields.Selection(selection=[('new', 'New'),
                                        ('on_going', 'On Going'),
                                        ('solved', 'Solved'),
                                        ('rejected', 'Rejected')],
                             default='new')

    def action_ticket_confirm(self):
        """action to change state from New"""
        self.state = 'on_going'

    def action_ticket_done(self):
        """action to change state to Solved"""
        self.state = 'solved'

    def action_ticket_cancel(self):
        """action to change state to Rejected"""
        self.state = 'rejected'
        
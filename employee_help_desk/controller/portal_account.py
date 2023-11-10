# -*- coding: utf-8 -*-
import datetime

from odoo.addons.portal.controllers.portal import CustomerPortal

from odoo import http
from odoo.http import request


class PortalAccount(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        user = request.env.user
        ticket_count = (request.env['employee.help.desk'].sudo().search_count([
            ('employee_id', '=', user.employee_id.id)]))
        values['ticket_count'] = ticket_count
        return values

    @http.route(route=['/helpdesk/ticket'], type='http', auth="user",
                website=True)
    def portal_my_tickets(self):
        user = request.env.user
        tickets = request.env['employee.help.desk'].sudo().search([
            ('employee_id', '=', user.employee_id.id)
        ])
        tickets = [{
            'name': record.name,
            'employee': record.employee_id.name,
            'manager': record.manager_id.name,
            'issued_date': record.issued_date,
            'issue': record.issue_id.name,
            'state': record.state,
        } for record in tickets]
        return request.render("employee_help_desk.portal_my_ticket",
                              {'tickets': tickets, 'page_name': 'tickets'})

    @http.route(['/helpdesk/ticket/new'], type='http', auth="user",
                website=True)
    def action_create_ticket(self):
        user = request.env.user
        issue = request.env['help.desk.issue'].sudo().search([])
        values = {
            'employee': user.employee_id,
            'manager': user.employee_id.parent_id,
            'type': issue,
            'issued_date': datetime.date.today()
        }
        return request.render('employee_help_desk.ticket_form', values)

    @http.route('/ticket/submit', type='http', auth='public', website=True)
    def action_submit_ticket(self, **kw):
        request.env['employee.help.desk'].sudo().create({
            'name': kw.get('name'),
            'employee_id': kw.get('employee'),
            'manager_id': kw.get('manager'),
            'issue_id': kw.get('type'),
            'issue': kw.get('issue'),
        })
        return request.redirect('/helpdesk/ticket')


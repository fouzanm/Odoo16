# -*- coding: utf-8 -*-
from odoo import Command, fields, models


class SaleOrder(models.Model):
    """to add fields in Sale order"""
    _inherit = 'sale.order'
    _description = 'Sale order'

    update_project = fields.Boolean('Create Project', default=False)
    task_count = fields.Integer(compute='_compute_task_count')

    def add_milestone_project(self):
        """action for creating project."""
        self.update_project = True
        project = self.env['project.project'].create({
            'name': self.name,
            'partner_id': self.partner_id.id,
            'company_id': self.company_id.id,
            'user_id': self.user_id.id,
        })
        milestone = []
        for record in self.order_line:
            task = f"Milestone {record.milestone}"
            sub_task_name = f'{task} - {record.product_id.name}'
            sub_task = Command.create({
                'name': sub_task_name,
                'product_id': record.product_id.id
            })
            if record.milestone in milestone:
                project.tasks.search([
                    ('name', '=', task),
                    ('project_id', '=', project.id)]).write({
                        'child_ids': [sub_task]
                    })
            else:
                project.write({
                    'tasks': [Command.create({
                        'name': task,
                        'child_ids': [sub_task]
                    })]
                })
            milestone.append(record.milestone)

    def update_milestone_project(self):
        """action for update project"""
        exist_project = self.env['project.project'].search([
            ('name', '=', self.name)
        ])
        for record in self.order_line:
            task = f"Milestone {record.milestone}"
            sub_task_name = f'{task} - {record.product_id.name}'
            exist_task = exist_project.tasks.search([
                ('name', '=', task),
                ('project_id', '=', exist_project.id)
            ])
            exist_subtask = exist_project.tasks.child_ids.search([
                ('product_id', '=', record.product_id.id),
                ('project_id', '=', exist_project.id)
            ])
            new_sub_task = Command.create({
                'name': sub_task_name,
                'product_id': record.product_id.id
            })
            sub_task = {
                    'name': sub_task_name,
                    'parent_id': exist_task.id
                }
            if exist_task and not exist_subtask:
                exist_task.write({
                        'child_ids': [new_sub_task]
                    })
            elif not exist_task and not exist_subtask:
                exist_project.write({
                    'tasks': [Command.create({
                        'name': task,
                        'child_ids': [new_sub_task]
                    })]
                })
            elif exist_task and exist_subtask:
                exist_subtask.write(sub_task)
            elif not exist_task and exist_subtask:
                exist_project.write({
                    'tasks': [Command.create({
                        'name': task,
                    })]
                })
                project = exist_project.tasks.search([
                    ('name', '=', task),
                    ('project_id', '=', exist_project.id)
                ])
                update_subtask = exist_project.tasks.child_ids.search([
                    ('product_id', '=', record.product_id.id),
                    ('project_id', '=', exist_project.id)
                ])
                project.update({
                    'child_ids': [Command.update(update_subtask.id, {
                        'name': sub_task_name,
                        'parent_id': project.id
                    })]
                })

    def action_project_view(self):
        """action to view project task view"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Project',
            'view_mode': 'kanban,tree,form',
            'res_model': 'project.task',
            'domain': [('project_id', '=', self.name),
                       ('parent_id', '=', False)]
        }

    def _compute_task_count(self):
        """to compute task count"""
        for record in self:
            record.task_count = self.env['project.task'].search_count(
                [('project_id', '=', self.name),
                 ('parent_id', '=', False)])

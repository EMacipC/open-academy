# -*- coding: UTF-8 -*-
from odoo import fields, models


class OpenenacademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Courses'

    name = fields.Char(
        string='Title', 
        required=True
        )
    description = fields.Text(
    )
    responsible_id = fields.Many2one(
        comodel_name='res.users',
        ondelete='set null', 
        index=True,
    )
    session_ids = fields.One2many(
        comodel_name='openacademy.session', 
        inverse_name='course_id', 
    )


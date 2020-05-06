# -*- coding: UTF-8 -*-
from odoo import fields, models
class OpenenacademySession(models.Model):
    _name = 'openacademy.session'
    _description = 'OpenAcademy Session'

    name = fields.Char(
        required=True
        )
    name = fields.Char(
        required=True
        )
    start_date = fields.Date(
    )
    duration = fields.Float(
        digits=(6, 2), 
        help="Duration in days"
    )
    seats = fields.Integer(
        string="Number of seats"
    )
    instructor_id = fields.Many2one(
        comodel_name='res.partner', 
        domain=[
            '|',
            ('instructor', '=', True),
            ('category_id.name', 'ilike', "Teacher")],
    )
    course_id = fields.Many2one(
        comodel_name='openacademy.course',
        ondelete='cascade',
        required=True,
    )
    attendee_ids = fields.Many2many(
        comodel_name='res.partner',
    )



# -*- coding: UTF-8 -*-
from odoo import api,fields, models
class OpenenacademySession(models.Model):
    _name = 'openacademy.session'
    _description = 'OpenAcademy Session'

    name = fields.Char(
        required=True,
        )
    name = fields.Char(
        required=True,
        )
    start_date = fields.Date(
        default=fields.Date.today,
    )
    duration = fields.Float(
        digits=(6, 2), 
        help="Duration in days",
    )
    seats = fields.Integer(
        string="Number of seats",
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
    active = fields.Boolean(
        default=True,
        )

    attendee_ids = fields.Many2many(
        comodel_name='res.partner',
    )
    taken_seats = fields.Float(
         compute='_taken_seats',
         )

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }



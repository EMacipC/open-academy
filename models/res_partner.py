
# -*- coding: UTF-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(
    )

    session_ids = fields.Many2many(
        comodel_name='openacademy.session',
        string="Attended Sessions", 
        readonly=True
    )



from odoo import models, fields, api

class OpenacademySessionWizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    def _default_sessions(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    
    session_ids = fields.Many2many(
        'openacademy.session',
        required=True,
         default=_default_sessions,
        )

    attendee_ids = fields.Many2many(
        'res.partner',
        )

    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
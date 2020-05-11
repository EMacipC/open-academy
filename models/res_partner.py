
# -*- coding: UTF-8 -*-
from odoo import api,fields, models ,exceptions
import webbrowser, time

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(
    )

    session_ids = fields.Many2many(
        comodel_name='openacademy.session',
        string="Attended Sessions", 
        readonly=True
    )

    phone = fields.Char(
    )
    mobile = fields.Char(
    )

    def whatsapp(self):
        if self.mobile == False:
            return{}
        return{

            "type": "ir.actions.act_url",
            "url": "https://wa.me/"+self.mobile,
            "target": "self",

        }
    @api.onchange('mobile')
    def _verify_valid_seats(self):
        if self.mobile == False:
            return{}
        if  10 > len(self.mobile):
            return {
                'warning': {
                    'title': "Not enough characters ",
                    'message': "The number of characters are not enough to be a mobile",
                },
            }
        if 10 < len(self.mobile):
            return {
                'warning': {
                    'title': "Too much characters",
                    'message': "The number of characters are too much to be a mobile",
                },
            }
    @api.constrains('mobile') # if these fields are changed, call method , 'Titular_Telefono2','Telefono2'
    def solonumero(self):
        if self.mobile == False:
            return{}
        numbers ={'1','2','3','4','5','6','7','8','9','0'}
        for n in self.mobile:
            if not n in numbers:
                raise exceptions.ValidationError("Mobile has one or more characters invalids")
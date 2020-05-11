from odoo import api,fields, models 

class Sale(models.Model):
    _inherit = 'sale.order'
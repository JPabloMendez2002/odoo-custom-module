
from odoo import models, fields

class Space(models.Model):
    _name = 'space.management'
    _description = 'Space Management'

    name = fields.Char(string='Space Name', required=True)
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity')

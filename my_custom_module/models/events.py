
from odoo import models, fields

class Event(models.Model):
    _name = 'event.management'
    _description = 'Event Management'

    name = fields.Char(string='Event Name', required=True)
    date = fields.Datetime(string='Event Date')
    description = fields.Text(string='Description')
    capacity = fields.Integer(string='Capacity')

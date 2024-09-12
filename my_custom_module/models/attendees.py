
from odoo import models, fields

class Attendee(models.Model):
    _name = 'attendee.management'
    _description = 'Attendee Management'

    name = fields.Char(string='Attendee Name', required=True)
    email = fields.Char(string='Email')
    event_id = fields.Many2one('event.management', string='Event')

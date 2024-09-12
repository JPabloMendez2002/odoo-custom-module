
from odoo import models, fields

class Booking(models.Model):
    _name = 'booking.management'
    _description = 'Booking Management'

    event_id = fields.Many2one('event.management', string='Event', required=True)
    space_id = fields.Many2one('space.management', string='Space', required=True)
    date = fields.Datetime(string='Booking Date', required=True)

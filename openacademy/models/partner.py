# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)

    other_field = fields.Boolean(default=True)
    other_field2 = fields.Boolean(default=True)


    #duration = fields.Float(digits=(6, 2), help="Duration in days")
    #seats = fields.Integer(string="Number of seats")

    #instructor_id = fields.Many2one('res.partner', string="Instructor", domain=[('instructor', '=', True)])
    #course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    #attendee_ids = fields.Many2many('res.partner', string="Attendees")

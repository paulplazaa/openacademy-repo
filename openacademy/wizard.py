# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = 'wizard'

    def _default_session(self):
        session_obj = self.env['openacademy.session']
        session_ids = self._context.get('active_ids')
        session_records = session_obj.browse(session_ids)
        return session_records;
        #return self.env['openacademy.session'].browse(self._context.get('active_id'))

    session_ids = fields.Many2many('openacademy.session', required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner')

    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}


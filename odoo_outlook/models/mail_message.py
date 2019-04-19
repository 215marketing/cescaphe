# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mail_message(models.Model):
    _inherit = 'mail.message'

    from_outlook = fields.Boolean(string='Added from Outlook', default=False)

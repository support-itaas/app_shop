# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from lxml import etree
from lxml.html import builder as html

from odoo import _, api, fields, models


class Invite(models.TransientModel):
    _inherit = 'mail.wizard.invite'
    _description = 'Invite wizard'

    @api.model
    def default_get(self, fields):
        result = super(Invite, self).default_get(fields)
        print('default_get:')
        if self._context.get('mail_invite_follower_channel_only'):
            result['send_mail'] = False
        if 'message' not in fields:
            return result

        user_name = self.env.user.name_get()[0][1]
        model = result.get('res_model')
        res_id = result.get('res_id')
        if model and res_id:
            document = self.env['ir.model']._get(model).display_name
            title = self.env[model].browse(res_id).display_name
            # msg_fmt = _('%(user_name)s invited you to follow %(document)s document: %(title)s')
            msg_fmt = _('ข้อร้องเรียนลูกค้า %(document)s : %(title)s')
        else:
            msg_fmt = _('%(user_name)s invited you to follow a new document.')

        text = msg_fmt % locals()
        message = html.DIV(
            # html.P(_('Hello,')),
            html.P(text)
        )
        result['message'] = etree.tostring(message)
        return result


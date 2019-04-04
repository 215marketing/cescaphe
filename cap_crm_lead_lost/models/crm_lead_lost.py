# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import api, models


class CRMLeadLost(models.TransientModel):
    """Manage 'crm.lead.lost' model. Overriding model."""
    _inherit = "crm.lead.lost"

    @api.multi
    def action_lost_reason_apply(self):
        """Manage 'lost reason' of some 'crm.lead'. Overriding method."""
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        leads.write({'lost_reason': self.lost_reason_id.id,
                     'x_studio_lost_reason': self.x_description})
        return leads.action_set_lost()

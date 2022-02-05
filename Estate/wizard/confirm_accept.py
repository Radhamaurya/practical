from odoo import fields, models

class ConfirmAccept(models.TransientModel):
    _name = 'confirm.accept'
    _description = 'Confirm Accept'

    selected_partner_id = fields.Many2one('res.partner')
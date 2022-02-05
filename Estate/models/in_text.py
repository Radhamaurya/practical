from odoo import models,fields
from odoo.exceptions import UserError, ValidationError

class BanbkProperty(models.Model):
        _inherit = 'estate.property'

        bankname = fields.Char()
        bankinterest = fields.Float()

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    bankname = fields.Char()
    bankinterest = fields.Float()








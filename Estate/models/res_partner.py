from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ResPartner(models.Model):
	_inherit = 'res.partner'


	offer_ids = fields.One2many('estate.property.offer', 'partner_id')
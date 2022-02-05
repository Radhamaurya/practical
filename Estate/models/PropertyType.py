from odoo import models,fields,api

class EstatePropertyType(models.Model):
        _name = "estate.property.type"
        _description = "EstatePropertyType"
        
        name = fields.Char()
        property_ids = fields.One2many('estate.property', 'property_type_id')
        offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
        offer_count = fields.Integer(compute='_compute_offer_count')


        @api.depends('offer_ids')
        def _compute_offer_count(self):
            for record in self:
                record.offer_count =  len(record.offer_ids)

class EstatePropertyTag(models.Model):
        _name = "estate.property.tag"
        _description = "EstatePropertyTag"
        color = fields.Integer()
        
        name = fields.Char()

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    _order = 'price desc'
    
    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('rejected', 'Rejected')])
    partner_id = fields.Many2one('res.partner')
    property_id = fields.Many2one('estate.property')
    property_type_id = fields.Many2one(related='property_id.property_type_id', store=True)
    

    def action_accepted(self):

        for record in self:
            record.status = 'accepted'
            # # Set Buyer and selling price
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            #Do something to change status of other properties as rejected
            for rec in record.property_id.property_offer_ids:
                 if rec.status != 'accepted':
                   rec.status = 'rejected'


    def action_rejected(self):
        for record in self:
            record.status = 'rejected'



from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class EstateProperty(models.Model):

    def _get_description(self):
        if self.env.context.get('is_my_property'):
            return self.env.user.name + '\'s Property'

    _name = "estate.property"
    _description = "Estate Property"
    _inherit = [
        'image.mixin',
    ]
    name = fields.Char(string="Property Name",
                       defauit="unknown", required=True)
    description = fields.Text(default=_get_description)
    Tag = fields.Char()
    postcode = fields.Char()
    date_availability = fields.Date(
        default=lambda self: fields.Datetime.now(), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'), ('east', 'East'),
        ('south', 'South'), ('west', 'West')
    ])
    active = fields.Boolean(default=True)
    # image = fields.Image()
    validity = fields.Integer(default=7)
    property_type_id = fields.Many2one('estate.property.type')
    buyer_id = fields.Many2one('res.partner')
    salesman_id = fields.Many2one('res.users')
    property_tag_ids = fields.Many2many('estate.property.tag')
    property_offer_ids = fields.One2many(
        'estate.property.offer', 'property_id')
    total_area = fields.Integer(
        compute="_compute_area", inverse="_inverse_area")
    best_price = fields.Float(compute="_compute_best_price", store=True)
    date_deadline = fields.Date(compute="_compute_date_deadline")
    state = fields.Selection(
        [('new', 'New'), ('sold', 'Sold'), ('cancel', 'Cancelled')], default='new')
    currency_id = fields.Many2one(
        'res.currency', default=lambda self: self.env.company.currency_id)

    @api.onchange('garden')
    def _onchange_garden(self):
        for record in self:
            if record.garden == True:
                record.garden_area = 10
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0
                record.garden_orientation = None

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.add(
                record.date_availability, days=record.validity)

    @api.depends('property_offer_ids.price')
    def _compute_best_price(self):  # Recordset [ Collection  of records]
        for record in self:
            max_price = 0
            for offer in record.property_offer_ids:
                if offer.price > max_price:
                    max_price = offer.price
            record.best_price = max_price

    @api.depends('living_area', 'garden_area')
    def _compute_area(self):
        print("\n\n ----- _compute_area method call")
        for record in self:
            record.total_area = record.living_area + record.garden_area

    def _inverse_area(self):
        for record in self:
            record.living_area = record.garden_area = record.total_area / 2

    def action_sold(self):
        print("\n\n In action sold")
        for record in self:
            if record.state == 'cancel':
                raise UserError("Cancel Property cannot be sold")
            record.state = 'sold'

    def action_cancel(self):
        print("\n\n In action sold")
        for record in self:
            if record.state == 'cancel':
                raise UserError("Sold Property cannot be canceled")
            record.state = 'cancel'

    @api.constrains('living_area', 'garden_area')
    def _check_garden_area(self):
        for record in self:
            if record.living_area < record.garden_area:
                raise ValidationError(
                    "Garden cannot be bigger than living area")

    def open_offers(self):
        print("offer is conferm**********************************************")
        return{
            'name': 'Offers',
            'domain': [('property_id', '=', self.id)],
            'res_model': 'estate.property.offer',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }


class Buyer_partner(models.Model):
    _inherit = 'res.partner'

    is_buyer = fields.Boolean()

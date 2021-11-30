    _name = 'estate.property'
    _description = 'Estate Property'
    # _sql_constraints = [('postive_price', 'check(expected_price > 0)', 'Enter positive value')]
    _order = "id desc"

    # def test(self):
    #     return fields.Datetime.now()

    name = fields.Char(string="Title", default="Unknown", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Datetime.now(), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])
    active = fields.Boolean(default=True)
    image = fields.Image()
    property_type_id = fields.Many2one('estate.property.type')
    salesman_id = fields.Many2one('res.users')
    buyer_id = fields.Many2one('res.partner')
    test_id = fields.Many2one('test')
    property_tag_ids = fields.Many2many('estate.property.tag')
    property_offer_ids = fields.One2many('estate.property.offer', 'property_id')
    total_area = fields.Integer(compute="_compute_area", inverse="_inverse_area")
    best_price = fields.Float(compute="_compute_best_price")
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline")

    @api.onchange('garden')
    def _onchange_garden(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
                record.garden_orientation = 'north'
            else:
                record.garden_area = 0
                record.garden_orientation = None

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.add(record.date_availability, days=record.validity)
            # date_availability

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
        # print("\n\n ----- _compute_area method call")
        for record in self:
            record.total_area = record.living_area + record.garden_area

    def _inverse_area(self):
        for record in self:
            record.living_area = record.garden_area = record.total_area / 2

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold Property cannot be canceled")
            record.state = 'cancel'

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold Property cannot be canceled")
        record.state = 'cancel'

    @api.constrains('living_area', 'garden_area')
    def _check_garden_area(self):
        for record in self:
            if record.living_area < record.garden_area:
                raise ValueError("Garden cannot be bigger than living area")


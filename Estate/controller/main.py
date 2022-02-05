from odoo import http
from odoo.http import request


class EstateProperty(http.Controller):

    @http.route('/hello',auth='public',website=True)
    def hello(self, **kw):
        return request.render('Estate.hello_world', {'user':request.env.user})

    @http.route('/hello_user', auth="user")
    def hello_user(self, **kw):
        return "Hello %s" % (request.env.user.name)


    @http.route('/hello_template')
    def hello_temp(self, **kw):
        return request.render('Estate.estate_property_list')

    @http.route('/hello_template_user')
    def hello_template_user(self, **kw):
        Properties = request.env['estate.property'].search([('state', '=', 'sold')])
        print ("property ::: ", Properties)
        return request.render('Estate.hello_user', { 'user': request.env.user, 'property': Properties })

    @http.route('/property', website=True)
    def property(self, **kw):
         Properties = request.env['estate.property'].search([])
        #  print ("property ::: ", Properties)
         return request.render('Estate.properties',{'user': request.env.user,'property': Properties})


    @http.route(['/property/<model("estate.property"):property>', '/property/<string:is_static>'], auth="public", website=True)
    def property_details(self, property=False, **kw):
            if property :
                return request.render('Estate.property_details',{
                    'property' :property
                })

# -*- coding: utf-8 -*-
# from odoo import http


# class OrderFieldAdding(http.Controller):
#     @http.route('/order_field_adding/order_field_adding', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order_field_adding/order_field_adding/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('order_field_adding.listing', {
#             'root': '/order_field_adding/order_field_adding',
#             'objects': http.request.env['order_field_adding.order_field_adding'].search([]),
#         })

#     @http.route('/order_field_adding/order_field_adding/objects/<model("order_field_adding.order_field_adding"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order_field_adding.object', {
#             'object': obj
#         })


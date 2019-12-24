# -*- coding: utf-8 -*-
from odoo import http

# class PoLocationBisnis(http.Controller):
#     @http.route('/po_location_bisnis/po_location_bisnis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/po_location_bisnis/po_location_bisnis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('po_location_bisnis.listing', {
#             'root': '/po_location_bisnis/po_location_bisnis',
#             'objects': http.request.env['po_location_bisnis.po_location_bisnis'].search([]),
#         })

#     @http.route('/po_location_bisnis/po_location_bisnis/objects/<model("po_location_bisnis.po_location_bisnis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('po_location_bisnis.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
from odoo import http

# class CapSalesforce(http.Controller):
#     @http.route('/cap_salesforce/cap_salesforce/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cap_salesforce/cap_salesforce/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cap_salesforce.listing', {
#             'root': '/cap_salesforce/cap_salesforce',
#             'objects': http.request.env['cap_salesforce.cap_salesforce'].search([]),
#         })

#     @http.route('/cap_salesforce/cap_salesforce/objects/<model("cap_salesforce.cap_salesforce"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cap_salesforce.object', {
#             'object': obj
#         })
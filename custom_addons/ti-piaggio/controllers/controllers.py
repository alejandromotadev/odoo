# -*- coding: utf-8 -*-
# from odoo import http


# class Ti-piaggio(http.Controller):
#     @http.route('/ti-piaggio/ti-piaggio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ti-piaggio/ti-piaggio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ti-piaggio.listing', {
#             'root': '/ti-piaggio/ti-piaggio',
#             'objects': http.request.env['ti-piaggio.ti-piaggio'].search([]),
#         })

#     @http.route('/ti-piaggio/ti-piaggio/objects/<model("ti-piaggio.ti-piaggio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ti-piaggio.object', {
#             'object': obj
#         })


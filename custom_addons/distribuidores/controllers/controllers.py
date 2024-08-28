# -*- coding: utf-8 -*-
# from odoo import http


# class Distribuidores(http.Controller):
#     @http.route('/distribuidores/distribuidores', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/distribuidores/distribuidores/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('distribuidores.listing', {
#             'root': '/distribuidores/distribuidores',
#             'objects': http.request.env['distribuidores.distribuidores'].search([]),
#         })

#     @http.route('/distribuidores/distribuidores/objects/<model("distribuidores.distribuidores"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('distribuidores.object', {
#             'object': obj
#         })


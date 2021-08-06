# -*- coding: utf-8 -*-
from odoo import http

# class L10nClHrMethod(http.Controller):
#     @http.route('/l10n_cl_hr_method/l10n_cl_hr_method/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_hr_method/l10n_cl_hr_method/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_hr_method.listing', {
#             'root': '/l10n_cl_hr_method/l10n_cl_hr_method',
#             'objects': http.request.env['l10n_cl_hr_method.l10n_cl_hr_method'].search([]),
#         })

#     @http.route('/l10n_cl_hr_method/l10n_cl_hr_method/objects/<model("l10n_cl_hr_method.l10n_cl_hr_method"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_hr_method.object', {
#             'object': obj
#         })
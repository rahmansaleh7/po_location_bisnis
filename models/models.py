# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Po_location_bisnis(models.Model):
	_name = 'stock.move'
	_inherit = 'stock.move'

	account_analytic_id = fields.Many2one(comodel_name='account.analytic.account', 
										string='Unit')
	analytic_tag_ids = fields.Many2many(comodel_name='account.analytic.tag', 
										string='Lokasi', 
										domain=[('analytic_dimension_id.name','=','LOCATION')]
										)
	bisnis = fields.Many2many(comodel_name='account.analytic.tag', 
							string='Bisnis', 
							domain=[('analytic_dimension_id.name','=','BUSINESS')]
							)
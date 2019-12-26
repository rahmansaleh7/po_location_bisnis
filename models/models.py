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
	

class Orderpurchase(models.Model):
	_name = 'purchase.order'
	_inherit = 'purchase.order'

	@api.multi
	def button_confirm(self):

		res = super(Orderpurchase, self).button_confirm()
		for x in self:

			for y in x.env['stock.picking'].search([('origin','=', x.name),('picking_type_code','=','incoming')]):
				y.move_lines.account_analytic_id = x.order_line.account_analytic_id
				y.move_lines.analytic_tag_ids = x.order_line.analytic_tag_ids
				y.move_lines.bisnis = x.order_line.bisnis

		return res

# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Po_location_bisnis(models.Model):
	_name = 'stock.move'
	_inherit = 'stock.move'

	account_analytic_id = fields.Many2one(comodel_name='account.analytic.account', 
										string='Unit')
	analytic_tag_ids = fields.Many2one(comodel_name='account.analytic.tag',
										string='Lokasi', 
										domain=[('analytic_dimension_id.name','=','LOCATION')]
										)
	bisnis = fields.Many2one(comodel_name='account.analytic.tag',
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
			for order in x.order_line.search([('order_id','=',x.id)]):
				pick = x.env['stock.picking'].search([('origin','=', x.name),('picking_type_code','=','incoming')])
				move = x.env['stock.move'].search([('picking_id','=', pick.id)])
			
				for m in move:
					for y in pick :
						m.account_analytic_id = order.account_analytic_id
						m.analytic_tag_ids = order.lokasi
						m.bisnis = order.bisniss

		return res
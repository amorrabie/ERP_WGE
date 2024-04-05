# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductCustom(models.Model):
    _inherit = "product.template"

    cost_price = fields.Float(
        compute='_compute_cost_price',
        store=True,
        readonly=True
    )

    total_value = fields.Float(
        compute='_compute_total_value',
        store=True,
        readonly=True
    )
    marge = fields.Float(
        compute='_compute_marge',
        store=True,
        readonly=True
    )

    @api.depends('list_price', 'standard_price')
    def _compute_marge(self):
        for product in self:
            if product.list_price > 0:
                product.marge = product.list_price - product.last_purchase_price

    @api.depends('qty_available', 'last_purchase_price', 'standard_price')
    def _compute_total_value(self):
        for product in self:
            if product.last_purchase_price > 0:
                product.total_value = product.qty_available * product.last_purchase_price
            else:
                product.total_value = product.qty_available * product.standard_price

    @api.onchange('purchase_ok', 'last_purchase_price', 'standard_price', 'bom_ids.total_cost')
    def _compute_standard_price(self):
        for product in self:
            if product.purchase_ok:
                product.standard_price = product.last_purchase_price
                
            # <<<<<<<<<<<<<<<<<<<<standard_price based on total_cost>>>>>>>>>>>>>>>>>>>>>>>
            elif product.bom_ids and product.bom_ids.total_cost > 0:
                product.standard_price = product.bom_ids.total_cost

            else:
                product.standard_price = product.standard_price


class StockCustom(models.Model):
    _inherit = "product.product"
    total_value = fields.Float(
        compute='_compute_total_value',
        store=True,
        readonly=True
    )
    marge = fields.Float(
        compute='_compute_marge',
        store=True,
        readonly=True
    )

    @api.depends('qty_available', 'last_purchase_price', 'standard_price')
    def _compute_total_value(self):
        for product in self:
            if product.last_purchase_price > 0:
                product.total_value = product.qty_available * product.last_purchase_price
            else:
                product.total_value = product.qty_available * product.standard_price

    @api.depends('list_price', 'standard_price')
    def _compute_marge(self):
        for product in self:
            if product.list_price > 0:
                product.marge = product.list_price - product.last_purchase_price

    @api.depends('purchase_ok', 'last_purchase_price', 'standard_price')
    def _compute_cost_price(self):
        for product in self:
            if product.purchase_ok:
                product.standard_price = product.last_purchase_price


class MrpBomLineCustom(models.Model):
    _inherit = 'mrp.bom.line'

    cost_price = fields.Float(
        related='product_tmpl_id.cost_price',
        string='Cost Price',
        readonly=True,
        store=True,
    )

    class MrpBomCustom(models.Model):
        _inherit = 'mrp.bom'

        total_cost = fields.Float(string='Total Cost', compute='_compute_total_cost', store=True)

        @api.depends('bom_line_ids.cost_price', 'bom_line_ids.product_qty')
        def _compute_total_cost(self):
            for bom in self:
                total_cost = 0.0
                for line in bom.bom_line_ids:
                    total_cost += line.cost_price * line.product_qty
                bom.total_cost = total_cost

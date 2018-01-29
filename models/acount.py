# -*- coding: utf-8 -*-
# Copyright 2016 Serpent Consulting Services Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

from odoo import api, models,fields, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.one
    @api.depends('taxes_supp','amount_total')
    def _compute_amount_with_ttc(self):
        taxes = self.taxes_supp / 100
        self.amount_total_ttc = float(self.amount_total) * (1 + taxes)

    taxes_supp = fields.Float( string='Taxes Supp (%)',degits=(16,2),default=0.00, related='partner_id.amount_tax_supp',readony='1',store=True )

    amount_total_ttc = fields.Monetary(string='Total TTC',store=True, readonly=True, compute='_compute_amount_with_ttc')










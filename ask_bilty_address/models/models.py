# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    bilty_address = fields.Char(
        string="Logistics Address",
        help="This is the bilty/shipping address for gate pass."
    )

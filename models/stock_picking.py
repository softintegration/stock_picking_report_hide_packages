# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Picking(models.Model):
    _inherit = "stock.picking"

    def _compute_has_packages(self):
        res = super(Picking,self)._compute_has_packages()
        for picking in self:
            picking.has_packages = picking.has_packages and picking.picking_type_id.display_move_lines_packages
        return res




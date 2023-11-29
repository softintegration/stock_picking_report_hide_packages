# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    display_move_lines_packages = fields.Boolean(
        string='Display packages in report', default=True,
        help="If this case is checked,the system will display the move lines of the picking by packages in the report.")


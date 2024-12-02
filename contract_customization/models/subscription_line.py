from odoo import models


class SaleSubscriptionLine(models.Model):
    _inherit = "sale.subscription.line"
    
    def _prepare_account_move_line(self):
        self.ensure_one()
        account = (
            self.product_id.with_company(self.company_id).property_account_income_id
            or self.product_id.with_company(self.company_id).categ_id.property_account_income_categ_id
        )
        return {
            "product_id": self.product_id.id,
            "name": self.name,
            "quantity": self.product_uom_qty,
            "price_unit": self.price_unit,
            "discount": self.discount,
            "price_subtotal": self.price_subtotal,
            "tax_ids": [(6, 0, self.tax_ids.ids)],
            "product_uom_id": self.product_id.uom_id.id,
            "account_id": account.id,
        }
from openerp.osv import fields, osv

class custom_invoice(osv.osv):
    
  _inherit = "account.invoice"

  _columns = {
    'refr_invoice': fields.char('Previous Invoice Ref', size=80),
  }

custom_invoice()
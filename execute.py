from odoo_connect import OdooConnect
if __name__ == '__main__':
    odoo = OdooConnect()
    odoo.send_attendances()
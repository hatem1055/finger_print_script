import csv
import pyodbc
from datetime import date
from db_read import db
import requests


class OdooConnect:
    url = 'https://eogroup14-testing-1867126.dev.odoo.com'
    checks = db.get_checkinout_today()

    def send_attendances(self):
        for check in self.checks:
            data = {
                "params": {
                    "user_name": check.get('name',None),
                    "check_in": check.get('check_in',None),
                    "check_out": check.get('check_out',None)
                }}

            requests.post(f'{self.url}/create_attendance', json=data)


odoo = OdooConnect()

odoo.send_attendances()

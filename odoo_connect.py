import csv
import pyodbc
from datetime import date
from db_read import db
import requests
from time import sleep
import urllib3
#this to enable warnings because (verify = false) make the script crash
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class OdooConnect:
    url = 'https://eogroup14-testing-1867126.dev.odoo.com'
    checks = db.get_checkinout_today()
    def send_attendnee(self,check):
        data = {
            "params": {
                "user_name": check.get('name',None),
                "check_in": check.get('check_in',None),
                "check_out": check.get('check_out',None)
            }}
        requests.post(f'{self.url}/create_attendance', json=data,timeout=30,verify=False)
    def send_attendances(self):
        for check in self.checks:
            #this try and catch to avoid bad handshack error 
            try:
                self.send_attendnee(check)
            except:
                sleep(5)
                self.send_attendnee(check)



odoo = OdooConnect()

odoo.send_attendances()

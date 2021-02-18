import csv
import pyodbc
from datetime import date


class DB:
    # set up some constants
    MDB = 'F:/odoo reserved/eogrop trials/finger_print/att2000.mdb'
    DRV = '{MICROSOFT ACCESS DRIVER (*.mdb, *.accdb)}'
    PWD = 'pw'

    def get_cursur(self):
        # connect to db
        con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(
            self.DRV, self.MDB, self.PWD))
        return con.cursor()

    def get_user_name_by_id(self, id):
        SQL = f'SELECT name FROM userinfo WHERE userid = {id};'
        record = self.get_cursur().execute(SQL).fetchall()
        return record[0][0]
    def format_time(self,date):
        return date.strftime('%m/%d/%Y %I:%M:%S %p')
    def format_records(self, recs):
        output = {}
        for rec in recs:
            id = rec[0]
            date = self.format_time(rec[1])
            type = rec[2]
            if not(id in output):
                output[id] = {}
            output[id]['name'] = self.get_user_name_by_id(id)
            if type == 'I':
                output[id]['check_in'] = date
            else:
                output[id]['check_out'] = date
        return output.values()
    def get_checkinout_today(self):  
        today = date.today().strftime("%m/%d/%Y")
        SQL = f'SELECT * FROM checkinout WHERE checktime Between #{today} 00:00:00# And #{today} 23:59:59 PM#;' 
        recs = self.get_cursur().execute(SQL).fetchall()
        return self.format_records(recs)

db = DB()
# print(db.get_checkinout_today())


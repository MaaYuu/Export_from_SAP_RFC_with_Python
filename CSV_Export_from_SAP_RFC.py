from pyrfc import Connection
import csv
import sys
from datetime import datetime, date

ASHOST='10.10.10.10'
CLIENT='100'
SYSNR='00'
USER='RFCUSER'
PASSWD='RFCPASSW'
conn = Connection(ashost=ASHOST, sysnr=SYSNR, client=CLIENT, user=USER, passwd=PASSWD)

datadate = sys.argv[1]

today = date.today()
vCurrDate = today.strftime('%Y-%m-%d')
vTimestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

result = conn.call('ZSD_033_FM_FULL', IV_DATADATE=datadate)
table = list(result.keys())[0] 

csv_columns = list(result[table][0].keys())
csv_columns.append('TIMESTAMP')

dict_data = result[table]
dict_data[0]['TIMESTAMP'] = vTimestamp

csv_file = './ExampleFile_' + vCurrDate + '.csv'

with open(csv_file, 'w', encoding='utf-8-sig', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = csv_columns, delimiter = ';')
    writer.writeheader()
    writer.writerows(dict_data)
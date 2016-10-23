'''
Author: Bhishan Bhandari
bbhishan@gmail.com
skype: vsun.eror

'''

import subprocess 
import glob
import time
import csv
csvwriter = csv.writer(file('final.csv', 'wb'))
csvwriter.writerow(['Description', 'Withdrawals', 'Deposits', 'Date', 'Balance'])

def parse_pdf_buffer(buffer_file):
    with open(buffer_file, 'rb') as f:
        all_content = f.readlines()
        for each_line in all_content[26:]:
            desc_part = each_line[:40]
            withdraw_part = each_line[40:70]
            deposit_part = each_line[70:95]
            date_part = each_line[95:103]
            balance_part = each_line[103:]
            description = " ".join(desc_part.split())
            withdraws = " ".join(withdraw_part.split())
            deposits = " ".join(deposit_part.split())
            date = " ".join(date_part.split())
            balance = " ".join(balance_part.split())
            csvwriter.writerow([description, withdraws, deposits, date, balance])

def read_pdf_file(file_name):
    print file_name
    try:
        fileptr = open('pdfbuffer.txt', 'wb')
        command_out = subprocess.Popen(['less', file_name], stdout=fileptr, stderr=subprocess.STDOUT)
        time.sleep(2)
        parse_pdf_buffer('pdfbuffer.txt')
    except:
        print "failed for file", file_name

def main():
    for file_name in glob.glob("*.pdf"):
        read_pdf_file(file_name) 

if __name__ == '__main__':
    main()

import PyPDF2 as pdf
import pandas as pd
import numpy as np
import pymysql

connection = pymysql.connect(host="localhost", user="root", password="toor", db="Core")
cursor = connection.cursor()

PDFfile = open("ABC COMPLETION LISTS.pdf", "rb")
pdfRead = pdf.PdfFileReader(PDFfile)

x = pdfRead.getPage(0)

text = x.extractText()

data = {'Floor':[],'Section':[], 'Unit':[], 'Date Complete':[], 'Contractor':[], 'Problem':[], 'Status':[]}

df = pd.DataFrame(data)

sql1 = "insert into organized(floor, section, unit, date_done, contractor, problem, status_check) values (%s, %s, %s, %s, %s, %s, %s)"

# floors: 1-4
# section a-c
# unit 440-454
# problems:
# •	BR DOOR NEEDS PAINT
# •	PEEPHOLE NEEDED
# •	MAJOR CUTS IN DRYWALL
# •	VENT COVER
# •	DOORS NEEDING PAINT
# •	ACCESS PANEL COVERS
# •	FART FAN
# •	SHOWER RODS
# •	ACCESS PANEL COVERS
# •	KNEEBOARD NEEDS
# •	TRIM NEEDS PAINT
# •	OUTLET COVERS
# •	THERMOSTAT
# •	SMOKE
# •	CARPET
# •	LIGHT IN KITCHEN


insert_data = ('440', 'N', 'N', 'BR DOOR NEEDS PAINT', 'Not', 'N')



if "ECTION" and "A" and "440" and "BR DOOR NEEDS PAINT" and "Floor" and "4" in text:
    cursor.execute(sql1, insert_data)
    connection.commit()

elif "SECTION B" and "461" and "SMOKE MISSING" in text:
    data = {'Section': ['B'], 'Unit': ['440'], 'Date Complete': ['A'], 'Contractor': ['N/A'], 'Problem': ['1'], 'Status': ['N/A']}
    df = pd.DataFrame(data)

print(df)
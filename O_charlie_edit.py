import pandas as pd
import pymysql
# I use re to help break up string by number and character
import re

# In this code I assume that Floor must be numeric, Section must be Alphabetic.
# Instead of reading from PDF, this code read from txt that's generated by GS, a pdf to txt software.
connection = pymysql.connect(host="localhost", user="root", password="000000", db="sys")
cursor = connection.cursor()

TXTfile = open("output.txt", "r")
whole_doc = TXTfile.readlines()

data = {'Floor':[],'Section':[], 'Unit':[], 'Date Complete':[], 'Contractor':[], 'Problem':[], 'Status':[]}
df = pd.DataFrame(data)

sql1 = "insert into organized(floor, section, unit, date_done, contractor, problem, status_check) values (%s, %s, %s, %s, %s, %s, %s)"

floor = ""
section = ""
unit = ""
current_string = ""

# Logic, break txt into list of strings, iterate thru these string and if a problem is read, inject sql. Elif read digit
# assume it's unit number, use it to update unit. Elif read FLOOR and SECTION, update floor and section. Elif read FLOOR
# then update floor. Elif read SECTION, update section.
for j in whole_doc:
    j = j.strip()
    if j.startswith('â€¢'): # Only if the symbol remains the same.
        injection = (floor, section, unit, 'N', 'N', j.replace('â€¢   ', ''), 'Not')
        print(floor + " " + section + " " + unit + " " + j.replace('â€¢   ', ''))
        cursor.execute(sql1, injection)
        connection.commit()
        continue
    elif j.replace('-', '').isdigit(): # if only digit left after stripping '-', assume it's unit number.
        unit = j.replace('-', '')
        continue
    elif 'FLOOR' in j.upper() and 'SECTION' in j.upper(): # If both FLOOR and SECTION in same line, break them.
        current_string = j.upper().replace('FLOOR', '').replace('SECTION', '') # Strip FLOOR SECTION, leave only number and section.
        floor = re.findall('\d+', current_string)[0]
        continue
    elif 'FLOOR' in j.upper():
        current_string = j.upper().replace('FLOOR', '').strip()
        floor = re.findall('\d+', current_string)[0]
        continue
    elif 'SECTION' in j.upper():
        section = j.upper().replace('SECTION', '').strip()
        continue
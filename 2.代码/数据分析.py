

import xlrd

book = xlrd.open_workbook(r'F:\income.xlsx')

print(f"包含表单数量 {book.nsheets}")
print(f"表单的名分别为: {book.sheet_names()}")
import pandas
bk=pandas.read_excel(r'F:\income.xlsx',sheet_name=1)
print(bk.head())
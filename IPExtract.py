import xlrd

file_location = "location/file_name.xlsx"

workbook = xlrd.open_workbook(file_location)

sheet = workbook.sheet_by_name('sheet')

x = []

for rownum in range(sheet.nrows):
    x.append(sheet.cell(rownum, 7))

print(x)

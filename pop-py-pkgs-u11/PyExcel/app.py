import openpyxl

wb = openpyxl.load_workbook("transactions.xlsx")

sheet = wb["Sheet1"]

for row in range(1,10):
    cell = sheet.cell(row,1)
    print(cell.value)
sheet.append([1,2,3])

wb.save("transaction3.xlsx")
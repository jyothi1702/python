import xlsxwriter
workbook=xlsxwriter.Workbook("addemp.xlsx")
worksheet=workbook.add_worksheet("mysheet")
scores = (
    ['an', 1000],
    ['ra',   100],


)
col=0
row=0
for name,score in scores:
    worksheet.write(row,col,name)
    worksheet.write(row,col+1,score)
    row+=1
workbook.close

import xlrd, os

#os.listdir('.')
book = xlrd.open_workbook('phailin_tweets.xls')
worksheet = book.sheet_by_name('')
num_rows = worksheet.nrows - 1
curr_row = -1
while curr_row < num_rows:
                if 
                curr_row += 1
                row  = worksheet.row(curr_row)
                print row
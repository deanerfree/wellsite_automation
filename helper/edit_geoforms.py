from helper.workbook_func import create_workbook, check_rows_used, write_to_wb
# porosity_log = r"/mnt/c/Users/kurti/OneDrive/Desktop/SPL 1-13 HZ 104 MARTENH 04-17-074-25W4/WL_0504937-04-04-17-074-25W4-00_Geoforms.xlsm"
# data =  {'por0': 92.0, 'por1': 88.5, 'por2': 371.5, 'por3': 628.0, 'por4': 305.0, 'por5': 8.5}
# output_file=r"/mnt/c/Users/kurti/OneDrive/Desktop/SPL 1-13 HZ 104 MARTENH 04-17-074-25W4/demo.xlsm"

def edit_geo_forms(input_file, data, output_file):
  wb = create_workbook(input_file, True)
  wb_edit = create_workbook(input_file, False)

  sheets = wb.sheetnames
  count = 0

  for iteration, sheet in enumerate(sheets):
    if (sheet == 'Porosity Log'):
      count = iteration

  porosity_sheet = wb[sheets[count]]
  porosity_sheet_edit = wb_edit[sheets[count]]

  list_of_rows_used = check_rows_used(porosity_sheet)
  # wb = load_workbook(porosity_log, data_only=True)


  print(list_of_rows_used["rows_used"][-1][3:])

  write_to_wb(porosity_sheet_edit, list_of_rows_used, data)
  wb_edit.save(output_file)
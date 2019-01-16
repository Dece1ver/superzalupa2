import xlrd


def if_int(str):
    if str[-2:] == '.0':
        str = str[:-2]
        return str
    else:
        return str


def if_empty(str):
    if str in ('""', "''"):
        str = ''
        return str
    else:
        return str


def get_wia_details(details=[]):
    file = xlrd.open_workbook('./misc/WIA.xlsx')
    sheet = file.sheet_by_index(0)
    for row in range(5, sheet.nrows):
        detail = str(sheet.row(row)[0]).replace('text:', '').replace('empty:', '')
        detail = detail[1:-1]
        machine_time = str(sheet.row(row)[1]).replace('number:', '').replace('text:', '').replace('empty:', '')
        machine_time = if_int(machine_time)
        machine_time = if_empty(machine_time)
        replace_time = str(sheet.row(row)[2]).replace('number:', '').replace('text:', '').replace('empty:', '')
        replace_time = if_int(replace_time)
        replace_time = if_empty(replace_time)
        setup_time = str(sheet.row(row)[4]).replace('number:', '').replace('text:', '').replace('empty:', '')
        setup_time = if_int(setup_time)
        setup_time = if_empty(setup_time)

        detail = f'{detail: <49} наладка: {setup_time: <3} машинное время: {machine_time: <4} замена: {replace_time: <3}'

        details.append(detail)
        # print(detail)
    return details


def get_200_details(details=[]):
    file = xlrd.open_workbook('./misc/200.xlsx')
    sheet = file.sheet_by_index(0)
    for row in range(5, sheet.nrows):
        detail = str(sheet.row(row)[0]).replace('text:', '').replace('empty:', '')
        detail = detail[1:-1]
        machine_time = str(sheet.row(row)[1]).replace('number:', '').replace('text:', '').replace('empty:', '')
        machine_time = if_int(machine_time)
        machine_time = if_empty(machine_time)
        replace_time = str(sheet.row(row)[2]).replace('number:', '').replace('text:', '').replace('empty:', '')
        replace_time = if_int(replace_time)
        replace_time = if_empty(replace_time)
        setup_time = str(sheet.row(row)[4]).replace('number:', '').replace('text:', '').replace('empty:', '')
        setup_time = if_int(setup_time)
        setup_time = if_empty(setup_time)

        detail = f'{detail: <49} наладка: {setup_time: <3} машинное время: {machine_time: <4} замена: {replace_time: <3}'

        details.append(detail)
        # print(detail)
    return details


# if __name__ == '__main__':
#     get_wia_details()
#     get_200_details()

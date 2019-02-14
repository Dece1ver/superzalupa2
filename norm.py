import xlrd
import os
import logging

programm_dir, _ = os.path.split(__file__)
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s : %(thread)d : %(threadName)s : %(asctime)s :\n%(message)s\n')


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
    file = xlrd.open_workbook(os.path.join(programm_dir, 'misc', 'WIA.xlsx'))
    sheet = file.sheet_by_index(0)
    logging.info(file)
    for row in range(5, sheet.nrows):
        logging.debug(sheet.row(row))
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
    file = xlrd.open_workbook((os.path.join(programm_dir, 'misc', '200.xlsx')))
    sheet = file.sheet_by_index(0)
    logging.info(file)
    for row in range(5, sheet.nrows):
        logging.debug(sheet.row(row))
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

        detail = f'{detail: <48} наладка: {setup_time: <3} машинное время: {machine_time: <4} замена: {replace_time: <3}'

        details.append(detail)
        # print(detail)
    return details


def get_350_details(details=[]):
    file = xlrd.open_workbook((os.path.join(programm_dir, 'misc', '350.xlsx')))
    sheet = file.sheet_by_index(1)
    logging.info(file)
    for row in range(5, sheet.nrows):
        logging.debug(sheet.row(row))
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

        detail = f'{detail: <48} наладка: {setup_time: <3} машинное время: {machine_time: <4} замена: {replace_time: <3}'

        details.append(detail)
        # print(detail)
    return details


# if __name__ == '__main__':
#     get_wia_details()
#     get_200_details()

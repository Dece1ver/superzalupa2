# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from design import Ui_MainWindow  # импорт сгенерированного файла дизайна
from datetime import datetime
import norm
import time
import sys
import os
import logging
import configparser

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s : %(thread)d : %(threadName)s : %(asctime)s :\n%(message)s\n')
if not os.path.isfile('settings.ini'):
    logging.info('Settings file not found, creating a new one.')
    config = configparser.ConfigParser()
    config['SETTINGS'] = {'FastScanCheckboxState': 'False',
                          'IgnoredFiles': '.PBG, PYC, .PY, .PYW, .KV, .UI, .MP3, .FLAC, .WAV, .OGG, .JPG, .JPEG, .BMP, .ICO, .TIFF, .JPE, .OXPS, .PSD, .PNG, .GIF, .MPEG, .MP4, .WEBM, .WMA, .FLV, .MOV, 3GP, .AVI, .VOB, .EXE, .RAR, .ZIP, .7Z, .MSI, .INSTALL, .APK, .XLS, .XLSX, .WPS, .FRW, .INI, .CFG, .DB, .DAT, .TMP, .DOC, .DOCX, .PDF, .DJVU, .FB2, .EPUB, .DB, .LNK, .URL, .HTML, .GP3, .GP4, .GP5, .GPX, .CDW, .FRW, .M3D, .KDW, .SPW, .A3D, .SYS, .HLP, .HTM, .HTML, .PPT, .COM'}

    with open('settings.ini', 'w') as config_file:
        config.write(config_file)
settings_file = 'settings.ini'


def get_badfiles(path):
    config = configparser.ConfigParser()
    config.read(settings_file)
    badfiles_string = config['SETTINGS']['IgnoredFiles']
    return badfiles_string


def get_chexbox_status(path):
    config = configparser.ConfigParser()
    config.read(settings_file)
    status = config['SETTINGS']['FastScanCheckboxState']
    if status == 'True':
        return True
    else:
        return False


def set_badfiles(badfiles_string):
    badfiles = badfiles_string.upper().replace(' ', '')
    badfiles = badfiles.split(',')
    while '' in badfiles:
        badfiles.remove('')
    badfiles = tuple(badfiles)
    return badfiles


badfiles = set_badfiles(get_badfiles(settings_file))
logging.info(f'BadFiles: {badfiles}')


class MyInterface(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyInterface, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cwd = os.getcwd()
        self.ui.scaner_path.setText(self.ui.cwd)
        self.ui.scaner_button.clicked.connect(self.scaner_button_handler)
        self.ui.rename_mazatrol_button.clicked.connect(self.rename_mazatrol)
        self.ui.rename_fanuc_button.clicked.connect(self.rename_fanuc)
        self.ui.rename_mazatrol_button.setEnabled(False)
        self.ui.rename_fanuc_button.setEnabled(False)
        self.ui.scaner_path_dialog_button.clicked.connect(self.get_path)
        self.ui.action.triggered.connect(self.show_settings)
        self.ui.action_2.triggered.connect(self.show_wia_norm)
        self.ui.action_3.triggered.connect(self.show_help)
        self.ui.action_4.triggered.connect(self.show_200_norm)
        self.ui.action_5.triggered.connect(self.close)
        self.ui.label_fanuc_list.clicked.connect(self.change_fanuc_view)
        self.ui.label_mazatrol_list.clicked.connect(self.change_mazatrol_view)
        self.ui.progressBar.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        self.ui.statusbar.showMessage('Кнопки переименовывателей станут активны после сканирования.')
        self.fast_scan_check = get_chexbox_status(settings_file)
        logging.info(f'Readed status: {self.fast_scan_check}')

        # созданиие инстанса потока сканера и подключение сигналов
        self.scaner_thread = ScanerThread()
        self.scaner_thread.started.connect(self.on_start)
        self.scaner_thread.scaner_signal.connect(self.add_file)
        self.scaner_thread.finished.connect(self.finish_scan)

        # создание инстанса потока мазаковского переименовывателя с сигналами
        self.rename_mazatrol_thread = MazatrolRenamer()
        self.rename_mazatrol_thread.mazatrol_signal.connect(self.add_mazatrol_file, QtCore.Qt.QueuedConnection)
        self.rename_mazatrol_thread.finished.connect(self.finish_rename_mazatrol)

        # создание инстанса потока фанусковского переименовывателя с сигналами
        self.rename_fanuc_thread = FanucRenamer()
        self.rename_fanuc_thread.fanuc_signal.connect(self.add_fanuc_file, QtCore.Qt.QueuedConnection)
        self.rename_fanuc_thread.finished.connect(self.finish_rename_fanuc)

    # реализовал как еблан, надо сделать одну функцию на вывод обоих окон с нормами
    def show_wia_norm(self):
        norm_label = 'Нормы для SKT/WIA:'
        norm_window = QtWidgets.QWidget(self, Qt.Window)
        norm_window.setWindowModality(QtCore.Qt.WindowModal)
        norm_window.setMinimumSize(700, 500)
        norm_window.setMaximumSize(700, 500)
        norm_window.setWindowTitle('Нормы')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(norm_window.sizePolicy().hasHeightForWidth())
        norm_window.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("window.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        norm_window.setWindowIcon(icon)
        label = QtWidgets.QLabel(norm_window)
        label.setText(norm_label)
        label.setGeometry(QtCore.QRect(10, 0, 691, 31))
        label.setObjectName("label")
        line = QtWidgets.QFrame(norm_window)
        line.setGeometry(QtCore.QRect(10, 20, 681, 16))
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
        norm_list = QtWidgets.QListWidget(norm_window)
        norm_list.setEnabled(True)
        norm_list.setGeometry(QtCore.QRect(1, 30, 698, 469))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(norm_list.sizePolicy().hasHeightForWidth())
        norm_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        norm_list.setFont(font)
        norm_list.addItems(norm.get_wia_details())
        norm_window.show()

    def show_200_norm(self):
        norm_label = 'Нормы для Мазака 200ML:'
        norm_window = QtWidgets.QWidget(self, Qt.Window)
        norm_window.setWindowModality(QtCore.Qt.WindowModal)
        norm_window.setMinimumSize(700, 500)
        norm_window.setMaximumSize(700, 500)
        norm_window.setWindowTitle('Нормы')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(norm_window.sizePolicy().hasHeightForWidth())
        norm_window.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("window.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        norm_window.setWindowIcon(icon)
        label = QtWidgets.QLabel(norm_window)
        label.setText(norm_label)
        label.setGeometry(QtCore.QRect(10, 0, 691, 31))
        label.setObjectName("label")
        line = QtWidgets.QFrame(norm_window)
        line.setGeometry(QtCore.QRect(10, 20, 681, 16))
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
        norm_list = QtWidgets.QListWidget(norm_window)
        norm_list.setEnabled(True)
        norm_list.setGeometry(QtCore.QRect(1, 30, 698, 469))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(norm_list.sizePolicy().hasHeightForWidth())
        norm_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        norm_list.setFont(font)
        norm_list.addItems(norm.get_200_details())
        norm_window.show()

    def show_help(self):
        help_window = QtWidgets.QMessageBox(4, 'Справка', 'Что-то будет когда-нибудь')
        help_window.exec()

    def save_settings(self):

        logging.info(f'Fast scan checkbox status: {self.check_box.isChecked()}\nRead Ignored Files: {self.textBrowser.toPlainText()}')
        config = configparser.ConfigParser()
        config['SETTINGS'] = {'FastScanCheckboxState': str(self.check_box.isChecked()), 'IgnoredFiles': self.textBrowser.toPlainText().upper()}

        with open(settings_file, 'w') as config_file:
            config.write(config_file)

        self.fast_scan_check = self.check_box.isChecked()
        badfiles = set_badfiles(get_badfiles(settings_file))
        logging.info(f'BadFiles: {badfiles}')
        self.settings.close()

    # окно с настройками (через жопу, надо наверно переделать, но хз как)
    def show_settings(self):
        self.settings = QtWidgets.QWidget(self, Qt.Window)
        self.settings.setWindowModality(QtCore.Qt.WindowModal)
        self.settings.resize(400, 300)
        self.settings.setWindowTitle('Настройки')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("window.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setWindowIcon(icon)
        label = QtWidgets.QLabel(self.settings)
        label.setText('Выбор настроек:')
        label.setGeometry(QtCore.QRect(10, 0, 391, 31))
        label.setObjectName("label")
        line = QtWidgets.QFrame(self.settings)
        line.setGeometry(QtCore.QRect(10, 20, 381, 16))
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
        self.check_box = QtWidgets.QCheckBox(self.settings)
        self.check_box.setText('Быстрое сканирование')
        self.check_box.setGeometry(QtCore.QRect(10, 30, 191, 17))
        self.check_box.setObjectName("check_box")

        self.check_box.setChecked(self.fast_scan_check)
        label_2 = QtWidgets.QLabel(self.settings)
        label_2.setText('При сканировании отключает моментальное добавление элементов в списки интерфейса. Рекомендуется использовать, когда предполагаемое количество управляющих программ больше тысячи.')
        label_2.setGeometry(QtCore.QRect(10, 50, 381, 41))
        label_2.setWordWrap(True)
        label_2.setIndent(0)
        label_2.setObjectName("label_2")
        line_2 = QtWidgets.QFrame(self.settings)
        line_2.setGeometry(QtCore.QRect(10, 90, 381, 16))
        line_2.setFrameShape(QtWidgets.QFrame.HLine)
        line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_2.setObjectName("line_2")
        label_3 = QtWidgets.QLabel(self.settings)
        label_3.setText('Расширения файлов, исключенные для сканирования:')
        label_3.setGeometry(QtCore.QRect(10, 100, 381, 16))
        label_3.setObjectName("label_3")
        pushButton = QtWidgets.QPushButton(self.settings)
        pushButton.setText('Сохранить')
        pushButton.setGeometry(QtCore.QRect(300, 270, 91, 23))
        pushButton.setObjectName("pushButton")
        pushButton.clicked.connect(self.save_settings)
        badfiles_string = get_badfiles(settings_file)
        self.textBrowser = QtWidgets.QPlainTextEdit(self.settings)
        self.textBrowser.setGeometry(QtCore.QRect(10, 120, 381, 141))
        self.textBrowser.setStyleSheet("font: 10pt \"Consolas\";")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.insertPlainText(badfiles_string)
        if self.scaner_thread.status:
            self.check_box.setEnabled(False)
            self.textBrowser.setEnabled(False)
            pushButton.setEnabled(False)
        self.settings.show()

    # получает путь с кнопки
    def get_path(self):
        new_path = QtWidgets.QFileDialog.getExistingDirectory()
        if new_path != '':
            self.ui.cwd = new_path
        self.ui.scaner_path.setText(self.ui.cwd)
        logging.info(f'Set new path to: "{self.ui.cwd}"')
        self.ui.rename_mazatrol_button.setEnabled(False)
        self.ui.rename_fanuc_button.setEnabled(False)

    # получает название детали из мазаковской программы
    def get_mazatrol_name(self, full_path_to_file):
        with open(full_path_to_file, 'rb') as file:
            file.seek(80)
            file_name = file.read(32).rstrip(b'\x00').decode()
            file_name = file_name.replace('\\', '-').replace('*', '-').replace('/', '-').strip(' ')
            return file_name

    # проверяет является ли файл фануковской пограммой (наличием % или O вначале)
    def check_fanuc_programm(self, full_path_to_file):
        try:
            with open(full_path_to_file, 'r') as f:
                first_symbols = f.read(2)
                if first_symbols in ('%\n', 'O0'):
                    return True
                else:
                    return False
        except PermissionError:
            return False
        except UnicodeDecodeError:
            return False

    # получает название детали из фануковской программы
    def get_fanuc_name(self, full_path_to_file):
        try:
            with open(full_path_to_file, 'rb') as f:
                f.seek(2)
                file_name = f.read(55)
                if b')' not in file_name:
                    try:
                        file_name.decode()
                        file_name = 'Название отсутствует!'
                    except UnicodeDecodeError:
                        file_name = 'Скорее всего это не программа Fanuc!'

                else:
                    file_name = file_name.split(b'(')
                    file_name = file_name[1].split(b')')
                    file_name = file_name[0].decode()
                    file_name = file_name.replace('\\', '-').replace('*', '-').replace('/', '-').strip(' ')

            return file_name
        except ZeroDivisionError:
            return f'Не удалось получить имя файла: {full_path_to_file}'
            self.error_files.append(self.full_path_to_file)

    def scaner(self):

        self.mazatrol_files = []
        self.fanuc_files = []
        self.mazatrol_labels = []
        self.fanuc_labels = []

        # логи до сканирования
        logging.info('Scaner started.')
        logging.info(f'''Lists len:
            len(self.mazatrol_files) = {len(self.mazatrol_files)}
            len(self.mazatrol_files) = {len(self.fanuc_files)}
            len(self.mazatrol_labels) = {len(self.mazatrol_labels)}
            len(self.fanuc_labels) = {len(self.fanuc_labels)}''')

        self.ui.mazatrol_list_widget.clear()
        self.ui.fanuc_list_widget.clear()
        self.ui.info_window.clear()

        self.ui.info_window.insertPlainText(f'Сканирование директории "{self.ui.cwd}"...\n')
        self.ui.progressBar.setRange(0, 0)
        self.ui.progressBar.setValue(-1)
        self.scaner_thread.start()

    def scaner_button_handler(self):
        logging.info(f'Scaner thread status is: "{self.scaner_thread.status}"')
        if self.scaner_thread.status:
            self.stop_scaner()
        else:
            self.scaner()

    def on_start(self):
        self.ui.scaner_button.setText('Остановить')
        self.ui.label_mazatrol_list.setEnabled(False)
        self.ui.label_fanuc_list.setEnabled(False)

    def stop_scaner(self):
        self.scaner_thread.running = False

    def add_file(self, full_path_to_file, file_label):
        if self.fast_scan_check:
            if full_path_to_file.upper().endswith('.PBG'):
                self.ui.label_mazatrol_list.setText(f'Файлов Mazatrol: {len(self.mazatrol_files)}')
            else:
                self.ui.label_fanuc_list.setText(f'Файлов Fanuc: {len(self.fanuc_files)}')
        else:
            if full_path_to_file.upper().endswith('.PBG'):
                item = QtWidgets.QListWidgetItem()
                self.ui.mazatrol_list_widget.addItem(item)
                item.setText(file_label)
                self.ui.mazatrol_list_widget.setCurrentItem(item)
                self.ui.label_mazatrol_list.setText(f'Файлов Mazatrol: {len(self.mazatrol_files)}')
            else:
                item = QtWidgets.QListWidgetItem()
                self.ui.fanuc_list_widget.addItem(item)
                item.setText(file_label)
                self.ui.fanuc_list_widget.setCurrentItem(item)
                self.ui.label_fanuc_list.setText(f'Файлов Fanuc: {len(self.fanuc_files)}')

        self.ui.statusbar.showMessage('Сканировние.')

    def finish_scan(self):

        if len(self.mazatrol_files) != 0:
            if self.fast_scan_check:
                self.ui.mazatrol_list_widget.addItems(self.mazatrol_labels)
            self.ui.label_mazatrol_list.setEnabled(True)
            self.ui.rename_mazatrol_button.setEnabled(True)
            self.ui.statusbar.showMessage('Можно переименовывать.')
            self.ui.info_window.insertPlainText(f'Файлов Mazatrol: {len(self.mazatrol_files)}\n')
            self.ui.label_mazatrol_list.setText(f'Файлов Mazatrol: {len(self.mazatrol_files)}')
        else:
            self.ui.label_mazatrol_list.setText(f'Файлов Mazatrol не найдено.')
            self.ui.info_window.insertPlainText(f'Файлов Mazatrol не найдено.\n')

        if len(self.fanuc_files) != 0:
            if self.fast_scan_check:
                self.ui.fanuc_list_widget.addItems(self.fanuc_labels)
            self.ui.label_fanuc_list.setEnabled(True)
            self.ui.rename_fanuc_button.setEnabled(True)
            if self.scaner_thread.status:
                self.ui.statusbar.showMessage('Можно переименовывать.')
            else:
                self.ui.statusbar.showMessage('Сканирование остановлено. Рекомендуется отсканировать снова.')
            self.ui.info_window.insertPlainText(f'Файлов Fanuc: {len(self.fanuc_files)}\n')
            self.ui.label_fanuc_list.setText(f'Файлов Fanuc: {len(self.fanuc_files)}')
        else:
            self.ui.label_fanuc_list.setText(f'Файлов Fanuc не найдено.')
            self.ui.info_window.insertPlainText(f'Файлов Fanuc не найдено.\n')

        if self.mazatrol_files == 0 and self.fanuc_files == 0:
            self.ui.statusbar.showMessage('Нечего переименовывать.')

        # логи после сканирования
        logging.info('Scaner finished.')
        logging.info(f'''Lists len:
            len(self.mazatrol_files) = {len(self.mazatrol_files)}
            len(self.mazatrol_files) = {len(self.fanuc_files)}
            len(self.mazatrol_labels) = {len(self.mazatrol_labels)}
            len(self.fanuc_labels) = {len(self.fanuc_labels)}''')

        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(0)

        self.ui.scaner_button.setText('Сканировать')
        self.scaner_thread.status = False

        self.fanuc_view = True
        self.mazatrol_view = True

    def change_fanuc_view(self):
        if not self.fanuc_view:
            self.ui.fanuc_list_widget.clear()
            self.ui.fanuc_list_widget.addItems(self.fanuc_labels)
            self.fanuc_view = True
        else:
            self.ui.fanuc_list_widget.clear()
            self.ui.fanuc_list_widget.addItems(self.fanuc_files)
            self.fanuc_view = False

    def change_mazatrol_view(self):
        if not self.mazatrol_view:
            self.ui.mazatrol_list_widget.clear()
            self.ui.mazatrol_list_widget.addItems(self.mazatrol_labels)
            self.mazatrol_view = True
        else:
            self.ui.mazatrol_list_widget.clear()
            self.ui.mazatrol_list_widget.addItems(self.mazatrol_files)
            self.mazatrol_view = False

    # переименовыватель мазаковских программ
    def rename_mazatrol(self, mazatrol_files):
        self.ui.info_window.clear()
        self.error_files = []
        self.ui.progressBar.setRange(0, len(self.mazatrol_files))
        self.ui.progressBar.setValue(0)
        self.progress_bar_steps = 0
        self.count = 0
        self.rename_mazatrol_thread.start()

    def add_mazatrol_file(self, file_name, new_file_name):
        if file_name == new_file_name:
            self.ui.info_window.insertPlainText(f'Программа "{file_name}" уже называется как надо, пропуск.\n')
            self.error_files.append(f'{file_name} уже называется как надо.')
        elif new_file_name == 'Название отсутствует!':
            self.ui.info_window.insertPlainText(f'Программа "{file_name}" не имеет названия внутри, пропуск.\n')
            self.error_files.append(f'{file_name} не имеет названия внутри.')
        else:
            self.ui.info_window.insertPlainText(f'{file_name} переименован в {new_file_name}\n')
            self.count += 1
        self.progress_bar_steps += 1
        self.ui.progressBar.setValue(self.progress_bar_steps)
        self.ui.info_window.ensureCursorVisible()

    def finish_rename_mazatrol(self):
        self.ui.info_window.insertPlainText(f'\nПереименовано {self.count} из {len(self.mazatrol_files)} файлов.')
        self.ui.info_window.ensureCursorVisible()
        self.ui.info_window.insertPlainText(f'\n\nОшибок {len(self.error_files)}:\n')
        self.ui.info_window.insertPlainText('\n'.join(self.error_files))
        self.ui.rename_mazatrol_button.setEnabled(False)
        self.ui.statusbar.showMessage('Переименовывание завершено.')

        logging.info(f'Renamed {self.count} from {len(self.mazatrol_files)}. Errors: {len(self.error_files)}')

        self.open_cwd_dialog()

    # переименовыватель фануковских программ
    def rename_fanuc(self, fanuc_files):
        self.ui.info_window.clear()
        self.error_files = []
        self.ui.progressBar.setRange(0, len(self.fanuc_files))
        self.ui.progressBar.setValue(0)
        self.progress_bar_steps = 0
        self.count = 0
        self.rename_fanuc_thread.start()

    def add_fanuc_file(self, file_name, new_file_name):
        if file_name == new_file_name:
            self.ui.info_window.insertPlainText(f'Программа "{file_name}" уже называется как надо, пропуск.\n')
            self.error_files.append(f'{file_name} уже называется как надо.')
        elif new_file_name == 'Название отсутствует!':
            self.ui.info_window.insertPlainText(f'Программа "{file_name}" не имеет названия внутри, пропуск.\n')
            self.error_files.append(f'{file_name} не имеет названия внутри.')
        else:
            self.ui.info_window.insertPlainText(f'{file_name} переименован в {new_file_name}\n')
            self.count += 1
        self.progress_bar_steps += 1
        self.ui.progressBar.setValue(self.progress_bar_steps)
        self.ui.info_window.ensureCursorVisible()

    def finish_rename_fanuc(self):
        self.ui.info_window.insertPlainText(f'\nПереименовано {self.count} из {len(self.fanuc_files)} файлов.')
        self.ui.info_window.ensureCursorVisible()
        self.ui.info_window.insertPlainText(f'\n\nОшибок {len(self.error_files)}:\n')
        self.ui.info_window.insertPlainText('\n'.join(self.error_files))
        self.ui.rename_fanuc_button.setEnabled(False)
        self.ui.statusbar.showMessage('Переименовывание завершено.')

        logging.info(f'Renamed {self.count} from {len(self.fanuc_files)}. Errors: {len(self.error_files)}')

        self.open_cwd_dialog()

    def open_cwd_dialog(self):
        message_box = QtWidgets.QMessageBox(4, 'Переименовывание завершено', 'Открыть папку с программами?')
        message_box.addButton(QtWidgets.QPushButton('Да'), QtWidgets.QMessageBox.YesRole)
        message_box.addButton(QtWidgets.QPushButton('Нет'), QtWidgets.QMessageBox.NoRole)
        result = message_box.exec()
        if result == 0:
            os.startfile(self.ui.cwd)
            logging.info('Open CWD')


class ScanerThread(QThread, MyInterface):

    scaner_signal = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)
        self.running = False
        self.status = False

    def __del__(self):
        self.wait()

    def run(self):
        self.running = True
        self.status = True
        logging.info(f'Scaner thread is started')
        for dir_paths, dir_names, file_names in os.walk(application.ui.cwd):
            if not self.status:
                logging.info(f'Highlevel terminating')
                break
            for file in file_names:
                if not self.running:
                    logging.info(f'Lowlevel terminating')
                    self.status = False
                    break
                full_path_to_file = os.path.join(dir_paths, file)
                if full_path_to_file.upper().endswith('.PBG'):
                    application.mazatrol_files.append(full_path_to_file)
                    programm_name = application.get_mazatrol_name(full_path_to_file)
                    file_label = f'{file: <8}:({programm_name})'
                    application.mazatrol_labels.append(file_label.replace('/', '\\'))
                    logging.debug(f'File "{file_label}" appended to list')
                    self.scaner_signal.emit(full_path_to_file, file_label)
                else:
                    if not full_path_to_file.upper().endswith(badfiles):
                        check = self.check_fanuc_programm(full_path_to_file)
                        if check:
                            application.fanuc_files.append(full_path_to_file)
                            programm_name = application.get_fanuc_name(full_path_to_file)
                            file_label = f'{file: <8}:({programm_name})'
                            application.fanuc_labels.append(file_label.replace('/', '\\'))
                            logging.debug(f'File "{file_label}" appended to list')
                            self.scaner_signal.emit(full_path_to_file, file_label)


class MazatrolRenamer(QThread, MyInterface):

    mazatrol_signal = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        for path_to_file in application.mazatrol_files:
            file_dir, file_name = os.path.split(path_to_file)
            new_file_name = application.get_mazatrol_name(path_to_file) + '.PBG'
            if new_file_name in (file_name, 'Название отсутствует!'):
                self.mazatrol_signal.emit(file_name, new_file_name)
                continue
            new_file_path = os.path.join(file_dir, new_file_name)
            if os.path.isfile(new_file_path):
                time.sleep(0.001)
                new_file_path = new_file_path[:-4]
                current_time = datetime.time(datetime.now()).strftime("%M-%S-%f")
                new_file_path += f'(копия {current_time}).PBG'
            os.rename(path_to_file, new_file_path)
            logging.debug(f'{file_name} renamed: {new_file_name}')
            self.mazatrol_signal.emit(file_name, new_file_name)


class FanucRenamer(QThread, MyInterface):

    fanuc_signal = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        for path_to_file in application.fanuc_files:
            file_dir, file_name = os.path.split(path_to_file)
            new_file_name = application.get_fanuc_name(path_to_file)
            if new_file_name in (file_name, 'Название отсутствует!'):
                self.fanuc_signal.emit(file_name, new_file_name)
                continue
            new_file_path = os.path.join(file_dir, new_file_name)
            if os.path.isfile(new_file_path):
                time.sleep(0.001)
                current_time = datetime.time(datetime.now()).strftime("%M-%S-%f")
                new_file_path += f'(копия {current_time})'
            os.rename(path_to_file, new_file_path)
            logging.debug(f'{file_name} renamed: {new_file_name}')
            self.fanuc_signal.emit(file_name, new_file_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    # splash = QtWidgets.QSplashScreen(QtGui.QPixmap('img.png'))
    # splash.show()
    application = MyInterface()
    application.show()
    # splash.finish(application)
sys.exit(app.exec())

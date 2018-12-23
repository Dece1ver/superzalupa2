# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from design import Ui_MainWindow  # импорт сгенерированного файла дизайна
from datetime import datetime
from constants import badfiles
import time
import sys
import os


class MyInterface(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyInterface, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cwd = os.getcwd()
        self.ui.scaner_path.setText(self.ui.cwd)
        self.ui.scaner_button.clicked.connect(self.scaner)
        self.ui.rename_mazatrol_button.clicked.connect(self.rename_mazatrol)
        self.ui.rename_fanuc_button.clicked.connect(self.rename_fanuc)
        self.ui.rename_mazatrol_button.setEnabled(False)
        self.ui.rename_fanuc_button.setEnabled(False)
        self.ui.scaner_path_dialog_button.clicked.connect(self.get_path)
        self.ui.action_5.triggered.connect(self.close)
        self.ui.statusbar.showMessage('Кнопки переименовывателей станут активны после сканирования.')

    # получает путь с кнопки
    def get_path(self):
        new_path = QtWidgets.QFileDialog.getExistingDirectory()
        if new_path != '':
            self.ui.cwd = new_path
        self.ui.scaner_path.setText(self.ui.cwd)
        self.ui.rename_mazatrol_button.setEnabled(False)
        self.ui.rename_fanuc_button.setEnabled(False)

    # получает название детали из мазаковской программы
    def get_mazatrol_name(self, full_path_to_file):
        try:
            with open(full_path_to_file, 'rb') as file:
                file.seek(80)
                file_name = file.read(32).rstrip(b'\x00').decode()
                file_name = file_name.replace('\\', '-').replace('*', '-').replace('/', '-').strip(' ')
                return file_name
        except ZeroDivisionError:
            return f'Не удалось получить имя файла: {self.full_path_to_file}'
            self.error_files.append(self.full_path_to_file)

    def check_fanuc_programm(self, full_path_to_file):
        try:
            with open(full_path_to_file, 'r') as f:
                first_symbol = f.read(1)
                if first_symbol in ('%', 'O'):
                    return True
                else:
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
        self.error_files = []

        self.ui.mazatrol_list_widget.clear()
        self.ui.fanuc_list_widget.clear()
        self.ui.info_window.clear()
        self.ui.info_window.insertPlainText(f'Сканирование директории "{self.ui.cwd}"...\n')
        self.ui.progressBar.setRange(0, 0)
        self.ui.progressBar.setValue(-1)

        self.scaner_thread = ScanerThread()
        self.scaner_thread.scaner_signal.connect(self.add_file, QtCore.Qt.QueuedConnection)
        self.scaner_thread.finished.connect(self.finish_scan)
        self.scaner_thread.start()

    def add_file(self, full_path_to_file, file_label):

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

    def finish_scan(self):

        if len(self.mazatrol_files) != 0:
            self.ui.rename_mazatrol_button.setEnabled(True)
            self.ui.statusbar.showMessage('Можно переименовывать.')
            self.ui.info_window.insertPlainText(f'Файлов Mazatrol: {len(self.mazatrol_files)}\n')
            self.ui.label_mazatrol_list.setText(f'Файлов Mazatrol: {len(self.mazatrol_files)}')
        else:
            self.ui.label_mazatrol_list.setText(f'Файлов Mazatrol не найдено.')
            self.ui.info_window.insertPlainText(f'Файлов Mazatrol не найдено.\n')

        if len(self.fanuc_files) != 0:
            self.ui.rename_fanuc_button.setEnabled(True)
            self.ui.statusbar.showMessage('Можно переименовывать.')
            self.ui.info_window.insertPlainText(f'Файлов Fanuc: {len(self.fanuc_files)}\n')
            self.ui.label_fanuc_list.setText(f'Файлов Fanuc: {len(self.fanuc_files)}')
        else:
            self.ui.label_fanuc_list.setText(f'Файлов Fanuc не найдено.')
            self.ui.info_window.insertPlainText(f'Файлов Fanuc не найдено.\n')

        if self.mazatrol_files == 0 and self.fanuc_files == 0:
            self.ui.statusbar.showMessage('Нечего переименовывать.')

        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(0)

    def rename_mazatrol(self, mazatrol_files):
        self.ui.info_window.clear()
        self.ui.progressBar.setRange(0, len(self.mazatrol_files))
        self.ui.progressBar.setValue(0)
        progress_bar_steps = 0

        count = 0
        for path_to_file in self.mazatrol_files:
            file_dir, file_name = os.path.split(path_to_file)
            new_file_name = self.get_mazatrol_name(path_to_file) + '.PBG'
            if file_name == new_file_name:
                progress_bar_steps += 1
                self.ui.info_window.insertPlainText(f'Программа "{file_name}" уже называется как надо, пропуск.\n')
                continue
            new_file_path = os.path.join(file_dir, new_file_name)
            if os.path.isfile(new_file_path):
                time.sleep(0.001)
                new_file_path = new_file_path[:-4]
                current_time = datetime.time(datetime.now()).strftime("%M-%S-%f")
                new_file_path += f'(копия {current_time}).PBG'
            os.rename(path_to_file, new_file_path)
            self.ui.info_window.insertPlainText(f'{file_name} переименован в {new_file_name}\n')
            count += 1
            progress_bar_steps += 1
        self.ui.info_window.insertPlainText(f'Переименовано {count} из {len(self.mazatrol_files)} файлов.\n')
        self.ui.rename_mazatrol_button.setEnabled(False)
        self.ui.statusbar.showMessage('Переименовывание завершено.')

    def rename_fanuc(self, fanuc_files):
        self.ui.info_window.clear()
        self.ui.progressBar.setRange(0, len(self.fanuc_files))
        self.ui.progressBar.setValue(0)
        progress_bar_steps = 0

        count = 0
        for path_to_file in self.fanuc_files:
            file_dir, file_name = os.path.split(path_to_file)
            new_file_name = self.get_fanuc_name(path_to_file)
            if file_name == new_file_name:
                progress_bar_steps += 1
                self.ui.info_window.insertPlainText(f'Программа "{file_name}" уже называется как надо, пропуск.\n')
                continue
            new_file_path = os.path.join(file_dir, new_file_name)
            if os.path.isfile(new_file_path):
                time.sleep(0.001)
                current_time = datetime.time(datetime.now()).strftime("%M-%S-%f")
                new_file_path += f'(копия {current_time})'
            try:
                os.rename(path_to_file, new_file_path)
                self.ui.info_window.insertPlainText(f'{file_name} переименован в {new_file_name}\n')
                progress_bar_steps += 1
                count += 1
            except Exception as e:
                print(e)

        self.ui.info_window.insertPlainText(f'Переименовано {count} из {len(self.fanuc_files)} файлов.\n')
        self.ui.rename_fanuc_button.setEnabled(False)
        self.ui.statusbar.showMessage('Переименовывание завершено.')


class ScanerThread(QThread, MyInterface):

    scaner_signal = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):

        for dir_paths, dir_names, file_names in os.walk(application.ui.cwd):
            for file in file_names:
                full_path_to_file = os.path.join(dir_paths, file)
                if full_path_to_file.upper().endswith('.PBG'):
                    application.mazatrol_files.append(full_path_to_file)
                    programm_name = application.get_mazatrol_name(full_path_to_file)
                    file_label = f'{file: <8}:({programm_name})'
                    self.scaner_signal.emit(full_path_to_file, file_label)

                else:
                    if not full_path_to_file.upper().endswith(badfiles):
                        check = self.check_fanuc_programm(full_path_to_file)
                        if check:
                            application.fanuc_files.append(full_path_to_file)
                            programm_name = application.get_fanuc_name(full_path_to_file)
                            file_label = f'{file: <8}:({programm_name})'
                            self.scaner_signal.emit(full_path_to_file, file_label)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyInterface()
    application.show()

sys.exit(app.exec())

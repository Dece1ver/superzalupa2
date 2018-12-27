# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
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
        self.ui.action.triggered.connect(self.show_settings)
        self.ui.action_5.triggered.connect(self.close)
        self.ui.statusbar.showMessage('Кнопки переименовывателей станут активны после сканирования.')
        self.fast_scan_check = False

    def save_check_box_settings(self):
        print(self.check_box.isChecked())
        self.fast_scan_check = self.check_box.isChecked()

    def show_settings(self):
        settings = QtWidgets.QWidget(self, Qt.Window)
        settings.setWindowModality(QtCore.Qt.WindowModal)
        settings.resize(400, 300)
        settings.setWindowTitle('Настройки')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings.sizePolicy().hasHeightForWidth())
        settings.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("window.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settings.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(settings)
        self.label.setText('Настройки:')
        self.label.setGeometry(QtCore.QRect(10, 0, 391, 31))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(settings)
        self.line.setGeometry(QtCore.QRect(10, 20, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.check_box = QtWidgets.QCheckBox(settings)
        self.check_box.setText('Быстрое сканирование')
        self.check_box.setGeometry(QtCore.QRect(10, 30, 191, 17))
        self.check_box.setObjectName("check_box")
        self.check_box.setChecked(self.fast_scan_check)
        self.check_box.clicked.connect(self.save_check_box_settings)
        self.label_2 = QtWidgets.QLabel(settings)
        self.label_2.setText('При сканировании отключает моментальное добавление элементов в списки интерфейса. Рекомендуется использовать когда предполагаемое количество управляющих программ больше тысячи.')
        self.label_2.setGeometry(QtCore.QRect(10, 50, 381, 41))
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(settings)
        self.line_2.setGeometry(QtCore.QRect(10, 90, 381, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(settings)
        self.label_3.setText('Расширения файлов исключенные для сканирования:')
        self.label_3.setGeometry(QtCore.QRect(10, 100, 381, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(settings)
        self.pushButton.setText('Сохранить')
        self.pushButton.setGeometry(QtCore.QRect(300, 270, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(settings.close)
        self.textBrowser = QtWidgets.QTextBrowser(settings)
        self.textBrowser.setGeometry(QtCore.QRect(10, 120, 381, 141))
        self.textBrowser.setStyleSheet("font: 12pt \"Consolas\";")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                 "p, li { white-space: pre-wrap; }\n"
                                 "</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>")
        settings.show()

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
        self.error_files = []

        self.ui.mazatrol_list_widget.clear()
        self.ui.fanuc_list_widget.clear()
        self.ui.info_window.clear()
        self.ui.info_window.insertPlainText(f'Сканирование директории "{self.ui.cwd}"...\n')
        self.ui.progressBar.setRange(0, 0)
        self.ui.progressBar.setValue(-1)

        self.scaner_thread = ScanerThread()
        self.scaner_thread.started.connect(self.on_start)
        if self.fast_scan_check:
            self.scaner_thread.finished.connect(self.fast_scan)
        else:
            self.scaner_thread.scaner_signal.connect(self.add_file, QtCore.Qt.QueuedConnection)
            self.scaner_thread.finished.connect(self.finish_scan)

        self.scaner_thread.start()

    def on_start(self):
        pass
        self.ui.scaner_button.setText('Остановить')
        self.ui.scaner_button.clicked.connect(self.stop_scaner)
        # self.ui.scaner_button.setDisabled(True)

    def stop_scaner(self):
        self.ui.scaner_button.setText('Сканировать')
        self.ui.scaner_button.clicked.connect(self.scaner)
        self.ui.statusbar.showMessage('Сканирование остановлено. Рекомендуется отсканировать снова.')
        self.scaner_thread.running = False

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

    def fast_scan(self):
        if len(self.mazatrol_files) != 0:
            self.ui.mazatrol_list_widget.addItems(self.mazatrol_files)
            self.ui.rename_mazatrol_button.setEnabled(True)
            self.ui.statusbar.showMessage('Можно переименовывать.')
            self.ui.info_window.insertPlainText(f'Файлов Mazatrol: {len(self.mazatrol_files)}\n')
            self.ui.label_mazatrol_list.setText(f'Файлов Mazatrol: {len(self.mazatrol_files)}')
        else:
            self.ui.label_mazatrol_list.setText(f'Файлов Mazatrol не найдено.')
            self.ui.info_window.insertPlainText(f'Файлов Mazatrol не найдено.\n')
        if len(self.fanuc_files) != 0:
            self.ui.fanuc_list_widget.addItems(self.fanuc_files)
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
        self.ui.scaner_button.clicked.setText('Сканировать')
        self.ui.scaner_button.clicked.connect(self.scaner)

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

        self.ui.scaner_button.setText('Сканировать')
        self.ui.scaner_button.clicked.connect(self.scaner)

    def rename_mazatrol(self, mazatrol_files):
        self.ui.info_window.clear()
        self.ui.progressBar.setRange(0, len(self.mazatrol_files))
        self.ui.progressBar.setValue(0)
        self.progress_bar_steps = 0
        self.count = 0
        self.rename_mazatrol_thread = MazatrolRenamer()
        self.rename_mazatrol_thread.mazatrol_signal.connect(self.add_mazatrol_file, QtCore.Qt.QueuedConnection)
        self.rename_mazatrol_thread.finished.connect(self.finish_rename_mazatrol)
        self.rename_mazatrol_thread.start()

    def add_mazatrol_file(self, file_name, new_file_name):
        if file_name == new_file_name:
            self.ui.info_window.insertPlainText(f'Программа "{file_name}" уже называется как надо, пропуск.\n')
        else:
            self.ui.info_window.insertPlainText(f'{file_name} переименован в {new_file_name}\n')
            self.count += 1
        self.ui.progressBar.setValue(self.progress_bar_steps)
        self.progress_bar_steps += 1
        self.ui.info_window.ensureCursorVisible()

    def finish_rename_mazatrol(self):
        self.ui.info_window.insertPlainText(f'Переименовано {self.count} из {len(self.mazatrol_files)} файлов.\n')
        self.ui.rename_mazatrol_button.setEnabled(False)
        self.ui.statusbar.showMessage('Переименовывание завершено.')

    def rename_fanuc(self, fanuc_files):
        self.ui.info_window.clear()
        self.ui.progressBar.setRange(0, len(self.fanuc_files))
        self.ui.progressBar.setValue(0)
        self.progress_bar_steps = 0
        self.count = 0
        self.rename_fanuc_thread = FanucRenamer()
        self.rename_fanuc_thread.fanuc_signal.connect(self.add_fanuc_file, QtCore.Qt.QueuedConnection)
        self.rename_fanuc_thread.finished.connect(self.finish_rename_fanuc)
        self.rename_fanuc_thread.start()

    def add_fanuc_file(self, file_name, new_file_name):
        if file_name == new_file_name:
            self.ui.info_window.insertPlainText(f'Программа "{file_name}" уже называется как надо, пропуск.\n')
        else:
            self.ui.info_window.insertPlainText(f'{file_name} переименован в {new_file_name}\n')
            self.count += 1
        self.progress_bar_steps += 1
        self.ui.progressBar.setValue(self.progress_bar_steps)
        self.ui.info_window.ensureCursorVisible()

    def finish_rename_fanuc(self):
        self.ui.info_window.insertPlainText(f'Переименовано {self.count} из {len(self.fanuc_files)} файлов.\n')
        self.ui.rename_fanuc_button.setEnabled(False)
        self.ui.statusbar.showMessage('Переименовывание завершено.')


class ScanerThread(QThread, MyInterface):

    scaner_signal = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)
        self.running = False
        self.status = True

    def __del__(self):
        self.wait()

    def run(self):
        self.running = True
        for dir_paths, dir_names, file_names in os.walk(application.ui.cwd):
            if not self.status:
                break
            for file in file_names:
                if not self.running:
                    self.status = False
                    break
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
            if file_name == new_file_name:
                self.mazatrol_signal.emit(file_name, new_file_name)
                continue
            new_file_path = os.path.join(file_dir, new_file_name)
            if os.path.isfile(new_file_path):
                time.sleep(0.001)
                new_file_path = new_file_path[:-4]
                current_time = datetime.time(datetime.now()).strftime("%M-%S-%f")
                new_file_path += f'(копия {current_time}).PBG'
            os.rename(path_to_file, new_file_path)
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
            if file_name == new_file_name:
                self.fanuc_signal.emit(file_name, new_file_name)
                continue
            new_file_path = os.path.join(file_dir, new_file_name)
            if os.path.isfile(new_file_path):
                time.sleep(0.001)
                current_time = datetime.time(datetime.now()).strftime("%M-%S-%f")
                new_file_path += f'(копия {current_time})'
            os.rename(path_to_file, new_file_path)
            self.fanuc_signal.emit(file_name, new_file_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    # splash = QtWidgets.QSplashScreen(QtGui.QPixmap('img.png'))
    # splash.show()
    application = MyInterface()
    application.show()
    # splash.finish(application)
    sys.exit(app.exec())

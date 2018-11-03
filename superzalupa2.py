from PyQt5 import QtWidgets, QtCore
from design import Ui_MainWindow  # импорт нашего сгенерированного файла
from constants import badfiles
import sys
import os


class MyInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyInterface, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.scaner_button.clicked.connect(self.scaner)

        self.ui.mazatrol_files = []
        self.ui.fanuc_files = []
        self.ui.error_files = []

    # Получает название детали из мазаковской программы
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

    # Получает название детали из фануковской программы
    def get_fanuc_name(self, full_path_to_file):
        try:
            with open(full_path_to_file, 'rb') as f:
                f.seek(2)
                file_name = f.read(55)
                if b')' not in file_name:
                    try:
                        file_name.decode()
                        file_name = 'Название отсутствует!'
                    except(UnicodeDecodeError):
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

        # Очищает списки
        self.mazatrol_files = []
        self.fanuc_files = []
        self.error_files = []
        self.ui.mazatrol_list_widget.clear()
        self.ui.fanuc_list_widget.clear()
        self.ui.progressBar.setRange(0, 0)
        self.ui.progressBar.setValue(-1)

        for dir_paths, dir_names, file_names in os.walk(os.getcwd()):
            for file in file_names:
                full_path_to_file = os.path.join(dir_paths, file)
                if full_path_to_file.upper().endswith('.PBG'):
                    self.mazatrol_files.append(full_path_to_file)
                    programm_name = self.get_mazatrol_name(full_path_to_file)
                    file_label = f'{file: <8}:({programm_name})'

                    item = self.ui.mazatrol_list_widget.addItem(file_label)

                else:
                    if not full_path_to_file.upper().endswith(badfiles):
                        check = self.check_fanuc_programm(full_path_to_file)
                        print(check)
                        if check:
                            self.fanuc_files.append(full_path_to_file)
                            programm_name = self.get_fanuc_name(full_path_to_file)
                            file_label = f'{file: <8}:({programm_name})'

                            item = self.ui.fanuc_list_widget.addItem(file_label)

        count_fanuc = len(self.fanuc_files)
        count_mazatrol = len(self.mazatrol_files)
        self.ui.info_window.setPlainText(f'Найдено:\nФайлов Fanuc: {count_fanuc}\nФайлов Mazatrol: {count_mazatrol}')
        self.ui.label_fanuc_list.setText(f'Файлов Fanuc: {count_fanuc}')
        self.ui.label_mazatrol_list.setText(f'Файлов Mazatrol: {count_mazatrol}')
        self.ui.progressBar.setRange(0, 100)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyInterface()
    application.show()

    sys.exit(app.exec())

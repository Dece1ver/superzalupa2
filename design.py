# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("window.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lists_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lists_frame.sizePolicy().hasHeightForWidth())
        self.lists_frame.setSizePolicy(sizePolicy)
        self.lists_frame.setMinimumSize(QtCore.QSize(782, 250))
        self.lists_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lists_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lists_frame.setLineWidth(0)
        self.lists_frame.setObjectName("lists_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.lists_frame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fanuc_frame = QtWidgets.QFrame(self.lists_frame)
        self.fanuc_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fanuc_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fanuc_frame.setObjectName("fanuc_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.fanuc_frame)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setVerticalSpacing(3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.rename_fanuc_button = QtWidgets.QPushButton(self.fanuc_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rename_fanuc_button.sizePolicy().hasHeightForWidth())
        self.rename_fanuc_button.setSizePolicy(sizePolicy)
        self.rename_fanuc_button.setObjectName("rename_fanuc_button")
        self.gridLayout_6.addWidget(self.rename_fanuc_button, 2, 0, 1, 2)
        self.fanuc_list_widget = QtWidgets.QListWidget(self.fanuc_frame)
        self.fanuc_list_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fanuc_list_widget.sizePolicy().hasHeightForWidth())
        self.fanuc_list_widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.fanuc_list_widget.setFont(font)
        self.fanuc_list_widget.setAcceptDrops(False)
        self.fanuc_list_widget.setFrameShape(QtWidgets.QFrame.Box)
        self.fanuc_list_widget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fanuc_list_widget.setLineWidth(1)
        self.fanuc_list_widget.setMidLineWidth(0)
        self.fanuc_list_widget.setObjectName("fanuc_list_widget")
        self.gridLayout_6.addWidget(self.fanuc_list_widget, 1, 0, 1, 2)
        self.label_fanuc_list = QtWidgets.QToolButton(self.fanuc_frame)
        self.label_fanuc_list.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_fanuc_list.sizePolicy().hasHeightForWidth())
        self.label_fanuc_list.setSizePolicy(sizePolicy)
        self.label_fanuc_list.setAutoFillBackground(False)
        self.label_fanuc_list.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_fanuc_list.setAutoRaise(True)
        self.label_fanuc_list.setObjectName("label_fanuc_list")
        self.gridLayout_6.addWidget(self.label_fanuc_list, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.fanuc_frame, 0, 0, 1, 1)
        self.mazatrol_frame = QtWidgets.QFrame(self.lists_frame)
        self.mazatrol_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mazatrol_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mazatrol_frame.setObjectName("mazatrol_frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.mazatrol_frame)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setHorizontalSpacing(6)
        self.gridLayout_7.setVerticalSpacing(3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.rename_mazatrol_button = QtWidgets.QPushButton(self.mazatrol_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rename_mazatrol_button.sizePolicy().hasHeightForWidth())
        self.rename_mazatrol_button.setSizePolicy(sizePolicy)
        self.rename_mazatrol_button.setObjectName("rename_mazatrol_button")
        self.gridLayout_7.addWidget(self.rename_mazatrol_button, 2, 0, 1, 2)
        self.mazatrol_list_widget = QtWidgets.QListWidget(self.mazatrol_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mazatrol_list_widget.sizePolicy().hasHeightForWidth())
        self.mazatrol_list_widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.mazatrol_list_widget.setFont(font)
        self.mazatrol_list_widget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mazatrol_list_widget.setAutoFillBackground(False)
        self.mazatrol_list_widget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.mazatrol_list_widget.setFrameShape(QtWidgets.QFrame.Box)
        self.mazatrol_list_widget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mazatrol_list_widget.setLineWidth(1)
        self.mazatrol_list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mazatrol_list_widget.setResizeMode(QtWidgets.QListView.Adjust)
        self.mazatrol_list_widget.setViewMode(QtWidgets.QListView.ListMode)
        self.mazatrol_list_widget.setModelColumn(0)
        self.mazatrol_list_widget.setUniformItemSizes(False)
        self.mazatrol_list_widget.setBatchSize(100)
        self.mazatrol_list_widget.setWordWrap(False)
        self.mazatrol_list_widget.setSelectionRectVisible(False)
        self.mazatrol_list_widget.setObjectName("mazatrol_list_widget")
        self.gridLayout_7.addWidget(self.mazatrol_list_widget, 1, 0, 1, 2)
        self.label_mazatrol_list = QtWidgets.QToolButton(self.mazatrol_frame)
        self.label_mazatrol_list.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mazatrol_list.sizePolicy().hasHeightForWidth())
        self.label_mazatrol_list.setSizePolicy(sizePolicy)
        self.label_mazatrol_list.setAutoRaise(True)
        self.label_mazatrol_list.setObjectName("label_mazatrol_list")
        self.gridLayout_7.addWidget(self.label_mazatrol_list, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.mazatrol_frame, 0, 1, 1, 1)
        self.lists_line = QtWidgets.QFrame(self.lists_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lists_line.sizePolicy().hasHeightForWidth())
        self.lists_line.setSizePolicy(sizePolicy)
        self.lists_line.setMinimumSize(QtCore.QSize(0, 1))
        self.lists_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.lists_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lists_line.setObjectName("lists_line")
        self.gridLayout_4.addWidget(self.lists_line, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.lists_frame, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(782, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.info_window = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_window.sizePolicy().hasHeightForWidth())
        self.info_window.setSizePolicy(sizePolicy)
        self.info_window.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.info_window.setFont(font)
        self.info_window.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.info_window.setMouseTracking(False)
        self.info_window.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.info_window.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.info_window.setAcceptDrops(False)
        self.info_window.setFrameShape(QtWidgets.QFrame.Box)
        self.info_window.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.info_window.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.info_window.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.info_window.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.info_window.setReadOnly(True)
        self.info_window.setPlainText("")
        self.info_window.setCursorWidth(1)
        self.info_window.setCenterOnScroll(False)
        self.info_window.setObjectName("info_window")
        self.gridLayout_3.addWidget(self.info_window, 2, 0, 1, 1)
        self.label_info_window = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info_window.sizePolicy().hasHeightForWidth())
        self.label_info_window.setSizePolicy(sizePolicy)
        self.label_info_window.setObjectName("label_info_window")
        self.gridLayout_3.addWidget(self.label_info_window, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.label_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_frame.sizePolicy().hasHeightForWidth())
        self.label_frame.setSizePolicy(sizePolicy)
        self.label_frame.setMinimumSize(QtCore.QSize(782, 80))
        self.label_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_frame.setLineWidth(0)
        self.label_frame.setObjectName("label_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.label_frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.label_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scaner_path = QtWidgets.QLineEdit(self.frame_3)
        self.scaner_path.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaner_path.sizePolicy().hasHeightForWidth())
        self.scaner_path.setSizePolicy(sizePolicy)
        self.scaner_path.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scaner_path.setFont(font)
        self.scaner_path.setMouseTracking(True)
        self.scaner_path.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.scaner_path.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scaner_path.setText("")
        self.scaner_path.setReadOnly(True)
        self.scaner_path.setObjectName("scaner_path")
        self.gridLayout_5.addWidget(self.scaner_path, 0, 1, 1, 1)
        self.label_line = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_line.sizePolicy().hasHeightForWidth())
        self.label_line.setSizePolicy(sizePolicy)
        self.label_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_line.setObjectName("label_line")
        self.gridLayout_5.addWidget(self.label_line, 1, 0, 1, 5)
        self.label_path = QtWidgets.QLabel(self.frame_3)
        self.label_path.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_path.sizePolicy().hasHeightForWidth())
        self.label_path.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_path.setFont(font)
        self.label_path.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_path.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_path.setObjectName("label_path")
        self.gridLayout_5.addWidget(self.label_path, 0, 0, 1, 1)
        self.scaner_path_dialog_button = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaner_path_dialog_button.sizePolicy().hasHeightForWidth())
        self.scaner_path_dialog_button.setSizePolicy(sizePolicy)
        self.scaner_path_dialog_button.setMinimumSize(QtCore.QSize(0, 23))
        self.scaner_path_dialog_button.setObjectName("scaner_path_dialog_button")
        self.gridLayout_5.addWidget(self.scaner_path_dialog_button, 0, 2, 1, 1)
        self.scaner_button = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaner_button.sizePolicy().hasHeightForWidth())
        self.scaner_button.setSizePolicy(sizePolicy)
        self.scaner_button.setMinimumSize(QtCore.QSize(125, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.scaner_button.setFont(font)
        self.scaner_button.setObjectName("scaner_button")
        self.gridLayout_5.addWidget(self.scaner_button, 0, 4, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.label_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 68))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_superzalupa = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_superzalupa.sizePolicy().hasHeightForWidth())
        self.label_superzalupa.setSizePolicy(sizePolicy)
        self.label_superzalupa.setMinimumSize(QtCore.QSize(381, 0))
        self.label_superzalupa.setMaximumSize(QtCore.QSize(16777215, 388))
        self.label_superzalupa.setMouseTracking(True)
        self.label_superzalupa.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_superzalupa.setAutoFillBackground(False)
        self.label_superzalupa.setStyleSheet("font: 32pt \"Agency FB\";")
        self.label_superzalupa.setText("")
        self.label_superzalupa.setPixmap(QtGui.QPixmap("label.png"))
        self.label_superzalupa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_superzalupa.setObjectName("label_superzalupa")
        self.horizontalLayout.addWidget(self.label_superzalupa)
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setToolTip("")
        self.progressBar.setMaximum(1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.label_frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_calc = QtWidgets.QAction(MainWindow)
        self.action_calc.setObjectName("action_calc")
        self.action_Mazak_QTS350 = QtWidgets.QAction(MainWindow)
        self.action_Mazak_QTS350.setObjectName("action_Mazak_QTS350")
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_Mazak_QTS350)
        self.menu_3.addAction(self.action_calc)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Superzalupa 2"))
        self.rename_fanuc_button.setText(_translate("MainWindow", "Переименовать файлы Fanuc"))
        self.label_fanuc_list.setText(_translate("MainWindow", "Программы Fanuc"))
        self.rename_mazatrol_button.setText(_translate("MainWindow", "Переименовать файлы Mazatrol"))
        self.label_mazatrol_list.setText(_translate("MainWindow", "Программы Mazatrol"))
        self.label_info_window.setText(_translate("MainWindow", "<html><head/><body><p>Информация:</p></body></html>"))
        self.label_path.setText(_translate("MainWindow", "Путь:"))
        self.scaner_path_dialog_button.setText(_translate("MainWindow", "Обзор..."))
        self.scaner_button.setText(_translate("MainWindow", "Сканировать"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "Нормы"))
        self.menu_3.setTitle(_translate("MainWindow", "Калькулятор"))
        self.action.setText(_translate("MainWindow", "Настройки"))
        self.action_3.setText(_translate("MainWindow", "Справка"))
        self.action_5.setText(_translate("MainWindow", "Выход"))
        self.action_2.setText(_translate("MainWindow", "Нормы SKT/WIA"))
        self.action_6.setText(_translate("MainWindow", "Нормы Integrex"))
        self.action_4.setText(_translate("MainWindow", "Нормы Mazak 200ML"))
        self.action_calc.setText(_translate("MainWindow", "Выработка"))
        self.action_Mazak_QTS350.setText(_translate("MainWindow", "Нормы Mazak QTS350"))

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionUsers = QAction(Main)
        self.actionUsers.setObjectName(u"actionUsers")
        self.actionOrganisasi = QAction(Main)
        self.actionOrganisasi.setObjectName(u"actionOrganisasi")
        self.actionBantuan = QAction(Main)
        self.actionBantuan.setObjectName(u"actionBantuan")
        self.actionKategoriBantuan = QAction(Main)
        self.actionKategoriBantuan.setObjectName(u"actionKategoriBantuan")
        self.actionLaporan = QAction(Main)
        self.actionLaporan.setObjectName(u"actionLaporan")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuHalaman = QMenu(self.menubar)
        self.menuHalaman.setObjectName(u"menuHalaman")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHalaman.menuAction())
        self.menuHalaman.addAction(self.actionUsers)
        self.menuHalaman.addAction(self.actionOrganisasi)
        self.menuHalaman.addAction(self.actionBantuan)
        self.menuHalaman.addAction(self.actionKategoriBantuan)
        self.menuHalaman.addAction(self.actionLaporan)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionUsers.setText(QCoreApplication.translate("Main", u"Users", None))
        self.actionOrganisasi.setText(QCoreApplication.translate("Main", u"Organisasi", None))
        self.actionBantuan.setText(QCoreApplication.translate("Main", u"Bantuan", None))
        self.actionKategoriBantuan.setText(QCoreApplication.translate("Main", u"KategoriBantuan", None))
        self.actionLaporan.setText(QCoreApplication.translate("Main", u"Laporan", None))
        self.menuHalaman.setTitle(QCoreApplication.translate("Main", u"Halaman", None))
    # retranslateUi


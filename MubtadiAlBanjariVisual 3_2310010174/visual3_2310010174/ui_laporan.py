# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laporan.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 500)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.editIdLaporan = QLineEdit(self.groupBox)
        self.editIdLaporan.setObjectName(u"editIdLaporan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editIdLaporan)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.editIdBantuan = QLineEdit(self.groupBox)
        self.editIdBantuan.setObjectName(u"editIdBantuan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIdBantuan)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.editKeterangan = QLineEdit(self.groupBox)
        self.editKeterangan.setObjectName(u"editKeterangan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editKeterangan)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.editStatus = QLineEdit(self.groupBox)
        self.editStatus.setObjectName(u"editStatus")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editStatus)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.editTanggalLaporan = QLineEdit(self.groupBox)
        self.editTanggalLaporan.setObjectName(u"editTanggalLaporan")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editTanggalLaporan)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.horizontalLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")

        self.horizontalLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")

        self.horizontalLayout.addWidget(self.btnHapus)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")

        self.verticalLayout.addWidget(self.editCari)

        self.tabelLaporan = QTableWidget(Form)
        if (self.tabelLaporan.columnCount() < 5):
            self.tabelLaporan.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelLaporan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelLaporan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelLaporan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelLaporan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelLaporan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelLaporan.setObjectName(u"tabelLaporan")

        self.verticalLayout.addWidget(self.tabelLaporan)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Laporan", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Form Data Laporan", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID Laporan:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ID Bantuan:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Keterangan:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Tanggal Laporan:", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("Form", u"Cari data...", None))
        ___qtablewidgetitem = self.tabelLaporan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Laporan", None));
        ___qtablewidgetitem1 = self.tabelLaporan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID Bantuan", None));
        ___qtablewidgetitem2 = self.tabelLaporan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        ___qtablewidgetitem3 = self.tabelLaporan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Status", None));
        ___qtablewidgetitem4 = self.tabelLaporan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Tanggal Laporan", None));
    # retranslateUi


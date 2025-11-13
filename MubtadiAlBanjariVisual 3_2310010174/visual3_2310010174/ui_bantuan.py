# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bantuan.ui'
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

        self.editIdBantuan = QLineEdit(self.groupBox)
        self.editIdBantuan.setObjectName(u"editIdBantuan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editIdBantuan)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.editIdOrganisasi = QLineEdit(self.groupBox)
        self.editIdOrganisasi.setObjectName(u"editIdOrganisasi")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIdOrganisasi)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.editIdKategori = QLineEdit(self.groupBox)
        self.editIdKategori.setObjectName(u"editIdKategori")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editIdKategori)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.editNominal = QLineEdit(self.groupBox)
        self.editNominal.setObjectName(u"editNominal")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editNominal)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.editTanggal = QLineEdit(self.groupBox)
        self.editTanggal.setObjectName(u"editTanggal")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editTanggal)


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

        self.tabelBantuan = QTableWidget(Form)
        if (self.tabelBantuan.columnCount() < 5):
            self.tabelBantuan.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelBantuan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelBantuan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelBantuan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelBantuan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelBantuan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelBantuan.setObjectName(u"tabelBantuan")

        self.verticalLayout.addWidget(self.tabelBantuan)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Bantuan", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Form Data Bantuan", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID Bantuan:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ID Organisasi:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ID Kategori:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Nominal:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Tanggal:", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("Form", u"Cari data...", None))
        ___qtablewidgetitem = self.tabelBantuan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Bantuan", None));
        ___qtablewidgetitem1 = self.tabelBantuan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID Organisasi", None));
        ___qtablewidgetitem2 = self.tabelBantuan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"ID Kategori", None));
        ___qtablewidgetitem3 = self.tabelBantuan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Nominal", None));
        ___qtablewidgetitem4 = self.tabelBantuan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Tanggal", None));
    # retranslateUi


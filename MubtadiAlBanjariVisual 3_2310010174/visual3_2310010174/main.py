import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from users import users
from organisasi import organisasi
from kategoribantuan import kategoribantuan
from bantuan import bantuan
from laporan import laporan

class halamanUtama(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        fileformutama = QFile("main.ui")
        fileformutama.open(QFile.ReadOnly)
        formloader = QUiLoader()
        self.formutama = formloader.load(fileformutama,self)
        self.setMenuBar(self.formutama.menuBar())
        self.resize(self.formutama.size())
        self.formutama.actionUsers.triggered.connect(self.bukausers)
        self.formutama.actionOrganisasi.triggered.connect(self.bukaorganisasi)
        self.formutama.actionKategoriBantuan.triggered.connect(self.bukakategoribantuan)
        self.formutama.actionBantuan.triggered.connect(self.bukabantuan)
        self.formutama.actionLaporan.triggered.connect(self.bukalaporan)

    def bukausers(self):
        self.formusers = users()
        self.formusers.show()

    def bukaorganisasi(self):
        self.formorganisasi = organisasi()
        self.formorganisasi.show()

    def bukakategoribantuan(self):
        self.formkategoribantuan = kategoribantuan()
        self.formkategoribantuan.show()

    def bukabantuan(self):
        self.formbantuan = bantuan()
        self.formbantuan.show()

    def bukalaporan(self):
        self.formlaporan = laporan()
        self.formlaporan.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = halamanUtama()
    widget.show()
    sys.exit(app.exec())

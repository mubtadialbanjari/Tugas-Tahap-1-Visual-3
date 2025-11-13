import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class bantuan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("bantuan.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.form.btnSimpan.clicked.connect(self.doSimpanBantuan)
        self.form.btnUbah.clicked.connect(self.doUbahBantuan)
        self.form.btnHapus.clicked.connect(self.doHapusBantuan)
        self.form.editCari.textChanged.connect(self.doCarieBantuan)
        self.form.tabelBantuan.itemClicked.connect(self.doTabelKlik)

        self.tampilDataBantuan()

    def doSimpanBantuan(self):
        if not self.form.editIdBantuan.text().strip():
            QMessageBox.information(None,"Informasi","ID Bantuan belum di isi")
            self.form.editIdBantuan.setFocus()
        elif not self.form.editIdOrganisasi.text().strip():
            QMessageBox.information(None,"Informasi","ID Organisasi belum di isi")
            self.form.editIdOrganisasi.setFocus()
        elif not self.form.editIdKategori.text().strip():
            QMessageBox.information(None,"Informasi","ID Kategori belum di isi")
            self.form.editIdKategori.setFocus()
        elif not self.form.editNominal.text().strip():
            QMessageBox.information(None,"Informasi","Nominal belum di isi")
            self.form.editNominal.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Simpan Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdBantuan.text()
                tempIdOrganisasi = self.form.editIdOrganisasi.text()
                tempIdKategori = self.form.editIdKategori.text()
                tempNominal = self.form.editNominal.text()
                tempTanggal = self.form.editTanggal.text()
                self.crud.simpanBantuan(tempID, tempIdOrganisasi, tempIdKategori, tempNominal, tempTanggal)
                self.tampilDataBantuan()
            else:
                pass

    def doUbahBantuan(self):
        if not self.form.editIdBantuan.text().strip():
            QMessageBox.information(None,"Informasi","ID Bantuan belum di isi. Klik data dari tabel.")
            self.form.editIdBantuan.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Ubah Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdBantuan.text()
                tempIdOrganisasi = self.form.editIdOrganisasi.text()
                tempIdKategori = self.form.editIdKategori.text()
                tempNominal = self.form.editNominal.text()
                tempTanggal = self.form.editTanggal.text()
                self.crud.ubahBantuan(tempID, tempIdOrganisasi, tempIdKategori, tempNominal, tempTanggal)
                self.tampilDataBantuan()
            else:
                pass

    def doHapusBantuan(self):
        if not self.form.editIdBantuan.text().strip():
            QMessageBox.information(None,"Informasi","ID Bantuan belum di isi. Klik data dari tabel.")
            self.form.editIdBantuan.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Hapus Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdBantuan.text()
                self.crud.hapusBantuan(tempID)
                self.tampilDataBantuan()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilDataBantuan(self):
        baris = self.crud.dataBantuan()
        self.form.tabelBantuan.setRowCount(0)
        for r in baris:
            i = self.form.tabelBantuan.rowCount()
            self.form.tabelBantuan.insertRow(i)
            self.form.tabelBantuan.setItem(i,0, QTableWidgetItem(r["id_bantuan"]))
            self.form.tabelBantuan.setItem(i,1, QTableWidgetItem(r["id_organisasi"]))
            self.form.tabelBantuan.setItem(i,2, QTableWidgetItem(r["id_kategori"]))
            self.form.tabelBantuan.setItem(i,3, QTableWidgetItem(r["nominal"]))
            self.form.tabelBantuan.setItem(i,4, QTableWidgetItem(r["tanggal"]))

        self.bersihkanForm()

    def doCarieBantuan(self):
        cari = self.form.editCari.text()
        baris = self.crud.cariBantuan(cari)
        self.form.tabelBantuan.setRowCount(0)
        for r in baris:
            i = self.form.tabelBantuan.rowCount()
            self.form.tabelBantuan.insertRow(i)
            self.form.tabelBantuan.setItem(i,0, QTableWidgetItem(r["id_bantuan"]))
            self.form.tabelBantuan.setItem(i,1, QTableWidgetItem(r["id_organisasi"]))
            self.form.tabelBantuan.setItem(i,2, QTableWidgetItem(r["id_kategori"]))
            self.form.tabelBantuan.setItem(i,3, QTableWidgetItem(r["nominal"]))
            self.form.tabelBantuan.setItem(i,4, QTableWidgetItem(r["tanggal"]))

    def bersihkanForm(self):
        self.form.editIdBantuan.clear()
        self.form.editIdOrganisasi.clear()
        self.form.editIdKategori.clear()
        self.form.editNominal.clear()
        self.form.editTanggal.clear()

    def doTabelKlik(self, item):
        row = item.row()
        id_bantuan = self.form.tabelBantuan.item(row, 0).text()
        id_organisasi = self.form.tabelBantuan.item(row, 1).text()
        id_kategori = self.form.tabelBantuan.item(row, 2).text()
        nominal = self.form.tabelBantuan.item(row, 3).text()
        tanggal = self.form.tabelBantuan.item(row, 4).text()

        self.form.editIdBantuan.setText(id_bantuan)
        self.form.editIdOrganisasi.setText(id_organisasi)
        self.form.editIdKategori.setText(id_kategori)
        self.form.editNominal.setText(nominal)
        self.form.editTanggal.setText(tanggal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = bantuan()
    widget.show()
    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class organisasi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("organisasi.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.form.btnSimpan.clicked.connect(self.doSimpanOrganisasi)
        self.form.btnUbah.clicked.connect(self.doUbahOrganisasi)
        self.form.btnHapus.clicked.connect(self.doHapusOrganisasi)
        self.form.editCari.textChanged.connect(self.doCariOrganisasi)
        self.form.tabelOrganisasi.itemClicked.connect(self.doTabelKlik)

        self.tampilDataOrganisasi()

    def doSimpanOrganisasi(self):
        if not self.form.editIdOrganisasi.text().strip():
            QMessageBox.information(None,"Informasi","ID Organisasi belum di isi")
            self.form.editIdOrganisasi.setFocus()
        elif not self.form.editNamaOrganisasi.text().strip():
            QMessageBox.information(None,"Informasi","Nama Organisasi belum di isi")
            self.form.editNamaOrganisasi.setFocus()
        elif not self.form.editAlamat.text().strip():
            QMessageBox.information(None,"Informasi","Alamat belum di isi")
            self.form.editAlamat.setFocus()
        elif not self.form.editNoTelepon.text().strip():
            QMessageBox.information(None,"Informasi","No Telepon belum di isi")
            self.form.editNoTelepon.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Simpan Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdOrganisasi.text()
                tempNama = self.form.editNamaOrganisasi.text()
                tempAlamat = self.form.editAlamat.text()
                tempTelepon = self.form.editNoTelepon.text()
                tempStatus = self.form.editStatus.text()
                self.crud.simpanOrganisasi(tempID, tempNama, tempAlamat, tempTelepon, tempStatus)
                self.tampilDataOrganisasi()
            else:
                pass

    def doUbahOrganisasi(self):
        if not self.form.editIdOrganisasi.text().strip():
            QMessageBox.information(None,"Informasi","ID Organisasi belum di isi. Klik data dari tabel.")
            self.form.editIdOrganisasi.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Ubah Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdOrganisasi.text()
                tempNama = self.form.editNamaOrganisasi.text()
                tempAlamat = self.form.editAlamat.text()
                tempTelepon = self.form.editNoTelepon.text()
                tempStatus = self.form.editStatus.text()
                self.crud.ubahOrganisasi(tempID, tempNama, tempAlamat, tempTelepon, tempStatus)
                self.tampilDataOrganisasi()
            else:
                pass

    def doHapusOrganisasi(self):
        if not self.form.editIdOrganisasi.text().strip():
            QMessageBox.information(None,"Informasi","ID Organisasi belum di isi. Klik data dari tabel.")
            self.form.editIdOrganisasi.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Hapus Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdOrganisasi.text()
                self.crud.hapusOrganisasi(tempID)
                self.tampilDataOrganisasi()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilDataOrganisasi(self):
        baris = self.crud.dataOrganisasi()
        self.form.tabelOrganisasi.setRowCount(0)
        for r in baris:
            i = self.form.tabelOrganisasi.rowCount()
            self.form.tabelOrganisasi.insertRow(i)
            self.form.tabelOrganisasi.setItem(i,0, QTableWidgetItem(r["id_organisasi"]))
            self.form.tabelOrganisasi.setItem(i,1, QTableWidgetItem(r["nama_organisasi"]))
            self.form.tabelOrganisasi.setItem(i,2, QTableWidgetItem(r["alamat"]))
            self.form.tabelOrganisasi.setItem(i,3, QTableWidgetItem(r["no_telepon"]))
            self.form.tabelOrganisasi.setItem(i,4, QTableWidgetItem(r["status"]))

        self.bersihkanForm()

    def doCariOrganisasi(self):
        cari = self.form.editCari.text()
        baris = self.crud.cariOrganisasi(cari)
        self.form.tabelOrganisasi.setRowCount(0)
        for r in baris:
            i = self.form.tabelOrganisasi.rowCount()
            self.form.tabelOrganisasi.insertRow(i)
            self.form.tabelOrganisasi.setItem(i,0, QTableWidgetItem(r["id_organisasi"]))
            self.form.tabelOrganisasi.setItem(i,1, QTableWidgetItem(r["nama_organisasi"]))
            self.form.tabelOrganisasi.setItem(i,2, QTableWidgetItem(r["alamat"]))
            self.form.tabelOrganisasi.setItem(i,3, QTableWidgetItem(r["no_telepon"]))
            self.form.tabelOrganisasi.setItem(i,4, QTableWidgetItem(r["status"]))

    def bersihkanForm(self):
        self.form.editIdOrganisasi.clear()
        self.form.editNamaOrganisasi.clear()
        self.form.editAlamat.clear()
        self.form.editNoTelepon.clear()
        self.form.editStatus.clear()

    def doTabelKlik(self, item):
        row = item.row()
        id_organisasi = self.form.tabelOrganisasi.item(row, 0).text()
        nama_organisasi = self.form.tabelOrganisasi.item(row, 1).text()
        alamat = self.form.tabelOrganisasi.item(row, 2).text()
        no_telepon = self.form.tabelOrganisasi.item(row, 3).text()
        status = self.form.tabelOrganisasi.item(row, 4).text()

        self.form.editIdOrganisasi.setText(id_organisasi)
        self.form.editNamaOrganisasi.setText(nama_organisasi)
        self.form.editAlamat.setText(alamat)
        self.form.editNoTelepon.setText(no_telepon)
        self.form.editStatus.setText(status)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = organisasi()
    widget.show()
    sys.exit(app.exec())

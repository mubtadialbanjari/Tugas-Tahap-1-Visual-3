import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class kategoribantuan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("kategoribantuan.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.form.btnSimpan.clicked.connect(self.doSimpanKategoriBantuan)
        self.form.btnUbah.clicked.connect(self.doUbahKategoriBantuan)
        self.form.btnHapus.clicked.connect(self.doHapusKategoriBantuan)
        self.form.editCari.textChanged.connect(self.doCariKategoriBantuan)
        self.form.tabelKategoriBantuan.itemClicked.connect(self.doTabelKlik)

        self.tampilDataKategoriBantuan()

    def doSimpanKategoriBantuan(self):
        if not self.form.editIdKategori.text().strip():
            QMessageBox.information(None,"Informasi","ID Kategori belum di isi")
            self.form.editIdKategori.setFocus()
        elif not self.form.editNamaKategori.text().strip():
            QMessageBox.information(None,"Informasi","Nama Kategori belum di isi")
            self.form.editNamaKategori.setFocus()
        elif not self.form.editDeskripsi.text().strip():
            QMessageBox.information(None,"Informasi","Deskripsi belum di isi")
            self.form.editDeskripsi.setFocus()
        elif not self.form.editJenis.text().strip():
            QMessageBox.information(None,"Informasi","Jenis belum di isi")
            self.form.editJenis.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Simpan Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdKategori.text()
                tempNama = self.form.editNamaKategori.text()
                tempDeskripsi = self.form.editDeskripsi.text()
                tempJenis = self.form.editJenis.text()
                tempStatus = self.form.editStatus.text()
                self.crud.simpanKategoriBantuan(tempID, tempNama, tempDeskripsi, tempJenis, tempStatus)
                self.tampilDataKategoriBantuan()
            else:
                pass

    def doUbahKategoriBantuan(self):
        if not self.form.editIdKategori.text().strip():
            QMessageBox.information(None,"Informasi","ID Kategori belum di isi. Klik data dari tabel.")
            self.form.editIdKategori.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Ubah Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdKategori.text()
                tempNama = self.form.editNamaKategori.text()
                tempDeskripsi = self.form.editDeskripsi.text()
                tempJenis = self.form.editJenis.text()
                tempStatus = self.form.editStatus.text()
                self.crud.ubahKategoriBantuan(tempID, tempNama, tempDeskripsi, tempJenis, tempStatus)
                self.tampilDataKategoriBantuan()
            else:
                pass

    def doHapusKategoriBantuan(self):
        if not self.form.editIdKategori.text().strip():
            QMessageBox.information(None,"Informasi","ID Kategori belum di isi. Klik data dari tabel.")
            self.form.editIdKategori.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Hapus Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdKategori.text()
                self.crud.hapusKategoriBantuan(tempID)
                self.tampilDataKategoriBantuan()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilDataKategoriBantuan(self):
        baris = self.crud.dataKategoriBantuan()
        self.form.tabelKategoriBantuan.setRowCount(0)
        for r in baris:
            i = self.form.tabelKategoriBantuan.rowCount()
            self.form.tabelKategoriBantuan.insertRow(i)
            self.form.tabelKategoriBantuan.setItem(i,0, QTableWidgetItem(r["id_kategori"]))
            self.form.tabelKategoriBantuan.setItem(i,1, QTableWidgetItem(r["nama_kategori"]))
            self.form.tabelKategoriBantuan.setItem(i,2, QTableWidgetItem(r["deskripsi"]))
            self.form.tabelKategoriBantuan.setItem(i,3, QTableWidgetItem(r["jenis"]))
            self.form.tabelKategoriBantuan.setItem(i,4, QTableWidgetItem(r["status"]))

        self.bersihkanForm()

    def doCariKategoriBantuan(self):
        cari = self.form.editCari.text()
        baris = self.crud.cariKategoriBantuan(cari)
        self.form.tabelKategoriBantuan.setRowCount(0)
        for r in baris:
            i = self.form.tabelKategoriBantuan.rowCount()
            self.form.tabelKategoriBantuan.insertRow(i)
            self.form.tabelKategoriBantuan.setItem(i,0, QTableWidgetItem(r["id_kategori"]))
            self.form.tabelKategoriBantuan.setItem(i,1, QTableWidgetItem(r["nama_kategori"]))
            self.form.tabelKategoriBantuan.setItem(i,2, QTableWidgetItem(r["deskripsi"]))
            self.form.tabelKategoriBantuan.setItem(i,3, QTableWidgetItem(r["jenis"]))
            self.form.tabelKategoriBantuan.setItem(i,4, QTableWidgetItem(r["status"]))

    def bersihkanForm(self):
        self.form.editIdKategori.clear()
        self.form.editNamaKategori.clear()
        self.form.editDeskripsi.clear()
        self.form.editJenis.clear()
        self.form.editStatus.clear()

    def doTabelKlik(self, item):
        row = item.row()
        id_kategori = self.form.tabelKategoriBantuan.item(row, 0).text()
        nama_kategori = self.form.tabelKategoriBantuan.item(row, 1).text()
        deskripsi = self.form.tabelKategoriBantuan.item(row, 2).text()
        jenis = self.form.tabelKategoriBantuan.item(row, 3).text()
        status = self.form.tabelKategoriBantuan.item(row, 4).text()

        self.form.editIdKategori.setText(id_kategori)
        self.form.editNamaKategori.setText(nama_kategori)
        self.form.editDeskripsi.setText(deskripsi)
        self.form.editJenis.setText(jenis)
        self.form.editStatus.setText(status)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = kategori_bantuan()
    widget.show()
    sys.exit(app.exec())

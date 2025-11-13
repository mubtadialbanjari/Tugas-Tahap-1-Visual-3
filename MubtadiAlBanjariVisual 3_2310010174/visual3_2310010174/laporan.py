import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class laporan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("laporan.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.form.btnSimpan.clicked.connect(self.doSimpanLaporan)
        self.form.btnUbah.clicked.connect(self.doUbahLaporan)
        self.form.btnHapus.clicked.connect(self.doHapusLaporan)
        self.form.editCari.textChanged.connect(self.doCariLaporan)
        self.form.tabelLaporan.itemClicked.connect(self.doTabelKlik)

        self.tampilDataLaporan()

    def doSimpanLaporan(self):
        if not self.form.editIdLaporan.text().strip():
            QMessageBox.information(None,"Informasi","ID Laporan belum di isi")
            self.form.editIdLaporan.setFocus()
        elif not self.form.editIdBantuan.text().strip():
            QMessageBox.information(None,"Informasi","ID Bantuan belum di isi")
            self.form.editIdBantuan.setFocus()
        elif not self.form.editKeterangan.text().strip():
            QMessageBox.information(None,"Informasi","Keterangan belum di isi")
            self.form.editKeterangan.setFocus()
        elif not self.form.editStatus.text().strip():
            QMessageBox.information(None,"Informasi","Status belum di isi")
            self.form.editStatus.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Simpan Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdLaporan.text()
                tempIdBantuan = self.form.editIdBantuan.text()
                tempKeterangan = self.form.editKeterangan.text()
                tempStatus = self.form.editStatus.text()
                tempTanggal = self.form.editTanggalLaporan.text()
                self.crud.simpanLaporan(tempID, tempIdBantuan, tempKeterangan, tempStatus, tempTanggal)
                self.tampilDataLaporan()
            else:
                pass

    def doUbahLaporan(self):
        if not self.form.editIdLaporan.text().strip():
            QMessageBox.information(None,"Informasi","ID Laporan belum di isi. Klik data dari tabel.")
            self.form.editIdLaporan.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Ubah Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdLaporan.text()
                tempIdBantuan = self.form.editIdBantuan.text()
                tempKeterangan = self.form.editKeterangan.text()
                tempStatus = self.form.editStatus.text()
                tempTanggal = self.form.editTanggalLaporan.text()
                self.crud.ubahLaporan(tempID, tempIdBantuan, tempKeterangan, tempStatus, tempTanggal)
                self.tampilDataLaporan()
            else:
                pass

    def doHapusLaporan(self):
        if not self.form.editIdLaporan.text().strip():
            QMessageBox.information(None,"Informasi","ID Laporan belum di isi. Klik data dari tabel.")
            self.form.editIdLaporan.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Hapus Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdLaporan.text()
                self.crud.hapusLaporan(tempID)
                self.tampilDataLaporan()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilDataLaporan(self):
        baris = self.crud.dataLaporan()
        self.form.tabelLaporan.setRowCount(0)
        for r in baris:
            i = self.form.tabelLaporan.rowCount()
            self.form.tabelLaporan.insertRow(i)
            self.form.tabelLaporan.setItem(i,0, QTableWidgetItem(r["id_laporan"]))
            self.form.tabelLaporan.setItem(i,1, QTableWidgetItem(r["id_bantuan"]))
            self.form.tabelLaporan.setItem(i,2, QTableWidgetItem(r["keterangan"]))
            self.form.tabelLaporan.setItem(i,3, QTableWidgetItem(r["status"]))
            self.form.tabelLaporan.setItem(i,4, QTableWidgetItem(r["tanggal_laporan"]))

        self.bersihkanForm()

    def doCariLaporan(self):
        cari = self.form.editCari.text()
        baris = self.crud.cariLaporan(cari)
        self.form.tabelLaporan.setRowCount(0)
        for r in baris:
            i = self.form.tabelLaporan.rowCount()
            self.form.tabelLaporan.insertRow(i)
            self.form.tabelLaporan.setItem(i,0, QTableWidgetItem(r["id_laporan"]))
            self.form.tabelLaporan.setItem(i,1, QTableWidgetItem(r["id_bantuan"]))
            self.form.tabelLaporan.setItem(i,2, QTableWidgetItem(r["keterangan"]))
            self.form.tabelLaporan.setItem(i,3, QTableWidgetItem(r["status"]))
            self.form.tabelLaporan.setItem(i,4, QTableWidgetItem(r["tanggal_laporan"]))

    def bersihkanForm(self):
        self.form.editIdLaporan.clear()
        self.form.editIdBantuan.clear()
        self.form.editKeterangan.clear()
        self.form.editStatus.clear()
        self.form.editTanggalLaporan.clear()

    def doTabelKlik(self, item):
        row = item.row()
        id_laporan = self.form.tabelLaporan.item(row, 0).text()
        id_bantuan = self.form.tabelLaporan.item(row, 1).text()
        keterangan = self.form.tabelLaporan.item(row, 2).text()
        status = self.form.tabelLaporan.item(row, 3).text()
        tanggal_laporan = self.form.tabelLaporan.item(row, 4).text()

        self.form.editIdLaporan.setText(id_laporan)
        self.form.editIdBantuan.setText(id_bantuan)
        self.form.editKeterangan.setText(keterangan)
        self.form.editStatus.setText(status)
        self.form.editTanggalLaporan.setText(tanggal_laporan)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = laporan()
    widget.show()
    sys.exit(app.exec())

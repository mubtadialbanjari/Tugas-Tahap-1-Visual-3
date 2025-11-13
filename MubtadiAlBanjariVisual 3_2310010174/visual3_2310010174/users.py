import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class users(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("users.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.form.btnSimpan.clicked.connect(self.doSimpanUsers)
        self.form.btnUbah.clicked.connect(self.doUbahUsers)
        self.form.btnHapus.clicked.connect(self.doHapusUsers)
        self.form.editCari.textChanged.connect(self.doCariUsers)
        self.form.tabelUsers.itemClicked.connect(self.doTabelKlik)

        self.tampilDataUsers()

    def doSimpanUsers(self):
        if not self.form.editIdUser.text().strip():
            QMessageBox.information(None,"Informasi","ID User belum di isi")
            self.form.editIdUser.setFocus()
        elif not self.form.editNamaUser.text().strip():
            QMessageBox.information(None,"Informasi","Nama User belum di isi")
            self.form.editNamaUser.setFocus()
        elif not self.form.editPassword.text().strip():
            QMessageBox.information(None,"Informasi","Password belum di isi")
            self.form.editPassword.setFocus()
        elif not self.form.editRole.text().strip():
            QMessageBox.information(None,"Informasi","Role belum di isi")
            self.form.editRole.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Simpan Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdUser.text()
                tempNama = self.form.editNamaUser.text()
                tempPassword = self.form.editPassword.text()
                tempRole = self.form.editRole.text()
                tempTelepon = self.form.editNoTelepon.text()
                self.crud.simpanUsers(tempID, tempNama, tempPassword, tempRole, tempTelepon)
                self.tampilDataUsers()
            else:
                pass

    def doUbahUsers(self):
        if not self.form.editIdUser.text().strip():
            QMessageBox.information(None,"Informasi","ID User belum di isi. Klik data dari tabel.")
            self.form.editIdUser.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Ubah","Ubah Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdUser.text()
                tempNama = self.form.editNamaUser.text()
                tempPassword = self.form.editPassword.text()
                tempRole = self.form.editRole.text()
                tempTelepon = self.form.editNoTelepon.text()
                self.crud.ubahUsers(tempID, tempNama, tempPassword, tempRole, tempTelepon)
                self.tampilDataUsers()
            else:
                pass

    def doHapusUsers(self):
        if not self.form.editIdUser.text().strip():
            QMessageBox.information(None,"Informasi","ID User belum di isi. Klik data dari tabel.")
            self.form.editIdUser.setFocus()
        else:
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Hapus Data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.form.editIdUser.text()
                self.crud.hapusUsers(tempID)
                self.tampilDataUsers()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
            else:
                pass

    def tampilDataUsers(self):
        baris = self.crud.dataUsers()
        self.form.tabelUsers.setRowCount(0)
        for r in baris:
            i = self.form.tabelUsers.rowCount()
            self.form.tabelUsers.insertRow(i)
            self.form.tabelUsers.setItem(i,0, QTableWidgetItem(r["id_user"]))
            self.form.tabelUsers.setItem(i,1, QTableWidgetItem(r["nama_user"]))
            self.form.tabelUsers.setItem(i,2, QTableWidgetItem(r["role"]))
            self.form.tabelUsers.setItem(i,3, QTableWidgetItem(r["no_telepon"]))

        self.bersihkanForm()

    def doCariUsers(self):
        cari = self.form.editCari.text()
        baris = self.crud.cariUsers(cari)
        self.form.tabelUsers.setRowCount(0)
        for r in baris:
            i = self.form.tabelUsers.rowCount()
            self.form.tabelUsers.insertRow(i)
            self.form.tabelUsers.setItem(i,0, QTableWidgetItem(r["id_user"]))
            self.form.tabelUsers.setItem(i,1, QTableWidgetItem(r["nama_user"]))
            self.form.tabelUsers.setItem(i,2, QTableWidgetItem(r["role"]))
            self.form.tabelUsers.setItem(i,3, QTableWidgetItem(r["no_telepon"]))

    def bersihkanForm(self):
        self.form.editIdUser.clear()
        self.form.editNamaUser.clear()
        self.form.editPassword.clear()
        self.form.editRole.clear()
        self.form.editNoTelepon.clear()

    def doTabelKlik(self, item):
        row = item.row()
        id_user = self.form.tabelUsers.item(row, 0).text()
        nama_user = self.form.tabelUsers.item(row, 1).text()
        role = self.form.tabelUsers.item(row, 2).text()
        no_telepon = self.form.tabelUsers.item(row, 3).text()

        self.form.editIdUser.setText(id_user)
        self.form.editNamaUser.setText(nama_user)
        self.form.editRole.setText(role)
        self.form.editNoTelepon.setText(no_telepon)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = users()
    widget.show()
    sys.exit(app.exec())

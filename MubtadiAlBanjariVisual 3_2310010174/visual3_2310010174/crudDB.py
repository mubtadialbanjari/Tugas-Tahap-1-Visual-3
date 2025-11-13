import mysql.connector

class my_cruddb:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'visual3_2310010174'
        )

    def simpanUsers(self, id_user, nama_user, password, role, no_telepon):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO users (id_user, nama_user, password, role, no_telepon) VALUES (%s, %s, %s, %s, %s)",(id_user, nama_user, password, role, no_telepon))
        self.conn.commit()
        alamat.close()

    def ubahUsers(self, id_user, nama_user, password, role, no_telepon):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE users SET nama_user=%s, password=%s, role=%s, no_telepon=%s WHERE id_user=%s",(nama_user, password, role, no_telepon, id_user))
        self.conn.commit()
        alamat.close()

    def hapusUsers(self, id_user):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM users WHERE id_user=%s",(id_user,))
        self.conn.commit()
        alamat.close()

    def dataUsers(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM users ORDER BY id_user ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariUsers(self, param):
        sql = "SELECT * FROM users WHERE id_user LIKE %s OR nama_user LIKE %s OR role LIKE %s OR no_telepon LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanOrganisasi(self, id_organisasi, nama_organisasi, alamat_org, no_telepon, status):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO organisasi (id_organisasi, nama_organisasi, alamat, no_telepon, status) VALUES (%s, %s, %s, %s, %s)",(id_organisasi, nama_organisasi, alamat_org, no_telepon, status))
        self.conn.commit()
        alamat.close()

    def ubahOrganisasi(self, id_organisasi, nama_organisasi, alamat_org, no_telepon, status):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE organisasi SET nama_organisasi=%s, alamat=%s, no_telepon=%s, status=%s WHERE id_organisasi=%s",(nama_organisasi, alamat_org, no_telepon, status, id_organisasi))
        self.conn.commit()
        alamat.close()

    def hapusOrganisasi(self, id_organisasi):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM organisasi WHERE id_organisasi=%s",(id_organisasi,))
        self.conn.commit()
        alamat.close()

    def dataOrganisasi(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM organisasi ORDER BY id_organisasi ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariOrganisasi(self, param):
        sql = "SELECT * FROM organisasi WHERE id_organisasi LIKE %s OR nama_organisasi LIKE %s OR alamat LIKE %s OR no_telepon LIKE %s OR status LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanKategoriBantuan(self, id_kategori, nama_kategori, deskripsi, jenis, status):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO kategori_bantuan (id_kategori, nama_kategori, deskripsi, jenis, status) VALUES (%s, %s, %s, %s, %s)",(id_kategori, nama_kategori, deskripsi, jenis, status))
        self.conn.commit()
        alamat.close()

    def ubahKategoriBantuan(self, id_kategori, nama_kategori, deskripsi, jenis, status):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE kategori_bantuan SET nama_kategori=%s, deskripsi=%s, jenis=%s, status=%s WHERE id_kategori=%s",(nama_kategori, deskripsi, jenis, status, id_kategori))
        self.conn.commit()
        alamat.close()

    def hapusKategoriBantuan(self, id_kategori):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM kategori_bantuan WHERE id_kategori=%s",(id_kategori,))
        self.conn.commit()
        alamat.close()

    def dataKategoriBantuan(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM kategori_bantuan ORDER BY id_kategori ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariKategoriBantuan(self, param):
        sql = "SELECT * FROM kategori_bantuan WHERE id_kategori LIKE %s OR nama_kategori LIKE %s OR deskripsi LIKE %s OR jenis LIKE %s OR status LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanBantuan(self, id_bantuan, id_organisasi, id_kategori, nominal, tanggal):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO bantuan (id_bantuan, id_organisasi, id_kategori, nominal, tanggal) VALUES (%s, %s, %s, %s, %s)",(id_bantuan, id_organisasi, id_kategori, nominal, tanggal))
        self.conn.commit()
        alamat.close()

    def ubahBantuan(self, id_bantuan, id_organisasi, id_kategori, nominal, tanggal):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE bantuan SET id_organisasi=%s, id_kategori=%s, nominal=%s, tanggal=%s WHERE id_bantuan=%s",(id_organisasi, id_kategori, nominal, tanggal, id_bantuan))
        self.conn.commit()
        alamat.close()

    def hapusBantuan(self, id_bantuan):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM bantuan WHERE id_bantuan=%s",(id_bantuan,))
        self.conn.commit()
        alamat.close()

    def dataBantuan(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM bantuan ORDER BY id_bantuan ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariBantuan(self, param):
        sql = "SELECT * FROM bantuan WHERE id_bantuan LIKE %s OR id_organisasi LIKE %s OR id_kategori LIKE %s OR nominal LIKE %s OR tanggal LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanLaporan(self, id_laporan, id_bantuan, keterangan, status, tanggal_laporan):
        alamat = self.conn.cursor()
        alamat.execute("INSERT INTO laporan (id_laporan, id_bantuan, keterangan, status, tanggal_laporan) VALUES (%s, %s, %s, %s, %s)",(id_laporan, id_bantuan, keterangan, status, tanggal_laporan))
        self.conn.commit()
        alamat.close()

    def ubahLaporan(self, id_laporan, id_bantuan, keterangan, status, tanggal_laporan):
        alamat = self.conn.cursor()
        alamat.execute("UPDATE laporan SET id_bantuan=%s, keterangan=%s, status=%s, tanggal_laporan=%s WHERE id_laporan=%s",(id_bantuan, keterangan, status, tanggal_laporan, id_laporan))
        self.conn.commit()
        alamat.close()

    def hapusLaporan(self, id_laporan):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM laporan WHERE id_laporan=%s",(id_laporan,))
        self.conn.commit()
        alamat.close()

    def dataLaporan(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("SELECT * FROM laporan ORDER BY id_laporan ASC")
        record = alamat.fetchall()
        alamat.close()
        return record

    def cariLaporan(self, param):
        sql = "SELECT * FROM laporan WHERE id_laporan LIKE %s OR id_bantuan LIKE %s OR keterangan LIKE %s OR status LIKE %s OR tanggal_laporan LIKE %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

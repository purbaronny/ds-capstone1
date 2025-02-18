pelajaran_list = [
    {"id": "BHS", "nama": "Bahasa Indonesia"},
    {"id": "MTK", "nama": "Matematika"},
    {"id": "ENG", "nama": "Bahasa Inggris"},
]

siswa_list = [
    {"id": 1, "nama": "Ali", "nilais": []},
    {"id": 2, "nama": "Budi", "nilais": []},
    {"id": 3, "nama": "Citra", "nilais": []},
]

# CREATE: Menambahkan data siswa
def tambah_siswa(nama):
    try:
        if not nama[0].isalpha():
            raise ValueError("Nama harus dimulai dengan huruf.")
        
        siswa_list.append({"id": len(siswa_list) + 1, "nama": nama, "nilais": []})
        print("Data siswa berhasil ditambahkan!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# CREATE: Menambahkan pelajaran ke siswa
def tambah_pelajaran_siswa(id_siswa, pelajaranId, nilai):
    try:
        if not (0 <= nilai <= 100):
            raise ValueError("Nilai harus berada dalam rentang 0-100.")
        if pelajaranId not in [p["id"] for p in pelajaran_list]:
            raise ValueError("ID pelajaran tidak ditemukan.")
        
        for siswa in siswa_list:
            if siswa["id"] == id_siswa:
                siswa["nilais"].append({"pelajaranId": pelajaranId, "nilai": nilai})
                print("Pelajaran berhasil ditambahkan ke siswa!")
                return
        raise ValueError("ID siswa tidak ditemukan!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# READ: Menampilkan semua data siswa
def tampilkan_siswa():
    for siswa in siswa_list:
        print(siswa)

# UPDATE: Memperbarui nilai siswa dalam pelajaran tertentu
def perbarui_nilai(id_siswa, pelajaranId, nilai_baru):
    try:
        # Validasi nilai baru harus dalam rentang 0-100
        if not (0 <= nilai_baru <= 100):
            raise ValueError("Nilai harus berada dalam rentang 0-100.")

        # Cari siswa berdasarkan ID
        for siswa in siswa_list:
            if siswa["id"] == id_siswa:
                # Cari pelajaran dalam daftar nilai siswa
                for nilai in siswa["nilais"]:
                    if nilai["pelajaranId"] == pelajaranId:
                        nilai["nilai"] = nilai_baru  # Perbarui nilai
                        print("Nilai berhasil diperbarui!")
                        return
                
                raise ValueError("Pelajaran tidak ditemukan pada siswa ini.")
        
        raise ValueError("ID siswa tidak ditemukan!")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# DELETE: Menghapus siswa berdasarkan ID
def hapus_siswa(id_siswa):
    global siswa_list  # Gunakan variabel global untuk memperbarui daftar siswa
    try:
        # Cek apakah ID siswa ada dalam daftar
        siswa_ditemukan = any(siswa["id"] == id_siswa for siswa in siswa_list)
        
        if not siswa_ditemukan:
            raise ValueError("ID siswa tidak ditemukan!")

        # Hapus siswa dari daftar
        siswa_list = [siswa for siswa in siswa_list if siswa["id"] != id_siswa]
        print("Siswa berhasil dihapus!")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# CREATE: Menambahkan pelajaran baru
def tambah_pelajaran(id_pelajaran, nama_pelajaran):
    try:
        if not id_pelajaran.isalnum():
            raise ValueError("ID pelajaran harus berupa huruf dan/atau angka.")
        if any(p["id"] == id_pelajaran for p in pelajaran_list):
            raise ValueError("ID pelajaran sudah ada.")
        
        pelajaran_list.append({"id": id_pelajaran, "nama": nama_pelajaran})
        print("Pelajaran berhasil ditambahkan!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# READ: Menampilkan semua pelajaran
def tampilkan_pelajaran():
    print("\n=== Daftar Pelajaran ===")
    for pelajaran in pelajaran_list:
        print(f"ID: {pelajaran['id']}, Nama: {pelajaran['nama']}")

# UPDATE: Memperbarui nama pelajaran
def perbarui_pelajaran(id_pelajaran, nama_baru):
    for pelajaran in pelajaran_list:
        if pelajaran["id"] == id_pelajaran:
            pelajaran["nama"] = nama_baru
            print("Pelajaran berhasil diperbarui!")
            return
    print("ID pelajaran tidak ditemukan!")

# DELETE: Menghapus pelajaran
def hapus_pelajaran(id_pelajaran):
    global pelajaran_list
    pelajaran_list = [p for p in pelajaran_list if p["id"] != id_pelajaran]
    print("Pelajaran berhasil dihapus!")


# Menu utama
def main():
    while True:
        print("\n=== Sistem Data Nilai Siswa ===")
        print("1. Menu Siswa")
        print("2. Menu Pelajaran")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            while True:
                print("\n=== Menu Siswa ===")
                print("1. Tambah Siswa")
                print("2. Tambah Pelajaran ke Siswa")
                print("3. Tampilkan Semua Siswa")
                print("4. Perbarui Nilai Siswa")
                print("5. Hapus Siswa")
                print("6. Kembali ke Menu Utama")
                sub_pilihan = input("Pilih menu: ")
                
                if sub_pilihan == "1":
                    nama = input("Masukkan nama siswa: ")
                    tambah_siswa(nama)
                elif sub_pilihan == "2":
                    try:
                        id_siswa = int(input("Masukkan ID siswa: "))
                        pelajaranId = input("Masukkan ID pelajaran: ")
                        nilai = int(input("Masukkan nilai: "))
                        tambah_pelajaran_siswa(id_siswa, pelajaranId, nilai)
                    except ValueError:
                        print("ID siswa dan nilai harus berupa angka.")
                elif sub_pilihan == "3":
                    tampilkan_siswa()
                elif sub_pilihan == "4":
                    try:
                        id_siswa = int(input("Masukkan ID siswa yang akan diperbarui: "))
                        pelajaranId = input("Masukkan ID pelajaran: ")
                        nilai_baru = int(input("Masukkan nilai baru: "))
                        perbarui_nilai(id_siswa, pelajaranId, nilai_baru)
                    except ValueError:
                        print("ID dan nilai harus berupa angka.")
                elif sub_pilihan == "5":
                    id_siswa = int(input("Masukkan ID siswa yang akan dihapus: "))
                    hapus_siswa(id_siswa)
                elif sub_pilihan == "6":
                    break
                else:
                    print("Pilihan tidak valid, coba lagi.")
        elif pilihan == "2":
            print("\n=== Menu Pelajaran ===")
            while True:
                print("\n=== Menu Pelajaran ===")
                print("1. Tambahkan Pelajaran")
                print("2. Tampilkan Semua Pelajaran")
                print("3. Perbarui Pelajaran")
                print("4. Hapus Pelajaran")
                print("5. Kembali ke Menu Utama")
                sub_pilihan = input("Pilih menu: ")

                if sub_pilihan == "1":
                    id_pelajaran = input("Masukkan ID pelajaran: ")
                    nama_pelajaran = input("Masukkan nama pelajaran: ")
                    tambah_pelajaran(id_pelajaran, nama_pelajaran)
                elif sub_pilihan == "2":
                    tampilkan_pelajaran()
                elif sub_pilihan == "3":
                    id_pelajaran = input("Masukkan ID pelajaran yang ingin diperbarui: ")
                    nama_baru = input("Masukkan nama baru: ")
                    perbarui_pelajaran(id_pelajaran, nama_baru)
                elif sub_pilihan == "4":
                    id_pelajaran = input("Masukkan ID pelajaran yang ingin dihapus: ")
                    hapus_pelajaran(id_pelajaran)
                elif sub_pilihan == "5":
                    break
                else:
                    print("Pilihan tidak valid, coba lagi.")
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()

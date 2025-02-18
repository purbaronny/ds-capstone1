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
            tampilkan_pelajaran()
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()

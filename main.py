print("=== PROGRAM DATA MAHASISWA ===")
print("Belajar Version Control System")

nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")

print("\n=== DATA MAHASISWA ===")
print("Halo,", nama)
print("Umur:", umur, "tahun")

status = input("Apakah mahasiswa aktif? (ya/tidak): ")

if status.lower() == "ya":
    print("Status: Mahasiswa Aktif")
else:
    print("Status: Tidak Aktif")
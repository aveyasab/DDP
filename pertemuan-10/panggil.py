import bangun_datar, bangun_ruang

print("===Luas Bangun Datar====")
print(f"Luas Persegi = {bangun_datar.luas_persegi(5)}")
print(f"Luas Segitiga = {bangun_datar.luas_segitiga(5, 5)}")
print(f"Luas Lingkaran = {bangun_datar.luas_lingkaran(5)}")
print(f"Luas Ketupat = {bangun_datar.luas_ketupat(5, 5)}")
print(f"Luas Jajar Genjang = {bangun_datar.luas_jajar_genjang(5, 5)}")

print("===Luas Bangun Ruang====")
print(f"Luas Kubus = {bangun_ruang.luas_kubus(5)}")
print(f"Luas Balok = {bangun_ruang.luas_balok(5, 5, 5)}")
print(f"Luas Bola  = {bangun_ruang.luas_bola(5)}")
print (f"Luas Tabung = {bangun_ruang.luas_tabung(5, 5)}")
print (f"Luas Kerucut = {bangun_ruang.luas_kerucut(5, 5)}")
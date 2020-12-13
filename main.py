# Nama : Agung Mubarok
# NIM  : 0110120196
# Kelas: Sistem Informasi - 05

def convert_list(multilist):
  # Variabel newList untuk menyimpan list dalam bentuk array
  newList = [] 
  # Membuat perulangan dimana nilai i berada di dalam parameter multilist
  for i in multilist:
    # Membuat perulangan dimana nilai j berada di dalam i
    for j in i:
      # Menambahkan nilai j ke dalam variabel newList 
      newList.append(j) 
  # Mengembalikan nilai newList
  return newList

# ==========================================================
# ==========================================================

def get_nilai(filename, nama):
  # Variabel f untuk membuka file dan merepresentasikan isi file tersebut dengan fungsi open()
  f = open(filename)
  # Membuat perulangan dengan data yang berada pada variabel f
  for each_line in f:
    # Variabel data untuk menyimpan nilai each_line yang sudah memecah string ke dalam sekumpulan string yang lebih kecil yang nantinya akan disimpan dalam bentuk list menggunakan fungsi split()
    data = each_line.split()
    # Jika nilai yang ada di variabel data dengan index ke 0 sama dengan nilai yang diterima oleh parameter nama.
    if data[0].lower() == nama.lower():
      # maka Mengembalikan nilai float lalu dibulatkan
      return round(float(data[1]))
  # Jika pengolahan file sudah selesai
  f.close()

# ==========================================================
# ==========================================================

def nilai_max(filename):
  # Variabel f untuk membuka file dan merepresentasikan isi file tersebut dengan fungsi open()
  f = open(filename)
  #Variabel name menyimpan nama tertinggi sementara dalam bentu string
  name = "" 
  # Variabel nilai menyimpan nilai tertinggi sementara
  nilai = 0 
  # Membuat perulangan dengan data yang berada pada variabel f
  for each_line in f:
    # Variabel data untuk menyimpan nilai each_line yang sudah memecah string ke dalam sekumpulan string yang lebih kecil yang nantinya akan disimpan dalam bentuk list menggunakan fungsi split()
    data = each_line.split()
    #jika nilai list saat ini lebih besar dari nilai tertinggi saat ini
    if float(data[1]) > nilai: 
      #Maka mengganti nama tertinggi saat ini
      name = data[0] 
      #Dan mengganti nilai tertinggi saat ini
      nilai = float(data[1]) 
  # Jika pengolahan file sudah selesai
  f.close()
  # Mengembalikan nilai parameter filename
  return (name, nilai)

# ==========================================================
# ==========================================================



# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = convert_list([[1,2], [3,4], [5,6]])
  print(f"convert_list([[1,2], [3,4], [5,6]]) = {r} \n(solusi: [1, 2, 3, 4, 5, 6])")
  print()
  r = get_nilai('nilai1.txt','joni')
  print(f"get_nilai('nilai1.txt','joni') = {r} \n(solusi: 76)")
  print()
  r = get_nilai('nilai2.txt','joni')
  print(f"get_nilai('nilai2.txt','joni') = {r} \n(solusi: None)")
  print()
  r = nilai_max('nilai1.txt')
  print(f"nilai_max('nilai1.txt') = {r} \n(solusi: ('Zack', 88.05)")
  print()
  r = nilai_max('nilai2.txt')
  print(f"nilai_max('nilai2.txt') = {r} \n(solusi: ('Arya', 90.00)")
  print()

if __name__ == '__main__':
  test()
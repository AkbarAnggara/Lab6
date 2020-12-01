# Tugas Praktikum 6 - Pertemuan 10

Nama : Bangkit Akbar Anggara<br>
NIM : 312010148<br>
Kelas : TI.20.B.1<br>

Pada pertemuan 10 saya di berikan tugas dan latihan praktikum 6

# Latihan
Berikut adalah soal latihan praktikum 6:<br>
![tugas_latihan.png](Pic/tugas_latihan.png)


Berikut adalah syntax yang saya gunakan:<br>
![syntax_latihan.png](Pic/syntax_latihan.png)<br>
Keterangan:
  - import digunakan untuk multi file maksudnya adalah kita dapat memanggil file lain di dalam satu module yang berbeda<br>
  - Lalu saya menggunakan double(aa,bb,cc,dd)karena dalam materi begitulah cara membuat fungsi lambda<br>
  - Lalu seperti biasa print kita gunakan untuk menulis kata - kata
  - Lalu print aa(5) adalah aa dari diuble tadi dan 5 adalah angka(bebas mau pake nomor berapa aja tapi saya disini mnggunakan angka 5)jadi nanti 5 ** 2 sama saja 5 X 5 sehingga hasilnya menjadi 25<br>
  - Lalu sqrt digunakan untuk mencari fungsi akar kuadrat dari 5 dan 10<br>
  - Lalu args digunakan untuk melewatkan satu atau beberapa argumen ke fungsi<br>
  - Lalu Join digunakan untuk menyatukan banyaknya string kedalam sebuah string<br>
  
Maka ketika kita run hasilnya akan seperti berikut<br>
![hasil_latihan.png](Pic/hasil_latihan.png)

# Tugas Praktikum 6

Berikut adalah tugas praktikum 6:<br>
![tugas_praktikum.png](Pic/tugas_praktikum.png)<br>

Untuk source code yang saya gunakan silahkan kalian klik tombol di samping:  [Click Here](prakikum_6.py)

Baiklah saya akan menjelaskan fungsi - fungsi dari syntax tersebut:<br>

1. Disini saya menggunakan dictionary<br>
  ![dictionary.png](Pic/dictionary.png)<br>
Keterangan:<br>
    - Kalian bisa menggunakan list atau dictionary sesuai keinginan kalian sendiri tapi tentu saja list dan dictionary berbeda ya tapi tujuannya sama<br>

2. Tambah data nilai mahasiswa<br>
  ![syntax_tambah.png](Pic/syntax_tambah.png)<br>
Keterangan:<br>
    - def tambah, def digunakan untuk membuat fungsi lalu tambah digunakan agar ketika kita memilih menu tambah langsung mengeksekusi syntax tersebut<br>
    - Lalu kita buat inputan nama, nim, nilai tugas, nilai uts, dan nilai uas, lalu kita buat hasil / total dari keseluruhan nilai<br>
  
3. Hapus data nilai mahasiswa<br>
  ![syntax_hapus.png](Pic/syntax_hapus.png)<br>
Keterangan:<br>
    - Lalu seperti biasa kita gunakan def hapus agar ketika kita memilih pilihan menu hapus akan masuk ke dalam syntax ini untuk menghapus data<br>
    - Kita buat inputan nama karena kita akan menghapus data nilai mahasiswa tersebut dengan menggunakan nama mereka untuk menghapusnya<br>
    - lalu gunakan if untuk mengeksekusi data yang di dictionary menggunakan nama(True)<br>
    - Lalu del untuk menghapus semua data nilai mahasiswa tersebut<br>
    - Lalu kita buat else gunanya untuk ketika kita belum menginputkan data apapun maka tidak ada data yang bisa di hapus(False)<br>

4. Ubah data nilai mahasiswa<br>
  ![syntax_ubah.png](Pic/syntax_ubah.png)<br>
Keterangan:<br>
    -  kita gunakan def ubah agar ketika kita memilih pilihan menu ubah akan masuk ke dalam syntax ini untuk mengubah data<br> 
    - Lalu kita buat inputan nama karena kita akan mengubah data nilai mahasiswa dengan menginputkan nama mahasiswa tersebut<br>
    - Lalu if nama in data_nilai.keys untuk mengeksekusi jika nama terdapat di dalam dictionary<br>
    - Lalu kita buat inputan untuk memasukkan nilai tugas, uts, dan uas yang terbaru<br>
    - Lalu kita gunakan hasil untuk menghitung total semua nilai tersebut<br>

5. Tampilkan data nilai mahasiswa<br>
  ![syntax_tampil.png](Pic/syntax_tampil.png)<br>
Keterangan:<br>
    - kita gunakan if data_nilai.items gunanya untuk melihat hasil / menampilkan semua data di dalam dictionary(True)<br>
    - Lalu kita gunakan print untuk membuat tablenya<br>
    - Lalu for i = 0 digunakan untuk membuat nomor urut otomatis dibagian No. didalam table<br>
    - Lalu kita gunakan for x gunanya untuk format penampilan data nilai mahasiswa<br>
    - lalu gunanya angka yang di dalam {} itu di gunakan untuk membatasi atau bisa di bilang seperti tab agar data yang di tampilkan lebih rapih<br>
    - Lalu else disini di gunakan ketika kita belum menginputkan atau menambahkan data apapun akan muncul tidak ada data(False)<br>

6. Membuat pilihan menu<br>
  ![pilihan.png](Pic/pilihan.png)<br>
Keterangan:<br>
    - Kita gunakan perulangan while True untuk membuat pilihan menunya<br>
    - Karena tidak disuruh untuk menampilkan outputnya seperti apa jadi saya menggunakan nomor saja untuk membuat pilihan menunya alasannya agar terlihat lebih rapih dan mudah<br>
    - Lalu kita buat dibawahnya inputan untuk memasukkan pilihan yang kita inginkan<br>
    - Lalu kita gunakan if dan elif agar ketika kita memiih menu 1, 2, 3, 4, atau 5 kita akan memasuki syntax yang def tadi<br>
    - Lalu dibawahnya kita gunakan tambah, tampil, hapus, dan ubah untuk mengeksekusi syntax yang tadi, itulah kenapa kita menulisnya def tambah, def tampil, def hapus, dan def ubah<br>
    - lalu kita break kita gunakan untuk keluar dari program tersebut<br>
    - Lalu else digunakan agar ketika kita tidak memilih pilihan menu maka akan muncul tulisan "pilih menu yang tersedia diatas"<br>

Maka ini adalah hasil running dari syntax di atas:

1. Pilihan menu tambah, tampil, hapus, ubah, dan keluar dari program<br>
  ![hasil_pilihan.png](Pic/hasil_pilihan.png)<br>


2. Tambah data nilai mahasiswa<br>
  ![tambah_tampilkan.png](Pic/tambah_tampilkan.png)<br>
  

3. Tampilkan data nilai mahasiwa<br>
  ![tampilan_tidak_ada_data.png](Pic/tampilan_tidak_ada_data.png)<br>
  

4. Hapus data nilai mahasiswa<br>
  ![hapus_tampilkan.png](Pic/hapus_tampilkan.png)<br>
  
5. Ubah data nilai mahasiswa<br>
  ![ubah_tampilkan.png](Pic/ubah_tampilkan.png)<br>
  

6. Keluar dari program<br>
  ![keluar.png](Pic/keluar.png)<br>


7. Ketika kita tidak memilih pilihan menu<br>
  ![ketika_tidak_memilih_menu.png](Pic/ketika_tidak_memilih_menu.png)<br>

Oke sekian penjelasan dari saya kurang lebihnya mohon maaf Wassalamualaikum wr.wb.<br>
Sampai jumpa lagi<br>

by:<br>
 _== Bangkit Akbar Anggara ==_<br>
 _== 312010148 ==_<br>
 _== TI.20.B.1 ==_<br>

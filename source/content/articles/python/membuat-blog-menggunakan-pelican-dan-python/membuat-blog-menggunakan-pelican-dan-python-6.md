Title: Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Melihat trafik menggunakan Google Analytics
Date: 2020-5-30 04:55
Modified: 2020-5-30 04:55
Category: python
Tags: python, pelican 
Slug: membuat-blog-menggunakan-pelican-dan-python-6
Authors: tegardp
Summary: Panduan membuat blog statis menggunakan Pelican

Untuk mengenal lebih baik tentang pengunjung website kamu. Maka, kamu perlu memiliki **web analytics service**. [Google Analytics](https://analytics.google.com/analytics/web/) adalah salah satu web analytics service yang paling banyak digunakan.

Pada tutorial kali ini aku mau berbagi cara mengimplementasikan Google Analyitics ke Web pelican kamu!.

## Prasyarat
* Sudah mendaftar di Google Account dan mengaktifkan Google Analytics

## Goal
- Mengimplementasikan Google Analyitics pada semua halaman website

## Memasang Google Analytics
Sign in ke Google Analytics dan klik ikon gear untuk membuka menu pengaturan. Klik tombol **Create Property**

<p align="center">
  <img src="https://i.imgur.com/EKLuZT6.png" alt="https://i.imgur.com/EKLuZT6.png">
</p>

Isi dan lengkapi form yang diperlukan. Pastika URL yang dimasukkan sama dengan domain yang digunakan untuk mengakses blog kita. Setelah itu klik buat.

<p align="center">
  <img src="https://i.imgur.com/uum1WDq.png" alt="https://i.imgur.com/uum1WDq.png">
</p>

Pada setelan properti kamu dapat melihat ID Pelacakan. Kita akan memberitahukannya ke pelican

<p align="center">
  <img src="https://i.imgur.com/CVipi0l.png" alt="https://i.imgur.com/CVipi0l.png">
</p>

Google Analytics hanya akan bekerja pada pelican yang telah di publikasikan. Oleh karena itu, edit file ```publishconf.py``` kemudian isi ID pelacakan sesuai dengan yang telah didapatkan tadi.

```
GOOGLE_ANALYTICS = 'UA-xxxxxxxxxxxx'
```

Setelah itu seperti biasa lakukan generate pelican

```
pelican content -s publishconf.py
pelican --listen
```

Setelah mengunggah website yang telah digenerate ke hosting. Google Analytics akan mulai bekerja melacak konten website kita.

## Kesimpulan
Jika kamu sudah mengikuti kita dari [awal]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-1.md). Berarti kita sudah berhasil menginstall pelican, mengunggahnya di github pages, dan menambah *3rd party service* untuk menambah fungsi tambahan. Terimakasih telah mengikuti kami dari awal.

[Membuat Blog Menggunakan Pelican dan Python Bagian 1 - Instalasi dan Tema Pelican]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-1.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 2 - Membuat Konten]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-2.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 3 - Mengunggah di Github Pages]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-3.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Custom domain menggunakan Github Pages dan Niagahoster]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-4)
[Membuat Blog Menggunakan Pelican dan Python Bagian 5 - Menambahkan kolom komentar menggunakan Disqus]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-5.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 6 - Melihat trafik menggunakan Google Analytics]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-6.md)
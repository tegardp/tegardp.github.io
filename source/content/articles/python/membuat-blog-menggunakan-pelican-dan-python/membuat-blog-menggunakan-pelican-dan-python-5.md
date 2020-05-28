Title: Membuat Blog Menggunakan Pelican dan Python Bagian 5 - Menambahkan kolom komentar menggunakan Disqus
Date: 2020-5-29 07:35
Modified: 2020-5-29 07:35
Category: python
Tags: python, pelican 
Slug: membuat-blog-menggunakan-pelican-dan-python-5
Authors: tegardp
Summary: Panduan membuat blog statis menggunakan Pelican

## Prasyarat
* Perlu mendaftar di disqus. Jangan khawatir. Gratis!
## Goal
- Menambahkan kolom komentar pada artikel

## Menginstall Disqus
Setelah kamu mendaftar Disqus, silahkan **create new site**. Perlu diperhatikan URL Disqus akan digenerate dan dapat dilihat di catatan di bawah **Website Name** pada gambar di bawah. Catat bagian **yourusername**.disqus.com karena nanti akan ditambahkan ke konfigurasi pelican

<p align="center">
  <img src="https://i.imgur.com/g8P2v4K.png" alt="https://i.imgur.com/g8P2v4K.png">
</p>

Pilih **basic plan**, jangan khawatir, ini gratis. Nanti, kalau dibutuhkan kamu bisa mengupgradenya kok.

<p align="center">
  <img src="https://matthewdevaney.com/img/disqus_tutorial_2.png" alt="https://matthewdevaney.com/img/disqus_tutorial_2.png">
</p>

Pilih **I don't see my platform liste, install manually with Universal Code**

<p align="center">
  <img src="https://matthewdevaney.com/img/disqus_tutorial_3.png" alt="https://matthewdevaney.com/img/disqus_tutorial_3.png">
</p>

Selanjutnya isi form konfigurasi disqus. Kamu bisa langsung pilih lanjut dan mengonfigurasinya nanti.

<p align="center">
  <img src="https://i.imgur.com/9eznDfN.png" alt="https://i.imgur.com/9eznDfN.png">
</p>

Kolom komentar Disqus hanya akan muncul di website pelican kita. Buka file ``publishconf.py`` dan isi variable DISQUS_SITENAME dengan url username disqus anda

```
DISQUS_SITENAME = 'yourusername'
```

Setelah itu seperti biasa lakukan generate pelican

```
pelican content -s publishconf.py
pelican --listen
```

Setelah itu coba buka website kamu dan cek apakah kolom komentar sudah muncul di halaman paling bawah

<p align="center">
  <img src="https://i.imgur.com/BO0jnru.png" alt="https://i.imgur.com/BO0jnru.png">
</p>


## Selanjutnya
Pada artikel ini kamu telah berhasil menambahkan kolom komentar menggunakan Disqus. Tutorial selanjutnya adalah bagaimana cara [Melihat trafik menggunakan Google Analytics]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-6.md)

## Series
Artikel ini adalah bagian dari seri tutorial bagaimana membuat blog menggunakan pelican dan Python

[Membuat Blog Menggunakan Pelican dan Python Bagian 1 - Instalasi dan Tema Pelican]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-1.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 2 - Membuat Konten]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-2.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 3 - Mengunggah di Github Pages]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-3.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Custom domain menggunakan Github Pages dan Niagahoster]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-4)
[Membuat Blog Menggunakan Pelican dan Python Bagian 5 - Menambahkan kolom komentar menggunakan Disqus]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-5.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 6 - Melihat trafik menggunakan Google Analytics]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-6.md)
Title: Membuat Blog Menggunakan Pelican dan Python Bagian 1 - Instalasi dan Tema
Date: 2020-5-17 16:10
Modified: 2020-5-17 16:10
Category: python
Tags: python, pelican 
Slug: membuat-blog-menggunakan-pelican-dan-python-1
Authors: tegardp
Summary: Panduan membuat blog statis menggunakan Pelican

Membuat web statis sendiri memiliki keunggulan dibandingkan tradisional web yang menggunakan database untuk menyimpan konten.

* Web statis lebih cepat dibandingkan tradisional web

* Hosting lebih murah karena tidak menggunakan database. Bahkan gratis apabila anda menggunakan github

Tutorial ini akan memandu kamu untuk membuat blog mu sendiri. Mulai dari menginstall Pelican hingga menunggahnya di Github (gratis)

## Prasyarat
* Memiliki pengetahuan python dasar
* Memiliki pengetahuan mengenai HTML & CSS

## Goal
 - Instalasi pelican
 - Generate static website
 - Menginstall Tema: Elegant

## Install Python
Lakukan instalasi python terlebih dahulu. Kamu bisa mengunduhnya [di sini](https://www.python.org/downloads/).

## Manajemen Folder

Selanjutnya buat folder bernama `blog`. Kemudian buat dua folder di dalamnya bernama `output` dan `source`.

```
blog
  └── output
  └── source
```

## Install Virtualenv
Virtualenv adalah tool yang digunakan untuk membuat suatu Python Environment yang terisolasi. Keuntungannya adalah komponen yang anda tambahkan atau hapus di environment ini tidak akan mempengaruhi environment lain. Begitupula apabila anda menghapus komponen yang sama di environment lain. Maka environment ini akan tetap aman terjaga.

Instalasi virtualenv menggunakan perintah di bawah ini
```
pip install virtualenv
```

Selanjutnya kita akan membuat environment di dalam folder blog.
```
cd blog
venv env
```

maka kontent folder blog akan menjadi seperti ini
```
blog
  └── env
  └── output
  └── source
```

Untuk mengaktifkan virtual environment pada platform macOS dan Linux gunakan:
```
source env/bin/activate
```

Pada Windows
```
.\env\Scripts\activate
```

Setelah selesai digunakan kamu bisa mematikan virtual environment menggunakan perintah:
```
deactivate
```
## Install Pelican
Pastikan virtual environment dalam kondisi aktif. Kemudian install komponen yang dibutuhkan

```
pip install pelican
pip install markdown
```

Setelah menginstall komponen anda perlu menginstall pelican ke dalam folder `source`.
```
cd source
pelican-quickstart
```

Pelican akan memunculkan pertanyaan instalasi website
```
Where do you want to create your new web site? [.] .
What will be the title of this web site? Tegar Dani's Blog
Who will be the author of this web site? Tegardp
What will be the default language of this web site? [English] en
Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
Do you want to enable article pagination? (Y/n) n
What is your time zone? [Europe/Paris] Asia/Jayapura
Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) n
```
Jawaban kita bisa berbeda, silahkan dikondisikan sesuai kebutuhan kamu.

Default language: Silakan pilih 2 kode bahasa dari Panduan [ISO 639.1](https://www.loc.gov/standards/iso639-2/php/code_list.php)

Time zone: pilih zona waktu kalian dari daftar zona waktu di [Wikipedia](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

Setelah kamu menginstall pelican, maka struktur folder akan menjadi seperti ini
```
blog
  ├── output
  └── source
       ├── content (folder)
       ├── output (folder)
       ├── pelicanconf.py
       └── publishconf.py
```
berikut adalah penjelasan masing-masing file:

- content (folder): tempat menyimpan kontent website
- output (folder): lokasi default tempat menyimpan hasil generate static site
- pelicanconf.py: file pengaturan website
- publishconf.py: file pengaturan tambahan ketika website di publikasikan

Secara default pelican akan menghasilkan static site di folder `blog/source/output`. Kita harus menyetel agar pelican menghasilkan output static site di folder `blog/output/`.

Hapus folder `blog/source/output`. Kemudian buka file `pelicanconf.py` dan tambahkan baris kode ini.

```
OUTPUT_PATH = '../output'
```

Untuk generate static site jalankan perintah di bawah ini pada folder source
```
pelican content
```

Untuk menjalankan website jalankan perintah ini
```
pelican --listen
```

Anda dapat mengakses blog anda di http://127.0.0.1

<p align="center">
  <img src="https://i.imgur.com/3CxmyHm.png" alt="https://i.imgur.com/3CxmyHm.png">
</p>

## Install Tema Pelican: Elegant
Agar web kamu terlihat lebih menarik kamu bisa menginstall beberapa tema yang telah di sediakan. Kamu bisa mengunduhnya di [tema pelican](https://github.com/getpelican/pelican-themes).
Pada tutorial kali ini saya akan menggunakan tema `elegant` yang dapat diunduh [di sini](https://github.com/Pelican-Elegant/elegant).

Instalasi tema dimulai dari membuat folder `theme` terlebih dahulu di dalam folder source. setelah itu kamu dapat mengekstrak tema elegant ke suatu folder di dalam folder `theme`
```
blog
  └── source
       ├── content
       └── theme (new)
            └── elegant (new)
```

Setelah itu setel pelican agar dapat membaca tema custom. Buka file `pelicanconf.py` dan tambahkan baris kode berikut

```
THEME = 'theme/elegant'
```

Setiap melakukan perubahan pada website. Jangan lupa jalankan perintah di bawah ini untuk melakukan generate static site
```
pelican content
```

lalu jalankan website
```
pelican --listen
```

Anda dapat mengakses tampilan terbaru blog anda di http://127.0.0.1

<p align="center">
  <img src="https://i.imgur.com/Zko0iM4.png" alt="https://i.imgur.com/Zko0iM4.png">
</p>

## Selanjutnya
Pada artikel ini kita belajar bagaimana cara menginstall pelican dan generate static site serta menambahkan tema elegant. Tutorial selanjutnya adalah bagaimana cara [membuat konten]()

## Series
Artikel ini adalah bagian dari seri tutorial bagaimana membuat blog menggunakan pelican dan Python

[Membuat Blog Menggunakan Pelican dan Python Bagian 1 - Instalasi dan Tema]()
[Membuat Blog Menggunakan Pelican dan Python Bagian 2 - Membuat Konten]()
[Membuat Blog Menggunakan Pelican dan Python Bagian 3 - Luncurkan di Github Pages]()
[Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Custom domain menggunakan Github Pages dan Google Domain]()
[Membuat Blog Menggunakan Pelican dan Python Bagian 5 - Menambahkan kolom komentar]()
[Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Melihat trafik menggunakan Google Analytics]()
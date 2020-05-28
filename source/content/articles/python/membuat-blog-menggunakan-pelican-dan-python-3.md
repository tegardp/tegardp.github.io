Title: Membuat Blog Menggunakan Pelican dan Python Bagian 3 - Mengunggah di Github Pages
Date: 2020-5-26 03:35
Modified: 2020-5-26 03:35
Category: python
Tags: python, pelican 
Slug: membuat-blog-menggunakan-pelican-dan-python-3
Authors: tegardp
Summary: Panduan membuat blog statis menggunakan Pelican

Setelah kamu berhasil membuat web statis. Kamu pasti ingin meluncurkannya supaya dapat dibaca oleh semua orang.

Cara yang paling mudah adalah meluncurkannya di github pages.

## Prasyarat
* Pengetahuan dasar mengenai git dan github
* Git sudah terinstall

## Goal
- Membuat repository github untuk menyimpan kode dan menjalankan website

## Mengunggah website ke Github Pages

Ketika membangun web statis, alangkah baiknya memisahkan antara folder *source code* dengan folder *website*. 
```
blog
  └── output
  └── source
```

Kita akan menyimpan kedua folder tersebut ke dalam satu *repository* github. Dari satu repo tersebut akan dibuat dua cabang. cabang *master* untuk menyimpan folder *website* dan cabang *dev* untuk menyimpan folder *source code*.
```
(github repo: tegardp.github.io)
blog
  └── output (branch: master)
  └── source (branch: dev)
```

Langkah pertama adalah login ke Github dan buatlah repository baru bernama *username.github.io*.

<p align="center">
  <img src="https://i.imgur.com/wyO0UD2.png" alt="https://i.imgur.com/wyO0UD2.png">
</p>

Buka command prompt / Terminal. Kemudian *generate* untuk perbarui *website* menggunakan perintah

```
pelican content -s publishconf.py
```

Sekarang gunakan perintah git di folder `blog`.
```
git init
git add remote add origin https://github.com/tegardp/tegardp.github.io.git
git checkout -b dev
git add .
git commit -m "First commit*
git push -u origin dev
ghp-import output -r origin -b master
git push origin master
```

Setelah itu anda tunggu sebentar sekitar 30 menit. Anda dapat mengakses website anda di `username.github.io`

## Selanjutnya
Pada artikel ini kamu telah berhasil mengunggah website kamu di github pages dan juga membuat custom domain. 

Tutorial selanjutnya adalah bagaimana cara [Custom domain menggunakan Github Pages dan Niagahoster]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-4)

## Series
Artikel ini adalah bagian dari seri tutorial bagaimana membuat blog menggunakan pelican dan Python

[Membuat Blog Menggunakan Pelican dan Python Bagian 1 - Instalasi dan Tema Pelican]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-1.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 2 - Membuat Konten]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-2.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 3 - Mengunggah di Github Pages]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-3.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Custom domain menggunakan Github Pages dan Niagahoster]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-4)
[Membuat Blog Menggunakan Pelican dan Python Bagian 5 - Menambahkan kolom komentar menggunakan Disqus]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-5.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 6 - Melihat trafik menggunakan Google Analytics]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-6.md)
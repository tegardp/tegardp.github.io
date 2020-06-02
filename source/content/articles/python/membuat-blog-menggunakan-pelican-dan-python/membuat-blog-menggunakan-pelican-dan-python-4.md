Title: Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Custom domain menggunakan Github Pages dan Niagahoster
Date: 2020-5-28 21:40
Modified: 2020-5-28 21:40
Category: python
Tags: python, pelican 
Slug: membuat-blog-menggunakan-pelican-dan-python-4
Authors: tegardp
Summary: Panduan membuat blog statis menggunakan Pelican

## Prasyarat
* Sudah melakukan langkah-langkah yang terdapat di [Tutorial sebelumnya](https://tegardani.com/articles/2020/05/26/membuat-blog-menggunakan-pelican-dan-python-3/)
* Menyewa domain di Niagahoster

## Goal
- Agar *website* anda bisa di akses di *yourdomain.com* 

## Sewa Domain
Aku sih tidak mengharuskan menyewa domain di niagahoster. Domain bisa disewa dimanapun seperti Google domain, hostgator dan lainnya. Tapi, di tutorial kali ini aku mau berbagi tutorial menyewa domain di niaga hoster dan mengonfigurasinya dengan Github Pages

## Menyewa domain di Niagahoster
Silahkan kunjungi https://www.niagahoster.co.id/domain-murah untuk mengecek ketersediaan domain.

<p align="center">
  <img src="https://i.imgur.com/H6bOJEg.png" alt="https://i.imgur.com/H6bOJEg.png">
</p>

Selanjutnya kamu tinggal mengikuti langkah seperti di gambar
<p align="center">
  <img src="https://i.imgur.com/YsCDx0h.png" alt="https://i.imgur.com/YsCDx0h.png">
</p>

Disini aku menggunakan paket personal karena harganya lagi diskon banget. hehe
<p align="center">
  <img src="https://i.imgur.com/d03VixQ.png" alt="https://i.imgur.com/d03VixQ.png">
</p>
<p align="center">
  <img src="https://i.imgur.com/Ma8QSp7.png" alt="https://i.imgur.com/Ma8QSp7.png">
</p>

Setelah kamu berhasil menyewa domain langkah selanjutnya adalah mendaftarkan ip address github ke domain kamu dengan menambahkan custom record. Caranya adalah pada sidebar di samping pilih **Layanan Anda > Domain**. Kemudian, pilih domain yang tadi disewa dan pilih **kelola domain**. Lalu pilih tab **DNS Management**. Kemudian pilih **Add new Record**

- A Record = 185.199.108.153
- A Record = 185.199.109.153
- A Record = 185.199.110.153
- A Record = 185.199.111.153
- CNAME = yourusername.github.io

<p align="center">
  <img src="https://i.imgur.com/4b9XHKW.png" alt="https://i.imgur.com/4b9XHKW.png">
</p>
<p align="center">
  <img src="https://i.imgur.com/WTcFzGQ.png" alt="https://i.imgur.com/WTcFzGQ.png">
</p>


## Konfigurasi custom domain di github

Masuk ke repository github `yourusername.github.io` kemudian pilih **Settings**.
<p align="center">
  <img src="https://i.imgur.com/SbIVUxJ.png" alt="https://i.imgur.com/SbIVUxJ.png">
</p>

Kemudian scroll ke bawah sampai menemukan Kolom Github Pages. Pada isian **Custom Domain** silahkan isi domain yang telah dibeli tadi dan klik save
<p align="center">
  <img src="https://i.imgur.com/Pjkk8rd.png" alt="https://i.imgur.com/Pjkk8rd.png">
</p>

Tunggu proses peralihan DNS agar domain aktif bisa diakses kira-kira maksimal 1x24 jam.

## Selanjutnya
Pada artikel ini kamu telah berhasil membuat custom domain menggunakan Github Pages dan niagahoster. Tutorial selanjutnya adalah bagaimana cara [Menambahkan kolom komentar menggunakan Disqus](https://tegardani.com/articles/2020/05/29/membuat-blog-menggunakan-pelican-dan-python-5/)

## Series
Artikel ini adalah bagian dari seri tutorial bagaimana membuat blog menggunakan pelican dan Python

[Membuat Blog Menggunakan Pelican dan Python Bagian 1 - Instalasi dan Tema Pelican](https://tegardani.com/articles/2020/05/17/membuat-blog-menggunakan-pelican-dan-python-1/)
[Membuat Blog Menggunakan Pelican dan Python Bagian 2 - Membuat Konten](https://tegardani.com/articles/2020/05/18/membuat-blog-menggunakan-pelican-dan-python-2/)
[Membuat Blog Menggunakan Pelican dan Python Bagian 3 - Mengunggah di Github Pages](https://tegardani.com/articles/2020/05/26/membuat-blog-menggunakan-pelican-dan-python-3/)
[Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Custom domain menggunakan Github Pages dan Niagahoster](https://tegardani.com/articles/2020/05/28/membuat-blog-menggunakan-pelican-dan-python-4/)
[Membuat Blog Menggunakan Pelican dan Python Bagian 5 - Menambahkan kolom komentar menggunakan Disqus](https://tegardani.com/articles/2020/05/29/membuat-blog-menggunakan-pelican-dan-python-5/)
[Membuat Blog Menggunakan Pelican dan Python Bagian 6 - Melihat trafik menggunakan Google Analytics](https://tegardani.com/articles/2020/05/30/membuat-blog-menggunakan-pelican-dan-python-6/)
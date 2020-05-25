Title: Membuat Blog Menggunakan Pelican dan Python Bagian 2 - Membuat konten
Date: 2020-5-18 06:10
Modified: 2020-5-22 20:04
Category: python
Tags: python, pelican 
Slug: membuat-blog-menggunakan-pelican-dan-python-2
Authors: tegardp
Summary: Panduan membuat blog statis menggunakan Pelican

## Prasyarat
* Telah melakukan instalasi dan konfigurasi pelican seperti pada [Instalasi dan Tema Pelican]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-1.md)

## Goal
- Membuat artikel dan halaman dengan Markdown

## Workflow
- Konten ditulis menggunakan markdown, di dalam folder `content`
- Buat file metadata
- generate ulang website


## Langkah-langkah membuat konten

Buatlah file bernama `first_post.md` di dalam folder `content`.

```
blog
  └── source
       ├── content
       |     └── first_post.md (new)
       └── theme
```

Buat metadata di dalam file tersebut. Metadata merupakan informasi dasar terkait konten yang akan dimuat. Letak metadata ada di paling atas dokumen. Setelah itu, konten di tulis di paragraf selanjutnya. Langkah pertama adalah buka file `first_post.md`, kemudian tambahkan baris di bawah

```
Title: My First Blog Post
Author: tegardp
Date: 2020-01-01 9:00
Category: blogging
Tags: python, markdown, pelican
Slug: my-first-blog-post

Blog post content goes here
```

Informasi terkait metadata

| Keyword | Required? | Usage |
| ------- | --------- | ----- |
|Title | Yes | Judul post|
|Author | Yes | Penulis post|
|Date | Yes | Tanggal publikasi dalam format YYYY-mm-dd hh:mm|
|Modified | No | Terakhir disunting dalam format YYYY-mm-dd hh:mm|
|Category | Yes | Topic post secara umum|
|Tags | No | Nerbagai jenis topik yang tercangkup dalam post, dipisah menggunakan koma|
|Summary | No | Sinopsis post|
|Slug | No | Nama file .html yang akan digenerate oleh pelican dipisah dengan simbol "-" |
|Status | No | Pilih salah satu published, draft or hidden|

generate ulang website menggunakan perintah
```
pelican content
pelican --listen
```

kemudian silahkan akses di `http://127.0.0.1:8000/`

<p align="center">
  <img src="https://i.imgur.com/O6l3U2c.png" alt="https://i.imgur.com/O6l3U2c.png">
</p>

tadaaaaaa!! mudah bukan?

## Merapikan folder content
Semakin sering kamu membuat konten. File-file yang terdapat pada folder konten akan makin tidak beraturan. Agar folder konten kamu lebih rapi, dan lebih terorganisir. Maka, alangkah baiknya jika kita buat struktur dalam folder `content`.

```
blog
└── source
     └── content
          └── articles (new)
          |   └── first_post.md
          |   └── second_post.md
          |   └── etc.md
          └── img (new)
          |   └── python_icon.png
          └── pages (new)
          |   └── about_me.md
          └── pdf (new)
              └── pelican.pdf
```

Agar pelican dapat menemukan konten artikel, gambar, halaman dan pdf. Maka kamu harus memberitahunya terlabih dahulu dengan cara menambahkan baris kode di bawah ini ke dalam file `pelicanconf.py`

```
 ARTICLE_PATHS = ['articles']
 STATIC_PATHS = ['img', 'pdf']
 PAGE_PATHS = ['pages']
```

Setelah itu, generate ulang website dengan menggunakan perintah

```
pelican content
pelican --listen
```

## Mendefinisikan struktur URL
Secara default, struktur url pada artikel adalah sebagai berikut

```
http://127.0.0.1:8000/my-first-post.html
```

Agar lebih informatif, kita perlu mendefinisikan tanggal publikasi pada post tersebut. Tambahkan baris kode di bawah ini ke dalam file `pelicanconf.py`

```
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
```

Seperti biasa, generate ulang website dengan menggunakan perintah

```
pelican content
pelican --listen
```

Sekarang url artikel akan berubah menjadi seperti di bawah

```
http://127.0.0.1:8000/articles/2020/01/01/my-first-post/
```

lakukan hal yang sama pada pages, categories, dan tags. Tambahkan kode di bawah ini ke dalam file `pelicanconf.py`

```
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
```

generate ulang website dengan menggunakan perintah

```
pelican content
pelican --listen
```


## Selanjutnya
Pada artikel ini kita belajar bagaimana cara membuat konten dengan menggunakan markdown. Tutorial selanjutnya adalah bagaimana cara [Meluncurkan di Github Pages]()

## Series
Artikel ini adalah bagian dari seri tutorial bagaimana membuat blog menggunakan pelican dan Python

[Membuat Blog Menggunakan Pelican dan Python Bagian 1 - Instalasi dan Tema Pelican]({filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-1.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 2 - Membuat Konten](filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-2.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 3 - Mengunggah di Github Pages](filename}/articles/python/membuat-blog-menggunakan-pelican-dan-python-3.md)
[Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Custom domain menggunakan Github Pages dan Niagahoster]()
[Membuat Blog Menggunakan Pelican dan Python Bagian 5 - Menambahkan kolom komentar menggunakan Disqus]()
[Membuat Blog Menggunakan Pelican dan Python Bagian 4 - Melihat trafik menggunakan Google Analytics]()
Title: 5 Metrics Klasifikasi Data
Date: 2019-12-30 12:04
Modified: 2019-12-30 12:04
Category: machine-learning
Tags: python, machine-learning, classification, metrics
Slug: 5-metrics--klasifikasi-data
Authors: tegardp
Summary: Pada kali ini saya ingin menulis tentang metrics yang biasa digunakan oleh Data Scientist untuk mengukur keakuratan dari model klasifikasi.

<p align="center">
  <img src="https://www.mememaker.net/api/bucket?path=static/img/memes/full/2019/Feb/14/9/more-metrics-you-say-16456.png" alt="https://www.mememaker.net/meme/more-metrics-you-say-16456">
</p>

Pada kali ini saya ingin menulis tentang metrics yang biasa digunakan oleh Data Scientist untuk mengukur keakuratan dari model klasifikasi. 

Kalau ada yang mengatakan bahwa "Indonesia adalah negara terhebat se-Asia Tenggara". Maka pertanyaan pertama yang muncul biasanya adalah: apa sih tolak ukurnya? apakah dari segi ekonomi? fasilitas kesehatan? atau yang lainnya?

Machine learning (ML) pun demikian. Pada dasarnya ML adalah menemukan solusi dengan cara yang berbeda dan dataset yang berbeda. Maka dari itu penting untuk mengetahui tujuan awal sebelum memilih metrics.

## **A. Accuracy, Precision, Recall**

<p align="center">
  <img src="https://blog.aimultiple.com/wp-content/uploads/2019/07/positive-negative-true-false-matrix.png" alt="https://blog.aimultiple.com/wp-content/uploads/2019/07/positive-negative-true-false-matrix.png">
</p>

1. ***Accuracy***

    metrics paling umum yang biasa digunakan untuk mengukur sebuah model. Bisa digunakan untuk klasifikasi biner class maupun multi-class.
    
    Accuracy = (TP+TN) / (TP+TN+FP+FN)
    
    ***Accuracy*** adalah proporsi dari prediksi yang benar dibandingkan dengan total prediksi.
    
    **Kapan digunakan?**
  
    *Accuracy* **cocok** untuk menilai data yang memiliki **class yang seimbang**. Namun tidak berarti apabila classnya tidak seimbang.

    **Notes:**

    Apabila kita ingin meneliti kasus yang **sangat jarang**. Seperti, kita ingin memprediksi bahwa berapa jumlah penumpang pesawat yang merupakan **teroris**. Model bisa saja memberi label "Tidak ada" untuk semua test. Setelah di test hasilnya adalah akurasi dari prediksi mencapai 99%. Model tersebut akurat namun tidak valuable.

2. ***Precision***

    Singkatnya, presisi adalah seberapa besar **proporsi prediksi positif** yang **benar**

    *Precision* = TP / (TP+FP)

    Pada penelitian prediksi teroris sebelumnya apabila model tidak dapat memprediksi True Positive. Maka, nilai *precision* juga 0.

    **Kapan digunakan?**

    *Precision* digunakan untuk meyakinkan peneliti dari hasil prediksi yang didapatkan.

3. ***Recall***
  
    Singkatnya, *recall* adalah seberapa besar presentase model **mendapatkan prediksi positif** dari **total positif seharusnya**

    *Recall* = TP / (TP+FN)

    Pada penelitian prediksi teroris sebelumnya apabila model tidak dapat memprediksi True Positive. Maka, nilai recall juga 0.

    **Kapan digunakan?**

    *Precision* digunakan untuk melihat seberapa besar kemampuan model untuk menemukan TP.

    **Notes:**

    Apabila **semua** penumpang kita beri **label teroris**, maka nilai **recall adalah 1.0**. namun nilai **precision adalah 0**. Hal ini biasa disebut **tradeoff of precision vs recall**. make perlu menggunakan nilai F1-Score untuk mendapatkan keseimbangan antara keduanya.

## **B. F1 Score**

  F1-Score adalah metrics yang digunakan jika ingin melihat **keseimbangan** antara ***precise*** dan ***recall***. Dapat digunakan di klasifikasi biner maupun multi-class

  F1-Score = 2 x (Precision x Recall) / (Precision + Recall)


## **C. Log Loss/Binary Crossentropy**

  <p align="center">
    <img src="https://miro.medium.com/max/556/0*8oDE1l2eWLw81clR.png">
  </p>

  ***Log loss*** sangat cocok digunakan untuk **mengukur klasifikasi biner**. 

  Log loss = -(y log(p) + (1-y) log(1-p))
  
  **Kapan digunakan?**

  Ketika output dari **klasifikasi adalah peluang**. Semakin kecil log loss maka akurasinya semakin tinggi

  **Notes:**

  Rentan terhadap kelas yang tidak seimbang.

## **D. Categorical Crossentropy**

  ***Categorical Crossentropy*** digunakan untuk mengukur multi-class.

  <p align="center">
    <img src="https://miro.medium.com/max/344/0*zneWdU4GN_WBzTIF.gif">
  </p>

  y_ij bernilai 1 apabila sample i tergolong kelas j, dan 0 untuk yang lain
  p_ij peluang dari model dalam memprediksi sample i tergolong kelas j.

  **Kapan digunakan?**

  Ketika output dari **klasifikasi adalah peluang multi-class**. Biasa digunakan pada *Neural Nets*. Semakin kecil nilai *categorical loss* semakin tinggi akurasi.

  **Notes:**

  Rentan terhadap kelas yang tidak seimbang.

## **E. AUC (*Area Under the ROC Curve.*)**

  <p align="center">
    <img src="https://miro.medium.com/max/875/0*Dkq9YLJM5t8k0Fcb">
  </p>

  Sensitivty = TPR(True Positive Rate)= Recall = TP/(TP+FP)
  
  Specificity = FPR(False Positive Rate)= FP/(TN+FP)


  **AUC** mengukur **seberapa baik peluang mengidentifikasikan TP dari seluruh nilai Positif**

  Nilai **treshold** dari AUC **tergantung dari tujuan penelitian**. Jika ingin mengidentifikasikan kanker nilai treshold 0,5 sudah dianggap terlalu tinggi. Misalnya seorang pasien hanya memiliki peluang sebesar 0,3 terkena kanker, sebaiknya orang tersebut diklasifikasikan sebagai positif kanker.

  **Kapan digunakan?**

  AUC menilai **ranking dari nilai prediksi**. Cocok apabila seseorang ingin mendapatkan **daftar user** yang akan merespon sebuah kejadian bisa dilihat dari nilai AUC dari terbesar hingga terendah.

## Kesimpulan

  Seperti yang telah dijelaskan di awal, bahwa metrics yang digunakan tergantung dari **tujuan penelitian**. Pemilihan metric yang **salah** bisa menyebabkan hasil yang **fatal**
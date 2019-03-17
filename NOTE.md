# Noted

* Permasalahan
	* [Check data](#check-data)
	* [Pemecahan kalimat menjadi perkata](#pemecahan-kalimat-menjadi-perkata)


# Quote
> mulailah dengan yang paling sederhana (*tidak efisien*) baru dikembangkan lagi menjadi lebih sederhana lagi (*lebih efisien*)
# Check Data
	clear
# Pemecahan kalimat menjadi perkata
	solved
# embedding kata, angka dan symbol
Dimodel yang kita buat, terkadang dalam satu kalimat jawaban mengandung kata berupa gabungan `huruf`, `angka`, ataupuun `simbol`. word2vec yang digunakan biasanya menggunakan hanya `huruf` saja mengacuhkan `angka` atau `simbol` 

##solusi 
```
Lets consider both ways of representing numbers:

1. Treating it as string and considering it as another word and assign an ID to it when forming a dictionary. Or
2. Converting the numbers to actual words : '1' becomes 'one', '2' as 'two' and so on.
```

analisis 
okelah kalau kita menggunakan cara ke dua untuk melakukan embedding. bisa menggunakan [num2words](https://github.com/savoirfairelinux/num2words) tetapi masalahnya adalah tanda baca, pertanyaannya adalah tanda baca apakah diperlukan untuk dilakukan embedding? 

**contoh kasus**
dalam kasus operator matematik `240/ 120 x 60 = 120` simbol `/` dan `=`

**rencana pemecahan masalah**
dimulai dari pemecahan angka menjadi kata, dan untuk simbol sementara diacuhkan dahulu.


[How to treat numbers inside text strings when vectorizing words?](https://stackoverflow.com/questions/44865840/how-to-treat-numbers-inside-text-strings-when-vectorizing-words)

# stemming 
sementara belum mengetahui apa plus minus dari `stemming`
[Sastrawi, Natural Language Processing Mudah Dengan Python](https://belajarpython.com/2018/05/sastrawi-natural-language-processing-bahasa-indonesia.html)

# Referency
[An Introduction to Bag-of-Words in NLP](https://medium.com/greyatom/an-introduction-to-bag-of-words-in-nlp-ac967d43b428)
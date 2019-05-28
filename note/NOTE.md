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

## solusi 
```
Lets consider both ways of representing numbers:

1. Treating it as string and considering it as another word and assign an ID to it when forming a dictionary. Or
2. Converting the numbers to actual words : '1' becomes 'one', '2' as 'two' and so on.
```
[How to treat numbers inside text strings when vectorizing words?](https://stackoverflow.com/questions/44865840/how-to-treat-numbers-inside-text-strings-when-vectorizing-words)

analisis 
okelah kalau kita menggunakan cara ke dua untuk melakukan embedding. bisa menggunakan [num2words](https://github.com/savoirfairelinux/num2words) tetapi masalahnya adalah tanda baca, pertanyaannya adalah tanda baca apakah diperlukan untuk dilakukan embedding? 

**contoh kasus**
dalam kasus operator matematik `240/ 120 x 60 = 120` simbol `/` dan `=`

**rencana pemecahan masalah**
dimulai dari pemecahan angka menjadi kata, dan untuk simbol sementara diacuhkan dahulu.


# stemming 
sementara belum mengetahui apa plus minus dari `stemming`
[Sastrawi, Natural Language Processing Mudah Dengan Python](https://belajarpython.com/2018/05/sastrawi-natural-language-processing-bahasa-indonesia.html)

# Embedding
cari data yang kecil dulu saja, perbaiki pengektrackan datanya, 
	```
	mau mendapatkan data angka dan symbol juga, masukkan daam to word list saja.
	```

Yan diubah adalah parameter `PAT_ALPHABETIC = re.compile(r'(((?![\d])\w)+)', re.UNICODE)` dalam file *utils* package gensim. 

**Pertanyaannya** 
	bagaimana cara menimpa variable dalam thirt vendor. `?`


# Referency
[An Introduction to Bag-of-Words in NLP](https://medium.com/greyatom/an-introduction-to-bag-of-words-in-nlp-ac967d43b428)

```
(soal)y\x(nilai)
	1	2	3	4	5
1	0	1	8	5	121
2	0	49	7	1	78
3	0	7	3	1	124
4	0	1	2	13	119
5	0	80	9	2	44
```

```
(soal)y\x(persentase)
	1	2	3	4	5	100%
1	0 	1 	6 	4 	90 	100%
2	0 	36 	5 	1 	58 	100% 
3	0 	5 	2 	1 	92 	100%
4	0 	1 	1 	10 	88 	100%
5	0 	59 	7 	1 	33 	100%

```

Seven of them are character based –Longest Common SubString, Damerau, Jaro, Jaro Winkler, Needleman Wunch, Simth Waterman and N-gram - while the other are term-based distance measures – Block Distance, Cosine Similarity, Dice’s Coefficient, Eclidean Distance, Jaccard Similarity, Levenshtein distance, Holistic Model, Sim Metrics

kemungkinan masalah ada di waktu pemberian nilai yang meetapkan kekurangan nilai degan menggunakan nilai 0 pada akhir rencana solusi berada pada perubahann peletaan penambahan nilai ke depan
# Noted

* Permasalahan
	* [Check data](#check-data)
	* [Pemecahan kalimat menjadi perkata](#pemecahan-kalimat-menjadi-perkata)


# Check Data
	clear
# Pemecahan kalimat menjadi perkata
	solved
# embedding kata, angka dan symbol
Dimodel yang kita buat, terkadang dalam satu kalimat jawaban mengandung kata berupa gabungan `huruf`, `angka`, ataupuun `simbol`. word2vec yang digunakan biasanya menggunakan hanya `huruf` saja mengacuhkan `angka` atau `simbol` 

solusi 
```
Lets consider both ways of representing numbers:

Treating it as string and considering it as another word and assign an ID to it when forming a dictionary. Or
Converting the numbers to actual words : '1' becomes 'one', '2' as 'two' and so on.
```
[How to treat numbers inside text strings when vectorizing words?](https://stackoverflow.com/questions/44865840/how-to-treat-numbers-inside-text-strings-when-vectorizing-words)

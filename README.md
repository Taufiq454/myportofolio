Nama : Muhammad Taufiq Ramadhan 

NPM : 2506536143

Kelas : PBP B

### Tugas 1

1. Saya hanya memakai <section>, namun karena saya melakukan navigasi bukan di satu html yang sama jadi penggunannya sectionnya mungkin kurang maksimal. Namun section sendiri sangat membantu untuk memper rapi web misalnya saya dapat dengan mudah mengatur batas kiri dan kanan (max-width) pada section tertentu.

2. Tantangan yang saya temukan adalah salah satu tombol navigasi yang hilang pada mobile, pada akhirnya saya menggunakan warp agar saat mengecil tombol navigasi akan kebawah. Namun ada masalah lain layout navigasinya jadi jelek, jadi saya mengatur gapnya lagi. 

3. Saya tidak menemukan masalah/batasan dari static web ini, mungkin karena memang web portofolio yang saya buat ini masih dasar dan memang tidak terlalu terganggu dengan batasan web static

### AI Disclosure Tugas 1

- Saya menggunakan copilot untuk menanyakan bagaimana membuat layout grid (kotak-kotak) untuk bagian skill dan interest

- Saya juga menggunakan copilot untuk menanyakan bagaimana membuat animasi pada poin sebelumnya


### Tugas 2

1. Alurnya saat pengguna membuka halaman, request akan masuk ke urls.py portofolio lalu diarahkan ke urls.py aplikasi main. Barulah dari sana dipanggil fungsi view yang mengambil data dari model , kemudian data dilanjutkan dikirim ke template untuk ditampilkan.
jadi peran masing-masing kurang lebih begini:
urls.py proyek= menerima request dan diteruskan ke urls.py aplikasi
urls.py aplikasi= request tadinya sudah dikirim dilanjutkan lagi ke fungsi view (contohnya show_experience)
view= mengambil data dari database lewat model
model= sebagai tempat mendefinisikan struktur data yang akan dibuat
template= sebagai wadah untuk menampilkan data

2. Karena menyimpan data di model membuat aplikasi lebih mudah dipelihara, konsisten, dan juga fleksibel. Jadi template hanya akan fokus ke pada tampilan, sedangkan model untuk mengatur data sehingga tidak perlu mengubah HTML yang mungkin dapat mengakibatkan kerusakan tampilan

3. makemigrations membuat file migrasi berdasarkan perubahan di models.py, sedangkan migrate mengeksekusi migrasi itu ke database jadi keduanya mempunyai fungsi yang berbeda dan saling membantu. Contoh yang memakai keduanya adalah menambahkan field di model misalnya menambahkan field nama di model Experience kita perlu menjalankan keduanya.


### AI Disclosure Tugas 2
Pada tugas ini saya hampir tidak menggunakan AI sama sekali karena tugasnya benar benar sama dengan tutorial 2, hanya perlu menambahkan 1 halaman lagi (yang kali ini saya tambahkan Education) jadi saya hanya perlu mengikuti ulang tutorial 2 jika lupa caranya. Saya hanya menggunakan AI untuk menjelaskan hal-hal yang dibahas pada pertanyaan reflektif

### Tugas 2 tambahan penjelasan
Saya juga tidak jadi menambahkan halaman project(menghapus), dan skill, dan memperbaiki tampilan untuk halaman yang tersisa.


### Tugas 3

1. Kitaa menggunakan ModelForm karena ModelForm dapat membuat form HTML berdasarkan model Django secara otomatis. Dengan begitu, kita tidak perlu menulis setiap input form secara manual dan validasi data juga dapat dilakukan berdasarkan aturan yang terdapat pada model. Hal ini membuat kode lebih singkat, konsisten, dan mudah dipelihara. Kita diwajibkan menggunakan CSRF adalah untuk mencegah penyerang aplikasi mengubah request yang awalnya ke server Django kita menjadi ke suatu API yang berbahaya dan mengirimkan data request kita ke mereka.

2. JSON lebih banyak digunakan dalam pengembangan web modern karena formatnya lebih sederhana, ringkas, dan mudah dibaca dibandingkan XML. Selain itu JSON juga lebih ringan dan hampir semua bahasa pemrograman modern punya dukunga bawaan untuk JSON

3. Saat fungsi view dipanggil dia akan mengambil data dari model, data tersebut masih berupa queryset dan belum berupa format JSON, maka dilakukanlah serialization data yang model tersebut diubah menjadi format JSON melalui proses serialization ini, barulah django mengirimkan hasil(response) dalam bentuk JsonResponse ke client.

### AI Disclosure Tugas 3
Saya menggunakan ChatGpt dan CoPilot untuk membantu mengetahui bagaimana implementasi method form experience pada bagian category dan DateTime juga bagaimana mengatur tampilan untuk category di menu add experience. Menggunakan AI untuk membantu membuat fungsi view untuk update dan menanyakan kesalahan pada educationForm


### AI Disclosure Tugas 4
Menyanyakan ke Copilot kenapa tombol edit tidak muncul setelah menambahkan editor(kurang context is_editor pada def show)


### Tugas 5

1. Debouncing adalah teknik untuk menunda sebuah fungsi hingga suatu jeda waktu berlalu tanpa event baru. Selama pengguna masih mengetik, timer sebelumnya dibatalkan dan dimulai lagi. Dengan demikian, browser hanya mengirim permintaan setelah pengguna berhenti mengetik selama sejenak. Teknik ini penting digunakan karena dapat mengurangi jumlah request ke server sehingga dapat mengurangi beban server, dan menghemat penggunaan jaringan.

2. Await adalah keyword yang hanya bisa digunakan di dalam async function dan berfungsi untuk “menunggu” Promise selesai diproses sebelum melanjutkan ke baris kode berikutnya. Tanpa await, sebuah Promise akan tetap berjalan di belakang layar dan kode berikutnya akan langsung dieksekusi tanpa menunggu hasilnya.

3. Cross-Site Scripting (XSS) adalah serangan ketika penyerang berhasil menyisipkan kode JavaScript miliknya ke dalam halaman web yang kemudian dijalankan di browser pengguna lain. Salah satu jenisnya adalah stored XSS, yaitu ketika kode berbahaya disimpan ke database (misalnya sebagai judul proyek) lalu ikut dijalankan setiap kali data tersebut ditampilkan. Template Django melakukan auto-escaping pada setiap { variabel }. Karakter seperti < dan > diubah menjadi &lt; dan &gt; sehingga browser menampilkannya sebagai teks biasa, bukan sebagai tag HTML. Saat kita pindah ke AJAX Tidak ada lagi Django yang melakukan escaping sehingga browser akan memperlakukan setiap tag HTML di dalam data sebagai kode sungguhan.


### AI Disclosure Tugas 5

Saya meminta bantuan AI, untuk mencek kesalahan pengetikan dan sebagainya, lalu juga minta bantuan AI dalam membuat implementasi javascript.

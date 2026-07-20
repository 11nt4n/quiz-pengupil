# To-Do List & Langkah Setup Laporan Tugas Praktikum

Berikut adalah panduan lengkap dari awal hingga akhir untuk menguji modul login dan register pada repository `quiz-pengupil`.

## Langkah 1: Persiapan Repositori Lokal
- [x] Lakukan clone repository dari Github (sudah saya lakukan di folder `C:\xampp\htdocs\Kuis PPL P15`).
- [ ] Pastikan XAMPP (Apache & MySQL) berjalan jika Anda ingin melihat/menguji kodenya secara manual di browser melalui `http://localhost/Kuis PPL P15/`.
- [ ] Jika Anda menggunakan XAMPP, buka phpMyAdmin, buat database dengan nama `quiz_pengupil`, kemudian import file `db/quiz_pengupil.sql` ke dalam database tersebut.

## Langkah 2: Pembuatan Test Case
- [x] Membuat dokumen berisi kemungkinan test case untuk modul Login dan Register.
- [ ] Silakan baca dan review test case yang telah saya buat di file [`tests/testcases.md`](tests/testcases.md).
- [ ] (Opsional) Anda bisa memindahkan tabel pada dokumen tersebut ke dalam format Word atau Excel untuk laporan tertulis Anda.

## Langkah 3: Pembuatan Script Selenium & Setup Stub/Driver
- [x] Membuat automation test dengan Selenium menggunakan Python (`tests/test_auth.py`). 
- [x] Menerapkan Stub/Driver bila diperlukan. Pada CI/CD pipeline, kita menggunakan manipulasi string (di `ci.yml`) untuk mengubah kredensial database `koneksi.php` secara otomatis sebagai "Stub" agar script dapat terhubung ke database pengujian (dummy database).
- [ ] Untuk menjalankan test ini di komputer lokal (Windows) Anda perlu Python terinstall:
  - Buka terminal/CMD di folder `C:\xampp\htdocs\Kuis PPL P15`.
  - Jalankan perintah: `pip install selenium`
  - Nyalakan PHP Server lokal di terminal: `php -S localhost:8000`
  - Pada tab terminal baru, jalankan test: `python tests/test_auth.py`

## Langkah 4: Penerapan CI/CD dengan Github Actions
- [x] Membuat workflow Github Actions di folder [`.github/workflows/ci.yml`](.github/workflows/ci.yml).
- [ ] Langkah untuk memicu CI/CD ini:
  1. Anda harus meng-upload seluruh folder `Kuis PPL P15` ini ke repository Github milik Anda sendiri (atau mem-fork repo asli).
  2. Gunakan perintah berikut di Git Bash / CMD:
     ```bash
     git add .
     git commit -m "Menambahkan test cases, script selenium, dan github actions"
     git push origin main
     ```
  3. Buka halaman repository Github Anda dan masuk ke tab **Actions**. Anda akan melihat pipeline sedang berjalan secara otomatis.
  4. Github Actions ini secara otomatis menyiapkan container Ubuntu, menginstall PHP dan MySQL, menjalankan server lokal, menginstall Selenium, dan menjalankan script automation testing.

## Ringkasan Hal yang Perlu Anda Lakukan Selanjutnya
1. **Memasukkan Test Case ke Laporan**: Buka `tests/testcases.md` dan salin isinya ke format laporan praktikum Anda.
2. **Memasukkan Source Code Selenium**: Copy-paste kode dari `tests/test_auth.py` sebagai lampiran atau isi laporan untuk bagian "Script Selenium".
3. **Mendokumentasikan CI/CD**: Push perubahan ini ke Github Anda dan ambil screenshot pipeline Github Actions ketika sudah *green/passed* untuk diletakkan di dalam laporan praktikum Anda.

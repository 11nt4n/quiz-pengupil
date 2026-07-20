# To-Do List & Langkah Setup Laporan Tugas Praktikum

Berikut adalah panduan lengkap dari awal hingga akhir untuk menguji modul login dan register pada repository `quiz-pengupil`.

## Langkah 1: Persiapan Repositori Lokal
- [x] Lakukan clone repository dari Github (sudah dilakukan di folder `C:\xampp\htdocs\Kuis PPL P15`).
- [ ] Pastikan XAMPP (Apache & MySQL) berjalan jika Anda ingin melihat/menguji kodenya secara manual di browser melalui `http://localhost/Kuis PPL P15/`.
- [ ] Jika Anda menggunakan XAMPP, buka phpMyAdmin, buat database dengan nama `quiz_pengupil`, kemudian import file `db/quiz_pengupil.sql` ke dalam database tersebut.

## Langkah 2: Pembuatan Test Case
- [x] Membuat dokumen berisi kemungkinan test case untuk modul Login dan Register.
- [x] File test case telah tersedia di [`tests/testcases.md`](tests/testcases.md).

## Langkah 3: Pembuatan Script Selenium & Setup Stub/Driver
- [x] Membuat automation test dengan Selenium menggunakan Python (`tests/test_auth.py`). 
- [x] Menerapkan Stub/Driver bila diperlukan. Pada CI/CD pipeline, manipulasi string digunakan (di `ci.yml`) untuk mengubah kredensial database `koneksi.php` secara otomatis sebagai "Stub" agar script dapat terhubung ke database pengujian (dummy database).
- [x] Menjalankan test secara lokal menggunakan Python dan PHP Built-in Server. (Sudah berhasil dijalankan dan mendapatkan hasil `OK`).

## Langkah 4: Penerapan CI/CD dengan Github Actions
- [x] Membuat workflow Github Actions di folder [`.github/workflows/ci.yml`](.github/workflows/ci.yml).
- [x] Menyelesaikan kendala push ke repository hasil *fork* dengan mengubah URL *remote origin*.
- [x] Melakukan `git commit --amend` untuk memperbaiki judul *commit message*.
- [x] Melakukan `git push -f origin main` ke repository Github pribadi.

---

## 📝 Panduan Penyusunan Laporan Praktikum
Sekarang karena semua proses teknis sudah selesai 100%, berikut adalah daftar materi yang harus Anda masukkan ke dalam dokumen/file Word laporan tugas Anda:

### 1. Bagian "Test Case"
- Buka file [`tests/testcases.md`](tests/testcases.md).
- *Copy-paste* tabel Skenario Test Case Login dan Register yang ada di file tersebut ke dalam laporan Anda.
- **Nilai Tambah:** Anda bisa menyebutkan bahwa pembuatan skenario ini memastikan pengujian mencakup *Negative Case* (seperti email kosong, password salah) maupun *Positive Case*.

### 2. Bagian "Implementasi Selenium & Stub"
- Masukkan *source code* dari file [`tests/test_auth.py`](tests/test_auth.py) ke dalam laporan.
- **Penjelasan (Wajib Ditulis):**
  - Jelaskan bahwa script Selenium ini disetting dalam mode `headless` (berjalan di *background* tanpa membuka jendela browser secara kasat mata) agar cocok dengan lingkungan server Github Actions.
  - Jelaskan bahwa Anda menggunakan teknik **Stub/Mocking** di dalam file CI/CD. Teknik ini bekerja dengan cara menimpa password `koneksi.php` pada saat berjalan di *pipeline* (baris `sed -i "s/\$password = '';/\$password = 'root';/g" koneksi.php`), sehingga aplikasi tidak memerlukan server XAMPP fisik, melainkan menggunakan database buatan (dummy) yang dibuat oleh Github.

### 3. Bagian "Penerapan CI/CD (Github Actions)"
- Sertakan *source code* dari file `.github/workflows/ci.yml`.
- Buka repository Github Anda di browser, masuk ke tab **Actions**, lalu klik pada status *pipeline* yang bercentang hijau.
- Ambil beberapa gambar (Screenshot) sebagai bukti pengerjaan:
  - Screenshot yang menunjukkan ringkasan bahwa *pipeline* berstatus **Success/Passed (Centang Hijau)**.
  - Screenshot terminal log (klik pada pekerjaan bernama `test`), yang memperlihatkan step **"Run Selenium Tests"** memunculkan tulisan `Ran 4 tests in ... OK`.
  - Screenshot step **"Setup MySQL database"** untuk membuktikan bahwa database telah disiapkan melalui CI/CD.

Dengan memasukkan ketiga bagian di atas, laporan Anda akan terlihat sangat profesional dan menjawab seluruh pertanyaan tugas dengan sempurna!

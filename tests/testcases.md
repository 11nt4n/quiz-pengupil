# Test Cases untuk Modul Authentication (Login & Register)

## 1. Modul Register (`register.php`)

| ID | Test Case | Skenario / Langkah | Expected Result (Hasil yang Diharapkan) | Status |
|---|---|---|---|---|
| TC_REG_01 | Register dengan data valid | 1. Buka halaman register<br>2. Isi Name, Username, Email, Password<br>3. Klik Register | Registrasi berhasil, data masuk ke database, dialihkan ke halaman login, muncul pesan sukses. | |
| TC_REG_02 | Register dengan username yang sudah ada | 1. Buka halaman register<br>2. Isi data dengan username yang sudah terdaftar<br>3. Klik Register | Muncul pesan error "Username sudah terdaftar". | |
| TC_REG_03 | Register dengan email yang sudah ada | 1. Buka halaman register<br>2. Isi data dengan email yang sudah terdaftar<br>3. Klik Register | Muncul pesan error "Email sudah terdaftar". | |
| TC_REG_04 | Register dengan field kosong | 1. Buka halaman register<br>2. Kosongkan semua field<br>3. Klik Register | Validasi form HTML5 akan mencegah submit atau muncul pesan error bahwa field harus diisi. | |

## 2. Modul Login (`login.php`)

| ID | Test Case | Skenario / Langkah | Expected Result (Hasil yang Diharapkan) | Status |
|---|---|---|---|---|
| TC_LOG_01 | Login dengan data valid | 1. Buka halaman login<br>2. Masukkan username dan password yang benar<br>3. Klik Login | Login berhasil, muncul pesan sukses. | |
| TC_LOG_02 | Login dengan password salah | 1. Buka halaman login<br>2. Masukkan username benar dan password salah<br>3. Klik Login | Muncul pesan error password salah. | |
| TC_LOG_03 | Login dengan username tidak terdaftar | 1. Buka halaman login<br>2. Masukkan username yang tidak ada di DB<br>3. Klik Login | Muncul pesan error username tidak ditemukan. | |
| TC_LOG_04 | Login dengan field kosong | 1. Buka halaman login<br>2. Kosongkan username dan password<br>3. Klik Login | Validasi form HTML5 akan mencegah submit. | |

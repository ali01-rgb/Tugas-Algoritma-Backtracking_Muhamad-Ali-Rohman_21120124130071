# Visualisasi Algoritma Backtracking: Sudoku Solver

[cite_start]Repositori ini berisi *source code* dan dokumentasi untuk pemenuhan Tugas Individu mata kuliah terkait implementasi algoritma Backtracking[cite: 168, 171]. Kasus yang dipilih untuk divisualisasikan adalah penyelesaian permainan Sudoku.

**Informasi Mahasiswa:**
* **Nama:** Muhamad Ali Rohman
* **NIM:** 21120124130071
* **Kelas/Mata Kuliah:** A/Algoritma & Pemrograman

---

## 1. Deskripsi Program
[cite_start]Program ini merupakan implementasi dari algoritma Backtracking yang dibuat menggunakan bahasa pemrograman Python[cite: 171]. [cite_start]Algoritma Backtracking adalah teknik untuk mencari solusi dari suatu permasalahan secara incremental (satu per satu) dan meng-eliminasi solusi yang tidak sesuai dengan kondisi batasan (constraint) yang ditentukan[cite: 7]. 

Visualisasi dibuat menggunakan GUI (Graphical User Interface) berbasis pustaka bawaan Python, yaitu `tkinter`. Program akan mendemonstrasikan bagaimana algoritma secara rekursif mencoba angka yang valid, dan melakukan proses *backtrack* (mundur dan menghapus angka) ketika menemui jalan buntu.

### Batasan (Constraint) Sudoku:
Program secara ketat mematuhi aturan Sudoku berikut:
* [cite_start]Kotak (cell) diisi dengan angka 1-9[cite: 53].
* [cite_start]Satu baris tidak boleh memiliki angka yang sama[cite: 57].
* [cite_start]Satu kolom tidak boleh memiliki angka yang sama[cite: 58].
* [cite_start]Satu kuadran berukuran 3x3 tidak boleh memiliki angka yang sama[cite: 56].

---

## 2. Cara Menjalankan Program
Pastikan Python sudah terinstal di sistem Anda. Pustaka `tkinter` umumnya sudah terinstal secara *default* bersama Python.

1. *Clone* repositori ini atau *download* file `sudoku_gui.py`.
2. Buka terminal atau *command prompt* di direktori penyimpanan file.
3. Jalankan perintah berikut:
   ```bash
   python sudoku_gui.py
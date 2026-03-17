import tkinter as tk
import time

class SudokuVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualisasi Backtracking Sudoku")
        self.root.geometry("400x450")
        
        # Papan Sudoku awal (0 berarti sel kosong)
        self.board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        
        self.cells = {}
        self.create_board()
        
        # Tombol untuk memulai animasi
        self.solve_btn = tk.Button(self.root, text="Selesaikan Sudoku", font=("Arial", 12, "bold"), command=self.start_solving)
        self.solve_btn.pack(pady=15)

    def create_board(self):
        """Membuat grid UI untuk papan Sudoku"""
        board_frame = tk.Frame(self.root, bg="black", bd=2)
        board_frame.pack(pady=10)

        for i in range(9):
            for j in range(9):
                # Mengatur ketebalan garis untuk memisahkan kuadran 3x3
                pad_y = (3 if i % 3 == 0 and i != 0 else 1)
                pad_x = (3 if j % 3 == 0 and j != 0 else 1)
                
                cell_frame = tk.Frame(board_frame, bg="white", width=40, height=40)
                cell_frame.grid(row=i, column=j, padx=(pad_x, 1), pady=(pad_y, 1))
                cell_frame.pack_propagate(False) # Mencegah frame menyusut

                val = self.board[i][j]
                text_val = str(val) if val != 0 else ""
                
                label = tk.Label(cell_frame, text=text_val, bg="white", fg="black", font=("Arial", 16, "bold"))
                label.pack(expand=True, fill="both")
                
                self.cells[(i, j)] = label

    def update_cell(self, row, col, val, color):
        """Memperbarui teks dan warna pada sel tertentu, lalu me-refresh UI"""
        text_val = str(val) if val != 0 else ""
        self.cells[(row, col)].config(text=text_val, fg=color)
        self.root.update() # Memaksa Tkinter menggambar ulang UI
        time.sleep(0.05)   # Jeda waktu (delay) untuk efek animasi

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self, num, pos):
        # Cek Baris
        for i in range(9):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False
        # Cek Kolom
        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False
        # Cek Kuadran 3x3
        box_x, box_y = pos[1] // 3, pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False
        return True

    def solve(self):
        """Algoritma Backtracking rekursif"""
        find = self.find_empty()
        if not find:
            return True # Solusi ditemukan
        else:
            row, col = find

        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i
                
                # VISUALISASI: Tampilkan angka yang sedang dicoba (Warna Hijau)
                self.update_cell(row, col, i, "green")

                if self.solve():
                    return True

                # BACKTRACKING: Kosongkan sel jika menemui jalan buntu
                self.board[row][col] = 0
                
                # VISUALISASI: Hapus angka dari UI (Efek backtrack)
                self.update_cell(row, col, 0, "red")

        return False

    def start_solving(self):
        """Fungsi yang dipanggil saat tombol diklik"""
        self.solve_btn.config(state="disabled", text="Sedang Menyelesaikan...")
        sukses = self.solve()
        
        if sukses:
            self.solve_btn.config(text="Solusi Selesai!", bg="lightgreen", fg="black")
        else:
            self.solve_btn.config(text="Tidak ada solusi", bg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuVisualizer(root)
    root.mainloop()
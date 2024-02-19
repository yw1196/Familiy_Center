import tkinter as tk
from tkinter import filedialog
import pandas as pd

# create_winning_excel 메서드 주석 처리
def create_winning_excel(base_path, win_dates, file_path):
    print(f"Creating Winner Excel for {win_dates} with file: {file_path}")

# GUI 창을 생성하는 클래스
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Create Winner Excel")
        self.master.geometry("400x200")

        self.label = tk.Label(master, text="Select Excel File:")
        self.label.pack(pady=10)

        self.button = tk.Button(master, text="Browse", command=self.browse_file)
        self.button.pack(pady=10)

        self.create_button = tk.Button(master, text="Create Winner Excel", command=self.create_winner_excel)
        self.create_button.pack()

        self.file_path = ""

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(initialdir="/", title="Select Excel File", filetypes=(("Excel files", "*.xlsx;*.xls"), ("all files", "*.*"))).replace("/","\\")

    def create_winner_excel(self):
        if self.file_path:
            print(f"Creating Winner Excel for file: {self.file_path}")
            # create_winning_excel("D:\\계정\\Desktop\\2024\\1기\\추가모집\\", "12. 26.", self.file_path)
            print("Winner Excel Created!")
        else:
            print("Please select an Excel file.")

# GUI 실행
root = tk.Tk()
app = App(root)
root.mainloop()
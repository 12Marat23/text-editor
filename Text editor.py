import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class TextEditorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Text Editor')
        self.geometry('500x500+100+200')
        self.app()
        self.app_menu()

    def app(self):
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Новый", command=self.new_file)
        file_menu.add_command(label="Открыть...", command=self.open_file)
        file_menu.add_command(label="Сохранить", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.close)
        menubar.add_cascade(label='Файл', menu=file_menu)
        self.config(menu=menubar)

    def app_menu(self):
        self.text = tk.Text()
        self.text.pack(fill="both", expand=True)


    def new_file(self):
        if tk.messagebox.askyesno("Сохранить?",  "Хотите сохранить текущий файл перед созданием нового?"):
            self.save_file()
        self.text.delete("1.0", tk.END)
        print("Создание нового файла")

    def open_file(self):
        print("Открытие файла")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file_path:
            return
        with open(file_path, 'w') as file:
            text_to_save = self.text.get("1.0", tk.END)
            file.write(text_to_save)
        print("Сохранение файла")

    def close(self):
        if tk.messagebox.askyesno("Сохранить?",  "Хотите сохранить текущий файл?"):
            self.save_file()
        self.quit()

if __name__ == '__main__':
    root = TextEditorApp()
    root.mainloop()

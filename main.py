from tkinter import *
from tkinter import messagebox, filedialog


def chenge_theme(theme):
    text_field["bg"] = view_menu_colors[theme]["text_bg"]
    text_field["fg"] = view_menu_colors[theme]["text_fg"]
    text_field["insertbackground"] = view_menu_colors[theme]["cursor"]
    text_field["selectbackground"] = view_menu_colors[theme]["select_bg"]


def chenge_fonts(font):
    text_field["font"] = fonts[font]["font"]


def nodeapd_exit():
    #  Создаём переменную в которой будет храниться
    #  функция которая будет спрашивать у нас "действительно ли мы хотим выйти"
    answer = messagebox.askokcancel("Выход", "Вы действительно хотите выйти?")
    if answer:
        root.destroy()


def nodepad_open_file():
    file_path = filedialog.askopenfilename(
        title="Выбор файла",
        filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")),
    )
    if file_path:
        text_field.delete('1.0', END)  # всё удаляется с первого символа
        text_field.insert('1.0', open(file_path, encoding='utf-8').read())  # добовляется с первого символа


def save_nodepad():
    file_path = filedialog.asksaveasfilename(filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)  # сохраняем файл от первого символа до последнего
    f.write(text)
    f.close()


root = Tk()
root.title("Блокнот")
root.geometry("600x700")
root.resizable(width=False, height=False)

# Создадим экземпляр класса Menu
main_menu = Menu(root)

# Файл
file_menu = Menu(main_menu, tearoff=False)
file_menu.add_command(label="Открыть", command=nodepad_open_file)
file_menu.add_command(label="Сохранить", command=save_nodepad)
file_menu.add_separator()  # полоска разделения в меню разделов
file_menu.add_command(label="Закрыть", command=nodeapd_exit)
root.config(menu=file_menu)

# Вид
view_menu = Menu(main_menu, tearoff=False)
view_menu_sub = Menu(view_menu, tearoff=False)  # Подменю
view_menu_sub.add_command(label="Тёмная тема", command=lambda: chenge_theme("dark"))
view_menu_sub.add_command(label="Светлая тема", command=lambda: chenge_theme("light"))
view_menu.add_cascade(label="Тема", menu=view_menu_sub)

font_menu_sub = Menu(view_menu, tearoff=False)
font_menu_sub.add_command(label="Arial 15", command=lambda: chenge_fonts("Arial"))
font_menu_sub.add_command(label="Comic Sans MS", command=lambda: chenge_fonts("CSMS"))
font_menu_sub.add_command(label="Times New Roman", command=lambda: chenge_fonts("TNR"))
view_menu.add_cascade(label="Шрифт...", menu=font_menu_sub)
root.config(menu=view_menu)

# создали список меню
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Вид", menu=view_menu)


root.config(menu=main_menu)


f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# создадим словарь с вариантами цвета
view_menu_colors = {
    "dark": {
        "text_bg": "black",
        "text_fg": "yellow",
        "cursor": "red",
        "select_bg": "#8D917A",
    },
    "light": {
        "text_bg": "white",
        "text_fg": "black",
        "cursor": "blue",
        "select_bg": "light green",
    },
}

# Создание словаря с вариантами шрифта
fonts = {
    "Arial": {"font": "Arial 14 bold"},
    "CSMS": {"font": ("Comic Sans MS", 14, "bold")},
    "TNR": {"font": ("Times New Roman", 14, "bold")},
}


text_field = Text(
    f_text,
    fg="yellow",
    bg="black",
    padx=15,  # отступ от левого края
    pady=15,  # отступ от верхнего края
    wrap=WORD,  # параметр который переносит текст правильно на новую строку
    insertbackground="red",  # добавление курсора
    selectbackground="#8D917A",  # цвет выделение текста
    spacing3=10,  # делаем красивый обзац
    width=68,
    font="Arial 14 bold",
)

scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=RIGHT, fill=Y)
text_field.config(yscrollcommand=scroll.set)  # для того что бы появился наш скролл

text_field.pack(fill=BOTH, expand=1, side=LEFT)

root.mainloop()

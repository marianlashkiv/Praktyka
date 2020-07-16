from tkinter import *


def triangle():
    """
    Малюємо трикутник
    """
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(o, (0, 0, 0, 0))
    canvas.itemconfig(t, fill=figure_color, outline='white')
    canvas.coords(t, (xx1, yy1, xx2, yy2, xx3, yy3))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення трикутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', font_size), foreground=font_color)


def rectangle():
    """
    Малюємо прямокутник
    """
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(o, (0, 0, 0, 0))
    canvas.itemconfig(r, fill=figure_color, outline='white')
    canvas.coords(r, (xx1, yy1, xx2, yy2))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення прямокутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', font_size),foreground=font_color)


def round():
    """
    Малюємо коло
    """
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    canvas.itemconfig(o, fill=figure_color, outline='white')
    canvas.coords(o, (xx1, yy1, xx2, yy2))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення кола')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', font_size),foreground=font_color)


def clear():
    """
    Очищення полотна
    """
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(o, (0, 0, 0, 0))
    text.delete(1.0, END)


def text_settings():
    """
    Меню вікна налаштувань тексту
    """
    def set():
        """
        Присвоюємо зміннам значення
        """
        global font_size
        global font_color
        font_size = text_size.get()
        font_color = var.get()
        text.destroy()

    text = Toplevel()
    text.title("Колір та розмір тексту")
    Label(text, text="Розмір шрифту").grid(row=0, column=0)
    text_size = Entry(text, width=5)
    text_size.grid(row=0, column=1, sticky=W)
    var = StringVar()
    Radiobutton(text, text="Cиній", variable=var, value='blue').grid(row=1, columnspan=4, sticky=W)
    Radiobutton(text, text="Жовтий", variable=var, value='yellow').grid(row=2, columnspan=4, sticky=W)
    Radiobutton(text, text="Зелений", variable=var, value='green').grid(row=3, columnspan=4, sticky=W)
    Radiobutton(text, text="Чорний", variable=var, value='black').grid(row=4, columnspan=4, sticky=W)
    Button(text, text="Внести зміни", command=set).grid(row=5, columnspan=4)


def figure_settings():
    """
    Меню вікна налаштувань фігур
    """
    def set():
        """
        Присвоюємо зміннам значення
        """
        global xx1
        global yy1
        global xx2
        global yy2
        global xx3
        global yy3
        global figure_color
        xx1 = x1.get()
        xx2 = x2.get()
        xx3 = x3.get()
        yy1 = y1.get()
        yy2 = y2.get()
        yy3 = y3.get()
        figure_color = var.get()
        figure.destroy()


    figure = Toplevel()
    figure.title("Колір та розмір фігури")
    Label(figure, text="x1").grid(row=0, column=0)
    Label(figure, text="y1").grid(row=0, column=2)
    Label(figure, text="x2").grid(row=1, column=0)
    Label(figure, text="y2").grid(row=1, column=2)
    Label(figure, text="x3").grid(row=2, column=0)
    Label(figure, text="y3").grid(row=2, column=2)
    x1 = Entry(figure, width=5)
    x1.grid(row=0, column=1, sticky=W)
    y1 = Entry(figure, width=5)
    y1.grid(row=0, column=3,  sticky=W)
    x2 = Entry(figure, width=5)
    x2.grid(row=1, column=1,  sticky=W)
    y2 = Entry(figure, width=5)
    y2.grid(row=1, column=3,  sticky=W)
    x3 = Entry(figure, width=5)
    x3.grid(row=2, column=1,  sticky=W)
    y3 = Entry(figure, width=5)
    y3.grid(row=2, column=3,  sticky=W)
    var = StringVar()
    Radiobutton(figure, text="Cиній", variable=var, value='blue').grid(row=3, columnspan=4, sticky=W)
    Radiobutton(figure, text="Жовтий", variable=var, value='yellow').grid(row=4, columnspan=4, sticky=W)
    Radiobutton(figure, text="Зелений", variable=var, value='green').grid(row=5, columnspan=4, sticky=W)
    Radiobutton(figure, text="Чорний", variable=var, value='black').grid(row=6, columnspan=4, sticky=W)
    Button(figure, text="Внести зміни", command=set).grid(row=7, columnspan=4)


# Створюємо елементи головного вікна
win = Tk()

mainmenu = Menu(win)
win.config(menu=mainmenu)


settingsmenu = Menu(mainmenu, tearoff=0)
settingsmenu.add_command(label="Налаштуваня зображень", command=figure_settings)
settingsmenu.add_command(label="Налаштуваня тексту", command=text_settings)

mainmenu.add_cascade(label="Налаштуваня", menu=settingsmenu)

b_triangle = Button(text="Трикутник", width=15,
command=triangle)

b_rectangle = Button(text="Прямокутник", width=15,
command=rectangle)

b_round = Button(text="Коло", width=15,
command=round)

b_clear = Button(text="Очищення", width=15,
command=clear)

canvas = Canvas(width=400, height=300, bg='#fff')
text = Text(width=55, height=5, bg='#fff', wrap=WORD)
t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
o = canvas.create_oval(0, 0, 0, 0)
r = canvas.create_rectangle(0, 0, 0, 0)
b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
b_round.grid(row=2, column=0)
b_clear.grid(row=3, column=0)
canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)
win.mainloop()

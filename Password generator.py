#Генератор паролей
# Есть особенности при работе на macOS, tkinter не совместим с некоторыми версиями
# и необходимо запускать через реплит.
# Вся необходимая информаия по tkinter есть https://docs.python.org/3/library/tkinter.html,
# https://metanit.com/python/tkinter/, https://github.com/ParthJadhav/Tkinter-Designer?tab=readme-ov-file,
# репозиторий с гитхаба очень удобный, с возможностью перевода на русский язык.




# Импортируем необходимые модули: `tkinter` для создания графического интерфейса,
# `choice` и `shuffle` из модуля `random` для генерации случайных значений,
# и `string` для работы со строками.
import tkinter
from random import choice, shuffle
import string

# Создаем корневое окно нашего приложения и устанавливаем заголовок.
root = tkinter.Tk()
root.geometry('300x80')
root.title('Генератор паролей')

# Создаем три переменные типа `BooleanVar()`, которые
# будут использоваться для хранения состояния флажков.
integer_in_password = tkinter.BooleanVar()
string_in_password = tkinter.BooleanVar()
symbols_in_password = tkinter.BooleanVar()

# Создаем три флажка (`Checkbutton`) с помощью `tk.Checkbutton`.
# Каждый флажок связан с соответствующей переменной `BooleanVar()`.
# Флажки отображаются с текстом "0-9", "A-z" и "symbols"
checkbutton_integer = tkinter.Checkbutton(text='0-9', variable=integer_in_password)
checkbutton_integer.place(x=0, y=0)

checkbutton_string = tkinter.Checkbutton(text='0-9', variable=string_in_password)
checkbutton_string.place(x=0, y=20)

checkbutton_symbols = tkinter.Checkbutton(text='0-9', variable=symbols_in_password)
checkbutton_symbols.place(x=0, y=40)

# Создаем поле ввода (`Entry`) для символов и устанавливаем его ширину
symbols = tkinter.Entry(width=10)
symbols.place(x=0, y=60)

# Создаем спинбокс (`Spinbox`) для выбора длины пароля.
# Флаг `wrap` установлен в `True`, чтобы значение спинбокса
# оборачивалось при достижении минимального или максимального значения.
# Состояние спинбокса установлено в "readonly", чтобы пользователь не мог вводить
# значения вручную.
password_length = tkinter.Spinbox(from_=1.0, to=100, wrap=True, state='readonly')
password_length.place(x=70, y=0)

# Cоздаем поле вывода (`Entry`), в котором будет отображаться сгенерированный пароль.
output = tkinter.Entry()
output.place(x=70, y=20)

# Пишем функцию, которая будет вызываться при нажатии на кнопку.
# В этой функции мы определяем длину пароля, инициализируем пустой список,
# и пустую строку.

# Проверяем состояние флажков и добавляем соответствующие символы в.
# Если флажок "symbols" выбран и поле символов не пустое, мы добавляем символы
# и выбираем случайный символ для пароля.
# Аналогично, если флажок "0-9" выбран, мы добавляем цифры,
# а если флажок "A-z" выбран, мы добавляем буквы верхнего или нижнего регистра.
def generate_password():
    password_length['from_'] = integer_in_password.get() + string_in_password.get() + symbols_in_password.get()

    length = int(password_length.get())
    password = []
    string_choice = ''

    if symbols_in_password.get() and len(symbols.get()) > 0:
        string_choice += symbols.get()
        password.append(choice(symbols.get()))
        length -= 1
    if integer_in_password.get():
        string_choice += string.digits
        password.append(choice(string.digits))
        length -= 1

    if string_in_password.get():
        string_choice += string.ascii_letters
        password.append(choice(string.ascii_letters))
        length -= 1

    if len(string_choice) > 0:
        for _ in range(length):
            password.append(choice(string_choice))

        shuffle(password)

        output.delete(0, tkinter.END)
        output.insert(0, ''.join(password))
    else:
        output.delete(0, tkinter.END)
        output.insert(0, 'None')


generation_button = tkinter.Button(text="Generate", command=generate_password)
generation_button.place(x=70, y=40)

# Запускаем основной цикл обработки событий, чтобы окно приложения оставалось открытым до его закрытия.
root.mainloop()
from tkinter import *
import english_words
import string as s
import tkinter.font as font
from tkinter import messagebox
import random

# Installing modules -> pip install english-words & pip install string

# Main gui window
gui = Tk()
gui.geometry('520x860')
gui.configure(bg='#e2eaff')
# Create Canvas for Squares
canvas = Canvas(gui, width=490, height=680, bg='#c4d4ff', relief='raised')
canvas.place(relx=.02, rely=.005)
# Create Canvas for buttons
buttons_canvas = Canvas(canvas, width=445, height=520, bg='#e2eaff')
buttons_canvas.place(relx=.05, rely=.2)
# Create Canvas for keyboard
keyb_canvas = Canvas(gui, width=490, height=145, relief='raised', bg='#c4d4ff')
keyb_canvas.place(relx=.02, rely=.815)

# Creating list of words of length 5
words_bag = english_words.english_words_alpha_set
words_bag = [x.upper() for x in words_bag if len(x) == 5]

# Select Secret word

secret_word = random.choice(words_bag)
print(secret_word)

# #FirstRow
b1 = buttons_canvas.create_rectangle(20, 20, 90, 85, width=3, fill='#118Bf4', outline='dodger blue')
b2 = buttons_canvas.create_rectangle(105, 20, 175, 85, width=3, fill='#118Bf4', outline='dodger blue')
b3 = buttons_canvas.create_rectangle(190, 20, 260, 85, width=3, fill='#118Bf4', outline='dodger blue')
b4 = buttons_canvas.create_rectangle(275, 20, 345, 85, width=3, fill="#118Bf4", outline='dodger blue')
b5 = buttons_canvas.create_rectangle(360, 20, 430, 85, width=3, fill="#118Bf4", outline='dodger blue')
# #SecondRow
b6 = buttons_canvas.create_rectangle(20, 105, 90, 170, width=3, fill='#118Bf4', outline='dodger blue')
b7 = buttons_canvas.create_rectangle(105, 105, 175, 170, width=3, fill='#118Bf4', outline='dodger blue')
b8 = buttons_canvas.create_rectangle(190, 105, 260, 170, width=3, fill='#118Bf4', outline='dodger blue')
b9 = buttons_canvas.create_rectangle(275, 105, 345, 170, width=3, fill="#118Bf4", outline='dodger blue')
b10 = buttons_canvas.create_rectangle(360, 105, 430, 170, width=3, fill="#118Bf4", outline='dodger blue')
# # #ThirdRow
b11 = buttons_canvas.create_rectangle(20, 190, 90, 255, width=3, fill='#118Bf4', outline='dodger blue')
b12 = buttons_canvas.create_rectangle(105, 190, 175, 255, width=3, fill='#118Bf4', outline='dodger blue')
b13 = buttons_canvas.create_rectangle(190, 190, 260, 255, width=3, fill='#118Bf4', outline='dodger blue')
b14 = buttons_canvas.create_rectangle(275, 190, 345, 255, width=3, fill="#118Bf4", outline='dodger blue')
b15 = buttons_canvas.create_rectangle(360, 190, 430, 255, width=3, fill="#118Bf4", outline='dodger blue')
# # #FourthRow
b16 = buttons_canvas.create_rectangle(20, 275, 90, 340, width=3, fill='#118Bf4', outline='dodger blue')
b17 = buttons_canvas.create_rectangle(105, 275, 175, 340, width=3, fill='#118Bf4', outline='dodger blue')
b18 = buttons_canvas.create_rectangle(190, 275, 260, 340, width=3, fill='#118Bf4', outline='dodger blue')
b19 = buttons_canvas.create_rectangle(275, 275, 345, 340, width=3, fill="#118Bf4", outline='dodger blue')
b20 = buttons_canvas.create_rectangle(360, 275, 430, 340, width=3, fill="#118Bf4", outline='dodger blue')
# # #FifthRow
b21 = buttons_canvas.create_rectangle(20, 360, 90, 425, width=3, fill='#118Bf4', outline='dodger blue')
b22 = buttons_canvas.create_rectangle(105, 360, 175, 425, width=3, fill='#118Bf4', outline='dodger blue')
b23 = buttons_canvas.create_rectangle(190, 360, 260, 425, width=3, fill='#118Bf4', outline='dodger blue')
b24 = buttons_canvas.create_rectangle(275, 360, 345, 425, width=3, fill="#118Bf4", outline='dodger blue')
b25 = buttons_canvas.create_rectangle(360, 360, 430, 425, width=3, fill="#118Bf4", outline='dodger blue')

# Title Label
title_label = Label(canvas, text='qwertle', font=('Arial Rounded MT Bold', 105),
                    bg='#c4d4ff', fg='#118Bf4')
title_label.place(relx=.1, rely=0.006)
# Textbox
text_box = Text(gui, bg='#c4d4ff', fg='black', height=1.3, width=14, font=('Arial Rounded MT Bold', 51))
text_box.config(state='disabled')
text_box.place(relx=.078, rely=.69)
# Line Decor
buttons_canvas.create_line(9, 445, 442, 445, width=7, fill='#118Bf4')
# create keyboard font
buttonFont = font.Font(family='Arial Rounded MT Bold', size=18, weight='bold')
buttonFont2 = font.Font(family='Arial Rounded MT Bold', size=13, weight='bold')

# Buttons function
word = ''


def textOnScreen(char):
    global word
    global words_bag
    text_box.config(state='normal')
    specials = ['ENTER', 'DELETE', ' ', '\n']
    if char not in specials and len(word) <= 5:
        word += char
        print(word)
        if len(word) == 0:
            text_box.insert(INSERT, chars=' ' + char + '  ')
        else:
            text_box.insert(INSERT, chars='  ' + char + '  ')
        text_box.config(state='disabled')
    elif 1 <= len(word) <= 5 and char == 'DELETE':
        word = ""
        text_box.delete("1.0", "end")
        text_box.config(state='disabled')
    if len(word) == 5 and char == 'ENTER':
        text_box.delete("1.0", "end")
        if word in words_bag:
            _eval(word)
            word = ''
        else:
            messagebox.showwarning(title='Not Found', message='Word does not exist!')
        text_box.config(state='disabled')
        return word


# Game logic
rows = [[b1, b2, b3, b4, b5], [b6, b7, b8, b9, b10], [b11, b12, b13, b14, b15], [b16, b17, b18, b19, b20],
        [b21, b22, b23, b24, b25]]
level = 0


def _eval(inputw):
    # global text_box
    global level
    global secret_word
    text_box.config(state='normal')
    level += 1
    y_coords = {'level1': 0.049, 'level2': 0.21, 'level3': 0.371, 'level4': 0.532, 'level5': 0.693}
    x_coors = [.085, .275, 0.465, 0.655, 0.845]
    y = y_coords.get('level' + str(level))
    for index, write_l, read_l in zip(range(len(inputw)), inputw, secret_word):
        if write_l == 'I':
            write_l = f" {write_l}"
        if write_l.lstrip() == read_l:  # Correct
            bgcolor = "#1ae825"
        elif write_l.lstrip() in secret_word:  # Correct but Wrong spot
            bgcolor = '#16f4c1'
        else:  # Wrong
            bgcolor = '#1576cb'
        Label(buttons_canvas, text=write_l, font=('Arial Rounded MT Bold', 42), bg=bgcolor, fg='black').place(
            relx=x_coors[index], rely=float(y))
        buttons_canvas.itemconfig(rows[level - 1][index], fill=bgcolor)

    if inputw == secret_word:
        text_box.insert(INSERT, '       WINNER!!!')
        text_box.config(bg='#1ae825')
    text_box.config(state='disabled')


# keyboards buttons
qq = Button(gui, text='Q', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('Q')).place(relx=.05, rely=.84)
qw = Button(gui, text='W', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('W')).place(relx=.14, rely=.84)
qe = Button(gui, text='E', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('E')).place(relx=.23, rely=.84)
qr = Button(gui, text='R', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('R')).place(relx=.32, rely=.84)
qt = Button(gui, text='T', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('T')).place(relx=.41, rely=.84)
qy = Button(gui, text='Y', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('Y')).place(relx=.50, rely=.84)
qu = Button(gui, text='U', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('U')).place(relx=.59, rely=.84)
qi = Button(gui, text='I', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('I')).place(relx=.68, rely=.84)
qo = Button(gui, text='O', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('O')).place(relx=.77, rely=.84)
qp = Button(gui, text='P', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('P')).place(relx=.86, rely=.84)

qa = Button(gui, text='A', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('A')).place(relx=.09, rely=.89)
qs = Button(gui, text='S', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('S')).place(relx=.18, rely=.89)
qd = Button(gui, text='D', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('D')).place(relx=.27, rely=.89)
qf = Button(gui, text='F', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('F')).place(relx=.36, rely=.89)
qg = Button(gui, text='G', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('G')).place(relx=.45, rely=.89)
qh = Button(gui, text='H', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('H')).place(relx=.54, rely=.89)
qj = Button(gui, text='J', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('J')).place(relx=.63, rely=.89)
qk = Button(gui, text='K', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('K')).place(relx=.72, rely=.89)
ql = Button(gui, text='L', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('L')).place(relx=.81, rely=.89)

qz = Button(gui, text='Z', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('Z')).place(relx=.185, rely=.94)
qx = Button(gui, text='X', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('X')).place(relx=.275, rely=.94)
qc = Button(gui, text='C', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('C')).place(relx=.365, rely=.94)
qv = Button(gui, text='V', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('V')).place(relx=.455, rely=.94)
qb = Button(gui, text='B', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('B')).place(relx=.545, rely=.94)
qn = Button(gui, text='N', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('N')).place(relx=.635, rely=.94)
qm = Button(gui, text='M', width=1, height=1, font=buttonFont, relief='groove',
            command=lambda: textOnScreen('M')).place(relx=.725, rely=.94)
qdel = Button(gui, text='DELETE', width=3, height=2, font=buttonFont2, relief='groove',
              command=lambda: textOnScreen('DELETE')).place(relx=.067, rely=.93)
qenter = Button(gui, text='ENTER', width=3, height=2, font=buttonFont2, relief='groove',
                command=lambda: textOnScreen('ENTER')).place(relx=.82, rely=.93)

# Exit out of gui
gui.mainloop()
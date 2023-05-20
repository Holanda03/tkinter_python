from tkinter import *
from functools import partial

def helloWorld():
    str = 'Hello World'
    text_result['text'] = str

def somar(valor1, valor2):
    result = int(valor1.get()) + int(valor2.get())
    somaResult['text'] = result


window = Tk()
window.geometry('400x150')
window.title('GUI em python')


# HELLO WORLD
main_text = Label(window, text='Título do conteúdo da janela')
main_text.grid(column=0, row=0)

btn = Button(window, text='clique aqui', command=helloWorld)
btn.grid(column=0, row=1)

text_result = Label(window, text='')
text_result.grid(column=0, row=2)

# OTHER
# SOMAR
somarLabel = Label(window, text='Somar')

valor1 = Entry(window)
valor2 = Entry(window)

somarCallable = partial(somar, valor1, valor2)

btnSomar = Button(window, text='Realizar Soma', command=somarCallable)

somaResult = Label(window, text='')

somarLabel.grid(column=2, row=0)
valor1.grid(column=2, row=1)
valor2.grid(column=2, row=2)
btnSomar.grid(column=2, row=3)
somaResult.grid(column=2, row=4)

# SUBTRAIR
subtrairLabel = Label(window, text='Subtrair')


window.mainloop()
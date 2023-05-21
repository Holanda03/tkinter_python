from tkinter import *
from functools import partial

def helloWorld():
    str = 'Hello World'
    text_result['text'] = str

def somar(valor1sum, valor2sum):
    result = int(valor1sum.get()) + int(valor2sum.get())
    somaResult['text'] = result

def subtrair(valor1dif, valor2dif):
    result = int(valor1dif.get()) - int(valor2dif.get())
    subtracaoResult['text'] = result

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

valor1sum = Entry(window)
valor2sum = Entry(window)

somarCallable = partial(somar, valor1sum, valor2sum)

btnSomar = Button(window, text='Realizar Soma', command=somarCallable)

somaResult = Label(window, text='')

somarLabel.grid(column=2, row=0)
valor1sum.grid(column=2, row=1)
valor2sum.grid(column=2, row=2)
btnSomar.grid(column=2, row=3)
somaResult.grid(column=2, row=4)

# SUBTRAIR
subtrairLabel = Label(window, text='Subtrair')

valor1dif = Entry(window)
valor2dif = Entry(window)

subtracaoCallable = partial(subtrair, valor1dif, valor2dif)

btnSubtrair = Button(window, text='Realizar Subtração', command=subtracaoCallable)

subtracaoResult = Label(window, text='')

subtrairLabel.grid(column=3, row=0)
valor1dif.grid(column=3, row=1)
valor2dif.grid(column=3, row=2)
btnSubtrair.grid(column=3, row=3)
subtracaoResult.grid(column=3, row=4)

window.mainloop()
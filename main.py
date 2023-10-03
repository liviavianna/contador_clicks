import tkinter as tk

root = tk.Tk()
root.geometry('600x600')
root.title('Contador de clicks')
root.configure(background='#1d1d1d')

numero = 0


def acrescentar():
    global numero
    numero += 1
    contagem_click.configure(text=numero)


def diminuir():
    global numero
    numero -= 1
    contagem_click.configure(text=numero)


margem = tk.Canvas(root, height=200, background='#1d1d1d',
                   bd=0, highlightthickness=0, relief='flat')
margem.pack()
botao_acrescentar = tk.Button(root, bg='#FFFFFF', text='+',
                              font=('Montserrat', 16, 'bold'), padx=10, command=acrescentar)
botao_acrescentar.pack()
contagem_click = tk.Label(root, text=numero, fg='#FFFFFF',
                          bg='#1d1d1d', font=('Montserrat', 16, 'bold'))
contagem_click.pack()
botao_diminuir = tk.Button(root, bg='#FFFFFF', text='-',
                           font=('Montserrat', 16, 'bold'), padx=10, command=diminuir)
botao_diminuir.pack()
root.mainloop()

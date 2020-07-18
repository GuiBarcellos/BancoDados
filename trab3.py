from tkinter import *

#INSIRA CODIGO BD AQUI

def changeWindow21(screen):
	screen.destroy()
	main_screen()

def changeWindow32(screen):
	screen.destroy()
	register()
	
def changeWindow12_login(screen):
	screen.destroy()
	login()
	
def changeWindow12_register(screen):
	screen.destroy()
	register()

def changeWindowSair(screen):
	screen.destroy()
	main_screen()	

def roundPolygon(x, y, sharpness, **kwargs):

    if sharpness < 2:
        sharpness = 2

    ratioMultiplier = sharpness - 1
    ratioDividend = sharpness

    points = []

    for i in range(len(x)):
        points.append(x[i])
        points.append(y[i])

        if i != (len(x) - 1):
            points.append((ratioMultiplier*x[i] + x[i + 1])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[i + 1])/ratioDividend)
            points.append((ratioMultiplier*x[i + 1] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[i + 1] + y[i])/ratioDividend)
        else:
            points.append((ratioMultiplier*x[i] + x[0])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[0])/ratioDividend)
            points.append((ratioMultiplier*x[0] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[0] + y[i])/ratioDividend)
            points.append(x[0])
            points.append(y[0])

    return canvas.create_polygon(points, **kwargs, smooth=TRUE)
	
	
def busca_aluno():
	global screenbuscaaluno
	screenoptions.destroy()
	screenbuscaaluno = Tk()
	screenbuscaaluno.title("Busca por Aluno")
	screenbuscaaluno.geometry("650x520+%d+%d" %(posx, posy))

	screenbuscaaluno.mainloop()

def busca_professor():
	global screenbuscaprofessor
	screenoptions.destroy()
	screenbuscaprofessor = Tk()
	screenbuscaprofessor.title("Busca por Professor")
	screenbuscaprofessor.geometry("650x520+%d+%d" %(posx, posy))

	screenbuscaprofessor.mainloop()

def busca_turma():
	global screenbuscaturma
	screenoptions.destroy()
	screenbuscaturma = Tk()
	screenbuscaturma.title("Busca por Turma")
	screenbuscaturma.geometry("650x520+%d+%d" %(posx, posy))

	screenbuscaturma.mainloop()

def busca_arte_marcial():
	global screenbuscaartemarcial
	screenoptions.destroy()
	screenbuscaartemarcial = Tk()
	screenbuscaartemarcial.title("Busca por Arte Marcial")
	screenbuscaartemarcial.geometry("650x520+%d+%d" %(posx, posy))

	screenbuscaartemarcial.mainloop()

def busca_imovel():
	global screenbuscaimovel
	screenoptions.destroy()
	screenbuscaimovel = Tk()
	screenbuscaimovel.title("Busca por Imovel")
	screenbuscaimovel.geometry("650x520+%d+%d" %(posx, posy))

	screenbuscaimovel.mainloop()

def busca_produto():
	global screenbuscaproduto
	screenoptions.destroy()
	screenbuscaproduto = Tk()
	screenbuscaproduto.title("Busca por Produto")
	screenbuscaproduto.geometry("650x520+%d+%d" %(posx, posy))

	screenbuscaproduto.mainloop()

def busca_fornecedor():			
	global screenbuscafornecedor
	screenoptions.destroy()
	screenbuscafornecedor = Tk()
	screenbuscafornecedor.title("Busca por Fornecedor")
	screenbuscafornecedor.geometry("650x520+%d+%d" %(posx, posy))

	screenbuscafornecedor.mainloop()

def tela_opcoes():
	global screenoptions
	screenlogin.destroy()
	screenoptions = Tk()
	screenoptions.title("Busca")
	screenoptions.geometry("650x520+%d+%d" %(posx, posy))

	Label(screenoptions, text = "O que voce deseja buscar?", fg = "black", font = ("Calibri", 15)).pack()
	Label(screenoptions, text = "").pack()

	Button(screenoptions, text = "Aluno",width = 20, height = 3, command = busca_aluno).pack()
	Button(screenoptions, text = "Professor", width = 20, height = 3, command = busca_professor).pack()
	Button(screenoptions, text = "Turma", width = 20, height = 3, command = busca_turma).pack()
	Button(screenoptions, text = "Arte Marcial", width = 20, height = 3, command = busca_arte_marcial).pack()
	Button(screenoptions, text = "Imovel", width = 20, height = 3, command = busca_imovel).pack()
	Button(screenoptions, text = "Produto", width = 20, height = 3, command = busca_produto).pack()
	Button(screenoptions, text = "Fornecedor", width = 20, height = 3, command = busca_fornecedor).pack()
	
	bsair = Button(screenoptions, text = "Sair", command = lambda: changeWindowSair(screenoptions))
	bsair.place(x=0, y=0)
	
	
	screenoptions.mainloop()	


def login_verify(flag):	
	
	user_login = username_verify.get()
	password_login = password_verify.get()
	 
	if user_login == "gui": #Aqui verifica na base dados se o login existe
		print("Login Sucesso")
		tela_opcoes()
		
	else:
		if flag[-1] == 1:	
			lb1 = Label(screenlogin, text = "Credencias incorretas! Tente novamente", bg = '#F5F5F5', fg = "red", font = ("Garamond", 12))
			lb1.place(relx=0.5, rely=0.9, anchor=CENTER)

		username_verify.delete(0, END)
		password_verify.delete(0, END)
		flag.append(0)
	

"""
def register_user():
	username_info = username.get()
	password_info = password.get()
	file = open(username_info, "w")
	file.write(username_info+"\n")
	file.write(password_info+"\n")
	file.close()
	username_entry.delete(0, END)
	password_entry.delete(0, END)
	Label(screen1, text = "Registro concluido", fg = "green", font = ("Calibri", 12)).pack()
def register():
	global screen1
	screen1 = Toplevel(screen)
	screen1.title("Register")
	screen1.geometry("600x350")
	global username
	global password
	global username_entry
	global password_entry
	username = StringVar()
	password = StringVar()
	Label(screen1, text = "Preencha os dados abaixo:").pack()
	Label(screen1, text = "").pack()
	Label(screen1, text = "Username * ").pack()
	username_entry = Entry(screen1, textvariable = username)
	username_entry.pack()
	Label(screen1, text = "Password * ").pack()
	password_entry = Entry(screen1, textvariable = password, show = "*")
	password_entry.pack()
	Label(screen1, text = "").pack()
	Button(screen1, text = "Register", height = 1, command = register_user).pack()
"""
def cadastra_estudante_banco():
	
	username_student_entry.delete(0,END)
	password_student_entry.delete(0, END)
	cpf_student_entry.delete(0,END)
	telefone_student_entry.delete(0,END)
	nome_student_entry.delete(0,END)
	graduacao_student_entry.delete(0,END)
	arte_marcial_student_entry.delete(0,END)
	idade_student_entry.delete(0,END)
	sexo_student_entry.delete(0,END)


	lb1 = Label(screenregstud, text = "Registro concluido", bg = '#F5F5F5',fg = "green", font = ("Garamond", 12))
	lb1.place(relx=0.5, rely=0.95, anchor=CENTER)

def register_student():
	global screenregstud
	screenreg.destroy()
	screenregstud = Tk()
	screenregstud.title("Registro Estudante")
	screenregstud.geometry("650x520+%d+%d" %(posx, posy))
	screenregstud['bg'] = '#F5F5F5'
	
	global username_student_entry
	global password_student_entry
	global cpf_student_entry
	global telefone_student_entry
	global nome_student_entry
	global graduacao_student_entry
	global arte_marcial_student_entry
	global idade_student_entry
	global sexo_student_entry

	lb1 = Label(screenregstud, text = "Preencha os dados abaixo", font = 'Garamond', bg = '#F5F5F5')
	lb1.place(relx=0.5, rely=0.05, anchor=CENTER)

	lb2 = Label(screenregstud, text = "Username * ", font = 'Garamond', bg = '#F5F5F5')
	username_student_entry = Entry(screenregstud, textvariable = username)
	lb2.place(relx=0.35, rely=0.17, anchor=CENTER)
	username_student_entry.place(relx=0.6, rely=0.17, anchor=CENTER)
	
	lb3 = Label(screenregstud, text = "Password * ", font = 'Garamond', bg = '#F5F5F5')
	password_student_entry = Entry(screenregstud, textvariable = password, show = "*")
	lb3.place(relx=0.35, rely=0.24, anchor=CENTER)
	password_student_entry.place(relx=0.6, rely=0.24, anchor=CENTER)
	
	lb4 = Label(screenregstud, text = "CPF * ", font = 'Garamond', bg = '#F5F5F5')
	cpf_student_entry = Entry(screenregstud, textvariable = cpf)
	lb4.place(relx=0.35, rely=0.31, anchor=CENTER)
	cpf_student_entry.place(relx=0.6, rely=0.31, anchor=CENTER)
	
	lb5 = Label(screenregstud, text = "Telefone * ", font = 'Garamond', bg = '#F5F5F5')
	telefone_student_entry = Entry(screenregstud, textvariable = telefone)
	lb5.place(relx=0.35, rely=0.38, anchor=CENTER)
	telefone_student_entry.place(relx=0.6, rely=0.38, anchor=CENTER)
	
	lb6 = Label(screenregstud, text = "Nome * ", font = 'Garamond', bg = '#F5F5F5')
	nome_student_entry = Entry(screenregstud, textvariable = nome)
	lb6.place(relx=0.35, rely=0.45, anchor=CENTER)
	nome_student_entry.place(relx=0.6, rely=0.45, anchor=CENTER)
	
	lb7 = Label(screenregstud, text = "Graduacao * ", font = 'Garamond', bg = '#F5F5F5')
	graduacao_student_entry = Entry(screenregstud, textvariable = graduacao)
	lb7.place(relx=0.35, rely=0.52, anchor=CENTER)
	graduacao_student_entry.place(relx=0.6, rely=0.52, anchor=CENTER)

	lb8 = Label(screenregstud, text = "Arte Marcial * ", font = 'Garamond', bg = '#F5F5F5')
	arte_marcial_student_entry = Entry(screenregstud, textvariable = arte_marcial)
	lb8.place(relx=0.35, rely=0.59, anchor=CENTER)
	arte_marcial_student_entry.place(relx=0.6, rely=0.59, anchor=CENTER)

	lb9 = Label(screenregstud, text = "Idade * ", font = 'Garamond', bg = '#F5F5F5')
	idade_student_entry = Entry(screenregstud, textvariable = idade)
	lb9.place(relx=0.35, rely=0.66, anchor=CENTER)
	idade_student_entry.place(relx=0.6, rely=0.66, anchor=CENTER)
	
	lb10 = Label(screenregstud, text = "Sexo * ", font = 'Garamond', bg = '#F5F5F5')
	sexo_student_entry = Entry(screenregstud, textvariable = sexo)
	lb10.place(relx=0.35, rely=0.73, anchor=CENTER)
	sexo_student_entry.place(relx=0.6, rely=0.73, anchor=CENTER)
	
	
	bt1 = Button(screenregstud, text = "Register", height = 1, font = 'Garamond',  bd=5, bg = '#A9A9A9', command = cadastra_estudante_banco)
	bt1.config(highlightbackground='#F5F5F5')
	bt1.place(relx=0.5, rely=0.85, anchor=CENTER)
	
	bvoltar = Button(screenregstud, text = "Voltar", font = 'Garamond',  bd=5, bg = '#A9A9A9', command = lambda: changeWindow32(screenregstud))
	bvoltar.place(x=0, y=0)
	bvoltar.config(highlightbackground='#F5F5F5')
	
	screenregstud.mainloop()


def cadastra_professor_banco():
	
	username_professor_entry.delete(0,END)
	password_professor_entry.delete(0, END)
	cpf_professor_entry.delete(0,END)
	telefone_professor_entry.delete(0,END)
	nome_professor_entry.delete(0,END)
	graduacao_professor_entry.delete(0,END)
	arte_marcial_professor_entry.delete(0,END)

	lb1 = Label(screenregprof, text = "Registro concluido", bg = '#F5F5F5',fg = "green", font = ("Garamond", 12))
	lb1.place(relx=0.5, rely=0.95, anchor=CENTER)


def register_professor():
	global screenregprof
	screenreg.destroy()
	screenregprof = Tk()
	screenregprof.title("Registro Professor")
	screenregprof.geometry("650x520+%d+%d" %(posx, posy))
	screenregprof['bg'] = '#F5F5F5'
	
	global username_professor_entry
	global password_professor_entry
	global cpf_professor_entry
	global telefone_professor_entry
	global nome_professor_entry
	global graduacao_professor_entry
	global arte_marcial_professor_entry

	lb1 = Label(screenregprof, text = "Preencha os dados abaixo", font = 'Garamond', bg = '#F5F5F5')
	lb1.place(relx=0.5, rely=0.05, anchor=CENTER)

	lb2 = Label(screenregprof, text = "Username * ", font = 'Garamond', bg = '#F5F5F5')
	username_professor_entry = Entry(screenregprof, textvariable = username)
	lb2.place(relx=0.35, rely=0.15, anchor=CENTER)
	username_professor_entry.place(relx=0.6, rely=0.15, anchor=CENTER)
	
	lb3 = Label(screenregprof, text = "Password * ", font = 'Garamond', bg = '#F5F5F5')
	password_professor_entry = Entry(screenregprof, textvariable = password, show = "*")
	lb3.place(relx=0.35, rely=0.25, anchor=CENTER)
	password_professor_entry.place(relx=0.6, rely=0.25, anchor=CENTER)
	
	lb4 = Label(screenregprof, text = "CPF * ", font = 'Garamond', bg = '#F5F5F5')
	cpf_professor_entry = Entry(screenregprof, textvariable = cpf)
	lb4.place(relx=0.35, rely=0.35, anchor=CENTER)
	cpf_professor_entry.place(relx=0.6, rely=0.35, anchor=CENTER)
	
	lb5 = Label(screenregprof, text = "Telefone * ", font = 'Garamond', bg = '#F5F5F5')
	telefone_professor_entry = Entry(screenregprof, textvariable = telefone)
	lb5.place(relx=0.35, rely=0.45, anchor=CENTER)
	telefone_professor_entry.place(relx=0.6, rely=0.45, anchor=CENTER)
	
	lb6 = Label(screenregprof, text = "Nome * ", font = 'Garamond', bg = '#F5F5F5')
	nome_professor_entry = Entry(screenregprof, textvariable = nome)
	lb6.place(relx=0.35, rely=0.55, anchor=CENTER)
	nome_professor_entry.place(relx=0.6, rely=0.55, anchor=CENTER)
	
	lb7 = Label(screenregprof, text = "Graduacao * ", font = 'Garamond', bg = '#F5F5F5')
	graduacao_professor_entry = Entry(screenregprof, textvariable = graduacao)
	lb7.place(relx=0.35, rely=0.65, anchor=CENTER)
	graduacao_professor_entry.place(relx=0.6, rely=0.65, anchor=CENTER)
	
	lb8 = Label(screenregprof, text = "Arte Marcial * ", font = 'Garamond', bg = '#F5F5F5')
	arte_marcial_professor_entry = Entry(screenregprof, textvariable = arte_marcial)
	lb8.place(relx=0.35, rely=0.75, anchor=CENTER)
	arte_marcial_professor_entry.place(relx=0.6, rely=0.75, anchor=CENTER)
	
	bt1 = Button(screenregprof, text = "Register",font = 'Garamond',  bd=5, bg = '#A9A9A9', height = 1, command = cadastra_professor_banco)
	bt1.place(relx=0.5, rely=0.85, anchor=CENTER)
	bt1.config(highlightbackground='#F5F5F5')
	
	bvoltar = Button(screenregprof, text = "Voltar", font = 'Garamond',  bd=5, bg = '#A9A9A9', command = lambda: changeWindow32(screenregprof))
	bvoltar.place(x=0, y=0)
	bvoltar.config(highlightbackground='#F5F5F5')	
	
	screenregprof.mainloop()

def cadastra_supplier_banco():
	
	username_supplier_entry.delete(0,END)
	password_supplier_entry.delete(0, END)
	cpf_supplier_entry.delete(0,END)
	telefone_supplier_entry.delete(0,END)
	nome_supplier_entry.delete(0,END)
	

	lb1 = Label(screenregsupp, bg = '#F5F5F5', text = "Registro concluido", fg = "green", font = ("Garamond", 12))
	lb1.place(relx=0.5, rely=0.9, anchor=CENTER)
		


def register_supplier():
	
	global screenregsupp
	screenreg.destroy()
	screenregsupp = Tk()
	screenregsupp.title("Registro Fornecedor")
	screenregsupp.geometry("650x520+%d+%d" %(posx, posy))
	screenregsupp['bg'] = '#F5F5F5'
	
	global username_supplier_entry
	global password_supplier_entry
	global cpf_supplier_entry
	global telefone_supplier_entry
	global nome_supplier_entry
	
	lb1 = Label(screenregsupp, font = 'Garamond', text = "Preencha os dados abaixo", bg = '#F5F5F5')
	lb1.place(relx=0.5, rely=0.05, anchor=CENTER)

	lb2 = Label(screenregsupp, text = "Username * ",font = 'Garamond', bg = '#F5F5F5')
	username_supplier_entry = Entry(screenregsupp, textvariable = username)
	lb2.place(relx=0.35, rely=0.2, anchor=CENTER)
	username_supplier_entry.place(relx=0.6, rely=0.2, anchor=CENTER)
	
	lb3 = Label(screenregsupp, text = "Password * ",font = 'Garamond', bg = '#F5F5F5')
	password_supplier_entry = Entry(screenregsupp, textvariable = password, show = "*")
	lb3.place(relx=0.35, rely=0.3, anchor=CENTER)
	password_supplier_entry.place(relx=0.6, rely=0.3, anchor=CENTER)
	
	lb4 = Label(screenregsupp, text = "CPF * ",font = 'Garamond', bg = '#F5F5F5')
	cpf_supplier_entry = Entry(screenregsupp, textvariable = cpf)
	lb4.place(relx=0.35, rely=0.4, anchor=CENTER)
	cpf_supplier_entry.place(relx=0.6, rely=0.4, anchor=CENTER)
	
	lb5 = Label(screenregsupp, text = "Telefone * ",font = 'Garamond', bg = '#F5F5F5')
	telefone_supplier_entry = Entry(screenregsupp, textvariable = telefone)
	lb5.place(relx=0.35, rely=0.5, anchor=CENTER)
	telefone_supplier_entry.place(relx=0.6, rely=0.5, anchor=CENTER)

	lb6 = Label(screenregsupp, text = "Nome * ",font = 'Garamond', bg = '#F5F5F5')
	nome_supplier_entry = Entry(screenregsupp, textvariable = nome)
	lb6.place(relx=0.35, rely=0.6, anchor=CENTER)
	nome_supplier_entry.place(relx=0.6, rely=0.6, anchor=CENTER)
	
	bt1 = Button(screenregsupp, text = "Register", font = 'Garamond',  bd=5, bg = '#A9A9A9', height = 1, command = cadastra_supplier_banco)
	bt1.place(relx=0.5, rely=0.8, anchor=CENTER)
	bt1.config(highlightbackground='#F5F5F5')
	
	bvoltar = Button(screenregsupp, text = "Voltar",font = 'Garamond',  bd=5, bg = '#A9A9A9', command = lambda: changeWindow32(screenregsupp))
	bvoltar.place(x=0, y=0)
	bvoltar.config(highlightbackground='#F5F5F5')	

	
	screenregsupp.mainloop()

def cadastra_owner_banco():

	et2.delete(0,END)
	et3.delete(0,END)
	et4.delete(0,END)
	et5.delete(0,END)
	et6.delete(0,END)
	
	lb1 = Label(screenregowner, text = "Registro concluido", fg = "green", bg = '#F5F5F5', font = ("Garamond", 12))
	lb1.place(relx=0.5, rely=0.9, anchor=CENTER)
	

def register_owner():
	global screenregowner
	screenreg.destroy()
	screenregowner = Tk()
	screenregowner.title("Registro Locador")
	screenregowner.geometry("650x520+%d+%d" %(posx, posy))
	screenregowner['bg'] = '#F5F5F5'
	
	global et1,et2,et3,et4,et5,et6
	
	lb1=Label(screenregowner, text = "Preencha os dados abaixo", font = 'Garamond', bg = '#F5F5F5')
	lb1.place(relx=0.5, rely=0.05, anchor=CENTER)

	lb2 = Label(screenregowner, text = "Username * ", font = 'Garamond', bg = '#F5F5F5')
	et2 = Entry(screenregowner, textvariable = username)
	lb2.place(relx=0.35, rely=0.2, anchor=CENTER)
	et2.place(relx=0.6, rely=0.2, anchor=CENTER)
	
	lb3 = Label(screenregowner, text = "Password * ", font = 'Garamond', bg = '#F5F5F5')
	et3 = Entry(screenregowner, textvariable = password, show = "*")
	lb3.place(relx=0.35, rely=0.3, anchor=CENTER)
	et3.place(relx=0.6, rely=0.3, anchor=CENTER)

	lb4 = Label(screenregowner, text = "CPF * ", font = 'Garamond', bg = '#F5F5F5')
	et4 = Entry(screenregowner, textvariable = cpf)
	lb4.place(relx=0.35, rely=0.4, anchor=CENTER)
	et4.place(relx=0.6, rely=0.4, anchor=CENTER)

	lb5 = Label(screenregowner, text = "Telefone * ", font = 'Garamond', bg = '#F5F5F5')
	et5 = Entry(screenregowner, textvariable = telefone)
	lb5.place(relx=0.35, rely=0.5, anchor=CENTER)
	et5.place(relx=0.6, rely=0.5, anchor=CENTER)

	lb6 = Label(screenregowner, text = "Nome * ", font = 'Garamond', bg = '#F5F5F5')
	et6 = nome_owner_entry = Entry(screenregowner, textvariable = nome)
	lb6.place(relx=0.35, rely=0.6, anchor=CENTER)
	et6.place(relx=0.6, rely=0.6, anchor=CENTER)

	bt1 = Button(screenregowner, text = "Register", height = 1, font = 'Garamond',  bd=5, bg = '#A9A9A9',command = cadastra_owner_banco)
	bt1.place(relx=0.5, rely=0.8, anchor=CENTER)
	bt1.config(highlightbackground='#F5F5F5')
	
	bvoltar = Button(screenregowner, text = "Voltar",font = 'Garamond',  bd=5, bg = '#A9A9A9', command = lambda: changeWindow32(screenregowner))
	bvoltar.place(x=0, y=0)
	bvoltar.config(highlightbackground='#F5F5F5')	
	
	screenregowner.mainloop()


def register():
	global screenreg

	screenreg = Tk()
	screenreg.title("Register")
	screenreg.geometry("650x520+%d+%d" %(posx, posy))
	screenreg['bg'] = '#F5F5F5'

	lb1 = Label(screenreg, text = "Escolha o tipo de cadastro", font = ("Garamond", 16), bg = '#F5F5F5')
	lb1.place(relx=0.5, rely=0.05, anchor=CENTER)

	bt1 = Button(screenreg, text = "Aluno", width = 20, font = 'Garamond', height = 3, bd=5, bg = '#A9A9A9', command = register_student)
	bt1.place(relx=0.5, rely=0.2, anchor=CENTER)
	bt1.config(highlightbackground='#F5F5F5')
	
	bt2 = Button(screenreg, text = "Professor", width = 20, font = 'Garamond', height = 3, bd=5, bg = '#A9A9A9', command = register_professor)
	bt2.place(relx=0.5, rely=0.4, anchor=CENTER)
	bt2.config(highlightbackground='#F5F5F5')
	
	bt3 = Button(screenreg, text = "Fornecedor", width = 20, font = 'Garamond',  height = 3, bd=5, bg = '#A9A9A9', command = register_supplier)
	bt3.place(relx=0.5, rely=0.6, anchor=CENTER)
	bt3.config(highlightbackground='#F5F5F5')
	
	bt4 = Button(screenreg, text = "Locador", width = 20, font = 'Garamond', height = 3, bd=5, bg = '#A9A9A9',command = register_owner)
	bt4.place(relx=0.5, rely=0.8, anchor=CENTER)
	bt4.config(highlightbackground='#F5F5F5')
	
	bvoltar = Button(screenreg, text = "Voltar", font = 'Garamond',  bd=5, bg = '#A9A9A9', command = lambda: changeWindow21(screenreg))
	bvoltar.place(x=0, y=0)
	bvoltar.config(highlightbackground='#F5F5F5')
	
	
	screenreg.mainloop()
	
	



def login():
	
	global screenlogin
	global username_verify
	global password_verify
	global canvas
	
	flag = [1]
	
	screenlogin = Tk()
	screenlogin.title("Login")
	screenlogin.geometry("650x520+%d+%d" %(posx, posy))

	canvas = Canvas(screenlogin, width=2000, height=2000, bg='#F5F5F5')
	
	my_rectangle = roundPolygon([165, 485, 485, 165], [420, 420, 100, 100], 10 , width=5, outline="black", fill="#F5F5F5")
	canvas.place(x=0, y=0, relwidth=1.0, relheight=1.0)
	
	lb3 = Label(screenlogin, text = "Faca login com seus dados", bg = '#F5F5F5', font = ("Garamond", 15))
	lb3.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lb1 = Label(screenlogin, text = "Username * ", font = 'Garamond', bg='#F5F5F5')
	lb1.place(relx=0.5, rely=0.3, anchor=CENTER)
	et1 = username_verify = Entry(screenlogin, textvariable = username)
	et1.place(relx=0.5, rely=0.35, anchor=CENTER)
	
	lb2 = Label(screenlogin, text = "Password * ", font = 'Garamond', bg='#F5F5F5')
	lb2.place(relx=0.5, rely=0.5, anchor=CENTER)
	et2 = password_verify = Entry(screenlogin, textvariable = password, show = "*")
	et2.place(relx=0.5, rely=0.55, anchor=CENTER)
	
	bt1 = Button(screenlogin, text = "Login", font = 'Garamond', bd=5, bg = '#A9A9A9',command = lambda: login_verify(flag))
	bt1.place(relx=0.5, rely=0.7, anchor=CENTER)
	
	bvoltar = Button(screenlogin, text = "Voltar", bd=5, font = 'Garamond', bg = '#A9A9A9', command = lambda: changeWindow21(screenlogin))
	bvoltar.place(x=0, y=0)
	
	bt1.config(highlightbackground='#F5F5F5')
	bvoltar.config(highlightbackground='#F5F5F5')

	
	screenlogin.mainloop()

def main_screen():
	global screen
	global posx
	global posy
	screen = Tk()
	
	lscreen = screen.winfo_screenwidth()
	ascreen = screen.winfo_screenheight()
	posx = lscreen/2 - 650/2
	posy = ascreen/2 - 520/2

	screen.geometry("650x520+%d+%d"%(posx, posy))
	screen.title("Luta Luta")
	
	global username #Todos
	global password #Todos
	global cpf #Todos
	global telefone #Todos
	global nome #Todos
	global graduacao #Aluno, Professor
	global arte_marcial #Aluno, Professor
	global sexo #Aluno
	global idade #Aluno
	username = StringVar()
	password = StringVar()
	cpf = StringVar()
	telefone = StringVar()
	nome = StringVar()
	graduacao = StringVar()
	arte_marcial = StringVar()
	sexo = StringVar()
	idade = StringVar()

	
	img = PhotoImage(file="img-1.png")
	lb_image = Label(screen, image=img)
	lb_image.place(x=0, y=0, relwidth=1.0, relheight=1.0)
	
	#lb = Label(text = "Luta Luta", bg = '#D2B48C', width = "300", height = "2", font = ("Garamond", 13)).pack()
	
	bt1 = Button(text = "Login", height = "2", relief = 'groove', bd=9, bg = '#D2B48C',	width = "20", command = lambda: changeWindow12_login(screen), font = ("Garamond", 13))
	bt2 = Button(text = "Register",height = "2", relief = 'groove', bd=9, bg ='#D2B48C', width = "20", command = lambda: changeWindow12_register(screen), font = ("Garamond", 13))
	bt1.config(highlightbackground='black')
	bt2.config(highlightbackground='black')
	
	bt1.place(relx=0.5, rely=0.4, anchor=CENTER)
	bt2.place(relx=0.5, rely=0.6, anchor=CENTER)
	
	screen.mainloop()

main_screen()

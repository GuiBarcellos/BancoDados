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
			Label(screenlogin, text = "Credencias incorretas! Tente novamente", fg = "red", font = ("Calibri", 12)).pack()
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


	Label(screenregstud, text = "Registro concluido", fg = "green", font = ("Calibri", 12)).pack()

def register_student():
	global screenregstud
	screenreg.destroy()
	screenregstud = Tk()
	screenregstud.title("Registro Estudante")
	screenregstud.geometry("650x520+%d+%d" %(posx, posy))

	global username_student_entry
	global password_student_entry
	global cpf_student_entry
	global telefone_student_entry
	global nome_student_entry
	global graduacao_student_entry
	global arte_marcial_student_entry
	global idade_student_entry
	global sexo_student_entry

	Label(screenregstud, text = "Preencha os dados abaixo:").pack()
	Label(screenregstud, text = "").pack()

	Label(screenregstud, text = "Username * ").pack()
	username_student_entry = Entry(screenregstud, textvariable = username)
	username_student_entry.pack()
	Label(screenregstud, text = "Password * ").pack()
	password_student_entry = Entry(screenregstud, textvariable = password, show = "*")
	password_student_entry.pack()
	Label(screenregstud, text = "CPF * ").pack()
	cpf_student_entry = Entry(screenregstud, textvariable = cpf)
	cpf_student_entry.pack()
	Label(screenregstud, text = "Telefone * ").pack()
	telefone_student_entry = Entry(screenregstud, textvariable = telefone)
	telefone_student_entry.pack()
	Label(screenregstud, text = "Nome * ").pack()
	nome_student_entry = Entry(screenregstud, textvariable = nome)
	nome_student_entry.pack()
	Label(screenregstud, text = "Graduacao * ").pack()
	graduacao_student_entry = Entry(screenregstud, textvariable = graduacao)
	graduacao_student_entry.pack()
	Label(screenregstud, text = "Arte Marcial * ").pack()
	arte_marcial_student_entry = Entry(screenregstud, textvariable = arte_marcial)
	arte_marcial_student_entry.pack()
	Label(screenregstud, text = "Idade * ").pack()
	idade_student_entry = Entry(screenregstud, textvariable = idade)
	idade_student_entry.pack()
	Label(screenregstud, text = "Sexo * ").pack()
	sexo_student_entry = Entry(screenregstud, textvariable = sexo)
	sexo_student_entry.pack()

	Label(screenregstud, text = "").pack()
	Button(screenregstud, text = "Register", height = 1, command = cadastra_estudante_banco).pack()
	
	bvoltar = Button(screenregstud, text = "Voltar", command = lambda: changeWindow32(screenregstud))
	bvoltar.place(x=0, y=0)
	
	screenregstud.mainloop()


def cadastra_professor_banco():
	
	username_professor_entry.delete(0,END)
	password_professor_entry.delete(0, END)
	cpf_professor_entry.delete(0,END)
	telefone_professor_entry.delete(0,END)
	nome_professor_entry.delete(0,END)
	graduacao_professor_entry.delete(0,END)
	arte_marcial_professor_entry.delete(0,END)

	Label(screenregprof, text = "Registro concluido", fg = "green", font = ("Calibri", 12)).pack()


def register_professor():
	global screenregprof
	screenreg.destroy()
	screenregprof = Tk()
	screenregprof.title("Registro Professor")
	screenregprof.geometry("650x520+%d+%d" %(posx, posy))

	global username_professor_entry
	global password_professor_entry
	global cpf_professor_entry
	global telefone_professor_entry
	global nome_professor_entry
	global graduacao_professor_entry
	global arte_marcial_professor_entry

	Label(screenregprof, text = "Preencha os dados abaixo:").pack()
	Label(screenregprof, text = "").pack()

	Label(screenregprof, text = "Username * ").pack()
	username_professor_entry = Entry(screenregprof, textvariable = username)
	username_professor_entry.pack()
	Label(screenregprof, text = "Password * ").pack()
	password_professor_entry = Entry(screenregprof, textvariable = password, show = "*")
	password_professor_entry.pack()
	Label(screenregprof, text = "CPF * ").pack()
	cpf_professor_entry = Entry(screenregprof, textvariable = cpf)
	cpf_professor_entry.pack()
	Label(screenregprof, text = "Telefone * ").pack()
	telefone_professor_entry = Entry(screenregprof, textvariable = telefone)
	telefone_professor_entry.pack()
	Label(screenregprof, text = "Nome * ").pack()
	nome_professor_entry = Entry(screenregprof, textvariable = nome)
	nome_professor_entry.pack()
	Label(screenregprof, text = "Graduacao * ").pack()
	graduacao_professor_entry = Entry(screenregprof, textvariable = graduacao)
	graduacao_professor_entry.pack()
	Label(screenregprof, text = "Arte Marcial * ").pack()
	arte_marcial_professor_entry = Entry(screenregprof, textvariable = arte_marcial)
	arte_marcial_professor_entry.pack()
	
	
	Label(screenregprof, text = "").pack()
	Button(screenregprof, text = "Register", height = 1, command = cadastra_professor_banco).pack()
	
	bvoltar = Button(screenregprof, text = "Voltar", command = lambda: changeWindow32(screenregprof))
	bvoltar.place(x=0, y=0)
	
	screenregprof.mainloop()

def cadastra_supplier_banco():
	
	username_supplier_entry.delete(0,END)
	password_supplier_entry.delete(0, END)
	cpf_supplier_entry.delete(0,END)
	telefone_supplier_entry.delete(0,END)
	nome_supplier_entry.delete(0,END)
	

	Label(screenregsupp, text = "Registro concluido", fg = "green", font = ("Calibri", 12)).pack()	


def register_supplier():
	
	global screenregsupp
	screenreg.destroy()
	screenregsupp = Tk()
	screenregsupp.title("Registro Fornecedor")
	screenregsupp.geometry("650x520+%d+%d" %(posx, posy))

	global username_supplier_entry
	global password_supplier_entry
	global cpf_supplier_entry
	global telefone_supplier_entry
	global nome_supplier_entry
	

	Label(screenregsupp, text = "Preencha os dados abaixo:").pack()
	Label(screenregsupp, text = "").pack()

	Label(screenregsupp, text = "Username * ").pack()
	username_supplier_entry = Entry(screenregsupp, textvariable = username)
	username_supplier_entry.pack()
	Label(screenregsupp, text = "Password * ").pack()
	password_supplier_entry = Entry(screenregsupp, textvariable = password, show = "*")
	password_supplier_entry.pack()
	Label(screenregsupp, text = "CPF * ").pack()
	cpf_supplier_entry = Entry(screenregsupp, textvariable = cpf)
	cpf_supplier_entry.pack()
	Label(screenregsupp, text = "Telefone * ").pack()
	telefone_supplier_entry = Entry(screenregsupp, textvariable = telefone)
	telefone_supplier_entry.pack()
	Label(screenregsupp, text = "Nome * ").pack()
	nome_supplier_entry = Entry(screenregsupp, textvariable = nome)
	nome_supplier_entry.pack()
	

	Label(screenregsupp, text = "").pack()
	Button(screenregsupp, text = "Register", height = 1, command = cadastra_supplier_banco).pack()
	
	bvoltar = Button(screenregsupp, text = "Voltar", command = lambda: changeWindow32(screenregsupp))
	bvoltar.place(x=0, y=0)
	
	screenregsupp.mainloop()

def cadastra_owner_banco():

	username_owner_entry.delete(0,END)
	password_owner_entry.delete(0, END)
	cpf_owner_entry.delete(0,END)
	telefone_owner_entry.delete(0,END)
	nome_owner_entry.delete(0,END)
	
	Label(screenregowner, text = "Registro concluido", fg = "green", font = ("Calibri", 12)).pack()	



def register_owner():
	global screenregowner
	screenreg.destroy()
	screenregowner = Tk()
	screenregowner.title("Registro Locador")
	screenregowner.geometry("650x520+%d+%d" %(posx, posy))

	global username_owner_entry
	global password_owner_entry
	global cpf_owner_entry
	global telefone_owner_entry
	global nome_owner_entry
	
	Label(screenregowner, text = "Preencha os dados abaixo:").pack()
	Label(screenregowner, text = "").pack()

	Label(screenregowner, text = "Username * ").pack()
	username_owner_entry = Entry(screenregowner, textvariable = username)
	username_owner_entry.pack()
	Label(screenregowner, text = "Password * ").pack()
	password_owner_entry = Entry(screenregowner, textvariable = password, show = "*")
	password_owner_entry.pack()
	Label(screenregowner, text = "CPF * ").pack()
	cpf_owner_entry = Entry(screenregowner, textvariable = cpf)
	cpf_owner_entry.pack()
	Label(screenregowner, text = "Telefone * ").pack()
	telefone_owner_entry = Entry(screenregowner, textvariable = telefone)
	telefone_owner_entry.pack()
	Label(screenregowner, text = "Nome * ").pack()
	nome_owner_entry = Entry(screenregowner, textvariable = nome)
	nome_owner_entry.pack()
	

	Label(screenregowner, text = "").pack()
	Button(screenregowner, text = "Register", height = 1, command = cadastra_owner_banco).pack()
	
	
	bvoltar = Button(screenregowner, text = "Voltar", command = lambda: changeWindow32(screenregowner))
	bvoltar.place(x=0, y=0)
	
	screenregowner.mainloop()


def register():
	global screenreg

	screenreg = Tk()
	screenreg.title("Register")
	screenreg.geometry("650x520+%d+%d" %(posx, posy))

	Label(screenreg, text = "Escolha o tipo de cadastro:", font = ("Calibri", 16)).pack()
	Button(screenreg, text = "Aluno", width = 20, height = 4, command = register_student).pack()
	Button(screenreg, text = "Professor", width = 20, height = 4, command = register_professor).pack()
	Button(screenreg, text = "Fornecedor", width = 20, height = 4, command = register_supplier).pack()
	Button(screenreg, text = "Locador", width = 20, height = 4, command = register_owner).pack() 
	
	bvoltar = Button(screenreg, text = "Voltar", command = lambda: changeWindow21(screenreg))
	bvoltar.place(x=0, y=0)
	
	screenreg.mainloop()
	
	



def login():
	
	global screenlogin
	global username_verify
	global password_verify
	flag = [1]
	
	screenlogin = Tk()
	screenlogin.title("Login")
	screenlogin.geometry("650x520+%d+%d" %(posx, posy))

	Label(screenlogin, text = "Faca login com seus dados:").pack()
	Label(screenlogin, text = "").pack()

	Label(screenlogin, text = "Username * ").pack()
	username_verify = Entry(screenlogin, textvariable = username)
	username_verify.pack()
	Label(screenlogin, text = "Password * ").pack()
	password_verify = Entry(screenlogin, textvariable = password, show = "*")
	password_verify.pack()
	Label(screenlogin, text = "").pack() 
	Button(screenlogin, text = "Login", command = lambda: login_verify(flag)).pack()
	bvoltar = Button(screenlogin, text = "Voltar", command = lambda: changeWindow21(screenlogin))
	bvoltar.place(x=0, y=0)
	
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
	
	#lb = Label(text = "Luta Luta", bg = '#D2B48C', width = "300", height = "2", font = ("Times", 13)).pack()
	
	bt1 = Button(text = "Login", height = "2", relief = 'groove', bd=9, bg = '#D2B48C',	width = "20", command = lambda: changeWindow12_login(screen), font = ("Times", 13))
	bt2 = Button(text = "Register",height = "2", relief = 'groove', bd=9, bg ='#D2B48C', width = "20", command = lambda: changeWindow12_register(screen), font = ("Times", 13))
	bt1.config(highlightbackground='black')
	bt2.config(highlightbackground='black')
	
	bt1.place(relx=0.5, rely=0.4, anchor=CENTER)
	bt2.place(relx=0.5, rely=0.6, anchor=CENTER)
	
	screen.mainloop()

main_screen()

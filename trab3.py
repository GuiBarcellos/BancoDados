from tkinter import *

#INSIRA CODIGO BD AQUI



def login_verify():
	username1 = username_verify.get()
	password1 = password_verify.get()
	username_entry1.delete(0, END)
	password_entry1.delete(0, END)

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
	
	screenregowner.mainloop()


def register():
	global screenreg
	screen.destroy()
	screenreg = Tk()
	screenreg.title("Register")
	screenreg.geometry("650x520+%d+%d" %(posx, posy))

	Label(screenreg, text = "Escolha o tipo de cadastro:", font = ("Calibri", 16)).pack()
	Button(screenreg, text = "Aluno", width = 20, height = 4, command = register_student).pack()
	Button(screenreg, text = "Professor", width = 20, height = 4, command = register_professor).pack()
	Button(screenreg, text = "Fornecedor", width = 20, height = 4, command = register_supplier).pack()
	Button(screenreg, text = "Locador", width = 20, height = 4, command = register_owner).pack() 
	screenreg.mainloop()



def login():
	
	global screen2
	global username_verify
	global password_verify
	global username_entry1
	global password_entry1

	username_verify = StringVar()
	password_verify = StringVar()
	
	screen.destroy()	
	screen2 = Tk()
	screen2.title("Login")
	screen2.geometry("650x520+%d+%d" %(posx, posy))

	Label(screen2, text = "Faca login com seus dados:").pack()
	Label(screen2, text = "").pack()

	Label(screen2, text = "Username * ").pack()
	username_entry1 = Entry(screen2, textvariable = username_verify)
	username_entry1.pack()
	Label(screen2, text = "Password * ").pack()
	password_entry1 = Entry(screen2, textvariable = password_verify, show = "*")
	password_entry1.pack()
	Label(screen2, text = "").pack() 
	Button(screen2, text = "Login", command = login_verify).pack()

	username_entry.delete(0, END)
	password_entry.delete(0, END)
	
	screen2.mainloop()

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

	Label(text = "Luta Luta", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
	Label(text = "").pack()
	Button(text = "Login", height = "2", width = "30", command = login).pack()
	Label(text = "").pack()
	Button(text = "Register",height = "2", width = "30", command = register).pack()
	
	screen.mainloop()

main_screen()

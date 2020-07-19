from tkinter import *
from tkinter import ttk
import psycopg2


#CODIGO BANCO DE DADOS -------------------------------------------------------------------------------------------------------
#CODIGO BANCO DE DADOS -------------------------------------------------------------------------------------------------------
#CODIGO BANCO DE DADOS -------------------------------------------------------------------------------------------------------
#CODIGO BANCO DE DADOS -------------------------------------------------------------------------------------------------------


#Funcao que cadastra um usuario no banco de dados.
#O objetivo eh que essa funcao seja soh uma parte do programa principal
#@Parametros:
#	- db: a base de dados retornada da funcao connect()
#	- info: vetor com informacoes sobre a pessoa estruturado da seguinte forma:
#	info [0] | [1]  |  [2]  | [3]  |  [4]  |  [5]    | [6]    |  [7]
#		 CPF   user	  nome    tel    grad 	 arte m.   idade     Sexo
#   - operacao: 0: add aluno; 1: add prof, 2: add locador;
#Retorna 0 se deu certo, 1 se deu errado
def signup(db, info, operation):


	cursor = db.cursor()

	cursor.execute("""SELECT CPF FROM PESSOA WHERE USERNAME = """ + "'" + info[1] + "'" + ";")
	test = cursor.fetchone()

	if test != None:
		return 1

	cursor.execute("""SELECT USERNAME FROM PESSOA WHERE CPF = """ + "'" + info[0] + "'" + ";")
	test = cursor.fetchone()

	if test == None:
		cursor.execute("""INSERT INTO PESSOA (CPF, USERNAME, NOME, TELEFONE) VALUES """ 
		+ "(" + "'" + info[0] + "'" + ", " + "'" + info[1] + "'" + ", " + "'" + info[2] + "'" 
		+ ", " + "'" + info[3] + "'" + ");")


	#Aluno
	if operation == 0:
		cursor.execute("""INSERT INTO ALUNO (CPF, GRADUACAO, ARTE, ANO_NASC, SEXO) VALUES """ 
		+ "(" + "'" + info[0] + "'" + ", " + "'" + info[4] + "'" + ", " + "'" + info[5] + "'" 
		+ ", " + info[6] + ", " + "'" + info[7] + "'" + ");")
		cursor.execute("""INSERT INTO TIPO (CPF, TIPO) VALUES """ 
		+ "(" + "'" + info[0] + "'" + ", " + "'Aluno'" + ");")
		

	#Professor
	elif operation == 1:
		cursor.execute("""INSERT INTO PROFESSOR (CPF, GRADUACAO, ARTE) VALUES """ 
		+ "(" + "'" + info[0] + "'" + ", " + "'" + info[4] + "'" + ", " + "'" + info[5] + "'" + ");")
		cursor.execute("""INSERT INTO TIPO (CPF, TIPO) VALUES """ 
		+ "(" + "'" + info[0] + "'" + ", " + "'Professor'" + ");")

	#Locador
	elif operation == 2:
		cursor.execute("""INSERT INTO TIPO (CPF, TIPO) VALUES """ 
		+ "(" + "'" + info[0] + "'" + ", " + "'Locador'" + ");")

	return 0

#Funcao que cadastra um FORNECEDOR no banco de dados.
#O objetivo eh que essa funcao seja soh uma parte do programa principal
#@Parametros:
#	- db: a base de dados retornada da funcao connect()
#	- info: vetor com informacoes sobre a pessoa estruturado da seguinte forma:
#	info [0]  |  [1]  |  [2]  |  [3]  |  [4]  |  [5]    | [6]    |  [7]  |  [8]  |  [9]  | 
#		 CNPJ   nome	 user   tel1   tel2 	 rua      num      cep    estado   cidade
def signProvider(db, info):
	
	cursor = db.cursor()
	cursor.execute("""INSERT INTO FORNECEDOR (CNPJ, NOME, USERNAME, TELEFONE1, TELEFONE2, RUA, NUMERO, CEP, ESTADO, CIDADE) VALUES """ 
	+ "(" + "'" + info[0] + "'" + ", " + "'" + info[1] + "'" + ", " + "'" + info[2] + "'" 
	+ ", " + "'" + info[3] + "'" + ", " + "'" + info[4] + "'" + ", " + "'" + info[5] + "'"
	+ ", " + "'" + info[6] + "'" + ", " + "'" + info[7] + "'" + ", " + "'" + info[8] + "'" 
	+ ", " + "'" + info[9] + "'" + ");")

	print("Insertion made successfully")
	



#CODIGO BANCO DE DADOS -------------------------------------------------------------------------------------------------------
#CODIGO BANCO DE DADOS -------------------------------------------------------------------------------------------------------
#CODIGO BANCO DE DADOS -------------------------------------------------------------------------------------------------------
#CODIGO BANCO DE DADOS -------------------------------------------------------------------------------------------------------

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

def searchAll():
	
	cursor = con.cursor()

	cursor.execute("""SELECT PESSOA.NOME, ALUNO.CPF, ALUNO.ANO_NASC, ALUNO.ARTE, PESSOA.TELEFONE FROM ALUNO, PESSOA
						WHERE ALUNO.CPF = PESSOA.CPF;""")

	type = cursor.fetchall()
	
	records = student_table.get_children()
	for element in records:
		student_table.delete(element)

	for row in type:
		student_table.insert("", "end", values=(row[1], row[0], row[2], row[3], row[4]))

	print(type)

def searchByCpf(db, cpf):
	
	cursor = db.cursor()

	cursor.execute("""SELECT PESSOA.NOME, ALUNO.CPF, ALUNO.ANO_NASC, ALUNO.ARTE, PESSOA.TELEFONE FROM ALUNO, PESSOA
						WHERE ALUNO.CPF = PESSOA.CPF AND PESSOA.CPF = """ + "'" + cpf + "'" + ";")

	type = cursor.fetchall()

	records = student_table.get_children()
	for element in records:
		student_table.delete(element)

	for row in type:
		student_table.insert("", "end", values=(row[1], row[0], row[2], row[3], row[4]))

	print(type)

def searchByName(db, nome):
	
	cursor = db.cursor()

	cursor.execute("""SELECT PESSOA.NOME, ALUNO.CPF, ALUNO.ANO_NASC, ALUNO.ARTE, PESSOA.TELEFONE FROM ALUNO, PESSOA
						WHERE ALUNO.CPF = PESSOA.CPF AND UPPER(PESSOA.NOME) LIKE UPPER(""" + "'" + "%" + nome + "%" + "'" + ")" + ";")

	type = cursor.fetchall()

	records = student_table.get_children()
	for element in records:
		student_table.delete(element)

	for row in type:
		student_table.insert("", "end", values=(row[1], row[0], row[2], row[3], row[4]))

	

	print(type)

def search_cpf_nome():
	
	texto_busca = search_aluno_entry.get()
	option_search = clicked_busca_aluno.get()
	print(texto_busca)

	if option_search == "CPF":
		searchByCpf(con, texto_busca)

	elif option_search == "Nome":
		searchByName(con, texto_busca)

	

def busca_aluno():
	global screenbuscaaluno
	screenoptions.destroy()
	screenbuscaaluno = Tk()
	screenbuscaaluno.title("Busca por Aluno")
	screenbuscaaluno.geometry("850x720+%d+%d" %(posx, posy))
	screenbuscaaluno['bg'] = '#F5F5F5'

	lbl_search = Label(screenbuscaaluno, text = "Procurar por:", bg = '#F5F5F5',fg = "black", font = ("times nem roman", 15, "bold"))
	lbl_search.grid(row = 0, column = 0, pady = 10, padx = 10, sticky = "w")

	global clicked_busca_aluno
	global option_search

	clicked_busca_aluno = StringVar()
	
	clicked_busca_aluno.set("Nome")
	drop = OptionMenu(screenbuscaaluno, clicked_busca_aluno,  "Nome", "CPF")
	drop.place(relx = 0.21, rely = 0.015)
	#drop.grid(row = 0, column = 0, pady = 10, padx = 200)
	
	option_search = StringVar()
	

	global search_aluno_entry
	global texto_busca 

	texto_busca = StringVar() 

	search_aluno_entry = Entry(screenbuscaaluno, textvariable = texto_busca, width = 30)
	search_aluno_entry.place(relx = 0.35, rely = 0.025)


	searchbtt = Button(screenbuscaaluno, text = "Buscar", width = 5, command = search_cpf_nome).place(relx = 0.73, rely = 0.015)

	showbtt = Button(screenbuscaaluno, text = "Mostrar Tudo", width = 8, command = searchAll).place(relx = 0.85, rely = 0.015)

#Table Frame----------------------------
	global table_frame
	table_frame = Frame(screenbuscaaluno, bd = 4, relief = RIDGE, bg = "white")
	table_frame.place(x = 10, y = 100, width = 825, height = 600)	

	scroll_x = Scrollbar(table_frame, orient = HORIZONTAL)
	scroll_y = Scrollbar(table_frame, orient = VERTICAL)
	global student_table
	student_table = ttk.Treeview(table_frame, columns = ("Cpf","Nome", "Ano", "Arte Marcial", "Telefone"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
	scroll_x.pack(side = BOTTOM, fill = X)
	scroll_y.pack(side = RIGHT, fill = Y)
	scroll_x.config(command=student_table.xview)
	scroll_y.config(command=student_table.yview)
	student_table.heading("Cpf", text="CPF")
	student_table.heading("Nome", text="Nome")
	student_table.heading("Ano", text="Ano")
	student_table.heading("Arte Marcial", text="Arte Marcial")
	student_table.heading("Telefone", text="Telefone")
	student_table['show']='headings'
	student_table.column("Cpf", width=50)
	student_table.column("Nome", width=220)
	student_table.column("Ano", width=28)
	student_table.column("Arte Marcial", width=80)
	student_table.column("Telefone", width=70)
	student_table.pack(fill=BOTH, expand=1)



	screenbuscaaluno.mainloop()

def busca_professor():
	global screenbuscaprofessor
	screenoptions.destroy()
	screenbuscaprofessor = Tk()
	screenbuscaprofessor.title("Busca por Professor")
	screenbuscaprofessor.geometry("850x720+%d+%d" %(posx, posy))
	screenbuscaprofessor['bg'] = '#F5F5F5'

	lbl_search = Label(screenbuscaprofessor, text = "Qual arte marcial voce deseja praticar?:", bg = '#F5F5F5',fg = "black", font = ("times nem roman", 15, "bold"))
	lbl_search.grid(row = 0, column = 0, pady = 10, padx = 10, sticky = "w")



#Table Frame----------------------------
	global table_frame_professor
	table_frame_professor = Frame(screenbuscaprofessor, bd = 4, relief = RIDGE, bg = "white")
	table_frame_professor.place(x = 10, y = 100, width = 825, height = 600)	

	scroll_x = Scrollbar(table_frame_professor, orient = HORIZONTAL)
	scroll_y = Scrollbar(table_frame_professor, orient = VERTICAL)
	global professor_table
	professor_table = ttk.Treeview(table_frame_professor, columns = ("Nome", "Telefone", "Arte Marcial", "Graduacao"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
	scroll_x.pack(side = BOTTOM, fill = X)
	scroll_y.pack(side = RIGHT, fill = Y)
	scroll_x.config(command=professor_table.xview)
	scroll_y.config(command=professor_table.yview)
	professor_table.heading("Nome", text="Nome")
	professor_table.heading("Telefone", text="Telefone")
	professor_table.heading("Arte Marcial", text="Arte Marcial")
	professor_table.heading("Graduacao", text="Graduacao")
	professor_table['show']='headings'
	professor_table.column("Nome", width=220)
	professor_table.column("Telefone", width=70)
	professor_table.column("Arte Marcial", width=80)
	professor_table.column("Graduacao", width=70)
	professor_table.pack(fill=BOTH, expand=1)



	screenbuscaprofessor.mainloop()



def busca_arte_marcial():
	global screenbuscaartemarcial
	screenoptions.destroy()
	screenbuscaartemarcial = Tk()
	screenbuscaartemarcial.title("Busca por Arte Marcial")
	screenbuscaartemarcial.geometry("650x520+%d+%d" %(posx, posy))

	screenbuscaartemarcial.mainloop()



def tela_opcoes():
	global screenoptions

	screenlogin.destroy()
	screenoptions = Tk()
	screenoptions.title("Busca")
	screenoptions.geometry("650x520+%d+%d" %(posx, posy))
	screenoptions['bg'] = '#F5F5F5'
	
	lb1 = Label(screenoptions, text = "O que voce deseja buscar?", bg = '#F5F5F5', fg = "black", font = "Garamond")
	lb1.place(relx=0.5, rely=0.05, anchor=CENTER)
	
	bt1=Button(screenoptions, text = "Aluno",width = 20, height = 2, font = 'Garamond',  bd=5, bg = '#A9A9A9', command = busca_aluno)
	bt1.place(relx=0.5, rely=0.2, anchor=CENTER)
	
	bt2=Button(screenoptions, text = "Professor", width = 20, height = 2, font = 'Garamond',  bd=5, bg = '#A9A9A9', command = busca_professor)
	bt2.place(relx=0.5, rely=0.4, anchor=CENTER)
		
	bt4=Button(screenoptions, text = "Arte Marcial", width = 20, height = 2,  font = 'Garamond',  bd=5, bg = '#A9A9A9', command = busca_arte_marcial)
	bt4.place(relx=0.5, rely=0.6, anchor=CENTER)
	

	
	bsair = Button(screenoptions, text = "Sair", font = 'Garamond',  bd=5, bg = '#A9A9A9', command = lambda: changeWindowSair(screenoptions))
	bsair.place(x=0, y=0)
	
	bsair.config(highlightbackground='#F5F5F5')
	bt1.config(highlightbackground='#F5F5F5')
	bt2.config(highlightbackground='#F5F5F5')
	bt4.config(highlightbackground='#F5F5F5')
	
	screenoptions.mainloop()	


def login_verify(flag):	
	
	user_login = username_verify.get()
	password_login = password_verify.get()
	 
	if user_login != "": 
		print("Login Sucesso")
		tela_opcoes()
		
	else:
		if flag[-1] == 1:	
			lb1 = Label(screenlogin, text = "Credencias incorretas! Tente novamente", bg = '#F5F5F5', fg = "red", font = ("Garamond", 12))
			lb1.place(relx=0.5, rely=0.9, anchor=CENTER)

		username_verify.delete(0, END)
		password_verify.delete(0, END)
		flag.append(0)
	



def cadastra_estudante_banco():
	

	

	cpf = cpf_student_entry.get()
	usuario = username_student_entry.get()
	nome = nome_student_entry.get()
	telefone = telefone_student_entry.get()
	graduacao = graduacao_student_entry.get()
	arte_marcial = arte_marcial_student_entry.get()
	idade = idade_student_entry.get()
	sexo = clicked_sexo.get()

	if sexo == "Masculino":
		sexo = "M"
	else:
		sexo = "F"

	info = [cpf, usuario, nome, telefone, graduacao, arte_marcial, idade, sexo]

	signup(con, info, 0)

	username_student_entry.delete(0,END)
	password_student_entry.delete(0, END)
	cpf_student_entry.delete(0,END)
	telefone_student_entry.delete(0,END)
	nome_student_entry.delete(0,END)
	graduacao_student_entry.delete(0,END)
	arte_marcial_student_entry.delete(0,END)
	idade_student_entry.delete(0,END)
	


	lb1 = Label(screenregstud, text = "Registro concluido", bg = '#F5F5F5',fg = "green", font = ("Garamond", 12))
	lb1.place(relx=0.5, rely=0.95, anchor=CENTER)
	con.commit()

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
	

	lb1 = Label(screenregstud, text = "Preencha os dados abaixo", font = 'Garamond', bg = '#F5F5F5')
	lb1.place(relx=0.5, rely=0.05, anchor=CENTER)

	lb2 = Label(screenregstud, text = "Usuario * ", font = 'Garamond', bg = '#F5F5F5')
	username_student_entry = Entry(screenregstud, textvariable = username)
	lb2.place(relx=0.35, rely=0.17, anchor=CENTER)
	username_student_entry.place(relx=0.6, rely=0.17, anchor=CENTER)
	
	lb3 = Label(screenregstud, text = "Senha * ", font = 'Garamond', bg = '#F5F5F5')
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

	lb9 = Label(screenregstud, text = "Ano * ", font = 'Garamond', bg = '#F5F5F5')
	idade_student_entry = Entry(screenregstud, textvariable = idade)
	lb9.place(relx=0.35, rely=0.66, anchor=CENTER)
	idade_student_entry.place(relx=0.6, rely=0.66, anchor=CENTER)
	
	lb10 = Label(screenregstud, text = "Sexo * ", font = 'Garamond', bg = '#F5F5F5')
	lb10.place(relx=0.35, rely=0.73, anchor=CENTER)
	global clicked_sexo
	clicked_sexo = StringVar()
	clicked_sexo.set("Masculino")
	drop = OptionMenu(screenregstud, clicked_sexo, "Masculino", "Feminino")
	drop.place(relx = 0.5, rely = 0.70)	
	

	bt1 = Button(screenregstud, text = "Registro", height = 1, font = 'Garamond',  bd=5, bg = '#A9A9A9', command = cadastra_estudante_banco)
	bt1.config(highlightbackground='#F5F5F5')
	bt1.place(relx=0.5, rely=0.85, anchor=CENTER)
	
	bvoltar = Button(screenregstud, text = "Voltar", font = 'Garamond',  bd=5, bg = '#A9A9A9', command = lambda: changeWindow32(screenregstud))
	bvoltar.place(x=0, y=0)
	bvoltar.config(highlightbackground='#F5F5F5')
	
	screenregstud.mainloop()


def cadastra_professor_banco():


	cpf = cpf_professor_entry.get()
	usuario = username_professor_entry.get()
	nome = nome_professor_entry.get()
	telefone = telefone_professor_entry.get()
	graduacao = graduacao_professor_entry.get()
	arte_marcial = arte_marcial_professor_entry.get()

	info = [cpf, usuario, nome, telefone, graduacao, arte_marcial]

	signup(con, info, 1)
	
	username_professor_entry.delete(0,END)
	password_professor_entry.delete(0, END)
	cpf_professor_entry.delete(0,END)
	telefone_professor_entry.delete(0,END)
	nome_professor_entry.delete(0,END)
	graduacao_professor_entry.delete(0,END)
	arte_marcial_professor_entry.delete(0,END)

	lb1 = Label(screenregprof, text = "Registro concluido", bg = '#F5F5F5',fg = "green", font = ("Garamond", 12))
	lb1.place(relx=0.5, rely=0.95, anchor=CENTER)
	con.commit()


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

	lb2 = Label(screenregprof, text = "Usuario * ", font = 'Garamond', bg = '#F5F5F5')
	username_professor_entry = Entry(screenregprof, textvariable = username)
	lb2.place(relx=0.35, rely=0.15, anchor=CENTER)
	username_professor_entry.place(relx=0.6, rely=0.15, anchor=CENTER)
	
	lb3 = Label(screenregprof, text = "Senha * ", font = 'Garamond', bg = '#F5F5F5')
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
	
	bt1 = Button(screenregprof, text = "Registro",font = 'Garamond',  bd=5, bg = '#A9A9A9', height = 1, command = cadastra_professor_banco)
	bt1.place(relx=0.5, rely=0.85, anchor=CENTER)
	bt1.config(highlightbackground='#F5F5F5')
	
	bvoltar = Button(screenregprof, text = "Voltar", font = 'Garamond',  bd=5, bg = '#A9A9A9', command = lambda: changeWindow32(screenregprof))
	bvoltar.place(x=0, y=0)
	bvoltar.config(highlightbackground='#F5F5F5')	
	
	screenregprof.mainloop()

def cadastra_supplier_banco():


	usuario = username_supplier_entry.get()
	cnpj = cnpj_supplier_entry.get()
	telefone = telefone_supplier_entry.get()
	telefone2 = telefone2_supplier_entry.get()
	nome = nome_supplier_entry.get()
	rua = rua_supplier_entry.get()
	numero = numero_supplier_entry.get()
	cep = cep_supplier_entry.get()
	estado = estado_supplier_entry.get()
	cidade = cidade_supplier_entry.get()


	info = [cnpj, nome, usuario, telefone, telefone2, rua, numero, cep, estado, cidade]
	signProvider(con, info)



	username_supplier_entry.delete(0,END)
	password_supplier_entry.delete(0, END)
	cnpj_supplier_entry.delete(0,END)
	telefone_supplier_entry.delete(0,END)
	nome_supplier_entry.delete(0,END)
	telefone2_supplier_entry.delete(0,END)
	rua_supplier_entry.delete(0,END)
	numero_supplier_entry.delete(0,END)
	cep_supplier_entry.delete(0,END)
	estado_supplier_entry.delete(0,END)
	cidade_supplier_entry.delete(0,END)
	

	lb1 = Label(screenregsupp, bg = '#F5F5F5', text = "Registro concluido", fg = "green", font = ("Garamond", 12))
	lb1.place(relx=0.5, rely=0.9, anchor=CENTER)
	con.commit()
		


def register_supplier():
	
	global screenregsupp
	screenreg.destroy()
	screenregsupp = Tk()
	screenregsupp.title("Registro Fornecedor")
	screenregsupp.geometry("650x520+%d+%d" %(posx, posy))
	screenregsupp['bg'] = '#F5F5F5'
	
	global username_supplier_entry
	global password_supplier_entry
	global cnpj_supplier_entry
	global telefone_supplier_entry
	global nome_supplier_entry
	global telefone2_supplier_entry
	global rua_supplier_entry
	global numero_supplier_entry
	global cep_supplier_entry
	global estado_supplier_entry
	global cidade_supplier_entry
	
	lb1 = Label(screenregsupp, font = 'Garamond', text = "Preencha os dados abaixo", bg = '#F5F5F5')
	lb1.place(relx=0.5, rely=0.05, anchor=CENTER)

	lb2 = Label(screenregsupp, text = "Usuario * ",font = 'Garamond', bg = '#F5F5F5')
	username_supplier_entry = Entry(screenregsupp, textvariable = username)
	lb2.place(relx=0.35, rely=0.12, anchor=CENTER)
	username_supplier_entry.place(relx=0.6, rely=0.12, anchor=CENTER)
	
	lb3 = Label(screenregsupp, text = "Senha * ",font = 'Garamond', bg = '#F5F5F5')
	password_supplier_entry = Entry(screenregsupp, textvariable = password, show = "*")
	lb3.place(relx=0.35, rely=0.19, anchor=CENTER)
	password_supplier_entry.place(relx=0.6, rely=0.19, anchor=CENTER)
	
	lb4 = Label(screenregsupp, text = "CNPJ * ",font = 'Garamond', bg = '#F5F5F5')
	cnpj_supplier_entry = Entry(screenregsupp, textvariable = cnpj)
	lb4.place(relx=0.35, rely=0.26, anchor=CENTER)
	cnpj_supplier_entry.place(relx=0.6, rely=0.26, anchor=CENTER)
	
	lb5 = Label(screenregsupp, text = "Telefone * ",font = 'Garamond', bg = '#F5F5F5')
	telefone_supplier_entry = Entry(screenregsupp, textvariable = telefone)
	lb5.place(relx=0.35, rely=0.33, anchor=CENTER)
	telefone_supplier_entry.place(relx=0.6, rely=0.33, anchor=CENTER)

	lb6 = Label(screenregsupp, text = "Nome * ",font = 'Garamond', bg = '#F5F5F5')
	nome_supplier_entry = Entry(screenregsupp, textvariable = nome)
	lb6.place(relx=0.35, rely=0.40, anchor=CENTER)
	nome_supplier_entry.place(relx=0.6, rely=0.40, anchor=CENTER)

	lb7 = Label(screenregsupp, text = "Telefone 2 * ",font = 'Garamond', bg = '#F5F5F5')
	telefone2_supplier_entry = Entry(screenregsupp, textvariable = telefone2)
	lb7.place(relx=0.35, rely=0.47, anchor=CENTER)
	telefone2_supplier_entry.place(relx=0.6, rely=0.47, anchor=CENTER)

	lb8 = Label(screenregsupp, text = "Rua * ",font = 'Garamond', bg = '#F5F5F5')
	rua_supplier_entry = Entry(screenregsupp, textvariable = rua)
	lb8.place(relx=0.35, rely=0.54, anchor=CENTER)
	rua_supplier_entry.place(relx=0.6, rely=0.54, anchor=CENTER)

	lb9 = Label(screenregsupp, text = "Numero * ",font = 'Garamond', bg = '#F5F5F5')
	numero_supplier_entry = Entry(screenregsupp, textvariable = numero)
	lb9.place(relx=0.35, rely=0.61, anchor=CENTER)
	numero_supplier_entry.place(relx=0.6, rely=0.61, anchor=CENTER)

	lb10 = Label(screenregsupp, text = "CEP * ",font = 'Garamond', bg = '#F5F5F5')
	cep_supplier_entry = Entry(screenregsupp, textvariable = cep)
	lb10.place(relx=0.35, rely=0.68, anchor=CENTER)
	cep_supplier_entry.place(relx=0.6, rely=0.68, anchor=CENTER)

	lb11 = Label(screenregsupp, text = "Cidade * ",font = 'Garamond', bg = '#F5F5F5')
	cidade_supplier_entry = Entry(screenregsupp, textvariable = cidade)
	lb11.place(relx=0.35, rely=0.75, anchor=CENTER)
	cidade_supplier_entry.place(relx=0.6, rely=0.75, anchor=CENTER)

	lb12 = Label(screenregsupp, text = "Estado * ",font = 'Garamond', bg = '#F5F5F5')
	estado_supplier_entry = Entry(screenregsupp, textvariable = estado)
	lb12.place(relx=0.35, rely=0.82, anchor=CENTER)
	estado_supplier_entry.place(relx=0.6, rely=0.82, anchor=CENTER)
	
	bt1 = Button(screenregsupp, text = "Registro", font = 'Garamond',  bd=5, bg = '#A9A9A9', height = 1, command = cadastra_supplier_banco)
	bt1.place(relx=0.5, rely=0.90, anchor=CENTER)
	bt1.config(highlightbackground='#F5F5F5')
	
	bvoltar = Button(screenregsupp, text = "Voltar",font = 'Garamond',  bd=5, bg = '#A9A9A9', command = lambda: changeWindow32(screenregsupp))
	bvoltar.place(x=0, y=0)
	bvoltar.config(highlightbackground='#F5F5F5')	

	
	screenregsupp.mainloop()

def cadastra_owner_banco():


	cpf = et4.get()
	usuario = et2.get()
	nome = et6.get()
	telefone = et5.get()
	

	info = [cpf, usuario, nome, telefone]

	signup(con, info, 2)

	et2.delete(0,END)
	et3.delete(0,END)
	et4.delete(0,END)
	et5.delete(0,END)
	et6.delete(0,END)
	
	lb1 = Label(screenregowner, text = "Registro concluido", fg = "green", bg = '#F5F5F5', font = ("Garamond", 12))
	lb1.place(relx=0.5, rely=0.9, anchor=CENTER)
	con.commit()

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

	lb2 = Label(screenregowner, text = "Usuario * ", font = 'Garamond', bg = '#F5F5F5')
	et2 = Entry(screenregowner, textvariable = username)
	lb2.place(relx=0.35, rely=0.2, anchor=CENTER)
	et2.place(relx=0.6, rely=0.2, anchor=CENTER)
	
	lb3 = Label(screenregowner, text = "Senha * ", font = 'Garamond', bg = '#F5F5F5')
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
	et6 = Entry(screenregowner, textvariable = nome)
	lb6.place(relx=0.35, rely=0.6, anchor=CENTER)
	et6.place(relx=0.6, rely=0.6, anchor=CENTER)

	bt1 = Button(screenregowner, text = "Registro", height = 1, font = 'Garamond',  bd=5, bg = '#A9A9A9',command = cadastra_owner_banco)
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
	
	lb1 = Label(screenlogin, text = "Usuario * ", font = 'Garamond', bg='#F5F5F5')
	lb1.place(relx=0.5, rely=0.3, anchor=CENTER)
	et1 = username_verify = Entry(screenlogin, textvariable = username)
	et1.place(relx=0.5, rely=0.35, anchor=CENTER)
	
	lb2 = Label(screenlogin, text = "Senha * ", font = 'Garamond', bg='#F5F5F5')
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
	global cnpj #Fornecedor
	global telefone2 #Fornecedor
	global rua #Fornecedor
	global numero #Fornecedor
	global cep #Fornecedor
	global estado #Fornecedor
	global cidade #Fornecedor

	username = StringVar()
	password = StringVar()
	cpf = StringVar()
	telefone = StringVar()
	nome = StringVar()
	graduacao = StringVar()
	arte_marcial = StringVar()
	sexo = StringVar()
	idade = StringVar()
	cnpj = StringVar()
	telefone2 = StringVar()
	rua = StringVar()
	numero = StringVar()
	cep = StringVar()
	estado = StringVar()
	cidade = StringVar()
	
	img = PhotoImage(file="img-1.png")
	lb_image = Label(screen, image=img)
	lb_image.place(x=0, y=0, relwidth=1.0, relheight=1.0)
	
	#lb = Label(text = "Luta Luta", bg = '#D2B48C', width = "300", height = "2", font = ("Garamond", 13)).pack()
	
	bt1 = Button(text = "Login", height = "2", relief = 'groove', bd=9, bg = '#D2B48C',	width = "20", command = lambda: changeWindow12_login(screen), font = ("Garamond", 13))
	bt2 = Button(text = "Registro",height = "2", relief = 'groove', bd=9, bg ='#D2B48C', width = "20", command = lambda: changeWindow12_register(screen), font = ("Garamond", 13))
	bt1.config(highlightbackground='black')
	bt2.config(highlightbackground='black')
	
	bt1.place(relx=0.5, rely=0.4, anchor=CENTER)
	bt2.place(relx=0.5, rely=0.6, anchor=CENTER)
	

	screen.mainloop()


con = psycopg2.connect(database="BancoDados", user="gui", password="123", host="127.0.0.1", port="5432")
print("Database opened successfully")


main_screen()
con.close()
print("Database foi fechada")

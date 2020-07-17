import psycopg2

#Funcao que cadastra um usuario no banco de dados.
#O objetivo eh que essa funcao seja soh uma parte do programa principal
#@Parametros:
#	- db: a base de dados retornada da funcao connect()
#	- info: vetor com informacoes sobre a pessoa estruturado da seguinte forma:
#	info [0] | [1]  |  [2]  | [3]  |  [4]  |  [5]    | [6]    |  [7]
#		 CPF   user	  nome    tel    grad 	 arte m.   idade     Sexo
#   - operacao: 0: add aluno; 1: add prof, 2: add locador;
#Nota: Apesar de nao ser tratado como pessoa, o fornecedor eh adicionado 
#por essa funcao pois possui muitos atributos em comum, so nao deve ser 
#colocado na tabela pessoa
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
		cursor.execute("""INSERT INTO ALUNO (CPF, GRADUACAO, ARTE, IDADE, SEXO) VALUES """ 
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
	pass

#
#Projeto do programa principal somente para testes
#
con = psycopg2.connect(database="mateus", user="mateus", password="mateus", host="127.0.0.1", port="5432")
print("Database opened successfully")

#info = ["41828381828", "@lucao", "Lucas", "11924232222", "Preta", "Judo", "20", "M"]

#signup(con, info, 1)

#info = ["41828381828", "@lucao", "Lucas", "11924232222", "Branca", "Karate", "20", "M"]
#info = ["48120029153", "@gabriel", "Gabriel", "11224532521", "Branca", "Muay-Thai", "19", "M"]
info = ["48120029153", "@gabriel", "Gabriel", "11324231521", "Preta", "Taekwondo", "19", "M"]

signup(con, info, 1)

#info = ["45865482648545", "Tech Insertion", "techins", "11924132222", "11923131242", "Rasmussen de Andrade", "13", "19203010", "SP", "Sao Jose do Rio Preto"]

#signProvider(con, info)

con.commit()
con.close()
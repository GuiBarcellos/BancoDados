import psycopg2

#Funcao que cadastra um usuario no banco de dados,
#agora, como a estrutura das tabelas completamente montada,
#essa funcao nao funciona mais. E necessario inserir o aluno
#na tabela pessoas e na aluno, assim como todas as pessoas
#
#o objetivo eh que essa funcao seja soh uma parte do programa principal
#@Parametros:
#	- db: a base de dados retornada da funcao connect()
#	- info: vetor com informacoes sobre a pessoa estruturado da seguinte forma:
#	info [0] | [1]  |  [2]  | [3]  |  [4]  |  [5]    | [6]    |  [7]
#		 CPF   user	  nome    tel    grad 	 arte m.   idade     Sexo
#   - operacao: 0: add aluno; 1: add prof; 2: add fornecedor; 3: add locatario
#Nota: Apesar de nao ser tratado como pessoa, o fornecedor eh adicionado 
#por essa funcao pois possui muitos atributos em comum, so nao deve ser 
#colocado na tabela pessoa
def signup(db, info, operation):

	#Aluno
	if operation == 0:
		cursor = db.cursor()
		cursor.execute("""INSERT INTO ALUNO (CPF, USERNAME, NOME, TELEFONE, GRADUACAO, ARTE, IDADE, SEXO) VALUES """ 
		+ "(" + "'" + info[0] + "'" + ", " + "'" + info[1] + "'" + ", " + "'" + info[2] + "'" + ", " + "'" + info[3] + "'" + ", " + "'" + info[4] + "'" + ", "
		+ "'" + info[5] + "'" + ", " + "'" + info[6] + "'" + ", " + "'" + info[7] + "'" + ")")
		print("Insertion made successfully")

	#Professor
	elif operation == 1:
		print("a")
	#Fornecedor
	elif operation == 2:
		print("n")
	#Locador
	else:
		print("b")
	pass


#
#Projeto do programa principal somente para testes
#
con = psycopg2.connect(database="mateus", user="mateus", password="mateus", host="127.0.0.1", port="5432")
print("Database opened successfully")

info = ["21822281892", "@asdij", "Pedrao", "19922222222", "Branca", "Judo", "13", "M"]

signup(con, info, 0)

con.commit()
con.close()
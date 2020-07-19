import psycopg2

def searchByArtMonth(db, art, month):

	cursor = db.cursor()

	command = """SELECT CODIGO AS TURMA, N_ALUNOS, CIDADE, ARTE, EXTRACT(MONTH FROM DATA) AS MES FROM TURMA, TREINO, PROPORCIONA, IMOVEL 
						WHERE CODIGO = CODIGO_TURMA AND
						CODIGO_TURMA = TREINO_CODIGO AND
						DATA = TREINO_DATA AND
						PROPORCIONA.IMOVEL = IMOVEL.ID AND
						UPPER(ARTE) = """ + "UPPER(" + "'" + art + "'" + ")"

	if month != '-1':
		command += "AND EXTRACT(MONTH FROM DATA) = " + "'" + month + "'"


	cursor.execute(command)
	type = cursor.fetchall()
	print(type)


def searchAll(db):
	
	cursor = db.cursor()

	cursor.execute("""SELECT PESSOA.NOME, ALUNO.CPF, ALUNO.IDADE, ALUNO.ARTE, PESSOA.TELEFONE FROM ALUNO, PESSOA
						WHERE ALUNO.CPF = PESSOA.CPF;""")

	type = cursor.fetchall()

	print(type)


def searchByCpf(db, cpf):
	
	cursor = db.cursor()

	cursor.execute("""SELECT PESSOA.NOME, ALUNO.CPF, ALUNO.IDADE, ALUNO.ARTE, PESSOA.TELEFONE FROM ALUNO, PESSOA
						WHERE ALUNO.CPF = PESSOA.CPF AND PESSOA.CPF = """ + "'" + cpf + "'" + ";")

	type = cursor.fetchall()

	print(type)



def searchByName(db, nome):
	
	cursor = db.cursor()

	cursor.execute("""SELECT PESSOA.NOME, ALUNO.CPF, ALUNO.IDADE, ALUNO.ARTE, PESSOA.TELEFONE FROM ALUNO, PESSOA
						WHERE ALUNO.CPF = PESSOA.CPF AND UPPER(PESSOA.NOME) LIKE UPPER(""" + "'" + nome + "%" + "'" + ")" + ";")

	type = cursor.fetchall()


	print(type)


con = psycopg2.connect(database="mateus", user="mateus", password="mateus", host="127.0.0.1", port="5432")
print("Database opened successfully")

arte = input()


searchByArtMonth(con, arte, '3')
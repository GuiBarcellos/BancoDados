/*
Seleciona o nome de usuario de todos os alunos,
pode ter a funcao de buscar pelo nome de usuario
de um deles
*/
SELECT NOME, USERNAME FROM PESSOA P, ALUNO A
WHERE P.CPF = A.CPF;

/*
Seleciona todos os imoveis cadastrados no aplicativo
disponiveis ou nao para locacao, associados ao nome e
telefone dos locadores
*/
SELECT P.NOME, P.TELEFONE, T.CPF, I.RUA, I.NUMERO, I.ESTADO, I.CIDADE FROM IMOVEL I, TIPO T, PESSOA P
WHERE I.LOCADOR = T.CPF AND UPPER(T.TIPO) = 'LOCADOR' AND P.CPF = T.CPF;

/*
Seleciona para quantos alunos cada professor deu aula
em todo o periodo, pode ter a funcao de verificar 
a experiencia do professor
*/
SELECT A.NOME, COUNT(B.NOME) AS NUMERO_ALUNOS FROM PESSOA A, PESSOA B
WHERE (A.CPF, B.CPF) IN (SELECT PROFESSOR, ALUNO FROM TURMA, PROPORCIONA, TREINO, COMPOE, ALUNO
							WHERE TREINO.CODIGO_TURMA = PROPORCIONA.TREINO_CODIGO AND 
							PROPORCIONA.TREINO_DATA = TREINO.DATA AND
							TREINO.CODIGO_TURMA = TURMA.CODIGO AND
							COMPOE.TURMA = TURMA.CODIGO AND
							COMPOE.ALUNO = ALUNO.CPF)
							GROUP BY A.NOME;
							
/*
Seleciona o estado e a quantidade de todos os produtos
*/
SELECT P.ESTADO, COUNT(P.ESTADO) AS QUANTIDADE FROM PRODUTO P, FORNECEDOR F
	WHERE F.CNPJ = P.FORNECEDOR
	GROUP BY P.ESTADO;
	
/*
Seleciona a idade media das turmas, pode auxiliar na 
alocacao de um aluno para as turmas
*/
SELECT CODIGO, N_ALUNOS, AVG(IDADE) AS MEDIA FROM TURMA T, COMPOE C, ALUNO A
	WHERE A.CPF = C.ALUNO AND C.TURMA = T.CODIGO
	GROUP BY CODIGO
	ORDER BY N_ALUNOS;


/*
Seleciona o numero de pessoas em diferentes graduacoes
pode ajudar a alocar os alunos de acordo com 
os niveis de cada turma, separando entre categorias
como basico e avancado

TESTAR
*/
SELECT C.TURMA, A.GRADUACAO, COUNT(A.GRADUACAO), P.NOME FROM ALUNO A
	JOIN COMPOE C ON A.CPF = C.ALUNO
	JOIN PESSOA P ON A.CPF = P.CPF
	GROUP BY C.TURMA, A.GRADUACAO, P.NOME
	ORDER BY C.TURMA;


/*
Seleciona diversas informacoes sobre os alunos que treinaram
em um determinado ano, nesse caso, 2008.
Funcionando para uma possivel consulta no historico
*/
SELECT P.NOME, P.CPF, A.SEXO, P.USERNAME FROM ALUNO A, PESSOA P
	WHERE A.CPF NOT IN (SELECT A.CPF FROM TREINO T, ALUNO A, COMPOE C
						 WHERE EXTRACT(YEAR FROM DATA) = '2008'
						 AND A.CPF = C.ALUNO
						 AND T.CODIGO_TURMA = C.TURMA) AND A.CPF = P.CPF;


/*
Seleciona todos os alunos que treinaram com todos os
professores de uma determinada arte marcial, nesse caso,
karate
*/
SELECT NOME, A1.CPF, A1.GRADUACAO, A1.ARTE, A1.IDADE, A1.SEXO FROM ALUNO A1, PESSOA
WHERE NOT EXISTS
	((SELECT DISTINCT PROFESSOR FROM PROPORCIONA, TREINO
	 WHERE TREINO.CODIGO_TURMA = PROPORCIONA.TREINO_CODIGO AND TREINO.DATA = PROPORCIONA.TREINO_DATA
	 AND UPPER(TREINO.ARTE) = 'KARATE')
	EXCEPT
	SELECT PROFESSOR FROM TREINO, PROPORCIONA, ALUNO, COMPOE, TURMA
		WHERE TREINO.CODIGO_TURMA = PROPORCIONA.TREINO_CODIGO AND TREINO.DATA = PROPORCIONA.TREINO_DATA AND
		TURMA.CODIGO = TREINO.CODIGO_TURMA AND
		TURMA.CODIGO = COMPOE.TURMA AND
		ALUNO.CPF = COMPOE.ALUNO AND
		(TREINO.ARTE, DATA) IN (SELECT TREINO.ARTE, DATA FROM TURMA, PROPORCIONA, TREINO, COMPOE, ALUNO
								WHERE TREINO.CODIGO_TURMA = PROPORCIONA.TREINO_CODIGO AND 
								PROPORCIONA.TREINO_DATA = TREINO.DATA AND
								TREINO.CODIGO_TURMA = TURMA.CODIGO AND
								COMPOE.TURMA = TURMA.CODIGO AND
								COMPOE.ALUNO = ALUNO.CPF) AND ALUNO.CPF = A1.CPF)
AND PESSOA.CPF = A1.CPF
						 
						 
/*
Seleciona todos os treinos que cada um dos alunos participou,
inclusive com as datas. Pode servir para avaliar se um aluno esta
ou nao indo com frequencia nos treinos
*/
SELECT ALUNO.CPF, TREINO.ARTE, DATA FROM TURMA, PROPORCIONA, TREINO, COMPOE, ALUNO
							WHERE TREINO.CODIGO_TURMA = PROPORCIONA.TREINO_CODIGO AND 
							PROPORCIONA.TREINO_DATA = TREINO.DATA AND
							TREINO.CODIGO_TURMA = TURMA.CODIGO AND
							COMPOE.TURMA = TURMA.CODIGO AND
							COMPOE.ALUNO = ALUNO.CPF;
							
							
/*
Seleciona quanto foi pago de cada aluno para
cada professor
*/		
SELECT ALUNO, PROFESSOR, VALOR FROM COBRANCA
	JOIN PAGAMENTO ON COBRANCA.PAGAMENTO = PAGAMENTO.N_BOLETO;


/*
Seleciona turmas e seus alunos
*/
SELECT ALUNO, TURMA FROM COMPOE
	JOIN ALUNO ON COMPOE.ALUNO = ALUNO.CPF;


/*
Seleciona o local onde sao realizados os treinos de todas as
artes marciais, util para encontrar um local para treinar
*/
SELECT DISTINCT CEP, ESTADO, NUMERO, ARTE FROM TREINO, PROPORCIONA, IMOVEL
	WHERE TREINO.CODIGO_TURMA = PROPORCIONA.TREINO_CODIGO AND 
		  PROPORCIONA.TREINO_DATA = TREINO.DATA AND
		  PROPORCIONA.IMOVEL = IMOVEL.ID;



/*
Verifica quais professores gastaram mais de 100 reais em produtos,
permitindo um controle de gastos
*/
SELECT PROFESSOR, AVG(CUSTO) AS MEDIA_GASTO FROM COMPRA C
	JOIN PRODUTO P ON P.CODIGO = C.PRODUTO
	GROUP BY PROFESSOR
	HAVING AVG(CUSTO) >= 100;
	

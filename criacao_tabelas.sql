CREATE TABLE PESSOA(
	
		CPF VARCHAR(11) PRIMARY KEY,
		USERNAME VARCHAR(40) UNIQUE NOT NULL,
		NOME VARCHAR(130) NOT NULL,
		TELEFONE VARCHAR(11) NOT NULL

);


CREATE TABLE ALUNO(
		
		CPF VARCHAR(11) PRIMARY KEY,
		GRADUACAO VARCHAR(30),
		ARTE VARCHAR(30) NOT NULL,
		ANO_NASC INT,
		SEXO VARCHAR(1) NOT NULL,
		CONSTRAINT FK_CPF FOREIGN KEY(CPF) REFERENCES PESSOA(CPF) ON DELETE CASCADE

);

CREATE TABLE PROFESSOR(
		
		CPF VARCHAR(11) PRIMARY KEY,
		GRADUACAO VARCHAR(30) NOT NULL,
		ARTE VARCHAR(30) NOT NULL,
		CONSTRAINT FK_CPF FOREIGN KEY(CPF) REFERENCES PESSOA(CPF) ON DELETE CASCADE
	
);

CREATE TABLE IMOVEL(

		ID SERIAL PRIMARY KEY,
		RUA VARCHAR(200) NOT NULL,
		NUMERO INT NOT NULL,
		CEP VARCHAR(8) NOT NULL,
		ESTADO VARCHAR(2) NOT NULL,
		CIDADE VARCHAR(100) NOT NULL,
		TAMANHO FLOAT,
		ABERTURA VARCHAR(1),
		JA_UTILIZADO VARCHAR(1),
		LOCADOR VARCHAR(11) NOT NULL,
		VALOR_HORA FLOAT,
		CONSTRAINT CK_ABERTURA CHECK(UPPER(ABERTURA) IN('S', 'N')),
		CONSTRAINT CK_UTILIZADO CHECK(UPPER(JA_UTILIZADO) IN('S', 'N')),
		CONSTRAINT FK_LOCADOR FOREIGN KEY(LOCADOR) REFERENCES PESSOA(CPF) ON DELETE CASCADE,
		CONSTRAINT UN_ENDERECO UNIQUE(RUA, NUMERO, CEP, ESTADO, CIDADE)
);


CREATE TABLE TIPO(

		CPF VARCHAR(11),
		TIPO VARCHAR(10),
		CONSTRAINT PK_TIPO PRIMARY KEY(CPF, TIPO),
		CONSTRAINT FK_CPF FOREIGN KEY(CPF) REFERENCES PESSOA(CPF) ON DELETE CASCADE,
		CONSTRAINT CK_TIPO CHECK(UPPER(TIPO) IN ('ALUNO', 'PROFESSOR', 'LOCADOR'))
	
);

CREATE TABLE PAGAMENTO(
		
		N_BOLETO SERIAL PRIMARY KEY,
		METODO VARCHAR(30),
		VALOR FLOAT NOT NULL
	
);

CREATE TABLE COBRANCA(

		PROFESSOR VARCHAR(11) NOT NULL,
		ALUNO VARCHAR(11) NOT NULL,
		PAGAMENTO INT NOT NULL,
		CONSTRAINT FK_PAGAMENTO FOREIGN KEY(PAGAMENTO) REFERENCES PAGAMENTO(N_BOLETO) ON DELETE CASCADE,
		CONSTRAINT FK_PROFESSOR FOREIGN KEY(PROFESSOR) REFERENCES PROFESSOR(CPF) ON DELETE CASCADE,
		CONSTRAINT FK_ALUNO FOREIGN KEY(ALUNO) REFERENCES ALUNO(CPF) ON DELETE CASCADE
	
);

CREATE TABLE FORNECEDOR(
		
		CNPJ VARCHAR(14) PRIMARY KEY,
		NOME VARCHAR(130) NOT NULL,
		USERNAME VARCHAR(40) UNIQUE,
		TELEFONE1 VARCHAR(11) NOT NULL,
		TELEFONE2 VARCHAR(11),
		RUA VARCHAR(200) NOT NULL,
		NUMERO INT NOT NULL,
		CEP VARCHAR(8) NOT NULL,
		ESTADO VARCHAR(30) NOT NULL,
		CIDADE VARCHAR(100) NOT NULL,
		CONSTRAINT UN_ENDERECO UNIQUE(RUA, NUMERO, CEP, ESTADO, CIDADE)

);

CREATE TABLE PRODUTO(
		
		CODIGO SERIAL PRIMARY KEY,
		FORNECEDOR VARCHAR(14) NOT NULL,
		CATEGORIA VARCHAR(15) NOT NULL,
		CUSTO FLOAT NOT NULL,
		ESTADO VARCHAR(20) NOT NULL,
		MARCA VARCHAR(50),
		TAMANHO VARCHAR(1) NOT NULL,
		TIPO VARCHAR(11),
		CONSTRAINT FK_PRODUTO FOREIGN KEY(FORNECEDOR) REFERENCES FORNECEDOR(CNPJ) ON DELETE CASCADE,
		CONSTRAINT CK_CATEGORIA CHECK(UPPER(CATEGORIA) IN ('PROTETOR', 'KIMONO', 'LUVA', 'CAMISETA', 'COLCHONETE', 'TATAME', 'SACO DE PANCADA', 'CALÇAS')),
		CONSTRAINT CK_TIPO CHECK(UPPER(TIPO) IN ('MUNHEQUEIRA', 'CANELEIRA', 'CAPACETE', 'BUCAL', 'JOELHEIRA', 'COTOVELEIRA'))
);


CREATE TABLE COMPRA(
	
		PROFESSOR VARCHAR(11),
		PRODUTO INT,
		CONSTRAINT PK_COMPRA PRIMARY KEY(PROFESSOR, PRODUTO),
		CONSTRAINT FK_PROFESSOR FOREIGN KEY(PROFESSOR) REFERENCES PROFESSOR(CPF) ON DELETE CASCADE,
		CONSTRAINT FK_PRODUTO FOREIGN KEY(PRODUTO) REFERENCES PRODUTO(CODIGO) ON DELETE CASCADE

);

CREATE TABLE TURMA(
		
		CODIGO SERIAL PRIMARY KEY,
		N_ALUNOS INT NOT NULL
		
);


CREATE TABLE COMPOE(
	
		ALUNO VARCHAR(11),
		TURMA INT,
		CONSTRAINT PK_COMPOE PRIMARY KEY(ALUNO, TURMA),
		CONSTRAINT FK_ALUNO FOREIGN KEY(ALUNO) REFERENCES ALUNO(CPF) ON DELETE CASCADE,
		CONSTRAINT FK_TURMA FOREIGN KEY(TURMA) REFERENCES TURMA(CODIGO) ON DELETE CASCADE

);

CREATE TABLE TREINO(
	
		CODIGO_TURMA INT,
		DATA DATE,
		ARTE VARCHAR(30),
		CONSTRAINT PK_TREINO PRIMARY KEY(CODIGO_TURMA, DATA),
		CONSTRAINT FK_TREINO FOREIGN KEY(CODIGO_TURMA) REFERENCES TURMA(CODIGO) ON DELETE CASCADE
	
);

CREATE TABLE PROPORCIONA(

		TREINO_CODIGO INT,
		TREINO_DATA DATE,
		PROFESSOR VARCHAR(11) NOT NULL,
		IMOVEL INT NOT NULL,
		CONSTRAINT PK_PROPORCIONA PRIMARY KEY(TREINO_CODIGO, TREINO_DATA),
		CONSTRAINT FK_PROPORCIONA FOREIGN KEY(TREINO_CODIGO, TREINO_DATA) REFERENCES TREINO(CODIGO_TURMA, DATA) ON DELETE CASCADE,
		CONSTRAINT FK_PROFESSOR FOREIGN KEY(PROFESSOR) REFERENCES PROFESSOR(CPF) ON DELETE CASCADE,
		CONSTRAINT FK_IMOVEL FOREIGN KEY(IMOVEL) REFERENCES IMOVEL(ID) ON DELETE CASCADE
);
INSERT INTO PESSOA VALUES ('41020010294', '@mateusfgomes', 'Mateus Ferreira Gomes', '18912220102');
INSERT INTO PESSOA VALUES ('71892991930', '@jaoramos', 'Joao Vitor Silva Ramos', '11992421223');
INSERT INTO PESSOA VALUES ('39193002939', '@igortakeo', 'Igor Takeo Ambo de Melo', '29993992919');
INSERT INTO PESSOA VALUES ('92910203028', '@barcellos', 'Guilherme Targon Marques Barcellos', '18993292115');
INSERT INTO PESSOA VALUES ('83910293929', '@lusmoura', 'Luisa Souza Moura', '77993211248');
INSERT INTO PESSOA VALUES ('91238812898', '@afonso', 'Afonso Matheus', '91993492011');
INSERT INTO PESSOA VALUES ('57193891930', '@moris', 'Felipe Moreira Neves de Souza', '16943432141');
INSERT INTO PESSOA VALUES ('48193010293', '@brumunizz', 'Bruna Migliorini Muniz', '18996226216');
INSERT INTO PESSOA VALUES ('82903919381', '@nina', 'Marina Machado', '17995198456');
INSERT INTO PESSOA VALUES ('78491399183', '@deividi', 'David Cairuz da Silva', '13991198551');
INSERT INTO PESSOA VALUES ('19419391939', '@joaogui1', 'Joao Guilherme Madeira Araujo', '19913093939');


INSERT INTO ALUNO VALUES ('71892991930', 'Verde', 'Taekwondo', 19, 'M');
INSERT INTO ALUNO VALUES ('39193002939', 'Azul', 'Karate', 20, 'M');
INSERT INTO ALUNO VALUES ('92910203028', 'Cinza', 'Jiu Jitsu', 22, 'M');
INSERT INTO ALUNO VALUES ('83910293929', 'Amarela', 'Kung Fu', 20, 'F');
INSERT INTO ALUNO VALUES ('91238812898', 'Branca', 'Kung Fu', 22, 'M');
INSERT INTO ALUNO VALUES ('82903919381', 'Branca', 'Judo', 19, 'F');
INSERT INTO ALUNO VALUES ('48193010293', 'Preta', 'Karate', 19, 'F');
INSERT INTO ALUNO VALUES ('19419391939', 'Vermelha', 'Karate', 20, 'M');



INSERT INTO PROFESSOR VALUES ('91238812898', 'Preta', 'Karate');
INSERT INTO PROFESSOR VALUES ('41020010294', 'Marrom', 'Karate');
INSERT INTO PROFESSOR VALUES ('92910203028', 'Preta', 'Kung Fu');
INSERT INTO PROFESSOR VALUES ('78491399183', 'Preta', 'Judo');
INSERT INTO PROFESSOR VALUES ('57193891930', 'Preta', 'Jiu Jitsu');

ALTER SEQUENCE IMOVEL_ID_SEQ RESTART WITH 1; --Reseta o contador do serial

INSERT INTO IMOVEL (RUA, NUMERO, CEP, ESTADO, CIDADE, TAMANHO, ABERTURA, JA_UTILIZADO, LOCADOR) VALUES ('Rua Um', 901, '19292012', 'SP', 'Franca', 102.1, 'N', 'N', '57193891930');
INSERT INTO IMOVEL (RUA, NUMERO, CEP, ESTADO, CIDADE, TAMANHO, ABERTURA, JA_UTILIZADO, LOCADOR) VALUES ('Rua Sete', 13, '19292013', 'MG', 'Uberaba', 131.3, 'S', 'N', '92910203028');
INSERT INTO IMOVEL (RUA, NUMERO, CEP, ESTADO, CIDADE, TAMANHO, ABERTURA, JA_UTILIZADO, LOCADOR) VALUES ('Rua Anibaldo de Moraes', 343, '13810293', 'AP', 'Macapa', 931.3, 'N', 'S', '92910203028');
INSERT INTO IMOVEL (RUA, NUMERO, CEP, ESTADO, CIDADE, TAMANHO, ABERTURA, JA_UTILIZADO, LOCADOR) VALUES ('Rua Tunisio de Freitas', 1333, '14814213', 'CE', 'Fortaleza', 200.3, 'N', 'S', '41020010294');

INSERT INTO TIPO VALUES ('71892991930', 'Aluno');
INSERT INTO TIPO VALUES ('39193002939', 'Aluno');
INSERT INTO TIPO VALUES ('92910203028', 'Aluno');
INSERT INTO TIPO VALUES ('83910293929', 'Aluno');
INSERT INTO TIPO VALUES ('91238812898', 'Aluno');
INSERT INTO TIPO VALUES ('82903919381', 'Aluno');
INSERT INTO TIPO VALUES ('48193010293', 'Aluno');
INSERT INTO TIPO VALUES ('19419391939', 'Aluno');
INSERT INTO TIPO VALUES ('91238812898', 'Professor');
INSERT INTO TIPO VALUES ('41020010294', 'Professor');
INSERT INTO TIPO VALUES ('92910203028', 'Professor');
INSERT INTO TIPO VALUES ('78491399183', 'Professor');
INSERT INTO TIPO VALUES ('57193891930', 'Locador');
INSERT INTO TIPO VALUES ('92910203028', 'Locador');
INSERT INTO TIPO VALUES ('41020010294', 'Locador');

ALTER SEQUENCE TURMA_CODIGO_SEQ RESTART WITH 1; --Reseta o contador do serial

INSERT INTO TURMA (N_ALUNOS) VALUES (2);
INSERT INTO TURMA (N_ALUNOS) VALUES (3);
INSERT INTO TURMA (N_ALUNOS) VALUES (1);
INSERT INTO TURMA (N_ALUNOS) VALUES (1);


INSERT INTO COMPOE VALUES ('83910293929', 1);
INSERT INTO COMPOE VALUES ('91238812898', 1);
INSERT INTO COMPOE VALUES ('71892991930', 2);
INSERT INTO COMPOE VALUES ('48193010293', 2);
INSERT INTO COMPOE VALUES ('19419391939', 2);
INSERT INTO COMPOE VALUES ('82903919381', 3);
INSERT INTO COMPOE VALUES ('92910203028', 4);

INSERT INTO TREINO VALUES (2, TO_DATE('2018/03/02 20:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Karate');
INSERT INTO TREINO VALUES (2, TO_DATE('2018/03/04 21:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Karate');
INSERT INTO TREINO VALUES (2, TO_DATE('2018/03/10 20:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Karate');
INSERT INTO TREINO VALUES (2, TO_DATE('2019/05/01 20:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Karate');
INSERT INTO TREINO VALUES (2, TO_DATE('2019/05/02 21:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Karate');
INSERT INTO TREINO VALUES (1, TO_DATE('2020/03/02 17:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Kung Fu');
INSERT INTO TREINO VALUES (1, TO_DATE('2008/03/01 18:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Kung Fu');
INSERT INTO TREINO VALUES (1, TO_DATE('2008/03/10 17:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Kung Fu');
INSERT INTO TREINO VALUES (1, TO_DATE('2008/03/15 18:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Kung Fu');
INSERT INTO TREINO VALUES (3, TO_DATE('2020/11/13 11:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Judo');
INSERT INTO TREINO VALUES (3, TO_DATE('2020/11/11 09:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Judo');
INSERT INTO TREINO VALUES (3, TO_DATE('2020/11/09 11:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Judo');
INSERT INTO TREINO VALUES (4, TO_DATE('2010/03/10 18:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Jiu Jitsu');
INSERT INTO TREINO VALUES (4, TO_DATE('2017/08/23 08:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Jiu Jitsu');
INSERT INTO TREINO VALUES (4, TO_DATE('2016/06/15 09:00:00', 'YYYY/MM/DD HH24:MI:SS'), 'Jiu Jitsu');

INSERT INTO PROPORCIONA VALUES (1, TO_DATE('2020/03/02 17:00:00', 'YYYY/MM/DD HH24:MI:SS'), '92910203028', 1);
INSERT INTO PROPORCIONA VALUES (1, TO_DATE('2008/03/01 18:00:00', 'YYYY/MM/DD HH24:MI:SS'), '92910203028', 1);
INSERT INTO PROPORCIONA VALUES (1, TO_DATE('2008/03/10 17:00:00', 'YYYY/MM/DD HH24:MI:SS'), '92910203028', 4);
INSERT INTO PROPORCIONA VALUES (1, TO_DATE('2008/03/15 18:00:00', 'YYYY/MM/DD HH24:MI:SS'), '92910203028', 1);
INSERT INTO PROPORCIONA VALUES (2, TO_DATE('2018/03/02 20:00:00', 'YYYY/MM/DD HH24:MI:SS'), '41020010294', 1);
INSERT INTO PROPORCIONA VALUES (2, TO_DATE('2018/03/04 21:00:00', 'YYYY/MM/DD HH24:MI:SS'), '41020010294', 2);
INSERT INTO PROPORCIONA VALUES (2, TO_DATE('2018/03/10 20:00:00', 'YYYY/MM/DD HH24:MI:SS'), '92910203028', 1);
INSERT INTO PROPORCIONA VALUES (2, TO_DATE('2019/05/01 20:00:00', 'YYYY/MM/DD HH24:MI:SS'), '92910203028', 2);
INSERT INTO PROPORCIONA VALUES (2, TO_DATE('2019/05/02 21:00:00', 'YYYY/MM/DD HH24:MI:SS'), '92910203028', 2);
INSERT INTO PROPORCIONA VALUES (3, TO_DATE('2020/11/13 11:00:00', 'YYYY/MM/DD HH24:MI:SS'), '78491399183', 3);
INSERT INTO PROPORCIONA VALUES (3, TO_DATE('2020/11/11 09:00:00', 'YYYY/MM/DD HH24:MI:SS'), '78491399183', 1);
INSERT INTO PROPORCIONA VALUES (3, TO_DATE('2020/11/09 11:00:00', 'YYYY/MM/DD HH24:MI:SS'), '78491399183', 2);
INSERT INTO PROPORCIONA VALUES (4, TO_DATE('2010/03/10 18:00:00', 'YYYY/MM/DD HH24:MI:SS'), '78491399183', 2);
INSERT INTO PROPORCIONA VALUES (4, TO_DATE('2017/08/23 08:00:00', 'YYYY/MM/DD HH24:MI:SS'), '78491399183', 4);
INSERT INTO PROPORCIONA VALUES (4, TO_DATE('2016/06/15 09:00:00', 'YYYY/MM/DD HH24:MI:SS'), '78491399183', 2);

ALTER SEQUENCE PAGAMENTO_N_BOLETO_SEQ RESTART WITH 1; --Reseta o contador do serial

INSERT INTO PAGAMENTO (METODO, VALOR) VALUES ('Cartao', 130.1);
INSERT INTO PAGAMENTO (METODO, VALOR) VALUES ('Dinheiro', 130.1);
INSERT INTO PAGAMENTO (METODO, VALOR) VALUES ('Transferencia', 100.2);
INSERT INTO PAGAMENTO (METODO, VALOR) VALUES ('Cartao', 149.9);
INSERT INTO PAGAMENTO (METODO, VALOR) VALUES ('Boleto', 110.9);
INSERT INTO PAGAMENTO (METODO, VALOR) VALUES ('Cartao', 130.5);

INSERT INTO COBRANCA VALUES ('91238812898', '48193010293', 1);
INSERT INTO COBRANCA VALUES ('91238812898', '19419391939', 2);
INSERT INTO COBRANCA VALUES ('92910203028', '39193002939', 3);
INSERT INTO COBRANCA VALUES ('91238812898', '83910293929', 4);
INSERT INTO COBRANCA VALUES ('92910203028', '39193002939', 5);
INSERT INTO COBRANCA VALUES ('57193891930', '92910203028', 6);

INSERT INTO FORNECEDOR VALUES ('12567923456782', 'Vidisney LTDA', '@vitao', '11987452168', '16987542657', 'Rua Eustaquio Vinhedo Araujo', 12, 'SP', 'Campinas');
INSERT INTO FORNECEDOR VALUES ('31897489813747', 'Yasmins SA', '@yasmin', '21938012938', '89143934801', 'Rua Alexandre Delbem', 12, 'SP', 'Bauru');
INSERT INTO FORNECEDOR VALUES ('78134979134787', 'Luvas na Mesa', '@lnm', '71834991840', '91384901348', 'Rua Marcia Federson', 12, 'MG', 'Cassia');
INSERT INTO FORNECEDOR VALUES ('91384139481890', 'Colchonetes do Ze', '@zezao', '12903810239', '41899403810', 'Avenida Sao Carlos', 12, 'AM', 'Manaus');

ALTER SEQUENCE PRODUTO_CODIGO_SEQ RESTART WITH 1; --Reseta o contador do serial

INSERT INTO PRODUTO (FORNECEDOR, CATEGORIA, CUSTO, ESTADO, MARCA, TAMANHO, TIPO) VALUES ('12567923456782', 'Protetor', 192.2, 'Novo', 'Traxart', 'P', 'Cotoveleira');
INSERT INTO PRODUTO (FORNECEDOR, CATEGORIA, CUSTO, ESTADO, MARCA, TAMANHO) VALUES ('31897489813747', 'Kimono', 100.0, 'Usado', 'Traxart', 'G');
INSERT INTO PRODUTO (FORNECEDOR, CATEGORIA, CUSTO, ESTADO, MARCA, TAMANHO) VALUES ('78134979134787', 'Luva', 120.0, 'Novo', 'Adidas', 'M');
INSERT INTO PRODUTO (FORNECEDOR, CATEGORIA, CUSTO, ESTADO, MARCA, TAMANHO) VALUES ('91384139481890', 'Colchonete', 60.0, 'Usado', 'Nike', 'M');


INSERT INTO COMPRA VALUES ('91238812898', 1);
INSERT INTO COMPRA VALUES ('92910203028', 2);
INSERT INTO COMPRA VALUES ('78491399183', 3);
INSERT INTO COMPRA VALUES ('41020010294', 4);




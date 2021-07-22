from selenium import webdriver
import openpyxl
from time import sleep
import pandas as pd

data = pd.read_excel(r"cpf teste.xlsx")
df = pd.DataFrame(data, columns=['CPF', 'NEMPRESA'])

nempresa = str(df['NEMPRESA'][0])
nempresa1 = str(df['NEMPRESA'][1])
nempresa2 = str(df['NEMPRESA'][2])

cpf1 = str(df['CPF'][0])
cpf2 = str(df['CPF'][1])
cpf3 = str(df['CPF'][2])
cpf4 = str(df['CPF'][3])
cpf5 = str(df['CPF'][4])
cpf6 = str(df['CPF'][5])
cpf7 = str(df['CPF'][6])
cpf8 = str(df['CPF'][7])

web = webdriver.Chrome()
web.get('http://www.portaldoempreendedorgoiano.go.gov.br/')
sleep(3)

fechar = web.find_element_by_xpath('//*[@id="button-close"]')
fechar.click()

sleep(3)
prosseguir = web.find_element_by_xpath('//*[@id="bt-choice-begin"]')
prosseguir.click()

sleep(3)
matriz = web.find_element_by_xpath('//*[@id="bt-menu-matriz"]')
matriz.click()

sleep(3)
abertura = web.find_element_by_xpath('//*[@id="bt-abertura-matriz"]')
abertura.click()

sleep(3)
login = ''
login1 = web.find_element_by_xpath('//*[@id="accountId"]')
login1.send_keys(login)

sleep(3)
avance = web.find_element_by_xpath('//*[@id="login-button-panel"]/button[2]')
avance.click()

sleep(3)
senha = ''
senha1 = web.find_element_by_xpath('//*[@id="password"]')
senha1.send_keys(senha)

sleep(3)
avancesenha = web.find_element_by_xpath('//*[@id="submit-button"]')
avancesenha.click()


#IDENTIFICAÇÃO DA MATRIZ
sleep(60)
JuntaComercial = web.find_element_by_xpath('//*[@id="solicitacao_perfil_104306"]')
JuntaComercial.click()

sleep(3)
nao1 = web.find_element_by_xpath('//*[@id="solicitacao_atualizaReceita_1"]')
nao1.click()


sleep(3)
gouvelandia = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_municipio"]/option[100]')
gouvelandia.click()

sleep(3)
SEL = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_natureza"]/option[19]')
SEL.click()

sleep(3)
avancar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
avancar.click()


#DADOS DO SOLICITANTE
sleep(3)
ddd = '11'
ddd11 = web.find_element_by_xpath('//*[@id="solicitacao_solicitante_ddd"]')
ddd11.send_keys(ddd)

sleep(3)
num = '999999999'
num1 = web.find_element_by_xpath('//*[@id="solicitacao_solicitante_telefone"]')
num1.send_keys(num)

sleep(3)
email = ''
email1 = web.find_element_by_xpath('//*[@id="solicitacao_solicitante_email"]')
email1.send_keys(email)

sleep(3)
naoesc = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_empresaSimplesCredito_1"]')
naoesc.click()

sleep(3)
me = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_porte_1"]')
me.click()

sleep(4)
cc = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_enquadramentoContratual_0"]')
cc.click()

sleep(3)
ne = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_autorizacaoUsoNomeEmpresarial_1"]')
ne.click()


#DENOMINAÇÃO/FIRMA SOCIAL PRETENDIDA
sleep(3)
avancar2 = web.find_element_by_xpath('//*[@id="botao-avancar"]')
avancar2.click()

sleep(3)
nomeE = nempresa
nomeEmpresa = web.find_element_by_xpath('//*[@id="solicitacao_nomesEmpresariais_0_nome"]')
nomeEmpresa.send_keys(nomeE)

sleep(3)
nomeE1 = nempresa1
nomeEmpresa1 = web.find_element_by_xpath('//*[@id="solicitacao_nomesEmpresariais_1_nome"]')
nomeEmpresa1.send_keys(nomeE1)

sleep(3)
nomeE2 = nempresa2
nomeEmpresa2 = web.find_element_by_xpath('//*[@id="solicitacao_nomesEmpresariais_2_nome"]')
nomeEmpresa2.send_keys(nomeE2)


sleep(60)
botaoavancar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
botaoavancar.click()


#NATUREZA DO IMÓVEL
sleep(5)
sr = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_naturezaTipoImovel_3"]')
sr.click()

sleep(3)
buscacep = web.find_element_by_xpath('//*[@id="button-buscar-cep"]')
buscacep.click()

sleep(3)
enderecocep = 'AVENIDA ABILIO RODRIGUES DA CUNHA'
enderecocep1 = web.find_element_by_xpath('//*[@id="cep-modal-field"]')
enderecocep1.send_keys(enderecocep)

sleep(3)
pesquisarcep = web.find_element_by_xpath('//*[@id="cep-modal-button"]')
pesquisarcep.click()

sleep(3)
selecionarcep = web.find_element_by_xpath('//*[@id="cep-modal-list"]/li[1]/a')
selecionarcep.click()

sleep(3)
avenida = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_tipoLogradouro"]/optgroup[1]/option[2]')
avenida.click()

sleep(3)
alugado = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_tipoUsoImovel"]/option[4]')
alugado.click()

sleep(3)
endereco = 'ABILIO RODRIGUES DA CUNHA'
endereco1 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_endereco"]')
endereco1.send_keys(endereco)

sleep(3)
bairro = 'GOUVELANDIA'
bairro1 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_bairro"]')
bairro1.send_keys(bairro)

sleep(3)
numendereco = '101'
numendereco1 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_numero"]')
numendereco1.send_keys(numendereco)

sleep(3)
pr = 'Supermercado Cristo Rei'
pr1 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_referencia"]')
pr1.send_keys(pr)

sleep(3)
ai = '4000'
ai1 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_metragem"]')
ai1.send_keys(ai)

sleep(3)
ae = '3000'
ae1 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_areaUtilizada"]')
ae1.send_keys(ae)

sleep(3)
autorizacao = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_endereco_autorizacaoUsoSolo"]/div[1]/label/input')
autorizacao.click()


#ATIVIDADES DA EMPRESA
sleep(3)
avancar3 = web.find_element_by_xpath('//*[@id="botao-avancar"]')
avancar3.click()

sleep(3)
ative = 'A  SOCIEDADE TEM POR OBJETO SOCIAL OS SERVICOS DE TREINAMENTO DE PROFISSIONAIS NA AREA GERENCIAL. '
ative1 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_objetoEmpresa"]')
ative1.send_keys(ative)

sleep(3)
ativest = 'A  SOCIEDADE TEM POR OBJETO SOCIAL OS SERVICOS DE TREINAMENTO DE PROFISSIONAIS NA AREA GERENCIAL. '
ativest1 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_objetoSocial"]')
ativest1.send_keys(ativest)

sleep(4)
pesquisacnae = web.find_element_by_xpath('//*[@id="cnae-search-primary"]')
pesquisacnae.click()

sleep(3)
inserecnae = 'Treinamento em desenvolvimento profissional e gerencial'
inserecnae1 = web.find_element_by_xpath('//*[@id="cnae-modal-description"]')
inserecnae1.send_keys(inserecnae)

sleep(3)
pesquisacnae2 = web.find_element_by_xpath('//*[@id="cnae-modal-search"]')
pesquisacnae2.click()

sleep(3)
pesquisacnae3 = web.find_element_by_xpath('//*[@id="cnae-modal-list"]/li/a')
pesquisacnae3.click()

sleep(3)
exercen = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_atividades_0_exerceNoEndereco"]/div[2]/label/input')
exercen.click()

sleep(3)
esca = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_tiposUnidade_2"]')
esca.click()

sleep(3)
avancar4 = web.find_element_by_xpath('//*[@id="botao-avancar"]')
avancar4.click()


#DADOS COMPLEMENTARES
sleep(3)
inocVirt = web.find_element_by_xpath('//*[@id="sexto_passo_question_25_0"]')
inocVirt.click()

sleep(3)
residencia = web.find_element_by_xpath('//*[@id="sexto_passo_question_1_1"]')
residencia.click()

sleep(3)
pav = '1'
pav1 = web.find_element_by_xpath('//*[@id="sexto_passo_question_3"]')
pav1.send_keys(pav)

sleep(3)
quantMax = '1'
quantMax1 = web.find_element_by_xpath('//*[@id="sexto_passo_question_4"]')
quantMax1.send_keys(quantMax)

sleep(3)
subsolo = web.find_element_by_xpath('//*[@id="sexto_passo_question_5_1"]')
subsolo.click()

sleep(3)
combustivel = '0'
combustivel1 = web.find_element_by_xpath('//*[@id="sexto_passo_question_6"]')
combustivel1.send_keys(combustivel)

sleep(3)
glp = '0'
glp1 = web.find_element_by_xpath('//*[@id="sexto_passo_question_7"]')
glp1.send_keys(combustivel)

sleep(3)
salvar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
salvar.click()



'''if cpf2 != '0':
    cpfv2 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_socios_0_pessoa_cpfCnpj"]')
    cpfv2.send_keys(cpf2)
    sleep(3)
    aperta = web.find_element_by_xpath('//*[@id="add-partner"]')
    aperta.click()
    sleep(1)
    aperta1 = web.find_element_by_xpath('//*[@id="portal-go"]/div[5]/div/div[3]/button[1]')
    aperta1.click()
    sleep(10)
    adicionar = web.find_element_by_xpath('//*[@id="add-partner"]')
    adicionar.click()
    sleep(2)
else:
    adicionar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
    adicionar.click()


if cpf3 != '0':
    cpfv3 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_socios_0_pessoa_cpfCnpj"]')
    cpfv3.send_keys(cpf2)
    sleep(3)
    aperta = web.find_element_by_xpath('//*[@id="add-partner"]')
    aperta.click()
    aperta1 = web.find_element_by_xpath('//*[@id="portal-go"]/div[5]/div/div[3]/button[1]')
    aperta1.click()
    sleep(10)
    adicionar = web.find_element_by_xpath('//*[@id="add-partner"]')
    adicionar.click()
    sleep(2)
else:
    adicionar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
    adicionar.click()


if cpf4 != '0':
    cpfv4 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_socios_0_pessoa_cpfCnpj"]')
    cpfv4.send_keys(cpf4)
    sleep(3)
    aperta = web.find_element_by_xpath('//*[@id="add-partner"]')
    aperta.click()
    aperta1 = web.find_element_by_xpath('//*[@id="portal-go"]/div[5]/div/div[3]/button[1]')
    aperta1.click()
    sleep(10)
    adicionar = web.find_element_by_xpath('//*[@id="add-partner"]')
    adicionar.click()
    sleep(2)
else:
    adicionar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
    adicionar.click()


if cpf5 != '0':
    cpfv5 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_socios_0_pessoa_cpfCnpj"]')
    cpfv5.send_keys(cpf5)
    sleep(3)
    aperta = web.find_element_by_xpath('//*[@id="add-partner"]')
    aperta.click()
    aperta1 = web.find_element_by_xpath('//*[@id="portal-go"]/div[5]/div/div[3]/button[1]')
    aperta1.click()
    sleep(10)
    adicionar = web.find_element_by_xpath('//*[@id="add-partner"]')
    adicionar.click()
    sleep(2)
else:
    adicionar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
    adicionar.click()


if cpf6 != '0':
    cpfv6 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_socios_0_pessoa_cpfCnpj"]')
    cpfv6.send_keys(cpf6)
    sleep(3)
    aperta = web.find_element_by_xpath('//*[@id="add-partner"]')
    aperta.click()
    aperta1 = web.find_element_by_xpath('//*[@id="portal-go"]/div[5]/div/div[3]/button[1]')
    aperta1.click()
    sleep(10)
    adicionar = web.find_element_by_xpath('//*[@id="add-partner"]')
    adicionar.click()
    sleep(2)
else:
    adicionar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
    adicionar.click()


if cpf7 != '0':
    cpfv7 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_socios_0_pessoa_cpfCnpj"]')
    cpfv7.send_keys(cpf7)
    sleep(3)
    aperta = web.find_element_by_xpath('//*[@id="add-partner"]')
    aperta.click()
    aperta1 = web.find_element_by_xpath('//*[@id="portal-go"]/div[5]/div/div[3]/button[1]')
    aperta1.click()
    sleep(10)
    adicionar = web.find_element_by_xpath('//*[@id="add-partner"]')
    adicionar.click()
    sleep(2)
else:
    adicionar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
    adicionar.click()


if cpf8 != '0':
    cpfv8 = web.find_element_by_xpath('//*[@id="solicitacao_empresas_0_socios_0_pessoa_cpfCnpj"]')
    cpfv8.send_keys(cpf8)
    sleep(3)
    aperta = web.find_element_by_xpath('//*[@id="add-partner"]')
    aperta.click()
    sleep(2)
    aperta1 = web.find_element_by_xpath('//*[@id="portal-go"]/div[5]/div/div[3]/button[1]')
    aperta1.click()
    sleep(10)
    adicionar = web.find_element_by_xpath('//*[@id="add-partner"]')
    adicionar.click()
    sleep(2)
else:
    adicionar = web.find_element_by_xpath('//*[@id="botao-avancar"]')
    adicionar.click()'''







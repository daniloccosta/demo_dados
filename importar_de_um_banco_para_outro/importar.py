from dborigem import *
from dbdestino import *
import queries
import sys

def importar_estoque_cds(ANO, MES):
    print("Iniciando importacao do historico de Estoque CDs")

    #pega dados do banco de origem
    orig = DBOrigem()
    sql = queries.sqlREstoqueCDs.replace("#ANO", ANO)
    sql = sql.replace("#MES", MES)
    
    dados = orig.consultar(sql)
    orig.fechar()

    #Conecta e importa dados para o banco de destino
    dest = DBDestino()

    print("Importando...")
    for dado in dados:
        if (dado[9] == None): val1 = "Null"
        else: val1 = dado[9]
        if (dado[10] == None): val2 = "Null"
        else: val2 = dado[10]
        if (dado[11] == None): val3 = "Null"
        else: val3 = dado[11]
        if dest.manipular(queries.sqlCEstoqueCDs.format(dado[0], dado[1], dado[2], "'"+ dado[3] +"'", dado[4], dado[5], "'"+ dado[6] +"'", \
        dado[7] , "'"+ dado[8] +"'", val1, val2, val3, dado[12], dado[13])) == False:
            print("dado: ", dado)
            break
    
    dest.fechar()

    print("Historico de Estoque CDs importados com sucesso!")

def importar_produtos_sem_giro(ANO, MES):
    print("Iniciando importacao do historico de Produtos Sem Giro")
    #pega dados do banco de origem
    orig = DBOrigem()
    sql = queries.sqlRProdutosSemGiro.replace("#ANO", ANO)
    sql = sql.replace("#MES", MES)
    
    dados = orig.consultar(sql)
    orig.fechar()

    #Conecta e importa dados para o banco de destino
    dest = DBDestino()

    cont = 0
    print("Importando...")
    for dado in dados:
        cont += 1

        val1 = dado[7]
        val2 = dado[8]

        if (dado[9] != None): dt1 = "'"+ dado[9] +"'"
        else: dt1 = "Null"

        if (dado[10] != None): dt2 = "'"+ dado[10] +"'"
        else: dt2 = "Null"

        if dest.manipular(queries.sqlCProdutosSemGiro.format(dado[0], dado[1], "'"+ dado[2] +"'", dado[3], dado[4], dado[5], dado[6], \
        val1, val2, dt1, dt2, dado[11], dado[12], dado[13])) == False:
            print(cont, ": ", dado)
            break

    dest.fechar()

    print("Historico de Produtos Sem Giro importados com sucesso!")


def importar_estoque_diario():
    print("Iniciando importacao do historico de estoque diario")
    #pega dados do banco de origem
    orig = DBOrigem()
    sql = queries.sqlREstoqueDia
    
    dados = orig.consultar(sql)
    orig.fechar()

    #Conecta e importa dados para o banco de destino
    dest = DBDestino()

    cont = 0
    print("Importando...")
    for dado in dados:
        dt = "'"+ dado[6] +"'"
        if dest.manipular(queries.sqlCEstoqueDia.format(dt, dado[0], "'"+ dado[1] +"'", dado[2], dado[3], "'"+ dado[4] +"'", dado[5])) == False:
            print(cont, ": ", dado)
            break
    
    dest.fechar()
    print("Historico de estoque diario importado com sucesso!")


def main():
    args = sys.argv
    if (args.__len__() != 2):
        print("")
        print("Use: importar.py [1|2] Ano Mes")
        print("")
        print("1: Estoques CDs")
        print("2: Produtos sem Giro")
        print("3: Estoque diario atual")
        return

    OP  = args[1]
    if (OP != "3"):
        ANO = args[2]
        MES = args[3]

    if (args[1] == "1"):
        importar_estoque_cds(ANO, MES)
    elif (args[1] == "2"):
        importar_produtos_sem_giro(ANO, MES)
    elif (args[1] == "3"):
        importar_estoque_diario()
    else:
        print("Not found!")


if __name__ == "__main__":
    main()

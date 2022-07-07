import math
import pandas as pd
from tkinter.filedialog import askopenfilename
from banco import *
import queries
import sys


idfilial = 0

def open_file():
    filepath = askopenfilename(
        filetypes=[("Planilha Excel", "*.xlsx")]
    )
    if not filepath:
        return

    return filepath

def importar_dados():
    planilha = open_file();
    if (planilha):
        df = pd.read_excel(planilha)
        nome_colunas = df.columns
        colunas = df.shape[1]
        linhas = df.shape[0]
        dados = []
        
        # Limpar tabelas
        #Conecta no banco
        bd = Banco()
        if linhas > 0: 
            bd.execSql(queries.sqlDel_Estfornec)

        #ler planilha e importar para banco
        for linha in range(linhas):
            for col in range(colunas):
                dados.append(df[nome_colunas[col]][linha])

            if (type(dados[0]) == str): 
                if (dados[0][0] == 'Z'): continue

            est_cosan = 0 if math.isnan(dados[2]) else dados[2]
            est_braslub = 0 if math.isnan(dados[3]) else dados[3]

            bd.execSql(queries.sqlCreate_Estfornec.format(idfilial, dados[0], "'"+ dados[1] +"'", est_cosan, est_braslub))
            dados.clear()
            

        bd.fechar()
        

def main():
    global idfilial

    args = sys.argv
    if (args.__len__() != 2):
        print("")
        print("Use: importar.py [codigo da filial]")
        return

    idfilial = args[1]

    importar_dados()

if __name__ == "__main__":
    main()
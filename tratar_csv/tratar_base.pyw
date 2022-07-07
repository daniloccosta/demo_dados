import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from sys import exit
import os

def linhaDeItem(idlinha):
    xlen = len(idlinha) - 1
    return (idlinha[1:7] == "-[-[-[" and idlinha[xlen].isnumeric())

def dadosLinha(line):
    cols = line.split("#")
    return cols

def tratarArquivo():
    #arquivo_base = open('auditoria.csv', 'r')
    arquivo792 = open_file()
    if (arquivo792 == None): return 0

    arquivo_tratado = os.path.dirname(arquivo792) + "/" + "base792.csv"
    arquivo_novo = open(arquivo_tratado, 'w')
    sep = "\t"

    arquivo_base = open(arquivo792, "r")
    num = 0

    for linha in arquivo_base:
        if (num == 0):
            linha = linha.replace("\t", "   #")
            cols = dadosLinha(linha)
            nova_linha = "codigo"
            for col in cols:
                nova_linha += col.strip() + sep
            nova_linha = nova_linha + "\n"
            arquivo_novo.write(nova_linha)
        else:
            #"	-[-[-[-"   <<<=== PADRAO: LINHA DE PRODUTO SEMPRE INICIA COM A STRING A ESQUERDA
            if linhaDeItem(linha[0: 8]):
                linha = linha.replace("\t", "   #")
                cols = dadosLinha(linha)
                nova_linha = ""
                codprod = cols[1].replace("-[", "").split("-")
                nova_linha = codprod[0].strip() + sep + \
                    codprod[1].strip() + sep + \
                    cols[2].strip().replace(".", "") + sep + \
                    cols[3].strip().replace(".", "") + sep + \
                    cols[4].strip().replace(".", "") + sep + \
                    cols[5].strip().replace(".", "") + sep + \
                    cols[6].strip().replace(".", "") + sep + \
                    cols[7].strip().replace(".", "") + sep + \
                    cols[8].strip().replace(".", "") + sep + \
                    cols[9].strip().replace(".", "") + "\n"

                arquivo_novo.write(nova_linha)
            else:
                continue    

        num += 1

    arquivo_base.close()
    arquivo_novo.close()
    return 1

def handle_click(event):
    if (tratarArquivo() == 1):
        messagebox.showinfo("Gestão de Produção", "Tratamento Concluído com muito Sucesso!!! Showwww :-)")

    exit(0)

def open_file():
    filepath = askopenfilename(
        filetypes=[("Arquivos csv", "*.csv")]
    )
    if not filepath:
        return

    return filepath

def desenha_tela():
    window = tk.Tk();
    
    window.title("Tratar 792")
    window.resizable(width=False, height=False)

    frame = tk.Frame(master=window, width=200, height=100)
    frame.pack(fill=tk.X)

    label1 = tk.Label(master=frame, text="Tratamento da base 792")
    label1.place(x=25, y=20)
    
    button = tk.Button(master=frame, text="Processar Arquivo", width=20)
    button.place(x=25, y=42)
    button.bind("<Button-1>", handle_click)
    
    window.mainloop()

def main():
    desenha_tela()

if __name__ == "__main__":
    main()

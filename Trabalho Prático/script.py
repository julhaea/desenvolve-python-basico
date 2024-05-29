import os
import tkinter as tk
from tkinter import messagebox
# Função para criar conta
def criar_conta():
    def criar():
        usuario=usuarioEntry.get().lower()
        senha=senhaEntry.get()
        tipo=tipoEntry.get().lower()
        usuarios=[]
        usu, tip= 0,0
        if tipo=="professor": 
            tipo=2
            tip=1
        elif tipo=="aluno": 
            tipo=1
            tip=1
        else: messagebox.showwarning("Aviso", f"Este tipo de conta não existe")
        with open("usuarios.csv","r") as docusuarios:
            for linha in docusuarios:
                linha=linha.split(",")
                usuarios.append(linha[0])
        if usuario in usuarios:
            messagebox.showwarning("Aviso", f"Este nome de usuário já está sendo usado") 
        else:usu=1
        if usu==1 and tip==1:
            with open("usuarios.csv","a") as docusuarios:
                docusuarios.write(f"{usuario},{senha},{tipo}\n")
            if tipo==1:
                with open("Boletim.csv","r") as boletim:
                    linha1=boletim.readline().strip()
                    linha1=linha1.split(",")
                    tam=",-"*((len(linha1))-1)
                with open("Boletim.csv","a") as boletim:
                    boletim.write(f"\n{usuario}{tam}")
            messagebox.showinfo("Sucesso", f"Conta adicionada")
            conta.destroy()
    conta=tk.Toplevel()
    conta.title("Criar conta")
    conta.geometry("800x600")

    tk.Label(conta, text="Digite o nome de usuário:").pack(pady=5)
    usuarioEntry = tk.Entry(conta, width=40)
    usuarioEntry.pack(pady=5)

    tk.Label(conta, text="Digite a senha:").pack(pady=5)
    senhaEntry = tk.Entry(conta, width=40)
    senhaEntry.pack(pady=5)

    tk.Label(conta, text="Qual o tipo de conta?").pack(pady=5)
    tipoEntry = tk.Entry(conta, width=40)
    tipoEntry.pack(pady=5)

    tk.Button(conta, text="Criar", command=criar).pack(pady=20)

    
# Função para professor ver notas
def ver_notasprof():
    def ver():
        usuario=usuarioEntry.get().lower()
        with open("Boletim.csv","r") as boletim:
            linhas=[]
            i=0
            iusuario=0
            for linha in boletim:
                linha=linha.replace("\n","")
                linha=linha.split(",")
                linhas.append(linha)
                if linha[0]==usuario:
                    iusuario=i
                i+=1
        if iusuario==0: messagebox.showwarning("Aviso","Este aluno não existe")
        else:
            notas=[f"Notas de {usuario}:\n"]
            for i in range(len(linhas[0])):
                if i==0: continue
                materia=linhas[0][i]
                nota=linhas[iusuario][i]
                if nota=="-":
                    nota="nota ainda não lançada"
                notas.append(f"{materia}: {nota}")
            nota="\n".join(notas)
            messagebox.showinfo("Notas", nota)
            notapag.destroy()
    notapag=tk.Toplevel()
    notapag.title("Ver notas")
    notapag.geometry("400x600")

    tk.Label(notapag, text="Digite o nome de usuário do aluno:").pack(pady=5)
    usuarioEntry = tk.Entry(notapag, width=40)
    usuarioEntry.pack(pady=5)

    tk.Button(notapag, text="Ver notas", command=ver).pack(pady=20)

# Função para sair
def sair():
    paglogin.deiconify()
    paglogin.destroy()
# Função para ver notas
def ver_notas():
    usuario=nome_entry.get().lower()
    with open("Boletim.csv","r") as boletim:
        linhas=[]
        i=0
        iusuario=0
        for linha in boletim:
            linha=linha.replace("\n","")
            linha=linha.split(",")
            linhas.append(linha)
            if linha[0]==usuario:
                iusuario=i
            i+=1
    notas=["Notas:\n"]
    for i in range(len(linhas[0])):
        if i==0: continue
        materia=linhas[0][i]
        nota=linhas[iusuario][i]
        if nota=="-":
            nota="nota ainda não lançada"
        notas.append(f"{materia}: {nota}")
    nota="\n".join(notas)
    messagebox.showinfo("Notas", nota)

# Função para atualizar boletim
def boletim():
    def att_boletim():
        usuario=usuarioEntry.get().lower()
        materia=matEntry.get().lower()
        nota=notaEntry.get()
        with open("Boletim.csv","r") as boletim:
            mat=0
            usu=0
            linhas=[]
            indmateria=0
            for linha in boletim:
                linha=linha.split(",")
                if mat==0:
                    for item in linha:
                        itemr=item.replace("\n","")
                        if itemr==materia:
                            indmateria=linha.index(item)
                            if item!=itemr: 
                                nota=f"{nota}\n"
                            mat=1
                if linha[0]==usuario:
                    linha[indmateria]=str(nota)
                    usu=1
                linhas.append(linha)
        if mat==0:
            messagebox.showwarning("Aviso", f"Esta matéria não existe")
        if usu==0:
            messagebox.showwarning("Aviso", f"Este usuário não existe")
        if usu==1 and mat==1:
            with open("Boletim.csv","w") as boletim:
                for linha in linhas:
                    linha=",".join(linha)
                    boletim.writelines(linha)
                messagebox.showinfo("Sucesso", f"Nota atualizada")
                bol.destroy()
    
    bol=tk.Toplevel()
    bol.title("Atualizar boletim")
    bol.geometry("800x600")

    tk.Label(bol, text="Digite o nome de usuário do aluno:").pack(pady=5)
    usuarioEntry = tk.Entry(bol, width=40)
    usuarioEntry.pack(pady=5)

    tk.Label(bol, text="Digite o nome da matéria:").pack(pady=5)
    matEntry = tk.Entry(bol, width=40)
    matEntry.pack(pady=5)

    tk.Label(bol, text="Digite a nota:").pack(pady=5)
    notaEntry = tk.Entry(bol, width=40)
    notaEntry.pack(pady=5)

    tk.Button(bol, text="Atualizar", command=att_boletim).pack(pady=20)

    
# Função para visualizar correções
def ver_correcao():
    def ver():
        usuario=nome_entry.get().lower()
        nome=nomeEntry.get().lower()
        path=f"atividadeCORRIGIDA_{nome}_{usuario}.txt"
        if os.path.isfile(path):
            os.startfile(path)
        else:
            if os.path.isfile(f"atividade_{nome}_{usuario}.txt"):
                messagebox.showwarning("Aviso", f"Esta atividade ainda não foi corrigida")
            else:
                messagebox.showwarning("Aviso", f"Você ainda não entregou essa atividade")
        verpag.destroy()
    verpag=tk.Toplevel()
    verpag.title("Ver correção")
    verpag.geometry("400x600")

    tk.Label(verpag, text="Digite o nome da atividade:").pack(pady=5)
    nomeEntry = tk.Entry(verpag, width=40)
    nomeEntry.pack(pady=5)

    tk.Button(verpag, text="Abrir atividade", command=ver).pack(pady=20)
# Função para corrigir
def correcao():
    def corrigir():
        prof=nome_entry.get().lower()
        nome=nomeEntry.get().lower()
        usuario=usuarioEntry.get().lower()
        correcao=correcaoEntry.get()
        path=f"atividade_{nome}_{usuario}.txt"
        with open(path,"a") as atividade:
            atividade.write(f"\nCorreção:\n{correcao}\nAss: {prof}")
        os.rename(path,f"atividadeCORRIGIDA_{nome}_{usuario}.txt")
        messagebox.showinfo("Sucesso", f"Correção enviada!")
        corpag.destroy()

    def abrir_att():
        nome=nomeEntry.get().lower()
        usuario=usuarioEntry.get().lower()
        path=f"atividade_{nome}_{usuario}.txt"
        if os.path.isfile(path):
            os.startfile(path)
                
        else:
            if os.path.isfile(f"atividadeCORRIGIDA_{nome}_{usuario}.txt"):
                messagebox.showwarning("Aviso", f"Esta atividade já foi corrigida")
            else:
                messagebox.showwarning("Aviso", f"{usuario} ainda não entregou a atividade {nome}")
    corpag=tk.Toplevel()
    corpag.title("Corrigir atividade")
    corpag.geometry("400x600")

    tk.Label(corpag, text="Digite o nome da atividade:").pack(pady=5)
    nomeEntry = tk.Entry(corpag, width=40)
    nomeEntry.pack(pady=5)

    tk.Label(corpag, text="Digite o nome de usuário do aluno:").pack(pady=5)
    usuarioEntry = tk.Entry(corpag, width=40)
    usuarioEntry.pack(pady=5)

    tk.Button(corpag, text="Abrir atividade", command=abrir_att).pack(pady=20)

    tk.Label(corpag, text="Cole aqui a correção").pack(pady=5)
    correcaoEntry = tk.Entry(corpag, width=40)
    correcaoEntry.pack(pady=5)
    tk.Button(corpag, text="Adicionar correção", command=corrigir).pack(pady=20)

# Função para enviar atividades
def envio():
    def enviar():
        usuario=nome_entry.get().lower()
        nome = nomeEntry.get().lower()
        atividade = atividadeEntry.get()
        if os.path.isfile(f"atividade_{nome}_{usuario}.txt"):
            messagebox.showwarning("Aviso","Esta atividade já foi entregue")
        elif os.path.isfile(f"atividadeCORRIGIDA_{nome}_{usuario}.txt"):
            messagebox.showwarning("Aviso","Esta atividade já foi entregue e corrigida")
        else: 
            with open(f"atividade_{nome}_{usuario}.txt", "w") as att:
                att.write(atividade)
            messagebox.showinfo("Sucesso", f"Atividade '{nome}' salva com sucesso!")
            enviopag.destroy()

    enviopag = tk.Toplevel()
    enviopag.title("Enviar Atividade")
    enviopag.geometry("400x200")

    tk.Label(enviopag, text="Digite o nome da atividade:").pack(pady=5)
    nomeEntry = tk.Entry(enviopag, width=40)
    nomeEntry.pack(pady=5)

    tk.Label(enviopag, text="Cole aqui a atividade:").pack(pady=5)
    atividadeEntry = tk.Entry(enviopag, width=40)
    atividadeEntry.pack(pady=5)

    tk.Button(enviopag, text="Salvar", command=enviar).pack(pady=20)
# Função para excluir atividades
def exclusao():
    def excluir():
        usuario=nome_entry.get().lower()
        nome = nomeEntry.get().lower()
        path=f"atividade_{nome}_{usuario}.txt"
        if os.path.isfile(path):
            os.remove(path)
            messagebox.showinfo("Sucesso", f"Atividade '{nome}' excluída com sucesso!")
            excpag.destroy()
        else:
            messagebox.showwarning("Aviso", f"Você não enviou a atividade {nome} ou ela já foi corrigida")

    excpag = tk.Toplevel()
    excpag.title("Exluir Atividade")
    excpag.geometry("400x200")

    tk.Label(excpag, text="Digite o nome da atividade:").pack(pady=5)
    nomeEntry = tk.Entry(excpag, width=40)
    nomeEntry.pack(pady=5)

    tk.Button(excpag, text="Excluir", command=excluir).pack(pady=20)
# Função para a página do professor
def pag_professor():
    pagmenu = tk.Toplevel(paglogin)
    pagmenu.title("Menu Professor")
    pagmenu.geometry("900x900")

    frame = tk.Frame(pagmenu)
    frame.pack(expand=True)

    labelmenu = tk.Label(frame, text="Menu Professor")
    labelmenu.pack(pady=10)

    tk.Button(frame, text="Corrigir atividade", command=correcao).pack(pady=10)
    tk.Button(frame, text="Atualizar boletim", command=boletim).pack(pady=10)
    tk.Button(frame, text="Ver notas", command=ver_notasprof).pack(pady=10)
    tk.Button(frame, text="Criar conta", command=criar_conta).pack(pady=10)
    tk.Button(frame, text="Sair", command=sair).pack(pady=10)



# Função para a página do aluno
def pag_aluno():
    pagmenu = tk.Toplevel(paglogin)
    pagmenu.title("Menu Aluno")
    pagmenu.geometry("900x900")
    
    frame = tk.Frame(pagmenu)
    frame.pack(expand=True)

    labelmenu = tk.Label(frame, text="Menu Aluno")
    labelmenu.pack(pady=10)

    tk.Button(frame, text="Enviar atividade", command=envio).pack(pady=10)
    tk.Button(frame, text="Excluir atividade", command=exclusao).pack(pady=10)
    tk.Button(frame, text="Ver atividade corrigida", command=ver_correcao).pack(pady=10)
    tk.Button(frame, text="Ver notas", command=ver_notas).pack(pady=10)
    tk.Button(frame, text="Sair", command=sair).pack(pady=10)

# Função para fazer login
def fazerlogin():
    nome = nome_entry.get().lower()
    senha = senha_entry.get()
    with open("usuarios.csv", "r") as usuario:
        leitor = usuario.readlines()
        existe = 0
        for linha in leitor:
            linha = linha.strip().split(",")
            if linha[0] == nome:
                existe = 1
                if linha[1] == senha:
                    paglogin.withdraw()
                    if int(linha[2]) == 2:
                        pag_professor()
                    elif int(linha[2]) == 1:
                        pag_aluno()
                    return
                else:
                    messagebox.showwarning("Aviso", "Senha incorreta")
                    return
        if existe == 0:
            messagebox.showwarning("Aviso", "Este usuário não existe")

# Cria a janela principal de login
paglogin = tk.Tk()
paglogin.title("Cursos")
paglogin.geometry("700x700")

# Adiciona os componentes da janela de login
label = tk.Label(paglogin, text="Faça seu login")
label.pack(pady=20)  # Adiciona o rótulo à janela

frame = tk.Frame(paglogin)
frame.pack(expand=True)

tk.Label(frame, text="Nome de usuário").pack(pady=5)
nome_entry = tk.Entry(frame, width=60)
nome_entry.pack(pady=5)

tk.Label(frame, text="Senha").pack(pady=5)
senha_entry = tk.Entry(frame, width=60, show="*")
senha_entry.pack(pady=5)

tk.Button(frame, text="Fazer Login", command=fazerlogin).pack(pady=20)

# Inicia o loop principal da aplicação
paglogin.mainloop()
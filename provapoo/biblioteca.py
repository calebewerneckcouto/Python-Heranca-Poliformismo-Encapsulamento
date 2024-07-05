import tkinter as tk
from tkinter import messagebox


class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status_emprestimo = "Disponivel"

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', id={self.id}, status='{self.status_emprestimo}')"


class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

    def __repr__(self):
        return f"Membro(nome='{self.nome}', numero_membro={self.numero_membro})"



class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionar_livro(self, livro):
        self.catalogo_livros.append(livro)

    def adicionar_membro(self, membro):
        self.registro_membros.append(membro)

    def buscar_membro(self, numero_membro):
        for membro in self.registro_membros:
            if membro.numero_membro == numero_membro:
                return membro
        return None

    def emprestar_livro(self, livro_id, membro_numero):
        for livro in self.catalogo_livros:
            if livro.id == livro_id and livro.status_emprestimo == "Disponivel":
                livro.status_emprestimo = "Emprestado"
                membro = self.buscar_membro(membro_numero)
                if membro:
                    membro.historico_emprestimos.append(livro)
                    return True
                else:
                    return False
        return False

    def devolver_livro(self, livro_id):
        for livro in self.catalogo_livros:
            if livro.id == livro_id:
                livro.status_emprestimo = "Disponivel"
                return True
        return False

    def pesquisar_livro(self, criterio):
        resultado = []
        for livro in self.catalogo_livros:
            if criterio.lower() in livro.titulo.lower() or criterio.lower() in livro.autor.lower() or criterio.lower() == str(livro.id):
                resultado.append(livro)
        return resultado

    def __init__(self):
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionar_livro(self, livro):
        self.catalogo_livros.append(livro)

    def adicionar_membro(self, membro):
        self.registro_membros.append(membro)

    def emprestar_livro(self, livro_id, membro_numero):
        for livro in self.catalogo_livros:
            if livro.id == livro_id and livro.status_emprestimo == "Disponivel":
                livro.status_emprestimo = "Emprestado"
                for membro in self.registro_membros:
                    if membro.numero_membro == membro_numero:
                        membro.historico_emprestimos.append(livro)
                        return True
        return False

    def devolver_livro(self, livro_id):
        for livro in self.catalogo_livros:
            if livro.id == livro_id:
                livro.status_emprestimo = "Disponivel"
                return True
        return False
    
    

    def __repr__(self):
        return f"Membro(nome='{self.nome}', numero_membro={self.numero_membro})"


    def pesquisar_livro(self, criterio):
        resultado = []
        for livro in self.catalogo_livros:
            if criterio.lower() in livro.titulo.lower() or criterio.lower() in livro.autor.lower() or criterio.lower() == str(livro.id):
                resultado.append(livro)
        return resultado


class BibliotecaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")

        self.biblioteca = Biblioteca()

        # Componentes da interface
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack()

        # Labels e Entry para adicionar livro
        self.label_titulo = tk.Label(self.frame, text="Título:")
        self.label_titulo.grid(row=0, column=0, sticky=tk.E)
        self.entry_titulo = tk.Entry(self.frame)
        self.entry_titulo.grid(row=0, column=1)

        self.label_autor = tk.Label(self.frame, text="Autor:")
        self.label_autor.grid(row=1, column=0, sticky=tk.E)
        self.entry_autor = tk.Entry(self.frame)
        self.entry_autor.grid(row=1, column=1)

        self.label_id = tk.Label(self.frame, text="ID:")
        self.label_id.grid(row=2, column=0, sticky=tk.E)
        self.entry_id = tk.Entry(self.frame)
        self.entry_id.grid(row=2, column=1)

        self.btn_adicionar_livro = tk.Button(self.frame, text="Adicionar Livro", command=self.adicionar_livro)
        self.btn_adicionar_livro.grid(row=3, columnspan=2, pady=10)

        # Labels e Entry para cadastrar membro
        self.label_nome_membro = tk.Label(self.frame, text="Nome do Membro:")
        self.label_nome_membro.grid(row=4, column=0, sticky=tk.E)
        self.entry_nome_membro = tk.Entry(self.frame)
        self.entry_nome_membro.grid(row=4, column=1)

        self.label_numero_membro = tk.Label(self.frame, text="Número do Membro:")
        self.label_numero_membro.grid(row=5, column=0, sticky=tk.E)
        self.entry_numero_membro = tk.Entry(self.frame)
        self.entry_numero_membro.grid(row=5, column=1)

        self.btn_adicionar_membro = tk.Button(self.frame, text="Adicionar Membro", command=self.adicionar_membro)
        self.btn_adicionar_membro.grid(row=6, columnspan=2, pady=10)

        # Labels e Entry para emprestar livro
        self.label_emprestimo = tk.Label(self.frame, text="Empréstimo - ID do Livro:")
        self.label_emprestimo.grid(row=7, column=0, sticky=tk.E)
        self.entry_emprestimo = tk.Entry(self.frame)
        self.entry_emprestimo.grid(row=7, column=1)

        self.label_membro = tk.Label(self.frame, text="Número do Membro:")
        self.label_membro.grid(row=8, column=0, sticky=tk.E)
        self.entry_membro = tk.Entry(self.frame)
        self.entry_membro.grid(row=8, column=1)

        self.btn_emprestar_livro = tk.Button(self.frame, text="Emprestar Livro", command=self.emprestar_livro)
        self.btn_emprestar_livro.grid(row=9, columnspan=2, pady=10)

        # Labels e Entry para devolver livro
        self.label_devolucao = tk.Label(self.frame, text="Devolução - ID do Livro:")
        self.label_devolucao.grid(row=10, column=0, sticky=tk.E)
        self.entry_devolucao = tk.Entry(self.frame)
        self.entry_devolucao.grid(row=10, column=1)

        self.btn_devolver_livro = tk.Button(self.frame, text="Devolver Livro", command=self.devolver_livro)
        self.btn_devolver_livro.grid(row=11, columnspan=2, pady=10)

        # Labels e Entry para pesquisa de livro
        self.label_pesquisa = tk.Label(self.frame, text="Pesquisar por Título, Autor ou ID:")
        self.label_pesquisa.grid(row=12, column=0, sticky=tk.E)
        self.entry_pesquisa = tk.Entry(self.frame)
        self.entry_pesquisa.grid(row=12, column=1)

        self.btn_pesquisar = tk.Button(self.frame, text="Pesquisar", command=self.pesquisar_livro)
        self.btn_pesquisar.grid(row=13, columnspan=2, pady=10)

    def adicionar_membro(self):
        nome = self.entry_nome_membro.get()
        numero_membro = int(self.entry_numero_membro.get())

        membro = Membro(nome, numero_membro)
        self.biblioteca.adicionar_membro(membro)
        messagebox.showinfo("Sucesso", f"Membro '{nome}' cadastrado com sucesso!")

    def adicionar_livro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        livro_id = int(self.entry_id.get())

        livro = Livro(titulo, autor, livro_id)
        self.biblioteca.adicionar_livro(livro)
        messagebox.showinfo("Sucesso", f"Livro '{titulo}' adicionado com sucesso!")

    def emprestar_livro(self):
        livro_id = int(self.entry_emprestimo.get())
        membro_numero = int(self.entry_membro.get())

        if self.biblioteca.emprestar_livro(livro_id, membro_numero):
            messagebox.showinfo("Sucesso", f"Livro ID {livro_id} emprestado para o membro número {membro_numero}.")
        else:
            messagebox.showerror("Erro", "Não foi possível emprestar o livro. Verifique o ID do livro ou o número do membro.")

    def devolver_livro(self):
        livro_id = int(self.entry_devolucao.get())

        if self.biblioteca.devolver_livro(livro_id):
            messagebox.showinfo("Sucesso", f"Livro ID {livro_id} devolvido com sucesso.")
        else:
            messagebox.showerror("Erro", "Não foi possível devolver o livro. Verifique o ID do livro.")

    def pesquisar_livro(self):
        criterio = self.entry_pesquisa.get()
        resultados = self.biblioteca.pesquisar_livro(criterio)

        if resultados:
            resultado_str = "\n".join([f"{livro}" for livro in resultados])
            messagebox.showinfo("Resultados da Pesquisa", f"Resultados:\n{resultado_str}")
        else:
            messagebox.showinfo("Resultados da Pesquisa", "Nenhum resultado encontrado.")

# Criando a aplicação e iniciando o loop principal
if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()

   
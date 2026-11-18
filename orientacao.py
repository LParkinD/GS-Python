
class Orientacao:

    def __init__(self, id, categoria, titulo, palavras_chave,
                 resposta, documentos, onde, fonte, verificado_em):

        self.id = id
        self.categoria = categoria
        self.titulo = titulo
        self.palavras_chave = palavras_chave
        self.resposta = resposta
        self.documentos = documentos
        self.onde = onde
        self.fonte = fonte
        self.verificado_em = verificado_em

    def exibir(self):
        print(self.titulo)
        print(self.resposta)
        print(self.documentos)
        print(self.onde)
        print(self.fonte)

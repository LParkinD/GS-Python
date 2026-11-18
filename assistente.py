
import json
from orientacao import Orientacao

ACENTOS = {
        "á": "a", "à": "a", "ã": "a", "â": "a",
        "é": "e", "ê": "e", "í": "i",
        "ó": "o", "õ": "o", "ô": "o",
        "ú": "u", "ç": "c"
    }

def normalizar(texto):
    texto = texto.lower().strip()

    for letra, troca in ACENTOS.items():
        texto = texto.replace(letra, troca)

    for sinal in "?!.,;:()":
        texto = texto.replace(sinal, " ")
    return " " + " ".join(texto.split()) + " "


class Assistente:

    def __init__(self):
        with open("base_conhecimento.json", "r", encoding="utf-8") as arquivo:
            self.dados = json.load(arquivo)
        self.registro = []

    def print_cat(self):
        categorias = []
        i = 0

        for orientacao in self.dados:
            categoria = orientacao["categoria"]

            if categoria not in categorias:
                categorias.append(categoria)
                i += 1
                print("[", i, "]", categoria)


        numero = int(input("Qual categoria você deseja selecionar? ")) - 1

        if 0 <= numero < len(categorias):
            return categorias[numero]

        print("Categoria inválida")
        return None

    def print_tit(self, categoria):
        titulos = []
        i = 0
        for orientacao in self.dados:
            titulo = orientacao["titulo"]

            if titulo not in titulos:
                if orientacao["categoria"] == categoria:
                    titulos.append(titulo)
                    i += 1
                    print("[", i, "]", titulo)

        numero = int(input("Selecione um título: "))
        if numero == 0:
            return None

        if 1 <= numero <= len(titulos):
            return titulos[numero - 1]

        print("Título inválido")
        return None


    class Assistente:

        def __init__(self):
            pass

    def navegar(self):
        categoria = self.print_cat()
        if categoria is None:
            return

        titulo = self.print_tit(categoria)
        if titulo is None:
            return

        for orientacao in self.dados:
            if orientacao["categoria"] == categoria:
                id_registro = orientacao["id"]
                self.registrar(id_registro)
                print("Título:", orientacao["titulo"])
                print("Resposta:", orientacao["resposta"])
                print("Documentos:", orientacao["documentos"])
                print("Onde:", orientacao["onde"])
                print("Fonte:", orientacao["fonte"])
                break

    def perguntar(self):
        categoria = self.print_cat()

        if categoria is None:
            return

        pergunta = input("Digite sua dúvida: ")
        pergunta_normalizada = normalizar(pergunta)
        maior_pontuacao = 0
        melhor_orientacao = None

        for orientacao in self.dados:
            if orientacao["categoria"] != categoria:
                continue

            pontos = 0
            titulo = orientacao["titulo"]

            if normalizar(titulo) in pergunta_normalizada:
                pontos += 1

            for palavra in orientacao["palavras_chave"]:
                if normalizar(palavra) in pergunta_normalizada:
                    pontos += 3

            print("Título:", titulo, "| Pontos:", pontos)

            if pontos > maior_pontuacao:
                maior_pontuacao = pontos
                melhor_orientacao = orientacao

        if melhor_orientacao is None:
            print("Nenhuma orientação correspondente foi encontrada.")
            return

        print("Título:", melhor_orientacao["titulo"])
        print("Resposta:", melhor_orientacao["resposta"])
        print("Documentos necessários:", melhor_orientacao["documentos"])
        print("Onde:", melhor_orientacao["onde"])
        print("Fonte:", melhor_orientacao["fonte"])
        print("Aviso: este assistente NÃO é um canal oficial.")

        self.registrar(pergunta, melhor_orientacao["resposta"])

        duvida = normalizar(input("Essa orientação respondeu sua dúvida? (s/n): "))



    def registrar(self, pergunta, resposta):
        try:
            with open("data/historico.json", "r", encoding="utf-8") as arquivo:
                historico = json.load(arquivo)

        except (FileNotFoundError, json.JSONDecodeError):
            historico = []

        n_registro =+ 1
        registro = {
            "Número de registro": n_registro,
            "pergunta": pergunta,
            "resposta": resposta
        }

        historico.append(registro)

        with open("data/historico.json", "w", encoding="utf-8") as arquivo:
            json.dump(historico, arquivo, ensure_ascii=False, indent=4)

    def indicadores(self):
        # Calcular indicadores dos atendimentos
        pass

    def exportar_csv(self):
        # Exportar atendimentos para CSV
        pass

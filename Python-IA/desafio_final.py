import json
from contato_com_llm import recebe_linha_e_retorna_json

# Etapa 1
lista_de_resenhas = []

with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

# Etapa 2 e 3
lista_de_resenhas_json = []

for resenha in lista_de_resenhas:
    resenha_json = recebe_linha_e_retorna_json(resenha)
    resenha_dict = json.loads(resenha_json)
    lista_de_resenhas_json.append(resenha_dict)

    # Etapa 4
    def contador_e_juntador(Lista_de_dicionarios):
        contador_positiva = 0
        contador_negativa = 0
        contador_neutra = 0
        Lista_de_dicionarios_str = []

        for dicionario in Lista_de_dicionarios:
            if dicionario['avaliacao'] == 'Positiva':
                contador_positiva = contador_positiva + 1
            elif dicionario['avaliacao'] == 'Negativa':
                contador_negativa += 1
            else:
                contador_neutra += 1

            Lista_de_dicionarios_str.append(str(dicionario))

        texto_unidos = "#####".join(Lista_de_dicionarios_str)
        
        return contador_positiva, contador_negativa, contador_neutra, texto_unidos

    # Etapa 5
    pos, neg, neut, textos = contador_e_juntador(lista_de_resenhas_json)
    print(f"Positivas: {pos}\n")
    print(f"Negativas: {neg}\n")
    print(f"Neutras: {neut}\n")
    print(textos)
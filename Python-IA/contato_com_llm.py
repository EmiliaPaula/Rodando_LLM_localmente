from openai import OpenAI


client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
)

def recebe_linha_e_retorna_json(linha):
    resposta_do_llm = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {"role":"system", 
            "content": """Você é um especialista em análise de dados e conversãode textos para JSON.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marktplace online. 
            Eu quero que você análise essa resenha, e me retorne um JSON com as seguintes chaves:
            - 'usuario': o nome do usuário que fez a resenha
            - 'resenha_original': a resenha no idioma original que você recebeu
            - 'resenha_pt': a resenha traduzida para o português do Brasil, deve estar sempre na língua portuguesa do Brasil.
            - 'avaliacao': uma avaliação se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra'

            Exemplo de entrada:
            '879485937$Emilia Paula $This is a positive review for the app.'
            Exemplo de saída:
            {
                "usuario": "Emilia Paula",
                "resenha_original": "This is a positive review for the app.",
                "resenha_pt": "Esta é uma resenha positiva para o aplicativo.",
                "avaliacao": "Positiva"
            }

            xemplo de entrada:
            '74398793$Joyce Alves$Je n'aime pas cette application.'
            Exemplo de saída:
            {
                "usuario": "Joyce Alves",
                "resenha_original": "Je n'aime pas cette application.",
                "resenha_pt": "Eu não gosto dessa aplicação.",
                "avaliacao": "Negativa"
            }

            Regra importante:
            - Você deve retornar apenas o JSON.
            - Sem nenhum outro texto além do JSON.
            """},
            
            {"role":"user", 
            "content": f"Resenha: {linha}"}
        ],
        temperature=0.0,
    )

    resposta = resposta_do_llm.choices[0].message.content.replace("```json", "").replace("```", "")
    print(resposta)
    return resposta
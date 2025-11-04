import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyDUCkgWqur7B09UmltRMgkPdqzivBWvWRs") 

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["Oi, quem é você?"]
    },
    {
        "role": "model",
        "parts": ["Olá! Eu sou a MIA 🌸 Sua assistente virtual de apoio emocional. Estou aqui pra te ouvir, te apoiar e compartilhar dicas suaves de autocuidado e bem-estar. Você nunca está sozinha enquanto conversamos 💜."]
    }
])

def conversar_com_mia(pergunta):
    resposta = chat.send_message(pergunta)
    return resposta.text

def exibir_logo():
    print("\n╔══════════════════════════════════════╗")
    print("║        🌷 MIA - Sua companhia        ║")
    print("║    emocional, gentil e presente.     ║")
    print("╚══════════════════════════════════════╝\n")
    time.sleep(1)

# Execução principal
if __name__ == "__main__":
    exibir_logo()
    print("MIA: Olá, como você está se sentindo hoje? Pode me contar 🌼")

    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() in ["sair", "exit", "tchau", "bye", "obrigada, tchau", "thanks, bye", "só isso, obrigada, tchau"]:
            print("\nMIA: Foi uma alegria estar com você hoje 💖 Se cuide, tá bem?")
            break

        try:
            resposta = conversar_com_mia(pergunta)
            print("\nMIA:", resposta.strip())
        except Exception as e:
            print("\nMIA: Opa... algo deu errado. Pode tentar de novo? 🙈")
            print("Erro:", e)
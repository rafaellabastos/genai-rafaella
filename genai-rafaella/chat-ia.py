import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"

mensagens = []

print("=" * 50)
print("       MINHA IA LOCAL")
print("       Llama + Ollama + Python")
print("=" * 50)
print("Digite /sair para encerrar.")
print("Digite /limpar para limpar a conversa.")
print()

while True:
    pergunta = input("Você: ").strip()

    if not pergunta:
        continue

    if pergunta.lower() == "/sair":
        print("Até mais!")
        break

    if pergunta.lower() == "/limpar":
        mensagens.clear()
        print("Memória da conversa apagada.\n")
        continue

    mensagens.append({
        "role": "user",
        "content": pergunta
    })

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": mensagens,
                "stream": False
            },
            timeout=300
        )

        resposta.raise_for_status()

        dados = resposta.json()
        texto = dados["message"]["content"]

        print(f"\nIA: {texto}\n")

        mensagens.append({
            "role": "assistant",
            "content": texto
        })

    except requests.exceptions.ConnectionError:
        print("\nErro: o Ollama não está rodando.\n")
        print("Abra o Ollama e tente novamente.\n")

    except Exception as erro:
        print(f"\nErro: {erro}\n")
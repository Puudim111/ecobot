import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Conteúdo do bot
dicas = [
    "Use garrafa reutilizável em vez de plástico descartável.",
    "Separe o lixo reciclável do orgânico.",
    "Evite desperdício de água no banho.",
    "Use sacolas reutilizáveis nas compras.",
    "Desligue aparelhos da tomada quando não estiver usando."
]

curiosidades = [
    "O plástico pode levar mais de 400 anos para se decompor.",
    "Uma lata reciclada economiza energia suficiente para ligar uma TV por horas.",
    "O lixo eletrônico cresce mais rápido que o lixo comum.",
    "Uma torneira pingando pode desperdiçar milhares de litros por ano."
]

# Estatísticas
stats = {
    "dicas": 0,
    "curiosidades": 0
}

@client.event
async def on_ready():
    print("EcoBot está online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    texto = message.content.lower()

    if texto == "!ajuda":
        await message.channel.send(
            "🌱 **EcoBot - Comandos**\n"
            "!dica - Receber uma dica ecológica\n"
            "!curiosidade - Receber uma curiosidade ambiental\n"
            "!stats - Ver estatísticas do bot"
        )

    elif texto == "!dica":
        dica = random.choice(dicas)
        stats["dicas"] = stats["dicas"] + 1
        await message.channel.send("💡 Dica ecológica:\n" + dica)

    elif texto == "!curiosidade":
        curiosidade = random.choice(curiosidades)
        stats["curiosidades"] = stats["curiosidades"] + 1
        await message.channel.send("🌍 Curiosidade ambiental:\n" + curiosidade)

    elif texto == "!stats":
        total = stats["dicas"] + stats["curiosidades"]
        await message.channel.send(
            "📊 **Estatísticas do EcoBot**\n"
            "Dicas enviadas: " + str(stats["dicas"]) + "\n"
            "Curiosidades enviadas: " + str(stats["curiosidades"]) + "\n"
            "Total de interações: " + str(total)
        )

    elif texto.startswith("!"):
        await message.channel.send("❌ Comando inválido. Use !ajuda")

# Coloque o token do seu bot aqui
client.run("INSIRA O TOKEN")

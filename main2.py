import discord
import random
import os

x = os.listdir("imagenes")
print(random.choice(x))


intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hola Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("Hi bot"):
        img_random = random.choice("hi C:") 
        if img_random == "contaminacion 1.jpg" :
            await message.channel.send ("https://www.pranaair.com/es/blog/effect-of-air-pollution-on-plants-and-animals/")
        elif img_random == "contaminacion 2.jpg" :
            await message.channel.send ("https://www.iberdrola.com/sostenibilidad/contaminacion-del-agua")
        if img_random == "contaminacion 3.jpg" :
            await message.channel.send ("https://www.fundacionaquae.org/agua-y-contaminacion/")
        if img_random == "contaminacion 4.jpg" :
            await message.channel.send ("https://www.ecologiaverde.com/problemas-ambientales-en-el-campo-y-la-ciudad-1607.html")
        if img_random == "contaminacion 5.jpg" :
            await message.channel.send ("https://www.ecologiaverde.com/como-afecta-la-contaminacion-al-medio-ambiente-1818.html")
        await message.channel.send(file= discord.File(f'imagenes/{img_random}'))
client.run("x")

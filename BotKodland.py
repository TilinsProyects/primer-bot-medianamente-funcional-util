import discord
import random
from BotExtra import gen_pass



#aqui cuando alguien se une me avisa

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'hola, señor bienvenido a **{guild.name}** se le apetece un te señor {member.mention}, gracias por venir y preparese para ver los mejores bots! :v'
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('Tu token')



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("bye")
    elif message.content.startswith("$contraseña porfis"):
        password = gen_pass(10)
        await message.channel.send(f'Tu nueva contraseña es: {password}')
    
    elif message.content.startswith("$haz un ricoshot"):
        options = [
            "acertar disparo a moneda, daño critico https://tenor.com/view/ultra-kill-ultrakill-game-ricoshots-chargeback-gif-5621191212649697279",
            "fallo disparo, sin daño https://tenor.com/view/ultrakill-ultraskill-skill-issue-ultraskill-issue-massive-skill-issue-gif-7869734484172336619",
            "disparo sin golpear moneda https://tenor.com/view/ultrakill-gif-26495714",
            "acertar disparo a moneda, daño simple https://tenor.com/view/touch-grass-ultrakill-gif-26421201"
        ]
        result = random.choice(options)
        await message.channel.send(f'Resultado del ricoshot: {result}')

    else:
        await message.channel.send(message.content)


client.run("Tu toke")


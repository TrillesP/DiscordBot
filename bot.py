import os
import random
import sqlite3

import discord
from discord.ext import commands
from dotenv import load_dotenv
from imdb import Cinemagoer

import responses

load_dotenv()

TOKEN = os.getenv("TOKEN")  # Siga as instruções no arquivo ".env.example"

ia = Cinemagoer()

try:
    SQLite_conexao = sqlite3.connect('Users_Discord.db')
    cursor = SQLite_conexao.cursor()
    print("Database conectada.")
    SQLite_select_Query = "SELECT * FROM usuarios"
    cursor.execute(SQLite_select_Query)
    usuarios = cursor.fetchall()
    print(usuarios)

except sqlite3.Error as error:
    print("Erro conectando ao SQLite", error)


def criar_usuario_database(conn, user):
    cur = conn.cursor()
    todos = cur.execute("SELECT * FROM usuarios").fetchall()
    for row in todos:
        user_id = str(user[0])
        var_id = str(row[0])
        if var_id == user_id:
            return f'Já disse que você é nota {row[2]}.'
    cur.execute("INSERT INTO usuarios VALUES(?,?,?)", user)
    conn.commit()
    return f'Você é nota {user[2]}!'


async def manda_mensagem(message, user_message, privada):
    try:
        resposta = responses.handle_response(user_message)
        await message.author.send(resposta) if privada else await message.channel.send(resposta)
    except Exception as e:
        print(e)


def rodar_bot():
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(bot))

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        user_message = str(message.content)
        if user_message.startswith('?'):
            user_message = user_message[1:]
            await manda_mensagem(message, user_message, privada=True)
        else:
            await manda_mensagem(message, user_message, privada=False)
        await bot.process_commands(message)

    @bot.command(name="slap")
    async def bate_em_usuario(ctx, user: discord.User):
        await user.send(f'{ctx.author} te deu um tapa ! :O')

    @bot.command(name="dice")
    async def joga_dados(ctx, arg):
        divisao = arg.split('d', 1)
        num = int(divisao[0])
        lados = int(divisao[1])
        lista_resultados = []
        resultado = 0
        for i in range(num):
            lista_resultados.append(random.randint(1, lados))
        for j in lista_resultados:
            resultado = resultado + j

        await ctx.send(f'Dados: {lista_resultados} - Total: {resultado}')

    @bot.command(name="rateme")
    async def dar_nota(ctx):
        rating = f'{random.randint(1, 10)}/10'
        user_completo = (ctx.author.id, ctx.author.name, rating)
        await ctx.send(criar_usuario_database(SQLite_conexao, user_completo))

    @bot.command(name="recommend")
    async def recomenda_filme(ctx):
        top250M = ia.get_top250_movies()
        filme = top250M[random.randint(1, 250)]
        top250S = ia.get_top250_tv()
        serie = top250S[random.randint(1, 250)]
        await ctx.send("Recomendo o filme '{}' e a série '{}'".format(filme, serie))

    bot.run(TOKEN)

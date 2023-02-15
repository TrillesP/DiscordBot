## Objetivo

Demonstrar conhecimentos de Python suficientes para criação de um bot no app Discord que receba diferentes informações sobre o servidor em que se encontra e responda a alguns comandos enviados por usuários formatados para melhor visualização.

## Primeiros passos

Para rodar o bot é necessário primeiro instalar as libs `discord`, `dotenv` e `cinemagoer`.

Na pasta do projeto, rode os seguintes códigos no terminal:

`pip install discord.py`

`pip install python-dotenv`

`pip install cinemagoer`

Ou, usando PyCharm, pesquise pelas libs em Python Packages e instale.

<h2>Discord Bot</h2>

Para fazer o bot logar no servidor, basta rodar o arquivo `main.py`.

As instruções sobre o token do bot podem ser encontradas nos arquivos `bot.py` e `.env.example`.

:fire: Esse bot responde a comandos que começam com `!`, utiliza um arquivo de banco de dados com a lib SQLite3 para gerenciar notas de usuários de um servidor, faz comandos básicos como 'roll' e interage com usuários via DM.

Os comandos são:

`!slap`, que deve vir acompanhado da tag de algum usuário do servidor.

Ex: Você, @Fulano, escreve "!slap @João"  ->  Output: Bot envia DM para @João dizendo "Fulano deu um tapa em você! :open_mouth:"

`!dice`, que deve vir acompanhado da informação de quantos dados de quantos dados você quer rolar.

Ex: "!dice 3d25"  ->  Output: Bot envia mensagem no mesmo chat dizendo "Dados: [9, 13, 1] - Total: 23"

`!rateme`, que é respondida com o bot lhe dando uma nota entre 1 e 10. Caso o bot já tenha lhe dado uma nota antes, ele busca no banco de dados e reafirma essa nota para você.

E `!recommend`, que é respondida com o bot recomendando um filme aleatório do top 250 filmes e uma série aleatória do top 250 séries do IMDb.

PS: O bot também responde "Olá" caso você envie um "oi" no chat, apenas para demonstrar o evento `on.message`, que também contém uma espera para a solução dos diversos comandos do bot, pois sem esse os comandos seriam ignorados, e um arquivo de respostas, os dois criados para possíveis incrementos ao bot de diversas respostas baseadas em falas e outros comandos, onde o bot também separa o conteúdo das mensagens de seus autores e possibilita um diálogo em mensagens privadas com o prefixo `?`.

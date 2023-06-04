# Living Dex Box Displayer (through Discord Bot)

This is my attempt at displaying every Pokemon in a given pokedex (through a Serebii link) in a neat 6 x 5 PC format. This is particularly useful for pokedex completionist that want to more easily organize their pokemoms without worrying about ordering much.

To set up the discord bot, simply add your own discord bot's token to `token` in `bot.py`, and invite the bot to your server. To start the bot, run `main.py`. Use `!dex <serebii pokedex link>` on Discord while the bot is up. This has been tested for full National dex and Paldea dex, but it should also work for any and all Serebii Pokedex link.

The Discord bot will send the pokedex organized in PC format. You can use the reactions as buttons to scroll through the boxes.

Python libraries needed: BeautifulSoup, discord.py, html-parser, asyncio

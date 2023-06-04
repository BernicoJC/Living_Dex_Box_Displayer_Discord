import discord
import asyncio
import livingdex

async def send_message(message, user_message, is_private, client):
    try:
        command = user_message.lower()
        command = command.split()
        response = ""

        if command[0] == "!dummy": #template
            response = "Message received"
            await message.channel.send(response)

        elif command[0] == "!dex":
            if(len(command) == 1 or "https://www.serebii.net/" not in command[1]):
                response = "Please add a valid serebii pokedex link after the command"
            
            boxno = 0
            box_amounts = livingdex.box_length(command[1])
            response = await message.channel.send(livingdex.pokedex(command[1], boxno))

            await response.add_reaction("⬅️")
            await response.add_reaction("➡️")
            
            def check(reaction, user):
                return user.id == message.author.id and str(reaction.emoji) in ["⬅️", "➡️"]
            
            while True:
                try:
                    reaction, user = await client.wait_for("reaction_add", timeout=600.0, check=check) # timeout of 10 minutes

                    # make a function so that if the OG author send another command, break

                    if str(reaction.emoji) == "⬅️":
                        if boxno == 0: # if current boxno is 0, then move to the last box
                            boxno = box_amounts
                        else:
                            boxno = boxno - 1

                    else:
                        if boxno == box_amounts:
                            boxno = 0
                        else:
                            boxno = boxno + 1

                    await response.edit(content = livingdex.pokedex(command[1], boxno))
                    await response.remove_reaction(str(reaction.emoji), user)

                
                except asyncio.TimeoutError:
                    timeout_message = response + "\nTimeout, please reenter command"
                    await response.edit(content = timeout_message)
                    break


        else:
            await message.author.send(response) if is_private else await message.channel.send(response) #if private, then send to message.author (the author of the message)
    
    except Exception as e:
        print(e)

def run_bot():
    token = "" # insert token here
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said {user_message} in {channel}")

        if user_message[0] == "??":
            user_message = user_message[2:]
            await send_message(message, user_message, True, client) #basically for if want direct message
        else:
            await send_message(message, user_message, False, client) #on the channel

    try:
        client.run(token)
    except Exception as e:
        print(f"An error occurred: {e}")
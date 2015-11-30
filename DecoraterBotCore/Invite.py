import discord

discord_user_id = '94203228043874304'

def invite(client, message):
    if(message.content.startswith('::join')):
        if message.author.id == discord_user_id:
            code = message.content[len("::join "):].strip()
            if code is not None:
                client.invite_by_code(code)
            else:
                client.send_message(message.channnel, 'Sorry,, You did not specify a code to Join a Server.')
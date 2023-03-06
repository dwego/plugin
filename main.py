from mcipc.rcon.je import Client
import pycraft
from mcipc.minecraft import Minecraft

clientPycraft = pycraft.connect("localhost", 4711)
host = "localhost"
port = 25565
password = None 
mc = Minecraft(host, port, password)

with Client(host, port, password) as client:
    client.send('scoreboard players tag add dweg0 tag_lider')
    client.send('scoreboard teams option dweg0 color black')
    client.send('scoreboard teams option dweg0 name "Lider"')

    client.send('scoreboard players tag add zZPatataZz tag_admin')
    client.send('scoreboard teams option tag_admin color gray')
    client.send('scoreboard teams option tag_admin name "Admin"')

    client.send('scoreboard players tag add ViniAlm tag_moderador')
    client.send('scoreboard teams option tag_moderador color gray')
    client.send('scoreboard teams option tag_moderador name "Admin"')

    permissions = {
    "lider": ["*"],
    "admin": ["*"],
    "moderator": ["gamemode", "give", "tp", "help", "me", "hub", "skin"],
    "default": ["help", "me", "hub", "skin"]
    }

    def has_permission(username, command):
        tags = client.send(f"tag {username} list").split(", ")
        for tag in tags:
            if tag in permissions and command not in permissions[tag]:
                return False
        return True

        if has_permission(username, command):
            response = client.send(command)
        else:
            response = client.send("Você não tem permissão para executar esse comando.")
    
    def permission_command(tag, command, args):
        if tag in permissions:
            if f'/{command}' in mc.help():
                permissions[tag].append(command)
            else:
                client.send("Essa tag não existe.")
        else:
            client.send("Essa tag não existe.")

    clientPycraft.register_command("p", permission_command)

    if has_permission(username, command):
        response = client.send(command)
    else:
        response = "Você não tem permissão para executar esse comando."
    

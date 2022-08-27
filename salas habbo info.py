import discord
from discord.ext import commands
import json
import requests
import time

import io



bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 

with open("configuracion.json") as f: #Creamos un archivo de configuracion para el bot
    config = json.load(f)



@bot.command()
async def infosala(ctx, idsala):
    response = requests.get(f"https://www.habbo.es/api/public/rooms/{idsala}")
    
    
    try:

     DescripcionSala = response.json()['description']
    except KeyError:
        DescripcionSala="❌"



    try:

     ModoPuerta =  response.json()['doorMode']
     
    
    except KeyError:
        ModoPuerta=""
        
   


    try:

      idsala =  response.json()['id']
    except KeyError:
        idsala=""

    try:

     NombreSala = response.json()['name']
    except KeyError:
        NombreSala="❌" 


     

    try:

     DuenoSala = response.json()['ownerName']
    except KeyError:
        DuenoSala="❌"

    try:    
     urlSalaFoto = response.json()['thumbnailUrl']
    except KeyError:
        urlSalaFoto="https://www.habbowidgets.com/images/web15_room.gif"

    try:

     ClasificacionSala  = response.json()['rating']
    except KeyError:
        ClasificacionSala="❌"


    try:
     CapacidadSala =  response.json()['maximumVisitors']   
    except KeyError:
        CapacidadSala="❌"   


    try:

     MiembroDesde =  response.json()['creationTime']
    except KeyError:
        MiembroDesde="" 
    registrado = MiembroDesde
    miembro = registrado.split("T")[0].split("-")
    fecha = "/".join(reversed(miembro))
    MiembroDesde = MiembroDesde.replace("."," ")
    MiembroDesde = MiembroDesde.replace("000+00:00"," ")


    registradodesde = MiembroDesde
    try:

     miembro1 = registradodesde.split("T")[1].split(" ")
    except IndexError:
        miembro1=""

   
    
    
    hora = " ".join(reversed(miembro1))



    
    
    
        
       



    

    

    
   

   
        
        
    await ctx.message.delete() #Borramos el comando para no dejar sucio el chat xD
    await ctx.send(f"Generando información de la sala {idsala}...", delete_after=0)
    time.sleep(3)

 



    
  
    

   
    
    

    
   
    if  response.status_code ==200:
      
        
        
        
            
      
        
     


        embed = discord.Embed(title=f"Información Sala Habbo Hotel", description=f':calendar:Fecha: {fecha} Hora: {hora}\n\n:star:Nombre: {NombreSala}\n\n:star:Descripción: {DescripcionSala}\n\n:bust_in_silhouette:Dueño: {DuenoSala}\n\n:id:SalaID: {int(idsala)}\n\n:door:Modo Puerta: {ModoPuerta.replace("open","Abierta <:abierto:1012924101712695327>").replace("closed","Cerrado <:cerrado:1012924103214239844>").replace("password","Contraseña <:clave:1012924103906295864>")}\n\n:1234:clasificación: {ClasificacionSala}\n\n:busts_in_silhouette:Capacidad: {CapacidadSala}\n\nComando para usar: **!infosala {idsala}**', color=discord.Colour.random())
    
            
        embed.set_thumbnail(url=f"{urlSalaFoto}")
        await ctx.send(embed=embed)
            
        
    else:
        await ctx.send("La Room ID no existe")
       
       
        
     
    
    
    
   

@bot.event
async def on_ready():
    print(f"BOT listo! {bot.user}")
    
bot.run(config["tokendiscord"])
import asyncio
import json
import random
import discord
#import youtube_dl
from discord.ext import commands
from discord.utils import get

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

TOKEN = read_token()

quotes  =   ["Normalmente no rezo, pero si estás ahí, ¡por favor, sálvame SUPERMAN!",
            "D'oh!",
            "Hazlo por Ella.",
            "Calma, que no panda el cúnico!",
            "OH! Gloria de las glorias!\nOh divino testamento de la eterna majestad de la creacion de Dios!\nMe lLeVa lA cAcHetAdA",
            "Solo porque no me importe no significa que no entienda.",
            "¡Operadora! ¡Deme el número para el 911!",
            "Lisa, los vampiros son seres inventados, como los duendes, los gremlins y los esquimales.",
            "Marge, eres tan hermosa como la princesa Leia y tan lista como Yoda.",
            "Tendrá todo el dinero del mundo, pero hay algo que jamás podrá comprar: un dinosaurio.",
            "¡Oh poderoso Dios del océano! Los griegos te llamaban Poseidón y los romanos... Acuaman.",
            "Bart, la mujer es como la cerveza: tiene buen aspecto, sabe bien y harías cualquier tontería por conseguir una.",
            "Te amo, cerveza; y a ti, Marge, que me das cerveza.",
            "Tres deseos: amor, dinero y salud. Amor por la cerveza, dinero para comprarla y salud para beberla.",
            "No dejes que la muerte de Krusty te hunda Bart. La gente se muere constantemente. Tú podrías amanecer muerto mañana... Buenas noches.",
            "Cuando miro las caras sonrientes de los niños, sólo sé que están planeando golpearme con algo.",
            "No es fácil organizarse con una mujer embarazada e hijos con problemas, pero de alguna forma consigo organizarme para ver el televisor ocho horas al día.",
            "Hijo, si realmente quieres algo en esta vida, tienes que luchar por ello. ¡Ahora silencio! Van a anunciar los números de la lotería.",
            "¿Nada de carne los viernes?, ¿y qué comen?, ¿focos?",
            "Si algo es muy difícil de hacer, entonces no merece la pena hacerlo.",
            "¡Brindo por el alcohol! La causa y la solución de todos los problemas de la vida.",
            "Chicos, lo intentaron con la mejor de sus intenciones y fracasaron. La moraleja es: nunca lo intenten.",
            "¡Los libros son inútiles! El único libro que yo leí en mi vida fue Matar un ruiseñor.\n ¡Y no me dio ninguna información sobre cómo matar ruiseñores!\n Sí, es cierto que me enseñó a no juzgar a un hombre por el color de su piel, ¿pero eso para qué me sirve?",
            "¡Oh Dios mío, aliens del espacio! Por favor, no me coman, tengo esposa e hijos, ¡cómanselos a ellos!.",
            "¡Bart, con 10 mil dólares seremos millonarios! Podremos comprar todo tipo de cosas útiles, como: ¡amor!",
            "¿Qué necesitamos de un psiquiatra? Ya sabemos que nuestros hijos están locos.",
            "Hoy estoy teniendo el mejor día de mi vida y todo se lo debo a ¡no ir a la iglesia!",
            "Tres pequeñas frases que te ayudarán a lo largo de tu vida:\n\n-¡Cúbreme!\n-¡Buena idea jefe!\n-Así estaba cuando llegué",
            "¿Cómo se supone que la educación me va a hacer más listo? Al contrario, cada vez que aprendo algo nuevo, algo que ya sabía desaparece de mi cerebro. ¿Recuerdas cuando tomé ese curso de fabricación de vino y se me olvidó conducir?",
            "Homero no funcionar cerveza bien sin.",
            "Nunca voy a estar de baja. Estoy enfermo de ser tan saludable.",
            "Me gusta mucho tener ideas contradictorias, porque así, aunque siempre estoy equivocado, siempre tengo la razón.",
            "Marge voy a pasarme toda la noche escribiendo. Haz café, bébelo y empieza a preparar hamburguesas.",
            "Marge, tienes muchas amigas; están Lisa.... la estufa...",
            "No estaba dormido... estaba ebrio.",
            "Si Marge se casa con Artie… ¡yo no naceré!",
            "No debes desanimarte. Seguro que Einstein se volvió de todos los colores antes de poder inventar el foco.",
            "Para mentir se necesitan dos: uno que mienta y otro que crea.",
            "Te advierto que si vas a enojarte conmigo cada vez que haga una estupidez, no tendré más remedio que dejar de hacer estupideces.",
            "¿Por qué es importante ir a ese edificio todos los domingos?, ¿no que Dios está en todas partes?",
            "Creo que odio a Michael Jackson. No, la verdad canta bien y es noble.",
            "Hijo, en un evento deportivo no importa quien gane o pierda, sino que tan ebrio te pongas.",
            "Quizá, sólo por una vez, alguien me llame 'Señor', sin añadir 'está usted haciéndo una escena'.",
            "Ya sé qué te puedo ofrecer, que nadie más puede hacerlo: completa y total dependencia.",
            "Dios es mi personaje de ficción favorito.",
            " Sólo digo que el matrimonio es un ataúd y cada hijo es otro clavo."]

client = commands.Bot(command_prefix='~')
client.remove_command('help')

@client.event
async def  on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("~ayuda"))
    print('Homero ha llegado, putas!')
    while True:
        VC = {i.name : i.id for i in client.guilds[0].voice_channels}
        with open('vc.json', 'w') as f:
            json.dump(VC, f, indent=2, ensure_ascii=False)
        f.close()
        await asyncio.sleep(3)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Homero no conoce ese comando")

@client.event
async def on_message(message):
    if message.channel.id == 730961452042682379: #ideas
        if message.content.startswith('Voto: '):
            await message.add_reaction("✅")
            await message.add_reaction("❌")
        else:
            await client.process_commands(message)
    else:
        await client.process_commands(message)

@client.command()
async def ayuda(ctx, categ = None):
    embed = discord.Embed(
        color = discord.Colour.red()
    )
    if categ == "muevenos":
        with open("vc.json") as f:
            data = json.load(f)
        f.close()
        embed.set_author(name = "Ayuda muevenos")
        embed.add_field(name = "Todos los parametros aceptables",
                        value = "\n\n".join(i for i in sorted(data)),
                        inline = False)
        embed.set_footer(text = "Importante: no es necesario escribir el emoji del nombre del canal.")
    elif categ == "clases":
        
        embed.add_field(name='~nuevaclase "nombreRamo" urlRamo dia',
                    value="Tambien ~nc\nAñade una sesion zoom con con los datos ingresados a un registro personal semestral",
                    inline=False)
        embed.add_field(name='~muestraclases dia @user',
                    value="Tambien ~mc\nMuestra las clases del dia para el usuario objetivo (@user)\nDe no especificar @user, se muestran las clases de quien ingreso el comando",
                    inline=False)
        embed.add_field(name='~borrarclases dia',
                    value="Elimina las Clases de un dia para la persona que ejecuta el comando\n PRECAUCION! BORRA TODAS LAS CLASES DEL DIA",
                    inline=False)
    
    else:
        embed.set_author(name="Ayuda General")
        embed.add_field(name="~ping",
                    value="Entrega el Ping de Homero",
                    inline=False)
        embed.add_field(name="~homero_habla",
                    value="Tambien ~hablar / ~habla / ~h\nEntrega una frase aleatoria de Homero",
                    inline=False)
        embed.add_field(name="~sr_thompson",
                    value="Tambien ~holaseñorthompson\nTu sabes que pasa",
                    inline=False)
        embed.add_field(name="~pintamicerca",
                    value="Pinta mi cerca!",
                    inline=False)
        embed.add_field(name="~pintamicocina",
                    value="Pinta mi cocina!",
                    inline=False)
        embed.add_field(name="~limpia n",
                    value="Limpia n comentarios en un chat de texto\nLimite: 200",
                    inline=False)
        embed.add_field(name="~muevenos nombre_canal",
                        value="Tambien ~m\nUsa >>~ayuda muevenos<< para mostrar los canales disponibles.",
                        inline=False)
        embed.add_field(name="~muestrafoto @user",
                    value="Tambien ~mf\nMuestra la foto del usuario objetivo @user")
    await ctx.send(embed=embed)

@client.command(aliases=['mf'])
async def muestrafoto(ctx, member : discord.Member):
    show_avatar = discord.Embed(
                  color = discord.Color.red()
                  )
    show_avatar.set_author(name=member.display_name)
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping de Homero: {round(client.latency * 1000)} ms')

@client.command(aliases=['hablar', 'habla', 'h'])
async def homero_habla(ctx):
    random.seed()
    await ctx.send(f'{random.choice(quotes)}')

@client.command(aliases=['holaseñorthompson', 'holasenorthompson'])
async def sr_thompson(ctx):
    user = random.choice(ctx.channel.guild.members)
    await ctx.send(file = discord.File("media/thompson.gif"))
    await ctx.send(f"Ah... creo que le habla a usted, {user.mention}...")

@client.command()
async def pintamicerca(ctx):
    await ctx.send(file = discord.File("media/cerca.gif"))
    await ctx.send(f"OBLIGAME!")

@client.command()
async def pintamicocina(ctx):
    await ctx.send(file = discord.File("media/cocina.gif"))
    await ctx.send(f"OBLIGAME!")

@client.command()
async def limpia(ctx, limite):
    l = (int)(limite)
    if l > 200:
        await ctx.send('Por el bien de todos, Homero solo sabe borrar hasta 200 comentarios')
        await asyncio.sleep(3)
        l = 200
    await ctx.channel.purge(limit = l+1)
    return 0

@client.command(aliases=['m'])
@commands.has_role("main_Borboton")
async def muevenos(ctx, *, nombre):
    with open('vc.json') as f:
        data = json.load(f)
    f.close()
    results_n = [i for i in data if nombre.lower() in i.lower()]
        
    if len(results_n) == 0:
        await ctx.send("No hay coincidencias de canales de voz con la entrada `{}`\nUsa **~ayuda muevenos** para ver la lista de parametros aceptables.".format(nombre))
    elif len(results_n) > 1:
        await ctx.send("Varias coincidencias con la entrada `{}` ```{}```".format(nombre, "\n".join(i for i in results_n)))
    else:
        toChannel = data[results_n[0]]
        fromChannel = ctx.author.voice.channel
        if fromChannel.id == toChannel:
            await ctx.send("Ya estas en ese canal")
        else:
            for member in fromChannel.members:
                await member.move_to(client.get_channel(toChannel))
                
            await ctx.send("Sí, señor!")

@client.command(aliases=["nc"])
async def nuevaclase(ctx, nombreRamo, urlRamo, dia):
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

    if dia.lower() in dias and urlRamo.startswith("http"):
        with open('classes.json') as f:
            data = json.load(f)
        if str(ctx.author) not in data:
            await ctx.send('Nuevo alumno ingresado al registro')

            data.update({str(ctx.author) : {
                        "lunes"     : {},
                        "martes"    : {},
                        "miercoles" : {},
                        "jueves"    : {},
                        "viernes"   : {}
                        }
                        })
                        
            data[str(ctx.author)][dia.lower()][nombreRamo] = urlRamo
            
        else:
            data[str(ctx.author)][dia.lower()][nombreRamo] = urlRamo
        
        await ctx.send("Link ingresado con exito: ```{}, {} para el dia {}```".format(nombreRamo, urlRamo, dia.lower()))

        with open('classes.json', 'w') as f: json.dump(data, f, indent=2, ensure_ascii=False)
        f.close()
    else:
        if dia.lower() not in dias: await ctx.send("El dia ingresado no es correcto")
        if not urlRamo.startswith("https://"): await ctx.send("El url ingresado no es valido (debe empezar con http:// (o https://))")
        await ctx.send("Para ver como ingresar bien una clase, usa **~ayuda clases**")

@client.command(aliases=["mc"])
async def muestraclases(ctx, dia, member : discord.Member = None):
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
    
    target = member if member != None else ctx.author

    with open('classes.json') as f:
        data = json.load(f)
    f.close()
    
    if str(target) in data and dia.lower() in dias:
        
        msg = ""
        
        if len(data[str(target)][dia.lower()]) > 0:
            await ctx.send("Tus ramos para el dia {} son:".format(dia.lower()))
            
            embed = discord.Embed(
                color = discord.Colour.red()
            )
        
            for ramo in data[str(target)][dia.lower()]:
                
                embed.add_field(name = ramo,
                            value = data[str(target)][dia.lower()][ramo],
                            inline = False)

            await ctx.send(embed = embed)

        else: await ctx.send("{} no tiene clases el dia {}!".format(target.mention, dia.lower()))
    
    else:
        if str(target) not in data: await ctx.send("{} no tiene clases ingresadas en el registro.".format(target.mention))
        if dia.lower() not in dias: await ctx.send("El dia ingresado no es correcto")
        await ctx.send("Para ver como ver bien una clase, usa **~ayuda clases**")

@client.command()
async def borrarclases(ctx, dia):
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

    with open('classes.json') as f: data = json.load(f)

    if str(ctx.author) in data and dia.lower() in dias:
        if len(data[str(ctx.author)][dia.lower()]) > 0:
            data[str(ctx.author)][dia.lower()] = {}
        
            with open('classes.json', 'w') as f: json.dump(data, f, indent=2, ensure_ascii=False)
            
            await ctx.send("Las clases de {} del dia {} fueron eliminadas".format(ctx.author.mention, dia.lower()))
        
        else: await ctx.send("{} no tiene clases el dia {}!".format(ctx.author.mention, dia.lower()))

    else:
        if str(ctx.author) not in data: await ctx.send("{} no tiene clases ingresadas en el registro.".format(ctx.author.mention))
        if dia.lower() not in dias: await ctx.send("El dia ingresado no es correcto")
        await ctx.send("Para ver como eliminar bien una clase, usa **~ayuda clases**")
    f.close()

@muevenos.error
async def muevenos_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('Homero no te conoce,\nNo tienes permiso.')

client.run(TOKEN)
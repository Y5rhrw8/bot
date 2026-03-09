import discord
from discord.ext import commands

TOKEN = "MTQ2OTUzODg5NzE5NjM1MTYyMA.GK-1Yu.Afuatr4TCHqIbe5t_63BROlRi2RwCnaRaqlNmQ"

ROL_AGREGAR = 1469934965947891722
ROL_QUITAR = 1469935217736290405

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

class PanelView(discord.ui.View):

    @discord.ui.button(label="Verificar", style=discord.ButtonStyle.green)
    async def verificar(self, interaction: discord.Interaction, button: discord.ui.Button):

        miembro = interaction.user

        rol_agregar = interaction.guild.get_role(ROL_AGREGAR)
        rol_quitar = interaction.guild.get_role(ROL_QUITAR)

        await miembro.add_roles(rol_agregar)
        await miembro.remove_roles(rol_quitar)

        await interaction.response.send_message(
            "Roles actualizados correctamente ✅",
            ephemeral=True
        )

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def panel(ctx):

    embed = discord.Embed(
        title="Panel de Verificación",
        description="Presiona el botón para verificarte",
        color=0x2ecc71
    )

    view = PanelView()

    await ctx.send(embed=embed, view=view)

import os
bot.run(os.getenv("TOKEN"))

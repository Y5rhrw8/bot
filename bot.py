import discord
from discord.ext import commands
import os

ROL_AGREGAR = 1469934965947891722
ROL_QUITAR = 1469935217736290405

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

class Panel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Verificar",
        style=discord.ButtonStyle.green,
        custom_id="verificar_panel"
    )
    async def verificar(self, interaction: discord.Interaction, button: discord.ui.Button):

        rol_add = interaction.guild.get_role(ROL_AGREGAR)
        rol_remove = interaction.guild.get_role(ROL_QUITAR)

        await interaction.user.add_roles(rol_add)
        await interaction.user.remove_roles(rol_remove)

        await interaction.response.send_message(
            "Ahora estás verificado ✅",
            ephemeral=True
        )

@bot.event
async def on_ready():
    bot.add_view(Panel())
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def panel(ctx):

    embed = discord.Embed(
        title="Panel de Verificación",
        description="Presiona el botón para verificarte",
        color=0x2ecc71
    )

    await ctx.send(embed=embed, view=Panel())

bot.run(TOKEN)


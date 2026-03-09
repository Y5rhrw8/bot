import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

ROL_AGREGAR = 123456789
ROL_QUITAR = 987654321

class Panel(discord.ui.View):

    @discord.ui.button(label="Verificar", style=discord.ButtonStyle.green)
    async def verificar(self, interaction: discord.Interaction, button: discord.ui.Button):

        rol_add = interaction.guild.get_role(ROL_AGREGAR)
        rol_remove = interaction.guild.get_role(ROL_QUITAR)

        await interaction.user.add_roles(rol_add)
        await interaction.user.remove_roles(rol_remove)

        await interaction.response.send_message("Roles actualizados ✅", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def panel(ctx):

    embed = discord.Embed(
        title="Verificación",
        description="Presiona el botón para verificarte",
        color=0x00ff00
    )

    await ctx.send(embed=embed, view=Panel())

bot.run(os.getenv("TOKEN"))

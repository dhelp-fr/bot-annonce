from nextcord import *
from nextcord.interactions import Interaction
from nextcord.ext.commands import Bot


class Confirm(ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @ui.button(label="Confirm", style=ButtonStyle.green)
    async def confirm(self, button: ui.Button, interaction: Interaction):
        self.value = True
        self.stop()

    @ui.button(label="Cancel", style=ButtonStyle.grey)
    async def cancel(self, button: ui.Button, interaction: Interaction):
        self.value = False
        self.stop()

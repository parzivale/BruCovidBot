from typing_extensions import ParamSpec
from commands.base_command  import BaseCommand
import requests
import matplotlib.pyplot as plt 
import pandas as pd
import discord

class CasesOverTime(BaseCommand):
        
    def __init__(self):
        description = "Graphs cases info from a selected period in the format YYYY-MM-DD"
        super().__init__(description, ["beggining","end"])

        
    async def handle(self, params, message, client):
        r = requests.get("https://graphics.thomsonreuters.com/data/2020/coronavirus/global-tracker/countries/brunei/counts/all.json").json()
        
        dates = []


        rangeofdates = pd.date_range(start=params[0],end=params[1])

        for element in r['cases']:
            if element['date'] in rangeofdates:
                dates.append(element["count"])
        
        path= "./commands/temp/fig.png"
        fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
        ax.plot(dates)
        ax.set_xlabel("days")
        ax.set_ylabel("cases")
        fig.savefig("./commands/temp/fig.png")   # save the figure to file
        plt.close(fig)      

        await  message.channel.send(file=discord.File(path))
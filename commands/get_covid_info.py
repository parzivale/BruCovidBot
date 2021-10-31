from typing_extensions import ParamSpec
from commands.base_command  import BaseCommand
import requests
from datetime import datetime



class getCases(BaseCommand):

    def __init__(self):

        description = "Pulls covid information from bruhealth in the format YYYY-MM-DD"
        super().__init__(description, ["date"])
        
    async def handle(self, param, message, client):
        r = requests.get("https://graphics.thomsonreuters.com/data/2020/coronavirus/global-tracker/countries/brunei/counts/all.json").json()

        try:
            todaysCases = "N/A"

            if(param[0] == "yesterday"):

                time = []
                now = datetime.now()
                time.append(now.strftime("%Y"))
                time.append(now.strftime("%m"))
                time.append(str(int(now.strftime("%d"))-1))
                today = "-".join(time)

                for i in r["cases"]:
                    if i["date"] == today:
                        todaysCases = i["count"]
                
                msg = f"Covid cases {param[0]}: {todaysCases}"

            else:

                for i in r["cases"]:
                    if i["date"] == param[0]:
                        todaysCases = i["count"]
                
                msg = f"Covid cases on {param[0]}: {todaysCases}"




        except:
            msg = "Invaild"

        await message.channel.send(msg)

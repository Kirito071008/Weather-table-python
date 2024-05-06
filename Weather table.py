import pandas as pd
import matplotlib.pyplot as plt
import python_weather,os,asyncio,platform,pyfiglet
from datetime import date,timedelta
sunrise,sunset,data, = [],[],[]
temperature = []
k = 0
today = date.today()
for day in range(3):
   if k == 0:
      d = (today - timedelta(days=1)).isoformat()
      data.append(d)
      k += 1
   else:
    d = (today + timedelta(days = day-1)).isoformat()
    data.append(d)
if platform.system() == "Windows":
    def clear(): os.system("cls")
else:
    def clear(): os.system("clear")
async def getWeather():
    clear()
    ascii_banner = pyfiglet.figlet_format("Weather")
    print("By Kirito071008 :D")
    print(ascii_banner)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
      try:
       x = input("Name of the city: ")
       weather = await client.get(f'{x}')
       for d in weather.forecasts:
         #sunrise.append(d.astronomy.sun_rise),sunset.append(d.astronomy.sun_set) #You can use them if you want
         temperature.append((round((d.temperature-32)*(5/9))))  
      except RuntimeError:
         getWeather()
    df = pd.DataFrame({
       "data": data,
       "temp": temperature,
       })
    df.plot(kind="line",x="data",y="temp",color="black",title="Temperature",fontsize=10)
    plt.show()
    x = input("Continue?").lower()
    if x == "yes" or x == "y":
       getWeather()
    else:
       print("See you next time! :D")
asyncio.run(getWeather())

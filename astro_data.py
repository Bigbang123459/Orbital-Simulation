import json
import datetime
from astroquery.jplhorizons import Horizons

now = datetime.datetime.now()
start_time = now.strftime("%Y-%m-%d %H:%M")
end_time = (now + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")

earth = Horizons(id='399', location='500@0', epochs={'start': start_time, 'stop': end_time, 'step': '1m'}).vectors()
lunar = Horizons(id='301', location='500@0', epochs={'start': start_time, 'stop': end_time, 'step': '1m'}).vectors()
sun = Horizons(id='10', location='500@0', epochs={'start': start_time, 'stop': end_time, 'step': '1m'}).vectors()
mercury = Horizons(id='199', location='500@0', epochs={'start': start_time, 'stop': end_time, 'step': '1m'}).vectors()
venus = Horizons(id='299', location='500@0', epochs={'start': start_time, 'stop': end_time, 'step': '1m'}).vectors()
mars = Horizons(id='499', location='500@0', epochs={'start': start_time, 'stop': end_time, 'step': '1m'}).vectors()

data = {
    "earth": {
        "position": [float(earth['x'][0])*1.496e11 , float(earth['y'][0])*1.496e11, float(earth['z'][0])*1.496e11],
        "velocity": [float(earth['vx'][0])*1.496e11/86400 , float(earth['vy'][0])*1.496e11/86400, float(earth['vz'][0])*1.496e11/86400]
    },
    "lunar": {
        "position": [float(lunar['x'][0])*1.496e11, float(lunar['y'][0])*1.496e11, float(lunar['z'][0])*1.496e11],
        "velocity": [float(lunar['vx'][0])*1.496e11/86400, float(lunar['vy'][0])*1.496e11/86400, float(lunar['vz'][0])*1.496e11/86400]
    },
    "sun": {
        "position": [float(sun['x'][0])*1.496e11, float(sun['y'][0])*1.496e11, float(sun['z'][0])*1.496e11],
        "velocity": [float(sun['vx'][0])*1.496e11/86400, float(sun['vy'][0])*1.496e11/86400, float(sun['vz'][0])*1.496e11/86400]
    },
    "mercury": {
        "position": [float(mercury['x'][0])*1.496e11, float(mercury['y'][0])*1.496e11, float(mercury['z'][0])*1.496e11],
        "velocity": [float(mercury['vx'][0])*1.496e11/86400, float(mercury['vy'][0])*1.496e11/86400, float(mercury['vz'][0])*1.496e11/86400]
    },
    "venus": {
        "position": [float(venus['x'][0])*1.496e11, float(venus['y'][0])*1.496e11, float(venus['z'][0])*1.496e11],
        "velocity": [float(venus['vx'][0])*1.496e11/86400, float(venus['vy'][0])*1.496e11/86400, float(venus['vz'][0])*1.496e11/86400]
    },
    "mars": {
        "position": [float(mars['x'][0])*1.496e11, float(mars['y'][0])*1.496e11, float(mars['z'][0])*1.496e11],
        "velocity": [float(mars['vx'][0])*1.496e11/86400, float(mars['vy'][0])*1.496e11/86400, float(mars['vz'][0])*1.496e11/86400]
    }

}

with open('orbital_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Orbital data has been saved to 'orbital_data.json'.")
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime

with open('orbital_data.json','r') as f:
    data = json.load(f)

mercury_pos = np.array(data['mercury']['position'], dtype=float)
mercury_delta_vel = np.array(data['mercury']['velocity'], dtype=float)

venus_pos = np.array(data['venus']['position'], dtype=float)
venus_delta_vel = np.array(data['venus']['velocity'], dtype=float)

earth_pos = np.array(data['earth']['position'], dtype=float)
earth_delta_vel = np.array(data['earth']['velocity'], dtype=float)

moon_pos = np.array(data['lunar']['position'], dtype=float)
moon_delta_vel = np.array(data['lunar']['velocity'], dtype=float)

mars_pos = np.array(data['mars']['position'], dtype=float)
mars_delta_vel = np.array(data['mars']['velocity'], dtype=float)

sun_pos = np.array([0, 0, 0], dtype=float)  

#วางตัวแปร
G = 6.67430e-11
m_sun = 1.989e30
m_mercury = 3.3011e23
m_venus = 4.8675e24
m_earth = 5.972e24
m_moon = 7.348e22
m_mars = 6.39e23
dt = 3600 * 7 #ตอนแรกเป็นวินาที

#ตั้งค่ากราฟ 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

#สร้างวัตถุ
sun_dot = ax.scatter([0], [0], [0], color='yellow', s=500, label='Sun')
mercury_dot = ax.scatter([], [], [], color='orange', s=150, label='Mercury')
venus_dot = ax.scatter([], [], [], color='green', s=200, label='Venus')
earth_dot = ax.scatter([], [], [], color='blue', s=250, label='Earth')
moon_dot = ax.scatter([], [], [], color='gray', s=100, label='Moon')
mars_dot = ax.scatter([], [], [], color='red', s=200, label='Mars')

#เก็บข้อมูลเส้นทาง
mercury_trail_x = []
mercury_trail_y = []
mercury_trail_z = []
mercury_trail_line, = ax.plot([], [], [], color='orange', alpha=0.5, linestyle='--')

venus_trail_x = []
venus_trail_y = []
venus_trail_z = []
venus_trail_line, = ax.plot([], [], [], color='green', alpha=0.5, linestyle='--')

earth_trail_x = []
earth_trail_y = []
earth_trail_z = []
earth_trail_line, = ax.plot([], [], [], color='blue', alpha=0.5, linestyle='--')

moon_trail_x = []
moon_trail_y = []
moon_trail_z = []
moon_trail_line, = ax.plot([], [], [], color='gray', alpha=0.5, linestyle='--')

mars_trail_x = []
mars_trail_y = []
mars_trail_z = []
mars_trail_line, = ax.plot([], [], [], color='red', alpha=0.5, linestyle='--')

#ตั้งขอบเขตของกราฟ
limit = 1.8e11
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit/2, limit/2)

ax.set_xlabel('X (meters)')
ax.set_ylabel('Y (meters)')
ax.set_zlabel('Z (meters)')
ax.set_title('Earth Orbital Simulation ')
ax.legend()

X_axis = np.array([1, 0, 0], dtype=float) 
total_seconds = 0 #เก็บเวลาไว้

#calculate
def update(frame):
    global earth_pos, earth_delta_vel, moon_pos, moon_delta_vel, mercury_pos, mercury_delta_vel, venus_pos, venus_delta_vel, mars_pos, mars_delta_vel, total_seconds

    for _ in range(5):

        vector_sun_mercury = sun_pos - mercury_pos
        F_sun_mercury = (G * m_sun * m_mercury / np.linalg.norm(vector_sun_mercury)**3) * vector_sun_mercury
        vector_mercury_earth = earth_pos - mercury_pos
        F_mercury_earth = (G * m_mercury * m_earth / np.linalg.norm(vector_mercury_earth)**3) * vector_mercury_earth
        
        vector_sun_venus = sun_pos - venus_pos
        F_sun_venus = (G * m_sun * m_venus / np.linalg.norm(vector_sun_venus)**3) * vector_sun_venus
        vector_venus_earth = earth_pos - venus_pos
        F_venus_earth = (G * m_venus * m_earth / np.linalg.norm(vector_venus_earth)**3) * vector_venus_earth

        vector_sun_mars = sun_pos - mars_pos
        F_sun_mars = (G * m_sun * m_mars / np.linalg.norm(vector_sun_mars)**3) * vector_sun_mars
        vector_mars_earth = earth_pos - mars_pos
        F_mars_earth = (G * m_mars * m_earth / np.linalg.norm(vector_mars_earth)**3) * vector_mars_earth
        
        vector_sun_earth = sun_pos - earth_pos
        F_sun_earth = (G * m_sun * m_earth / np.linalg.norm(vector_sun_earth)**3) * vector_sun_earth

        vector_earth_moon = moon_pos - earth_pos
        F_earth_moon = (G * m_earth * m_moon / np.linalg.norm(vector_earth_moon)**3) * vector_earth_moon
        F_net_earth = F_sun_earth + F_earth_moon + F_mercury_earth + F_venus_earth

        vector_sun_moon = sun_pos - moon_pos
        F_sun_moon = (G * m_sun * m_moon / np.linalg.norm(vector_sun_moon)**3) * vector_sun_moon

        F_moon_earth = -F_earth_moon
        F_net_moon = F_sun_moon + F_moon_earth

        mercury_delta_vel += F_sun_mercury / m_mercury * dt
        mercury_pos += mercury_delta_vel * dt

        venus_delta_vel += F_sun_venus / m_venus * dt
        venus_pos += venus_delta_vel * dt

        earth_delta_vel += F_net_earth / m_earth * dt
        earth_pos += earth_delta_vel * dt

        moon_delta_vel += F_net_moon / m_moon * dt
        moon_pos += moon_delta_vel * dt

        mars_delta_vel += F_sun_mars / m_mars * dt
        mars_pos += mars_delta_vel * dt

        total_seconds += dt

        pass

    #หามุม
    angle_mercury = np.arctan2(mercury_pos[1], mercury_pos[0])
    angle_mercury_deg = np.degrees(angle_mercury)
    if angle_mercury_deg < 0:
        angle_mercury_deg += 360

    angle_venus = np.arctan2(venus_pos[1], venus_pos[0])
    angle_venus_deg = np.degrees(angle_venus)
    if angle_venus_deg < 0:
        angle_venus_deg += 360

    angle_earth = np.arctan2(earth_pos[1], earth_pos[0])
    angle_earth_deg = np.degrees(angle_earth)
    if angle_earth_deg < 0:
        angle_earth_deg += 360

    angle_mars = np.arctan2(mars_pos[1], mars_pos[0])
    angle_mars_deg = np.degrees(angle_mars)
    if angle_mars_deg < 0:
        angle_mars_deg += 360

    vector_relative = moon_pos - earth_pos

    angle_moon = np.arctan2(vector_relative[1], vector_relative[0])
    angle_moon_deg = np.degrees(angle_moon)
    if angle_moon_deg < 0:
        angle_moon_deg += 360

    #หาวันที่
    start_date = datetime.datetime(2026, 6, 12)
    current_date = start_date + datetime.timedelta(seconds=total_seconds)

    date_str = current_date.strftime("%Y-%m-%d")

    ax.set_title(f'Earth Angle:{angle_earth_deg:.2f}° | Earth-Moon Angle:{angle_moon_deg:.2f}° | Mercury Angle:{angle_mercury_deg:.2f}° | Venus Angle:{angle_venus_deg:.2f}° | Mars Angle:{angle_mars_deg:.2f} | Date:{date_str}')


    scaled_moon_pos = earth_pos + (vector_relative * 30)

    earth_dot._offsets3d = ([earth_pos[0]], [earth_pos[1]], [earth_pos[2]])
    moon_dot._offsets3d = ([scaled_moon_pos[0]], [scaled_moon_pos[1]], [scaled_moon_pos[2]])

    earth_trail_x.append(earth_pos[0])
    earth_trail_y.append(earth_pos[1])
    earth_trail_z.append(earth_pos[2])
    earth_trail_line.set_data(earth_trail_x, earth_trail_y)
    earth_trail_line.set_3d_properties(earth_trail_z)

    moon_trail_x.append(scaled_moon_pos[0])
    moon_trail_y.append(scaled_moon_pos[1])
    moon_trail_z.append(scaled_moon_pos[2])
    moon_trail_line.set_data(moon_trail_x, moon_trail_y)
    moon_trail_line.set_3d_properties(moon_trail_z)

    mercury_dot._offsets3d = ([mercury_pos[0]], [mercury_pos[1]], [mercury_pos[2]])
    venus_dot._offsets3d = ([venus_pos[0]], [venus_pos[1]], [venus_pos[2]])
    mars_dot._offsets3d = ([mars_pos[0]], [mars_pos[1]], [mars_pos[2]])

    mercury_trail_x.append(mercury_pos[0])
    mercury_trail_y.append(mercury_pos[1])
    mercury_trail_z.append(mercury_pos[2])
    mercury_trail_line.set_data(mercury_trail_x, mercury_trail_y)
    mercury_trail_line.set_3d_properties(mercury_trail_z)

    venus_trail_x.append(venus_pos[0])
    venus_trail_y.append(venus_pos[1])
    venus_trail_z.append(venus_pos[2])
    venus_trail_line.set_data(venus_trail_x, venus_trail_y)
    venus_trail_line.set_3d_properties(venus_trail_z)

    mars_trail_x.append(mars_pos[0])
    mars_trail_y.append(mars_pos[1])
    mars_trail_z.append(mars_pos[2])
    mars_trail_line.set_data(mars_trail_x, mars_trail_y)
    mars_trail_line.set_3d_properties(mars_trail_z)

    return earth_dot, moon_dot, earth_trail_line, moon_trail_line, mercury_dot, venus_dot, mercury_trail_line, venus_trail_line, mars_dot, mars_trail_line

animation = FuncAnimation(fig, update, frames=range(1000), interval=1, blit=False)

try:
    plt.show()
except AttributeError:
    pass
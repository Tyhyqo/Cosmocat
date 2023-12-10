import time
import krpc

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

conn = krpc.connect()
vessel = conn.space_center.active_vessel

target_altitude = 150000

altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')

met = conn.add_stream(getattr, vessel, 'met')
mass = conn.add_stream(getattr, vessel, 'mass')
dry_mass = conn.add_stream(getattr, vessel, 'dry_mass')

pitch = conn.add_stream(getattr, vessel.flight(), 'pitch')
speed = conn.add_stream(getattr, vessel.flight(), 'speed')

horizontal_speed = conn.add_stream(getattr, vessel.flight(),
                                   'horizontal_speed')
vertical_speed = conn.add_stream(getattr, vessel.flight(),
                                 'vertical_speed')

met_stat = list()
mass_stat = list()
pitch_stat = list()
speed_stat = list()
dry_mass_stat = list()
altitude_stat = list()
horizontal_speed_stat = list()
vertical_speed_stat = list()

while apoapsis() <= target_altitude * 0.9:
    time.sleep(0.2)
    met_stat.append(met())
    mass_stat.append(mass())
    pitch_stat.append(pitch())
    speed_stat.append(speed())
    dry_mass_stat.append(dry_mass())
    altitude_stat.append(altitude())
    horizontal_speed_stat.append(horizontal_speed())
    vertical_speed_stat.append(vertical_speed())
    print(speed())

fig, ax = plt.subplots()
ax.plot(vertical_speed_stat, horizontal_speed_stat)
plt.show()

import time
import krpc
import matplotlib.pyplot as plt

conn = krpc.connect()
vessel = conn.space_center.active_vessel

target_altitude = 150000

altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
apoapsis = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')

met = conn.add_stream(getattr, vessel, 'met')
mass = conn.add_stream(getattr, vessel, 'mass')
dry_mass = conn.add_stream(getattr, vessel, 'dry_mass')

pitch = conn.add_stream(getattr, vessel.flight(), 'pitch')
speed = conn.add_stream(getattr, vessel.flight(vessel.orbit.body.
                                               reference_frame), 'speed')

horizontal_speed = conn.add_stream(getattr, vessel.flight(vessel.
                                                          orbit.body.
                                                          reference_frame),
                                   'horizontal_speed')
vertical_speed = conn.add_stream(getattr, vessel.flight(vessel.
                                                        orbit.body.
                                                        reference_frame),
                                 'vertical_speed')
fuel = conn.add_stream(vessel.resources.amount, 'LiquidFuel')

met_stat = list()
fuel_stat = list()
mass_stat = list()
pitch_stat = list()
speed_stat = list()
dry_mass_stat = list()
altitude_stat = list()
horizontal_speed_stat = list()
vertical_speed_stat = list()

while altitude() <= 3000:
    pass

while altitude() > 3000:
    time.sleep(0.2)
    met_stat.append(met())
    fuel_stat.append(fuel())
    mass_stat.append(mass())
    pitch_stat.append(pitch())
    speed_stat.append(speed())
    dry_mass_stat.append(dry_mass())
    altitude_stat.append(altitude())
    horizontal_speed_stat.append(horizontal_speed())
    vertical_speed_stat.append(vertical_speed())

fig_speed, ax_speed = plt.subplots()
ax_speed.plot(speed_stat, met_stat)
ax_speed.set_title('Зависимость скорости v от времени t')
ax_speed.set_xlabel('Скорость v')
ax_speed.set_ylabel('Время t')
plt.show()

fig_mass, ax_mass = plt.subplots()
ax_mass.plot(mass_stat, met_stat)
ax_mass.set_title('Зависимость массы m от времени t')
ax_mass.set_xlabel('Масса m')
ax_mass.set_ylabel('Время t')
plt.show()

fig_altitude, ax_altitude = plt.subplots()
ax_altitude.plot(altitude_stat, met_stat)
ax_altitude.set_title('Зависимость высоты h от времени t')
ax_altitude.set_xlabel('Высота h')
ax_altitude.set_ylabel('Время t')
plt.show()

fig_fuel, ax_fuel = plt.subplots()
ax_fuel.plot(fuel_stat, met_stat)
ax_fuel.set_title('Зависимость кол-ва топлива от времени t')
ax_fuel.set_xlabel('Кол-во топлива')
ax_fuel.set_ylabel('Время t')
plt.show()

import krpc
import matplotlib.pyplot as plt

conn = krpc.connect()
vessel = conn.space_center.active_vessel

target_altitude = 150000

altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')

met = conn.add_stream(getattr, vessel, 'met')
mass = conn.add_stream(getattr, vessel, 'mass')

speed = conn.add_stream(getattr, vessel.flight(vessel.orbit.body.
                                               reference_frame), 'speed')

fuel = conn.add_stream(vessel.resources.amount, 'LiquidFuel')

met_stat = list()
fuel_stat = list()
mass_stat = list()
speed_stat = list()
altitude_stat = list()

rocket_climb = True

while altitude() > 2000 or rocket_climb:
    if rocket_climb and altitude() > 2000:
        rocket_climb = False
    met_stat.append(met())
    fuel_stat.append(fuel())
    mass_stat.append(mass())
    speed_stat.append(speed())
    altitude_stat.append(altitude())

fig_speed, ax_speed = plt.subplots()
ax_speed.plot(met_stat, speed_stat)
ax_speed.set_title('Зависимость скорости v от времени t')
ax_speed.set_ylabel('Скорость v')
ax_speed.set_xlabel('Время t')
plt.show()

fig_mass, ax_mass = plt.subplots()
ax_mass.plot(met_stat, mass_stat)
ax_mass.set_title('Зависимость массы m от времени t')
ax_mass.set_ylabel('Масса m')
ax_mass.set_xlabel('Время t')
plt.show()

fig_altitude, ax_altitude = plt.subplots()
ax_altitude.plot(met_stat, altitude_stat)
ax_altitude.set_title('Зависимость высоты h от времени t')
ax_altitude.set_ylabel('Высота h')
ax_altitude.set_xlabel('Время t')
plt.show()

fig_fuel, ax_fuel = plt.subplots()
ax_fuel.plot(met_stat, fuel_stat)
ax_fuel.set_title('Зависимость кол-ва топлива от времени t')
ax_fuel.set_ylabel('Кол-во топлива')
ax_fuel.set_xlabel('Время t')
plt.show()

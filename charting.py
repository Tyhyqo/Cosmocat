import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect('data.db')
cur = con.cursor()

met_stat = list(map(lambda x: x[0],
                    cur.execute('SELECT met FROM vessel_values').fetchall()))

speed_stat = list(map(lambda x: x[0],
                      cur.execute(
                          'SELECT speed FROM vessel_values').fetchall()))
fig_speed, ax_speed = plt.subplots()
ax_speed.plot(met_stat, speed_stat)
ax_speed.set_title('Зависимость скорости v от времени t')
ax_speed.set_ylabel('Скорость v, м/с')
ax_speed.set_xlabel('Время t, с')
plt.show()
speed_stat.clear()

mass_stat = list(map(lambda x: x[0],
                     cur.execute('SELECT mass FROM vessel_values').fetchall()))
fig_mass, ax_mass = plt.subplots()
ax_mass.plot(met_stat, mass_stat)
ax_mass.set_title('Зависимость массы m от времени t')
ax_mass.set_ylabel('Масса m, кг')
ax_mass.set_xlabel('Время t, с')
plt.show()
mass_stat.clear()

altitude_stat = list(map(lambda x: x[0],
                         cur.execute(
                             'SELECT altitude FROM vessel_values').fetchall()))
fig_altitude, ax_altitude = plt.subplots()
ax_altitude.plot(met_stat, altitude_stat)
ax_altitude.set_title('Зависимость высоты h от времени t')
ax_altitude.set_ylabel('Высота h, м')
ax_altitude.set_xlabel('Время t, с')
plt.show()
altitude_stat.clear()

fuel_stat = list(map(lambda x: x[0],
                     cur.execute('SELECT fuel FROM vessel_values').fetchall()))
fig_fuel, ax_fuel = plt.subplots()
ax_fuel.plot(met_stat, fuel_stat)
ax_fuel.set_title('Зависимость кол-ва топлива от времени t')
ax_fuel.set_ylabel('Кол-во топлива')
ax_fuel.set_xlabel('Время t, с')
plt.show()
fuel_stat.clear()

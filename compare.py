import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect('data.db')
cur = con.cursor()

met_stat = list(map(lambda x: x[0],
                    cur.execute('SELECT met FROM vessel_values').fetchall()))
mass_stat = list(map(lambda x: x[0],
                     cur.execute('SELECT mass FROM vessel_values').fetchall()))
for ind in range(len(met_stat)):
    if int(met_stat[ind]) == 338:
        met_stat = met_stat[:ind]
        mass_stat = mass_stat[:ind]
        break


def m(t):
    if t == 0:
        return 50000
    elif 0 < t <= 80:
        return 50000 - 9000 * 3 / 80 * t
    elif 80 < t < 115:
        return 13409 - 4490 / 35 * (t - 80)
    elif 115 <= t < 320:
        return 9035
    elif 320 <= t < 338:
        return 9035 - 4490 / 18 * (t - 320)


mass_model_stat = []
time_stat = []
time = 0
while time < 338:
    mass_model_stat.append(m(time))
    time_stat.append(round(time, 1))
    time += 0.1

fig_mass, ax_mass = plt.subplots()
ax_mass.plot(met_stat, mass_stat, label='Kerbal Space Program')
ax_mass.plot(time_stat, mass_model_stat, label='Математическая модель')
ax_mass.set_title('Зависимость массы m от времени t')
ax_mass.set_ylabel('Масса m, кг')
ax_mass.set_xlabel('Время t, с')
ax_mass.legend()
plt.show()
mass_stat.clear()

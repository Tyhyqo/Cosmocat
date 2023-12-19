import krpc
import sqlite3
import time

con = sqlite3.connect('data.db')
cur = con.cursor()

conn = krpc.connect()
vessel = conn.space_center.active_vessel

target_altitude = 150000
altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
met = conn.add_stream(getattr, vessel, 'met')
mass = conn.add_stream(getattr, vessel, 'mass')

speed = conn.add_stream(getattr, vessel.flight(vessel.orbit.body.
                                               reference_frame), 'speed')
fuel = conn.add_stream(vessel.resources.amount, 'LiquidFuel')

start_altitude = altitude()
while altitude() <= start_altitude + 10:
    pass

rocket_climb = True

while altitude() > 2000 or rocket_climb:
    if rocket_climb and altitude() > 2000:
        rocket_climb = False
    time.sleep(1)
    cur.execute(f'''INSERT INTO vessel_values 
                    VALUES({met()}, {fuel()}, {mass()}, {speed()}, {altitude()}
                    )''')
    con.commit()

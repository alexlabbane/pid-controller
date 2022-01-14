from time import sleep
import krpc
from time import time
import matplotlib.pyplot as plt

conn = krpc.connect(name="Hover PID")
print(conn.krpc.get_status().version)

vessel = conn.space_center.active_vessel

body = vessel.orbit.body
control = vessel.control
surface_ref_frame = conn.space_center.ReferenceFrame.create_hybrid(
    body.reference_frame,
    vessel.surface_reference_frame,
    body.reference_frame,
    body.reference_frame
)


# Constants
target_altitude = 700
k = -1 / (target_altitude * 0.35)
ki = -1 / (target_altitude * 10)
kd = -1 / (target_altitude * 0.07)
total_time = 300 # how many seconds to run the controller

plt.axis([0, total_time, -500, 500])

# p, i ,d
p = 0
i = 0
d = 0

prev_altitude = vessel.flight(body.reference_frame).mean_altitude
prev_error = prev_altitude - target_altitude
start_time = time()
prev_measurement = start_time
x = []
y = []
sleep(0.2)
while time() - start_time < total_time:
    altitude = vessel.flight(body.reference_frame).mean_altitude
    measurement = time()

    p = altitude - target_altitude

    integral_error = p + prev_error
    if integral_error > 100:
        integral_error = 100
    if integral_error < -100:
        integral_error = -100

    i += abs(measurement - prev_measurement) * (integral_error) / 2
    d = (p - prev_error) / abs(measurement - prev_measurement)
    control.throttle = k * p + ki * i + kd * d
    print("p =", p, ", i =", i, "d =", d, "throttle = ", control.throttle)

    prev_altitude = altitude
    prev_measurement = measurement
    prev_error = p

    x.append(measurement - start_time)
    y.append(p)
    sleep(0.1)

plt.plot(x, y)
plt.show()
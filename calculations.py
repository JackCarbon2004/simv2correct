import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import json

#eq
def pendulum_eqn(theta, t, L, g):
    return [theta[1], -(g/L)*np.sin(theta[0])]

#defs
def simulate_pendulum(L, g, theta0, dt, t_max):
    t = np.arange(0, t_max, dt)
    theta = np.zeros((len(t), 2))
    theta[0] = [theta0, 0]

    height_data = np.zeros(len(t))
    theta_data = np.zeros(len(t))

    for i in range(1, len(t)):
        theta[i] = theta[i-1] + dt * np.array(pendulum_eqn(theta[i-1], t[i-1], L, g))
        height_data[i] = -L * np.cos(theta[i, 0])
        theta_data[i] = theta[i, 0]

    return t, theta, height_data, theta_data

#animation
def animate_pendulum(frame):
    i = frame % len(t)
    x = L * np.sin(thetas[i, 0])
    y = -L * np.cos(thetas[i, 0])
    line.set_data([0, x], [0, y])
    time_text.set_text(f"Time: {t[i]:.2f}s")
    length_text.set_text(f"Length: {L:.2f}m")
    return line, time_text, length_text

# Parameters
g = 10
L = 10 
theta0 = np.pi/6
dt = 0.02
t_max = 120  
animation_speed = 5 

#figures 
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

ax1.set_xlim(-L*1.1, L*1.1)
ax1.set_ylim(-L*1.1, L*1.1)
ax1.set_aspect('equal')
ax1.grid()

line, = ax1.plot([], [], 'o-', lw=2)
time_text = ax1.text(0.05, 0.9, "", transform=ax1.transAxes)
length_text = ax1.text(0.05, 0.85, "", transform=ax1.transAxes)

t, thetas, height_data, theta_data = simulate_pendulum(L, g, theta0, dt, t_max)

ani = FuncAnimation(fig, animate_pendulum, frames=len(t)*animation_speed, interval=dt*1000/animation_speed, blit=True, repeat=True)

ax2.plot(t, height_data)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Height (m)")
ax2.grid()

ax3.plot(t, theta_data)
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Theta (rad)")
ax3.grid()

plt.tight_layout()
plt.show()

# Save data to JSON file
data = {
    "time": list(t),
    "height": list(height_data),
    "theta": list(theta_data)
}

with open("pendulum_data.json", "w") as file:
    json.dump(data, file)
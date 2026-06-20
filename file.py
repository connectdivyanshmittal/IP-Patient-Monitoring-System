import matplotlib.pyplot as plt
import random
import time

# Enable interactive plotting
plt.ion()
fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

# Create lines for both patients (P1 and P2)
lines = {
    'hr': [axs[0].plot([], [], label='P1 HR', color='red')[0],
           axs[0].plot([], [], label='P2 HR', color='orange')[0]],
    'spo2': [axs[1].plot([], [], label='P1 SpO2', color='blue')[0],
             axs[1].plot([], [], label='P2 SpO2', color='cyan')[0]],
    'temp': [axs[2].plot([], [], label='P1 Temp', color='green')[0],
             axs[2].plot([], [], label='P2 Temp', color='lime')[0]]
}

# Graph titles and labels
titles = ['Heart Rate (bpm)', 'SpO2 (%)', 'Temperature (°C)']
for i, ax in enumerate(axs):
    ax.set_title(titles[i])
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)
axs[2].set_xlabel('Time (Reading Index)')

# Initialize lists for storing values
p1_hr, p2_hr = [], []
p1_spo2, p2_spo2 = [], []
p1_temp, p2_temp = [], []

x_vals = []

reading_num = 0

# Real-time loop
while True:
    try:
        reading_num += 1
        x_vals.append(reading_num)

        # Generate random values for both patients
        p1_hr.append(random.randint(70, 100))
        p2_hr.append(random.randint(68, 98))

        p1_spo2.append(random.randint(94, 99))
        p2_spo2.append(random.randint(93, 98))

        p1_temp.append(round(random.uniform(36.3, 37.4), 1))
        p2_temp.append(round(random.uniform(36.4, 37.5), 1))

        # Keep last 20 readings for scrolling
        x_recent = x_vals[-20:]
        p1_hr_recent, p2_hr_recent = p1_hr[-20:], p2_hr[-20:]
        p1_spo2_recent, p2_spo2_recent = p1_spo2[-20:], p2_spo2[-20:]
        p1_temp_recent, p2_temp_recent = p1_temp[-20:], p2_temp[-20:]

        # Update graph data
        lines['hr'][0].set_data(x_recent, p1_hr_recent)
        lines['hr'][1].set_data(x_recent, p2_hr_recent)
        lines['spo2'][0].set_data(x_recent, p1_spo2_recent)
        lines['spo2'][1].set_data(x_recent, p2_spo2_recent)
        lines['temp'][0].set_data(x_recent, p1_temp_recent)
        lines['temp'][1].set_data(x_recent, p2_temp_recent)

        # Update limits for smooth scrolling
        for ax in axs:
            ax.set_xlim(max(0, reading_num - 20), reading_num)
            ax.relim()
            ax.autoscale_view()

        plt.draw()
        plt.pause(0.5)
        time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nLive simulation stopped.")
        break

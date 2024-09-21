import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Skills and their strength levels
skills = ['Coding', 'Leadership', 'Communication', 'Presentation designing']
strengths = [83, 21, 8, 98]

# --- Create Radar Chart ---
# Define the skill and strength data
categories = skills
values = strengths
N = len(categories)

# What will be the angle of each axis in the radar chart (we divide the plot / number of variables)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Complete the loop by connecting the last value to the first

# Strength levels need to be repeated to complete the loop
values += values[:1]

# Initialize the radar chart
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)

# Draw one axis per skill and label it
plt.xticks(angles[:-1], categories)

# Plot the data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill the area under the plot
ax.fill(angles, values, 'skyblue', alpha=0.4)

plt.title('Strength-Skill Radar Chart')

# Save the radar chart to a bytes buffer
buf_radar = io.BytesIO()
plt.savefig(buf_radar, format='png')
buf_radar.seek(0)

# Convert the buffer contents to a base64 string for the radar chart
img_data_radar = base64.b64encode(buf_radar.getvalue()).decode('utf-8')

# --- Generate HTML with both bar and radar charts ---
html = f"""
<html>
<head><title>Strength-Skill Graphs</title></head>
<body>
    <h2>Radar Chart - Strength-Skill Graph</h2>
    <img src="data:image/png;base64,{img_data_radar}" />
</body>
</html>
"""

# Save the HTML to a file
with open("strength_skill_graph.html", "w") as f:
    f.write(html)

print("HTML file with bar and radar charts has been created!")

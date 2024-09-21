import matplotlib.pyplot as plt
import io
import base64

# Data for the chart
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [10, 20, 15, 25]

# --- Create Bar Chart ---
plt.figure(figsize=(8, 4))  # Set figure size
plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.title('Bar Chart with Four Elements')

# Save the bar chart to a bytes buffer
buf_bar = io.BytesIO()
plt.savefig(buf_bar, format='png')
buf_bar.seek(0)

# Convert the buffer contents to a base64 string for the bar chart
img_data_bar = base64.b64encode(buf_bar.getvalue()).decode('utf-8')

# Clear the figure to avoid overlap
plt.clf()

# --- Create Pie Chart ---
plt.figure(figsize=(8, 4))  # Set figure size
plt.pie(values, labels=categories, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'])
plt.title('Pie Chart with Four Elements')

# Save the pie chart to a bytes buffer
buf_pie = io.BytesIO()
plt.savefig(buf_pie, format='png')
buf_pie.seek(0)

# Convert the buffer contents to a base64 string for the pie chart
img_data_pie = base64.b64encode(buf_pie.getvalue()).decode('utf-8')
# Generate HTML with the embedded image
html = f"""
<html>
<head><title>Chart</title></head>
<body>
    <h2>Bar Chart with Four Elements</h2>
    <img src="data:image/png;base64,{img_data_bar}" />
    <h2>Pie Chart with Four Elements</h2>
    <img src="data:image/png;base64,{img_data_pie}" />
</body>
</html>
"""

# Save the HTML to a file
with open("pie.html", "w") as f:
    f.write(html)

print("HTML file with the chart has been created!")

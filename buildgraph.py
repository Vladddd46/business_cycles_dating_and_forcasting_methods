import matplotlib.pyplot as plt

"""
Functions for building graph based on given values.
"""

def build_graph(data, title="", xlable_name="", xylable_name=""):
	plt.figure(figsize=(20, 5), dpi=80)
	# Extract quarters and GDP values
	x_values = list(data.keys())
	y_values = list(data.values())
	# Plot the GDP values over time
	plt.plot(x_values, y_values)
	# Set chart title and labels
	plt.title(title)
	plt.xlabel('Quarter')
	plt.ylabel('')
	# Rotate x-axis labels by 45 degrees
	plt.xticks(rotation=45)
	# Show the plot
	plt.show()

def build_2graphs(data, data1, title="", xlable_name="", xylable_name=""):
    plt.figure(figsize=(20, 5), dpi=80)
    # Extract quarters and GDP values
    x_values = list(data.keys())
    y_values = list(data.values())

    x_values1 = list(data1.keys())
    y_values1 = list(data1.values())

    # Plot the GDP values over time
    plt.plot(x_values, y_values)
    plt.plot(x_values1, y_values1)
    # Set chart title and labels
    plt.title(title)
    plt.xlabel('Quarter')
    plt.ylabel('')
    # Rotate x-axis labels by 45 degrees
    plt.xticks(rotation=45)
    # Show the plot
    plt.show()
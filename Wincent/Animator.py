import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# List of coordinate pairs for the lines
test_case = 7
coordinates = []
points = []

with open(f"plot_{test_case}.out") as lines_file:
    for line in lines_file:
        x, y, x1, y1 = line.strip().split(",")
        coordinates.append(((int(x), int(y)), (int(x1), int(y1))))

with open(f"plot_points_{test_case}.out") as points_file:
    for line in points_file:
        x, y = line.strip().split(",")
        points.append((int(x), int(y)))
points.sort()  # Sort points for consistent rendering

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='datalim')
ax.set_xlim(min([x for x, _ in points]) - 10, max([x for x, _ in points]) + 10)  # Set x-axis limits
ax.set_ylim(min([y for _, y in points]) - 10, max([y for _, y in points]) + 10)  # Set x-axis limits

# Line objects that will be updated
lines = [ax.plot([], [], color="blue", lw=1, zorder=1)[0] for _ in coordinates]

# Plot points as scatter (initially all in one color)
scatter = ax.scatter(*zip(*points), color="gray", s=50, zorder=2)

# Keep track of points that change color
point_colors = ["gray"] * len(points)


def init():
    """Initialize all lines as empty and points in their default color."""

    for idx in range(len(point_colors)):
        point_colors[idx] = "gray"
    for line in lines:
        line.set_data([], [])
    start_x, start_y = coordinates[0][0]
    idx = points.index((start_x, start_y))
    point_colors[idx] = "orange"
    scatter.set_color(point_colors)
    return lines + [scatter]


def update(frame):
    """Update function to draw one line at a time and change point colors."""
    # Update the line for this frame
    x_start, y_start = coordinates[frame][0]
    x_end, y_end = coordinates[frame][1]
    lines[frame].set_data([x_start, x_end], [y_start, y_end])

    # Change the color of the endpoint of the current line
    if (x_end, y_end) in points:
        if (x_start, y_start) != coordinates[0][0]:
            idx_start = points.index((x_start, y_start))
            point_colors[idx_start] = "pink"
        idx_end = points.index((x_end, y_end))
        point_colors[idx_end] = "red"
        scatter.set_color(point_colors)

    return lines + [scatter]


# Create the animation
ani = FuncAnimation(fig, update,  frames=len(coordinates), init_func=init, blit=True, interval=50,
                    repeat=False, repeat_delay=30000)

# Display the animation
plt.show()

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

# display a tilemap from a 2D array
# 0 = ocean, 1 = plains, 2 = forest, 3 = mountain, 4 = desert, 5 = snow
def display_tilemap(tilemap):
    # Define colors for each tile type
    colors = ['blue', 'green', 'darkgreen', 'gray', 'yellow', 'white']
    cmap = ListedColormap(colors)

    # Convert tilemap to a numpy array for visualization
    tilemap_array = np.array(tilemap)

    # Create a figure and axis
    fig, ax = plt.subplots()
    ax.imshow(tilemap_array, cmap=cmap, interpolation='nearest')

    # Enable zooming and scrolling
    ax.set_title("Tilemap Viewer")
    ax.set_xticks([])
    ax.set_yticks([])

    # Show the plot
    plt.show()

# read a tilemap from a text file
# each line in the file represents a row in the tilemap
# the file should contain only integers separated by whitespace
def read_tilemap(filename):
    tilemap = []
    with open(filename, 'r') as file:
        for line in file:
            tilemap.append([int(x) for x in line.split()])
    return tilemap

tilemap = read_tilemap('tilemap.txt')

display_tilemap(tilemap)
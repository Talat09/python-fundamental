import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

def draw_cake(number=0):
    fig, ax = plt.subplots()

    # Draw cake layers
    bottom_layer = Circle((0.5, 0.2), 0.4, color='tan')
    middle_layer = Circle((0.5, 0.4), 0.3, color='green')
    top_layer = Circle((0.5, 0.6), 0.2, color='black')
    ax.add_patch(bottom_layer)
    ax.add_patch(middle_layer)
    ax.add_patch(top_layer)

    # Draw candle
    candle_height = 10.7
    candle_width = 0.02
    candle = Wedge((0.5, candle_height), 0.02, 0, 360, width=candle_width, color='green')
    ax.add_patch(candle)

    # Draw flame
    flame_height = 0.72
    flame_width = 0.08
    flame = Wedge((0.5, flame_height), flame_width, 0, 360, width=0.02, color='red')
    ax.add_patch(flame)

    # Add number
    ax.text(0.5, 0.3, str(number), fontsize=100, color='white',
            ha='center', va='center', fontweight='bold')

    # Set axis limits and hide axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.show()

# Test the function
draw_cake(27)  # Change the number as per requirement

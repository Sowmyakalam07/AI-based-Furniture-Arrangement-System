import numpy as np
import random
import matplotlib.pyplot as plt
import streamlit as st

ROOM_WIDTH, ROOM_HEIGHT = 10, 10  # 10x10 grid room
# To give input in 2D
FURNITURE_ITEMS = {
    "Bed": (3, 2),
    "Table": (2, 2),
    "Sofa": (3, 1),
    "Chair": (1, 1)
}

# Define Room and Furniture properties
def generate_random_room():
    return np.zeros((ROOM_WIDTH, ROOM_HEIGHT))

def check_valid_placement(room, x, y, width, height):
    if x + width > ROOM_WIDTH or y + height > ROOM_HEIGHT:
        return False
    if np.sum(room[x:+x+width, y:y+height]) > 0:
        return False
    return True

def place_furniture(room, furniture_list):
    placements = []
    for item, (w, h) in furniture_list.items():
        for _ in range(100):  # Try 100 random placements
            x, y = random.randint(0, ROOM_WIDTH-1), random.randint(0, ROOM_HEIGHT-1)
            if check_valid_placement(room, x, y, w, h):
                room[x:x+w, y:y+h] = 1
                placements.append((item, x, y, w, h))
                break
    return placements

def visualize_layout(placements):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(0, ROOM_WIDTH)
    ax.set_ylim(0, ROOM_HEIGHT)
    ax.set_xticks(range(ROOM_WIDTH+1))
    ax.set_yticks(range(ROOM_HEIGHT+1))
    ax.grid(True)
    
    for item, x, y, w, h in placements:
        rect = plt.Rectangle((x, y), w, h, fill=True, alpha=0.5, label=item)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, item, ha='center', va='center', fontsize=8)
    
    st.pyplot(fig)

# Streamlit Web App
st.title("AI Furniture Arrangement")
room = generate_random_room()
placements = place_furniture(room, FURNITURE_ITEMS)
visualize_layout(placements)

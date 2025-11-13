from PIL import Image, ImageDraw, ImageFont
import random
import os

# -----------------------------
# User info & emoji mapping
# -----------------------------
info = [
    ("waving.png", "Hi, I’m Onyenaucheya Emmanuel"),
    ("eyes.png", "Interested in Software Engineering with Java & Python"),
    ("seedling.png", "Using Springboot & Django Frameworks"),
    ("seedling.png", "Working on different projects (will share here)"),
    ("heart.png", "Open to collaborating"),
    ("mail.png", "Reach me: onyenaucheyaemma@gmail.com")
]

# Path to emoji folder
emoji_folder = "emojis/"

# -----------------------------
# Settings
# -----------------------------
width, height = 800, 500
cell_size = 25
cols, rows = width // cell_size, height // cell_size
bg_color = "black"
snake_color = "green"
food_color = "red"
font_color = "white"
text_size = 28
frames = []

# Load font
try:
    font = ImageFont.truetype("arial.ttf", text_size)
except:
    font = ImageFont.load_default()

# -----------------------------
# Initialize snake and food
# -----------------------------
snake = [(5, rows // 2), (4, rows // 2), (3, rows // 2)]
snake_dir = (1, 0)
food_positions = [(10 + i*8, 8 + ((-1)**i)*5) for i in range(len(info))]

# -----------------------------
# Helper function to draw frame
# -----------------------------
def draw_frame(snake, food_idx):
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Draw snake
    for i, (x, y) in enumerate(snake):
        bbox = [x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size]
        if i == 0:
            # Head with white eye
            draw.ellipse(bbox, fill=snake_color)
            eye_radius = 4
            eye_x = x*cell_size + cell_size//2
            eye_y = y*cell_size + cell_size//4
            draw.ellipse([eye_x-eye_radius, eye_y-eye_radius, eye_x+eye_radius, eye_y+eye_radius], fill="white")
        elif i == len(snake)-1:
            # Tail rounded
            draw.ellipse(bbox, fill=snake_color)
        else:
            # Body
            draw.rectangle(bbox, fill=snake_color)

    # Draw food
    if food_idx < len(food_positions):
        fx, fy = food_positions[food_idx]
        draw.ellipse([fx*cell_size, fy*cell_size, (fx+1)*cell_size, (fy+1)*cell_size], fill=food_color)

    # Draw collected info lines with emojis
    for j in range(food_idx):
        emoji_path, text = info[j]
        emoji_full_path = os.path.join(emoji_folder, emoji_path)
        if os.path.exists(emoji_full_path):
            emoji_img = Image.open(emoji_full_path).resize((text_size, text_size))
            img.paste(emoji_img, (10, 10 + j*40), emoji_img)
        draw.text((50, 10 + j*40), text, font=font, fill=font_color)

    return img

# -----------------------------
# Movement loop
# -----------------------------
for food_idx, food in enumerate(food_positions):
    fx, fy = food
    eaten = False
    while not eaten:
        # Determine direction step by step toward food
        head_x, head_y = snake[-1]
        dx = fx - head_x
        dy = fy - head_y
        if dx != 0:
            snake_dir = (1 if dx > 0 else -1, 0)
        elif dy != 0:
            snake_dir = (0, 1 if dy > 0 else -1)

        # Move snake
        new_head = (head_x + snake_dir[0], head_y + snake_dir[1])
        snake.append(new_head)

        # Check if eaten
        if new_head == (fx, fy):
            eaten = True  # Snake grows
        else:
            snake.pop(0)  # keep length same

        # Draw frame
        frames.append(draw_frame(snake, food_idx))

# -----------------------------
# Save GIF
# -----------------------------
frames[0].save(
    "snake_realistic_info.gif",
    save_all=True,
    append_images=frames[1:],
    duration=120,  # faster animation
    loop=0
)

print("GIF generated: snake_realistic_info.gif")

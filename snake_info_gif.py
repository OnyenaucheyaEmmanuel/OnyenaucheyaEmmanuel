# snake_info_gif.py
from PIL import Image, ImageDraw, ImageFont

# Your info lines
info = [
    "👋 Hi, I’m Onyenaucheya Emmanuel",
    "👀 Interested in Software Engineering with Java & Python",
    "🌱 Using Springboot & Django Frameworks",
    "🌱 Working on different projects (will share here)",
    "💞️ Open to collaborating",
    "📫 Reach me: onyenaucheyaemma@gmail.com"
]

# Settings
width, height = 700, 300
snake_color = "green"
bg_color = "black"
font_color = "white"
font = ImageFont.truetype("arial.ttf", 24)

frames = []

# Create frames: snake moves and collects info
for step in range(len(info)):
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw snake (simple horizontal rectangle)
    snake_x = 50 + step*100
    draw.rectangle([snake_x, 150, snake_x+80, 170], fill=snake_color)
    
    # Draw info collected so far
    for i in range(step+1):
        draw.text((10, 10 + i*35), info[i], font=font, fill=font_color)
    
    frames.append(img)

# Save GIF
frames[0].save(
    "snake_info.gif",
    save_all=True,
    append_images=frames[1:],
    duration=800,  # milliseconds per frame
    loop=0
)

print("GIF generated as 'snake_info.gif'")

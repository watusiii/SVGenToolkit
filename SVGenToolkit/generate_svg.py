import svgwrite
import random
import math
import os

def generate_picasso_style_svg(filename):
    width, height = 1200, 1900
    dwg = svgwrite.Drawing(filename, profile='tiny', size=(width, height))

    def add_shadow(shape, shadow_offset, shadow_color):
        shape_copy = shape.copy()
        shape_copy.translate(shadow_offset[0], shadow_offset[1])
        shape_copy.fill(shadow_color)
        shape_copy.stroke_width = 0
        dwg.add(shape_copy)

    def rgb_to_hex(r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def adjust_lightness(color, amount=-50):
        color = color.strip('#')
        red = int(color[0:2], 16)
        green = int(color[2:4], 16)
        blue = int(color[4:6], 16)
        red = max(0, min(255, red + amount))
        green = max(0, min(255, green + amount))
        blue = max(0, min(255, blue + amount))
        return rgb_to_hex(red, green, blue)

    # Create random abstract shapes
    for _ in range(random.randint(5, 15)):  # Random number of shapes
        shape_type = random.choice(['circle', 'rect', 'line'])
        color = rgb_to_hex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        if shape_type == 'circle':
            center = (random.randint(0, width), random.randint(0, height))
            radius = random.randint(int(10 * (width / 500)), int(100 * (width / 500)))
            circle = dwg.circle(center=center, r=radius, fill=color)
            
            if random.choice([True, False]):
                angle = random.uniform(0, 2 * math.pi)
                distance = random.randint(5, 20)
                shadow_offset = (distance * math.cos(angle), distance * math.sin(angle))
                shadow_color = adjust_lightness(color, -50)
                add_shadow(circle, shadow_offset, shadow_color)
            
            dwg.add(circle)
        
        elif shape_type == 'rect':
            insert = (random.randint(0, width - 100), random.randint(0, height - 100))
            size = (random.randint(int(20 * (width / 500)), int(100 * (width / 500))),
                    random.randint(int(20 * (height / 500)), int(100 * (height / 500))))
            rect = dwg.rect(insert=insert, size=size, fill=color)
            
            if random.choice([True, False]):
                angle = random.uniform(0, 2 * math.pi)
                distance = random.randint(5, 20)
                shadow_offset = (distance * math.cos(angle), distance * math.sin(angle))
                shadow_color = adjust_lightness(color, -50)
                add_shadow(rect, shadow_offset, shadow_color)
            
            dwg.add(rect)
        
        elif shape_type == 'line':
            start = (random.randint(0, width), random.randint(0, height))
            end = (random.randint(0, width), random.randint(0, height))
            stroke_width = random.randint(int(1 * (width / 500)), int(10 * (width / 500)))
            line = dwg.line(start=start, end=end, stroke=color, stroke_width=stroke_width)
            
            if random.choice([True, False]):
                angle = random.uniform(0, 2 * math.pi)
                distance = random.randint(5, 20)
                shadow_offset = (distance * math.cos(angle), distance * math.sin(angle))
                shadow_color = adjust_lightness(color, -50)
                add_shadow(line, shadow_offset, shadow_color)
            
            dwg.add(line)
    
    # Save the drawing
    dwg.save()

# Create 'images' directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Generate 333 SVG artworks
for i in range(333):
    generate_picasso_style_svg(os.path.join('images', f'{i+1}.svg'))

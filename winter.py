from PIL import Image

def apply_winter_filter(image):
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            # Apply a custom winter filter
            new_r = int(r * 0.9)
            new_g = int(g * 0.95)
            new_b = min(int(b * 1.1), 255)

            pixels[x, y] = (new_r, new_g, new_b)
    return image

image = Image.open('example.jpeg')
winter_image = apply_winter_filter(image.copy())
winter_image.save("winter_image_output.jpg")
print("Image saved as 'winter_image_output.jpg'. Check the file to see the result.")
from PIL import Image

def apply_summer_filter(image):
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            # Apply a custom summer filter
            new_r = min(int(r * 1.1), 255)
            new_g = min(int(g * 1.05), 255)
            new_b = min(int(b * 0.9), 255)

            pixels[x, y] = (new_r, new_g, new_b)
    return image

image = Image.open('example.jpeg')
summer_image = apply_summer_filter(image.copy())
summer_image.save("summer_image_output.jpeg")
print("Image saved as 'summer_image_output.jpeg'. Check the file to see the result.")
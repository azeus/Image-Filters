from PIL import Image

def apply_windy_filter(image):
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            # Apply a custom windy filter
            new_r = int(r * 1.1)
            new_g = int(g * 1.05)
            new_b = int(b * 0.9)

            pixels[x, y] = (new_r, new_g, new_b)
    return image

image = Image.open('example.jpeg')
windy_image = apply_windy_filter(image.copy())
windy_image.save("windy_image_output.jpeg")
print("Image saved as 'windy_image_output.jpeg'. Check the file to see the result.")
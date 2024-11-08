from PIL import Image

def apply_sinus_filter(image):
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            # Apply a custom sinus filter
            new_r = int(r * 1.5)
            new_g = int(g * 1.1)
            new_b = int(b * 0.5)

            pixels[x, y] = (new_r, new_g, new_b)
    return image

image = Image.open('example.jpeg')
sinus_image = apply_sinus_filter(image.copy())
sinus_image.save("sinus_image_output.jpeg")
print("Image saved as 'sinus_image_output.jpeg'. Check the file to see the result.")
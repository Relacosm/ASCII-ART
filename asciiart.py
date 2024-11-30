from PIL import Image
import os

# Define characters for different intensity levels (darker characters represent darker pixels)
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def scale_image(image, new_width=100):
    """Resize the image while maintaining the aspect ratio, adjusting for terminal display."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Scale height considering terminal aspect ratio
    return image.resize((new_width, new_height))

def grayify(image):
    """Convert image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Convert image pixels to ASCII characters based on intensity."""
    pixels = image.getdata()
    ascii_str = ''
    
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]  # Map pixel intensity to an ASCII character
    
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    """Convert the image to an ASCII art string."""
    try:
        # Open the image
        image = Image.open(image_path)

        # Resize image based on the specified width
        image = scale_image(image, new_width)

        # Convert image to grayscale
        image = grayify(image)

        # Convert pixels to ASCII
        ascii_str = pixels_to_ascii(image)

        # Format the ASCII string into lines to match the width of the image
        ascii_str_len = len(ascii_str)
        ascii_img = "\n".join([ascii_str[index:index+new_width] for index in range(0, ascii_str_len, new_width)])

        return ascii_img
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    image_path = input("Enter the image file path: ")
    
    # Get terminal's current width to ensure proper scaling
    terminal_width = os.get_terminal_size().columns
    ascii_image = image_to_ascii(image_path, new_width=terminal_width)

    print("\nHere is your ASCII Art:\n")
    print(ascii_image)

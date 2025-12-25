from PIL import Image
import os

screenshots_dir = 'screenshots'
for filename in os.listdir(screenshots_dir):
    if filename.endswith('.png'):
        filepath = os.path.join(screenshots_dir, filename)
        img = Image.open(filepath)
        # More aggressive resize - max 1280x720
        img.thumbnail((1280, 720), Image.Resampling.LANCZOS)
        # Convert to RGB and save as JPEG for better compression
        rgb_img = img.convert('RGB')
        new_filepath = filepath.replace('.png', '.jpg')
        rgb_img.save(new_filepath, quality=75, optimize=True)
        print(f"Compressed {filename} -> {new_filepath}")
        # Remove old PNG
        os.remove(filepath)

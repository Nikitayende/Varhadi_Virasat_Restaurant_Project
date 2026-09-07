from PIL import Image, ImageOps
import os

input_folder = "static/images/dishes"
output_folder = "static/images/dishes_resized"

os.makedirs(output_folder, exist_ok=True)

SIZE = (800, 600)

for filename in os.listdir(input_folder):

    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):

        path = os.path.join(input_folder, filename)

        img = Image.open(path).convert("RGB")

        # Resize and crop from the center
        img = ImageOps.fit(
            img,
            SIZE,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5)
        )

        img.save(
            os.path.join(output_folder, filename),
            quality=95
        )

print("✅ Done! All images saved in static/images/dishes_resized")



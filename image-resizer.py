import os
from PIL import Image

# Folders
INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"

# Desired size (width, height)
NEW_SIZE = (800, 800)   # change if you want

# Allowed image extensions
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def resize_images():
    # Create output folder if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # List all files in input folder
    files = os.listdir(INPUT_DIR)

    if not files:
        print("No files found in input_images folder.")
        return

    for filename in files:
        if not filename.lower().endswith(IMAGE_EXTENSIONS):
            print(f"Skipping non-image file: {filename}")
            continue

        input_path = os.path.join(INPUT_DIR, filename)

        try:
            with Image.open(input_path) as img:
                # Convert to RGB (avoids issues with PNG/transparent images)
                img = img.convert("RGB")

                # Resize image
                img = img.resize(NEW_SIZE)

                # Change extension to .jpg for output
                base_name, _ = os.path.splitext(filename)
                output_filename = base_name + ".jpg"
                output_path = os.path.join(OUTPUT_DIR, output_filename)

                # Save resized image
                img.save(output_path, "JPEG", quality=90)

                print(f"Processed: {filename} -> {output_filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print("\n✅ All images processed!")


if __name__ == "__main__":
    resize_images()

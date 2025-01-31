from PIL import Image
import os

def resize_images(folder_path, target_width=1600, target_height=1000):
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist")
        return

    # Get all files in the folder
    for filename in os.listdir(folder_path):
        # Check if file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            
            try:
                # Open the image
                with Image.open(image_path) as img:
                    # Convert image to RGB if it's in RGBA mode
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                    
                    # Resize image
                    resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                    
                    # Save the resized image, overwriting the original
                    resized_img.save(image_path, quality=95, optimize=True)
                    
                print(f"Successfully resized {filename}")
            
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

# Usage example
if __name__ == "__main__":
    # Replace this with your images folder path
    images_folder = "images/"
    resize_images(images_folder)
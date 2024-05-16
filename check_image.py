import os
import django
import random
from django.core.files import File
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))  # Debug print

try:
    django.setup()
    print("Django setup completed successfully")
except Exception as e:
    print(f"Error during django.setup(): {e}")

from products.models import Brand, Products

def update_image_if_missing(model, image_folder):
    # List of image file names
    image_files = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg', '09.jpg',
                    '10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg']    
    # Fetch instances without an image
    instances_without_image = model.objects.filter(image__isnull=True)
    print(f"Found {instances_without_image.count()} instances of {model.__name__} without images")

    for instance in instances_without_image:
        # Randomly select an image file
        image_filename = random.choice(image_files)
        # Construct the full path to the image
        image_path = os.path.join(settings.MEDIA_ROOT, image_folder, image_filename)
        print(f"Trying to update {model.__name__} {instance.pk} with image {image_path}")

        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                image_name = os.path.basename(image_path)
                instance.image.save(image_name, File(f), save=True)
                print(f"Updated image for {model.__name__} {instance.pk}")
        else:
            print(f"Image {image_filename} not found for {model.__name__} {instance.pk}")

def update_missing_images():
    update_image_if_missing(Brand, 'brand')
    update_image_if_missing(Products, 'product')

if __name__ == '__main__':
    update_missing_images()

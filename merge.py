import os
import django
import random
from django.core.files import File
from django.conf import settings
from faker import Faker
import pandas as pd

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))  # Debug print

try:
    django.setup()
    print("Django setup completed successfully")
except Exception as e:
    print(f"Error during django.setup(): {e}")

from products.models import Brand, Products, Review


def update_image_if_missing(model, image_folder):
    # List of image file names
    image_files = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg', '09.jpg',
                   '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg']
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


def seed_brand(n):
    faker = Faker()
    image = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']

    for x in range(n):
        Brand.objects.create(
            name=faker.name(),
            image=f'brand/{random.choice(image)}'
        )


def seed_products(n):
    faker = Faker()
    flag_types = ['New', 'Sale', 'Feature']
    brands = Brand.objects.all()
    image = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']

    for x in range(n):
        product = Products.objects.create(
            name=faker.name(),
            flag=random.choice(flag_types),
            price=round(random.uniform(20.99, 99.99), 2),
            sku=random.randint(1000, 9999),
            subtitle=faker.text(max_nb_chars=120),
            description=faker.text(max_nb_chars=500),
            brand=random.choice(brands),
            image=f'product/{random.choice(image)}'
        )
        # seed_reviews(product, random.randint(1, 5))  # Adjust the number of reviews per product as needed


def seed_reviews(product, n):
    faker = Faker()

    for x in range(n):
        Review.objects.create(
            product=product,
            rating=random.randint(1, 5),
            comment=faker.text(max_nb_chars=200)
        )


def update_products_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            product_name = row['product']
            quantity = row['quantity']
            price = row['price']
            brand_name = row['brand']

            # Get or create the brand
            brand, _ = Brand.objects.get_or_create(name=brand_name)
            # Generate random values for sku, subtitle, and description
            fake = Faker()

            sku = random.randint(1000, 9999)
            subtitle = fake.sentence(nb_words=6, variable_nb_words=True)
            description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)

            # Assuming product names are unique
            product, created = Products.objects.update_or_create(
                name=product_name,
                defaults={
                    'quantity': quantity,
                    'price': price,
                    'brand': brand
                }
            )
            if created:
                print(f'Created new product: {product_name}')
            else:
                print(f'Updated product: {product_name}')

        print('Successfully updated products from Excel file')

    except pd.errors.EmptyDataError:
        print('The provided Excel file is empty.')
    except FileNotFoundError:
        print('The provided file does not exist.')
    except Exception as e:
        print(f'Error updating products: {str(e)}')


def update_missing_images():
    update_image_if_missing(Brand, 'brand')
    update_image_if_missing(Products, 'product')


if __name__ == '__main__':
    update_missing_images()
    seed_products(1000)

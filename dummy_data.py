
import os ,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import pandas as pd
from faker import Faker
import random
from products.models import Products, Brand, Review
import pandas as pd
from faker import Faker
import random
from products.models import Products, Brand, Review

def seed_brand_from_excel(df):
    brands = df['brand'].unique()
    for brand_name in brands:
        Brand.objects.get_or_create(name=brand_name, defaults={
            'image': f'brand/{random.choice([f"{str(i).zfill(2)}.jpg" for i in range(1, 17)])}'
        })

def seed_products_from_excel(df):
    faker = Faker()
    for index, row in df.iterrows():
        product_name = row['product']
        quantity = row['quantity']
        price = row['price']
        brand_name = row['brand']

        # Get or create the brand
        brand, _ = Brand.objects.get_or_create(name=brand_name)
        
        # Generate random values for sku, subtitle, and description
        sku = random.randint(1000, 9999)
        subtitle = faker.text(max_nb_chars=120)
        description = faker.text(max_nb_chars=500)
        image = f'product/{random.choice([f"{str(i).zfill(2)}.jpg" for i in range(1, 11)])}'
        flag = random.choice(['New', 'Sale', 'Feature'])

        product, created = Products.objects.update_or_create(
            name=product_name,
            defaults={
                'flag': flag,
                'price': price,
                'sku': sku,
                'subtitle': subtitle,
                'description': description,
                'brand': brand,
                'image': image
            }
        )
        if created:
            print(f'Created new product: {product_name}')
        else:
            print(f'Updated product: {product_name}')

# def seed_reviews(product, n):
#     faker = Faker()
#     for x in range(n):
#         Review.objects.create(
#             product=product,
#             rating=random.randint(1, 5),
#             comment=faker.text(max_nb_chars=200)
#         )

def update_products_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        seed_brand_from_excel(df)
        seed_products_from_excel(df)
        print('Successfully updated products from Excel file')
    except pd.errors.EmptyDataError:
        print('The provided Excel file is empty.')
    except FileNotFoundError:
        print('The provided file does not exist.')
    except Exception as e:
        print(f'Error updating products: {str(e)}')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Update products from an Excel file')
    parser.add_argument('file_path', type=str, nargs='?', default='C:/Users/HPz/Desktop/pharma.xls', help='The path to the Excel file')
    args = parser.parse_args()

    update_products_from_excel(args.file_path)

import os
import django
import pandas as pd

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from products.models import Products, Brand  
from faker import Faker
import random

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

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Update products from an Excel file')
    parser.add_argument('file_path', type=str, help='The path to the Excel file')
    args = parser.parse_args()

    update_products_from_excel(args.file_path)


#python update_products.py C:/Users/HPz/Desktop/pharma.xls
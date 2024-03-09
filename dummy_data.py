import os ,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from faker import Faker
import random
from products.models import Products, Brand, Review

def seed_brand(n):
    faker = Faker()
    image = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']

    for x in range(n):
        Brand.objects.create(
            name=faker.name(),
            image=f'brand/{image[random.randint(0, 9)]}'
        )

def seed_products(n):
    faker = Faker()
    flag_types = ['New', 'Sale', 'Feature']
    brands = Brand.objects.all()
    image = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']

    for x in range(n):
        product = Products.objects.create(
            name=faker.name(),
            flag=flag_types[random.randint(0, 2)],
            price=round(random.uniform(20.99, 99.99), 2),
            sku=random.randint(1000, 9999),
            subtitle=faker.text(max_nb_chars=120),
            description=faker.text(max_nb_chars=500),
            brand=brands[random.randint(0, len(brands) - 1)],
            image=f'product/{image[random.randint(0, 9)]}'
        )
        #seed_reviews(product, random.randint(1, 5))  # Adjust the number of reviews per product as needed

def seed_reviews(product, n):
    faker = Faker()

    for x in range(n):
        Review.objects.create(
            product=product,
            rating=random.randint(1, 5),
            comment=faker.text(max_nb_chars=200)
        )

#seed_brand(300)

# Uncomment the line below to seed products and associated reviews
seed_products(1000)

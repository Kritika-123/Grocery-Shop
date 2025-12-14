from django.db import migrations
from django.utils.text import slugify

def add_daily_use_items(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Product = apps.get_model('products', 'Product')
    
    # Define new categories
    new_categories = [
        {
            'name': 'Personal Care',
            'description': 'Essential personal care and hygiene products for daily use',
            'image_url': 'https://cdn.shopify.com/s/files/1/0521/3925/8818/files/personal-care-banner.jpg'
        },
        {
            'name': 'Cleaning',
            'description': 'Household cleaning and maintenance products',
            'image_url': 'https://cdn.shopify.com/s/files/1/0521/3925/8818/files/cleaning-banner.jpg'
        },
        {
            'name': 'Beverages',
            'description': 'Refreshing drinks and beverages for every occasion',
            'image_url': 'https://cdn.shopify.com/s/files/1/0521/3925/8818/files/beverages-banner.jpg'
        },
        {
            'name': 'Snacks',
            'description': 'Delicious snacks and treats for your cravings',
            'image_url': 'https://cdn.shopify.com/s/files/1/0521/3925/8818/files/snacks-banner.jpg'
        }
    ]
    
    # Create categories if they don't exist
    created_categories = {}
    for cat_data in new_categories:
        slug = slugify(cat_data['name'])
        category, created = Category.objects.get_or_create(
            slug=slug,
            defaults={
                'name': cat_data['name'],
                'description': cat_data['description']
            }
        )
        created_categories[cat_data['name']] = category
    
    # Define products for each category
    products_data = {
        'Personal Care': [
            {
                'name': 'Toothpaste',
                'description': 'Fresh mint flavored toothpaste for daily oral hygiene',
                'price': 99.00,
                'stock': 100,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Shampoo',
                'description': 'Gentle cleansing shampoo for all hair types',
                'price': 149.00,
                'stock': 80,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Body Wash',
                'description': 'Moisturizing body wash with natural ingredients',
                'price': 129.00,
                'stock': 90,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Hand Sanitizer',
                'description': 'Alcohol-based hand sanitizer for effective germ protection',
                'price': 79.00,
                'stock': 150,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            }
        ],
        'Cleaning': [
            {
                'name': 'Dish Soap',
                'description': 'Effective dishwashing liquid that cuts through grease',
                'price': 89.00,
                'stock': 120,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Laundry Detergent',
                'description': 'Powerful laundry detergent for all types of clothes',
                'price': 299.00,
                'stock': 60,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Floor Cleaner',
                'description': 'Multi-surface floor cleaner with fresh fragrance',
                'price': 159.00,
                'stock': 70,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Glass Cleaner',
                'description': 'Streak-free glass cleaner for crystal clear windows',
                'price': 129.00,
                'stock': 80,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            }
        ],
        'Beverages': [
            {
                'name': 'Coffee',
                'description': 'Premium ground coffee for the perfect brew',
                'price': 399.00,
                'stock': 50,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Green Tea',
                'description': 'Organic green tea with antioxidants',
                'price': 199.00,
                'stock': 100,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Orange Juice',
                'description': 'Fresh squeezed orange juice with pulp',
                'price': 149.00,
                'stock': 40,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Mineral Water',
                'description': 'Pure mineral water from natural springs',
                'price': 49.00,
                'stock': 200,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            }
        ],
        'Snacks': [
            {
                'name': 'Potato Chips',
                'description': 'Crispy potato chips with sea salt',
                'price': 49.00,
                'stock': 150,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Cookies',
                'description': 'Delicious butter cookies with chocolate chips',
                'price': 79.00,
                'stock': 100,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Mixed Nuts',
                'description': 'Premium mixed nuts with dried fruits',
                'price': 299.00,
                'stock': 60,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            },
            {
                'name': 'Chocolate Bars',
                'description': 'Rich dark chocolate bars with almonds',
                'price': 129.00,
                'stock': 80,
                'image_url': 'https://m.media-amazon.com/images/I/71YGqXkGqQL._AC_SL1500_.jpg'
            }
        ]
    }
    
    # Add products for each category
    for category_name, products in products_data.items():
        category = created_categories[category_name]
        for product_data in products:
            slug = slugify(product_data['name'])
            # Check if product already exists
            if not Product.objects.filter(slug=slug).exists():
                Product.objects.create(
                    category=category,
                    name=product_data['name'],
                    slug=slug,
                    description=product_data['description'],
                    price=product_data['price'],
                    stock=product_data['stock'],
                    available=True,
                    image=product_data['image_url']
                )

def remove_daily_use_items(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Product = apps.get_model('products', 'Product')
    
    # Remove products first
    Product.objects.filter(
        category__name__in=['Personal Care', 'Cleaning', 'Beverages', 'Snacks']
    ).delete()
    
    # Then remove categories
    Category.objects.filter(
        name__in=['Personal Care', 'Cleaning', 'Beverages', 'Snacks']
    ).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0002_add_indian_products'),
    ]

    operations = [
        migrations.RunPython(add_daily_use_items, remove_daily_use_items),
    ] 
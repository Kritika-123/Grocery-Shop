from django.db import migrations
from django.utils.text import slugify

def add_indian_products(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Product = apps.get_model('products', 'Product')
    
    # Get or create categories
    fruits = Category.objects.get(slug='fruits')
    vegetables = Category.objects.get(slug='vegetables')
    dairy = Category.objects.get(slug='dairy')
    bakery = Category.objects.get(slug='bakery')
    
    # Indian Fruits
    indian_fruits = [
        {
            'name': 'Alphonso Mango',
            'description': 'Premium Indian mango variety known for its rich taste and aroma',
            'price': 899.00,
            'stock': 50,
            'category': fruits
        },
        {
            'name': 'Pomegranate',
            'description': 'Fresh and juicy Indian pomegranates',
            'price': 149.00,
            'stock': 100,
            'category': fruits
        },
        {
            'name': 'Sapota (Chikoo)',
            'description': 'Sweet and creamy Indian sapota',
            'price': 89.00,
            'stock': 75,
            'category': fruits
        },
        {
            'name': 'Guava',
            'description': 'Fresh Indian guava with seeds',
            'price': 69.00,
            'stock': 80,
            'category': fruits
        }
    ]
    
    # Indian Vegetables
    indian_vegetables = [
        {
            'name': 'Okra (Bhindi)',
            'description': 'Fresh and tender Indian okra',
            'price': 49.00,
            'stock': 100,
            'category': vegetables
        },
        {
            'name': 'Bitter Gourd (Karela)',
            'description': 'Fresh Indian bitter gourd',
            'price': 39.00,
            'stock': 60,
            'category': vegetables
        },
        {
            'name': 'Drumstick (Moringa)',
            'description': 'Fresh Indian drumstick pods',
            'price': 59.00,
            'stock': 70,
            'category': vegetables
        },
        {
            'name': 'Taro Root (Arbi)',
            'description': 'Fresh Indian taro root',
            'price': 45.00,
            'stock': 50,
            'category': vegetables
        }
    ]
    
    # Indian Dairy Products
    indian_dairy = [
        {
            'name': 'Paneer',
            'description': 'Fresh homemade Indian cottage cheese',
            'price': 129.00,
            'stock': 40,
            'category': dairy
        },
        {
            'name': 'Ghee',
            'description': 'Pure Indian clarified butter',
            'price': 599.00,
            'stock': 30,
            'category': dairy
        },
        {
            'name': 'Curd (Dahi)',
            'description': 'Fresh homemade Indian curd',
            'price': 49.00,
            'stock': 60,
            'category': dairy
        },
        {
            'name': 'Butter',
            'description': 'Fresh Indian butter',
            'price': 89.00,
            'stock': 45,
            'category': dairy
        }
    ]
    
    # Indian Bakery Items
    indian_bakery = [
        {
            'name': 'Naan',
            'description': 'Fresh Indian flatbread',
            'price': 39.00,
            'stock': 100,
            'category': bakery
        },
        {
            'name': 'Roti',
            'description': 'Whole wheat Indian flatbread',
            'price': 29.00,
            'stock': 100,
            'category': bakery
        },
        {
            'name': 'Puri',
            'description': 'Deep-fried Indian bread',
            'price': 49.00,
            'stock': 80,
            'category': bakery
        },
        {
            'name': 'Paratha',
            'description': 'Layered Indian flatbread',
            'price': 45.00,
            'stock': 90,
            'category': bakery
        }
    ]
    
    # Add all products
    all_products = indian_fruits + indian_vegetables + indian_dairy + indian_bakery
    
    for product_data in all_products:
        Product.objects.create(
            name=product_data['name'],
            slug=slugify(product_data['name']),
            description=product_data['description'],
            price=product_data['price'],
            stock=product_data['stock'],
            category=product_data['category'],
            available=True
        )

def remove_indian_products(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Product.objects.filter(
        name__in=[
            'Alphonso Mango', 'Pomegranate', 'Sapota (Chikoo)', 'Guava',
            'Okra (Bhindi)', 'Bitter Gourd (Karela)', 'Drumstick (Moringa)', 'Taro Root (Arbi)',
            'Paneer', 'Ghee', 'Curd (Dahi)', 'Butter',
            'Naan', 'Roti', 'Puri', 'Paratha'
        ]
    ).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_indian_products, remove_indian_products),
    ] 
import os
import django
from decimal import Decimal
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grocery_shop.settings')
django.setup()

from products.models import Category, Product

# Sample categories with their products
categories_data = {
    'Fruits': {
        'image_url': 'https://images.unsplash.com/photo-1610832958506-aa56368176cf',
        'products': [
            {
                'name': 'Fresh Apples',
                'description': 'Sweet and crispy red apples, perfect for snacking or baking.',
                'price': Decimal('199.00'),
                'stock': 100,
                'image_url': 'https://images.unsplash.com/photo-1567306226416-28f0efdc88ce'
            },
            {
                'name': 'Bananas',
                'description': 'Ripe yellow bananas, rich in potassium and perfect for breakfast.',
                'price': Decimal('89.00'),
                'stock': 150,
                'image_url': 'https://images.unsplash.com/photo-1603833665858-e61d17a86224'
            },
            {
                'name': 'Oranges',
                'description': 'Juicy oranges packed with vitamin C.',
                'price': Decimal('149.00'),
                'stock': 75,
                'image_url': 'https://images.unsplash.com/photo-1582979512210-99b6a53386f9'
            },
            {
                'name': 'Strawberries',
                'description': 'Sweet and juicy strawberries, perfect for desserts or snacking.',
                'price': Decimal('249.00'),
                'stock': 60,
                'image_url': 'https://images.unsplash.com/photo-1464965911861-746a04b4bca6'
            },
            {
                'name': 'Mangoes',
                'description': 'Sweet and ripe mangoes, a tropical delight.',
                'price': Decimal('299.00'),
                'stock': 45,
                'image_url': 'https://i.pinimg.com/474x/05/4e/eb/054eeb6aba42c405842389967d617763.jpg'
            },
            {
                'name': 'Grapes',
                'description': 'Sweet and juicy grapes, perfect for snacking or wine making.',
                'price': Decimal('179.00'),
                'stock': 80,
                'image_url': 'https://i.pinimg.com/736x/96/fa/e1/96fae1947ee7f4d962942efa278998a1.jpg'
            }
        ]
    },
    'Vegetables': {
        'image_url': 'https://images.unsplash.com/photo-1597362925123-77861d3fbac7',
        'products': [
            {
                'name': 'Fresh Tomatoes',
                'description': 'Ripe, juicy tomatoes perfect for salads and cooking.',
                'price': Decimal('79.00'),
                'stock': 80,
                'image_url': 'https://images.unsplash.com/photo-1546094096-0df4bcaaa337'
            },
            {
                'name': 'Cucumbers',
                'description': 'Crisp, fresh cucumbers ideal for salads and sandwiches.',
                'price': Decimal('49.00'),
                'stock': 120,
                'image_url': 'https://images.unsplash.com/photo-1604977042946-1eecc30f269e'
            },
            {
                'name': 'Carrots',
                'description': 'Sweet and crunchy carrots, great for snacking or cooking.',
                'price': Decimal('59.00'),
                'stock': 90,
                'image_url': 'https://images.unsplash.com/photo-1447175008436-054170c2e979'
            },
            {
                'name': 'Bell Peppers',
                'description': 'Colorful bell peppers, perfect for salads and stir-fries.',
                'price': Decimal('89.00'),
                'stock': 70,
                'image_url': 'https://images.unsplash.com/photo-1563565375-f3fdfdbefa83'
            },
            {
                'name': 'Spinach',
                'description': 'Fresh, leafy spinach rich in iron and vitamins.',
                'price': Decimal('69.00'),
                'stock': 50,
                'image_url': 'https://images.unsplash.com/photo-1576045057995-568f588f82fb'
            },
            {
                'name': 'Broccoli',
                'description': 'Nutritious broccoli, perfect for steaming or stir-frying.',
                'price': Decimal('99.00'),
                'stock': 65,
                'image_url': 'https://images.unsplash.com/photo-1584270354949-c26b0d5b4a0c'
            }
        ]
    },
    'Dairy': {
        'image_url': 'https://images.unsplash.com/photo-1628088062854-d1870b4553da',
        'products': [
            {
                'name': 'Fresh Milk',
                'description': 'Farm-fresh whole milk, rich and creamy.',
                'price': Decimal('39.00'),
                'stock': 50,
                'image_url': 'https://i.pinimg.com/736x/7f/7b/dd/7f7bdd703beb19c8bb3e3bbb6b1b20ba.jpg'
            },
            {
                'name': 'Lassi',
                'description': 'Lassi is a traditional Indian yogurt-based drink.',
                'price': Decimal('29.00'),
                'stock': 40,
                'image_url': 'https://i.pinimg.com/736x/49/f5/18/49f5180530d4ac26d928ebe2863d8fee.jpg'
            },
            {
                'name': 'Greek Yogurt',
                'description': 'Creamy Greek yogurt, high in protein.',
                'price': Decimal('129.00'),
                'stock': 60,
                'image_url': 'https://i.pinimg.com/736x/0a/3f/5c/0a3f5c6cd833a1af4aa9a8fa172a6b9d.jpg'
            },
            {
                'name': 'Butter',
                'description': 'Creamy butter, perfect for cooking and baking.',
                'price': Decimal('149.00'),
                'stock': 45,
                'image_url': 'https://i.pinimg.com/736x/53/c9/98/53c998edeed51c7e50ea1bd69ede04d1.jpg'
            },
            {
                'name': 'Cottage Cheese',
                'description': 'Fresh cottage cheese, high in protein and low in fat.',
                'price': Decimal('119.00'),
                'stock': 55,
                'image_url': 'https://i.pinimg.com/736x/8e/ab/0c/8eab0c21ee24d59a5280bcc5d6287fef.jpg'
            },
            {
                'name': 'Sour Cream',
                'description': 'Creamy sour cream, perfect for dips and toppings.',
                'price': Decimal('99.00'),
                'stock': 40,
                'image_url': 'https://i.pinimg.com/736x/aa/a5/56/aaa556db3f0365eefe3590516fcfb013.jpg'
            }
        ]
    },
    'Bakery': {
        'image_url': 'https://images.unsplash.com/photo-1608198093002-ad4e005484ec',
        'products': [
            {
                'name': 'Whole Wheat Bread',
                'description': 'Freshly baked whole wheat bread, nutritious and delicious.',
                'price': Decimal('69.00'),
                'stock': 30,
                'image_url': 'https://i.pinimg.com/736x/55/3d/ac/553dac03aff93e78c12bc875f6bcc2c0.jpg'
            },
            {
                'name': 'Croissants',
                'description': 'Buttery, flaky croissants, perfect for breakfast.',
                'price': Decimal('89.00'),
                'stock': 25,
                'image_url': 'https://images.unsplash.com/photo-1555507036-ab1f4038808a'
            },
            {
                'name': 'Bagels',
                'description': 'Fresh bagels, great for sandwiches.',
                'price': Decimal('59.00'),
                'stock': 35,
                'image_url': 'https://images.unsplash.com/photo-1612203985729-70726954388c'
            },
            {
                'name': 'Chocolate Cake',
                'description': 'Rich chocolate cake with chocolate frosting.',
                'price': Decimal('399.00'),
                'stock': 15,
                'image_url': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587'
            },
            {
                'name': 'Blueberry Muffins',
                'description': 'Moist blueberry muffins, perfect for breakfast or snacks.',
                'price': Decimal('129.00'),
                'stock': 20,
                'image_url': 'https://images.unsplash.com/photo-1607958996333-41aef7caefaa'
            },
            {
                'name': 'Sourdough Bread',
                'description': 'Artisanal sourdough bread, made with traditional methods.',
                'price': Decimal('149.00'),
                'stock': 25,
                'image_url': 'https://i.pinimg.com/736x/65/4b/49/654b496162a0c92f3090d2562a32d4f6.jpg'
            }
        ]
    },
    'Beverages': {
        'image_url': 'https://i.pinimg.com/736x/79/6c/34/796c34906c9111f02f41a319298a261b.jpg',
        'products': [
            {
                'name': 'Green Tea',
                'description': 'Premium green tea, rich in antioxidants.',
                'price': Decimal('249.00'),
                'stock': 45,
                'image_url': 'https://i.pinimg.com/474x/3f/56/39/3f5639caaa3c4633e75aa015d2b883f9.jpg'
            },
            {
                'name': 'Coffee Beans',
                'description': 'Freshly roasted coffee beans, perfect for your morning brew.',
                'price': Decimal('499.00'),
                'stock': 30,
                'image_url': 'https://images.unsplash.com/photo-1447933601403-0c6688de566e'
            },
            {
                'name': 'Orange Juice',
                'description': 'Freshly squeezed orange juice, packed with vitamin C.',
                'price': Decimal('159.00'),
                'stock': 40,
                'image_url': 'https://images.unsplash.com/photo-1621263764928-df1444c5e859'
            },
            {
                'name': 'Sparkling Water',
                'description': 'Refreshing sparkling water with a hint of lime.',
                'price': Decimal('79.00'),
                'stock': 60,
                'image_url': 'https://images.unsplash.com/photo-1622483767028-3f66f32aef97'
            },
            {
                'name': 'Apple Cider',
                'description': 'Sweet and tangy apple cider, perfect for autumn.',
                'price': Decimal('189.00'),
                'stock': 35,
                'image_url': 'https://images.unsplash.com/photo-1621263764928-df1444c5e859'
            },
            {
                'name': 'Herbal Tea Collection',
                'description': 'Assorted herbal teas for relaxation and wellness.',
                'price': Decimal('299.00'),
                'stock': 25,
                'image_url': 'https://i.pinimg.com/736x/c7/7d/10/c77d10d4dc4881343c6199f77d47696f.jpg'
            }
        ]
    },
    'Snacks': {
        'image_url': 'https://i.pinimg.com/736x/86/78/40/86784067debca3b306dce481e7077ac8.jpg',
        'products': [
            {
                'name': 'Potato Chips',
                'description': 'Crispy potato chips with sea salt.',
                'price': Decimal('49.00'),
                'stock': 150,
                'image_url': 'https://i.pinimg.com/736x/a6/31/50/a63150fc27bfb13e52b3b28b4ca80aa1.jpg'
            },
            {
                'name': 'Cookies',
                'description': 'Delicious butter cookies with chocolate chips.',
                'price': Decimal('79.00'),
                'stock': 100,
                'image_url': 'https://images.unsplash.com/photo-1499636136210-6f4ee915583e'
            },
            {
                'name': 'Mixed Nuts',
                'description': 'Premium mixed nuts with dried fruits.',
                'price': Decimal('299.00'),
                'stock': 60,
                'image_url': 'https://i.pinimg.com/736x/01/0d/90/010d90532d3cb44b86dfe980e6b6a6d3.jpg'
            },
            {
                'name': 'Dairy milk silk',
                'description': 'Rich dark chocolate bars with almonds.',
                'price': Decimal('129.00'),
                'stock': 80,
                'image_url': 'https://i.pinimg.com/736x/59/30/cf/5930cffca1f3444f98267bfdbd6407f0.jpg'
            },
            {
                'name': 'Popcorn',
                'description': 'Light and fluffy popcorn, perfect for movie nights.',
                'price': Decimal('89.00'),
                'stock': 70,
                'image_url': 'https://i.pinimg.com/736x/94/7c/fb/947cfbaae13433da69bcade6e8df77b9.jpg'
            },
            {
                'name': 'Kurkure',
                'description': 'spicy and crunchy kurkure',
                'price': Decimal('19.00'),
                'stock': 90,
                'image_url': 'https://i.pinimg.com/736x/04/33/1a/04331ad6cf3cfc1e2a484dfb30c9d6e8.jpg'
            }
        ]
    },
    'Personal Care': {
        'image_url': 'https://i.pinimg.com/736x/c3/ba/fd/c3bafd93e46a5394ffe4b0cbe2938710.jpg',
        'products': [
            {
                'name': 'Toothpaste',
                'description': 'Fresh mint flavored toothpaste for daily oral hygiene.',
                'price': Decimal('99.00'),
                'stock': 100,
                'image_url': 'https://i.pinimg.com/736x/f8/b4/5e/f8b45e6f6401b29bea67d552384928d2.jpg'
            },
            {
                'name': 'Shampoo',
                'description': 'Gentle cleansing shampoo for all hair types.',
                'price': Decimal('149.00'),
                'stock': 80,
                'image_url': 'https://i.pinimg.com/736x/a1/64/df/a164df4cc189f09fc82d01f7b4c1e592.jpg'
            },
            {
                'name': 'Body Wash',
                'description': 'Moisturizing body wash with natural ingredients.',
                'price': Decimal('129.00'),
                'stock': 90,
                'image_url': 'https://i.pinimg.com/736x/45/de/03/45de038fb6ec240b7cca7f2c8d4a7c23.jpg'
            },
            {
                'name': 'Hand Sanitizer',
                'description': 'Alcohol-based hand sanitizer for effective germ protection.',
                'price': Decimal('79.00'),
                'stock': 150,
                'image_url': 'https://i.pinimg.com/736x/07/61/41/076141b5be2ff402b11e53794916dc4b.jpg'
            },
            {
                'name': 'Face Cream',
                'description': 'Hydrating face cream for all skin types.',
                'price': Decimal('199.00'),
                'stock': 70,
                'image_url': 'https://i.pinimg.com/736x/f4/aa/27/f4aa2722791420089388b34f34a2c068.jpg'
            },
            {
                'name': 'Deodorant',
                'description': 'Long-lasting deodorant with a fresh scent.',
                'price': Decimal('89.00'),
                'stock': 110,
                'image_url': 'https://i.pinimg.com/736x/9a/10/90/9a1090904403e0852116ffb354d311c9.jpg'
            }
        ]
    }
}

def add_sample_data():
    # Clear existing data
    Category.objects.all().delete()
    Product.objects.all().delete()
    
    # Add categories and products
    for category_name, category_data in categories_data.items():
        print(f"\nProcessing category: {category_name}")
        
        # Create category
        category = Category.objects.create(
            name=category_name,
            slug=slugify(category_name),
            description=f'Fresh and high-quality {category_name.lower()} for your daily needs.',
            image_url=category_data['image_url']
        )
        
        # Add products for this category
        for product_data in category_data['products']:
            print(f"Processing product: {product_data['name']}")
            
            # Create product
            Product.objects.create(
                category=category,
                name=product_data['name'],
                slug=slugify(product_data['name']),
                description=product_data['description'],
                price=product_data['price'],
                stock=product_data['stock'],
                available=True,
                image_url=product_data['image_url']
            )
            
        print(f"Completed category: {category_name}")

if __name__ == '__main__':
    add_sample_data()
    print("\nSample data has been added successfully!") 
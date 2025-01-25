from django.core.management import BaseCommand
from recipe.models import Product


class Command(BaseCommand):
    """
    Creates products
    """

    def handle(self, *args, **options):
        self.stdout.write("Create products")
        products_names = [
            "булка",
            "хлеб",
            "печенька",
            "вафелька",
        ]
        for products_name in products_names:
            product, created = Product.objects.get_or_create(name=products_name)
        self.stdout.write(f"Created product {product.name}")

        self.stdout.write(self.style.SUCCESS("Products created"))

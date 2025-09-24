from variables.models import Product

def get_or_create_product_by_barcode(barcode: str, provider: str | None = None, name: str | None = None):
    product, _ = Product.objects.get_or_create(
        barcode=barcode,
        defaults={"provider": provider or "", "name": name or ""},
    )
    return product

from time import perf_counter
from django.db import transaction
from measurements.models import InventoryEntry
from variables.logic.products_logic import get_or_create_product_by_barcode

def register_inventory_scan(barcode: str, qty: int = 1, provider: str | None = None, scenario: str | None = None):
    """
    Registra una entrada de inventario para un barcode.
    Retorna (entry, duration_ms).
    """
    t0 = perf_counter()
    # Transacción corta para minimizar tiempo
    with transaction.atomic():
        product = get_or_create_product_by_barcode(barcode, provider=provider)
        entry = InventoryEntry.objects.create(
            product=product,
            quantity=max(1, int(qty)),
            provider=provider or "",
            scenario=(scenario or "").lower(),
        )
    duration_ms = int((perf_counter() - t0) * 1000)
    # Guarda la métrica en el propio registro para luego calcular promedios
    if entry.duration_ms != duration_ms:
        InventoryEntry.objects.filter(pk=entry.pk).update(duration_ms=duration_ms)
        entry.duration_ms = duration_ms
    return entry, duration_ms

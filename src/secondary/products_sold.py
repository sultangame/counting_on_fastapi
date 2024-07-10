from sqlalchemy import Table, Column, ForeignKey
from src.database import Model


products_sold = Table(
    'products_sold',
    Model.metadata,
    Column(
        "product_id",
        ForeignKey("products.pk", ondelete="CASCADE"),
        primary_key=True
    ),
    Column(
        "sold_id",
        ForeignKey("sold_products.pk", ondelete="CASCADE"),
        primary_key=True
    ),
)

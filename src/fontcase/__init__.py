"""fontcase: catálogo offline de fontes do Google Fonts."""
from .catalog import (
    all_fonts, categories, by_category, get, search,
    css_url, css_import, css_font_family, random_font,
)

__version__ = "0.1.0"
__all__ = [
    "all_fonts", "categories", "by_category", "get", "search",
    "css_url", "css_import", "css_font_family", "random_font",
]

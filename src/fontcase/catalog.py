from __future__ import annotations
import json, random
from functools import lru_cache
from importlib import resources
from typing import Dict, List, Optional


@lru_cache(maxsize=1)
def all_fonts() -> List[Dict]:
    """Retorna todas as fontes do catálogo."""
    text = resources.files("fontcase").joinpath("data/catalog.json").read_text(encoding="utf-8")
    return json.loads(text)


def categories() -> List[str]:
    """Lista de categorias, em ordem alfabética."""
    return sorted({f["category"] for f in all_fonts()})


def by_category(category: str) -> List[Dict]:
    """Fontes de uma categoria."""
    return [f for f in all_fonts() if f["category"] == category]


def get(family: str) -> Optional[Dict]:
    """Busca uma fonte pelo nome exato (sem diferenciar maiúsculas)."""
    fam = family.strip().lower()
    for f in all_fonts():
        if f["family"].lower() == fam or f["slug"] == fam:
            return f
    return None


def search(query: str = "", category: Optional[str] = None) -> List[Dict]:
    """Busca por trecho do nome, com filtro opcional de categoria."""
    q = query.strip().lower()
    return [
        f for f in all_fonts()
        if q in f["family"].lower() and (category is None or f["category"] == category)
    ]


def _need(family: str) -> Dict:
    font = get(family)
    if font is None:
        raise KeyError(f"Fonte não encontrada: {family!r}")
    return font


def css_url(family: str) -> str:
    """URL do CSS do Google Fonts."""
    return _need(family)["css"]


def css_import(family: str) -> str:
    """Linha @import pronta para colar em um CSS."""
    return f"@import url('{css_url(family)}');"


def css_font_family(family: str) -> str:
    """Valor para a propriedade font-family."""
    return _need(family)["css_stack"]


def random_font(category: Optional[str] = None) -> Dict:
    """Uma fonte aleatória, opcionalmente dentro de uma categoria."""
    pool = by_category(category) if category else all_fonts()
    if not pool:
        raise ValueError(f"Categoria sem fontes: {category!r}")
    return random.choice(pool)

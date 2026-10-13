# Font Atlas

Catálogo de fontes organizado por categoria, com site estático publicado no GitHub Pages.

- `fonts/` - 25 categorias, 6 fontes cada (150 subpastas)
- `site/` - página de busca e prévia
- `scripts/` - gera `site/catalog.json`
- `.github/workflows/` - deploy automático

Rode local: `python scripts/build_catalog.py && python -m http.server -d site`

## Biblioteca Python (`fontcase`)

```bash
pip install fontcase
```

```python
import fontcase as fa

fa.categories()                 # 25 categorias
fa.search("noto")               # busca por nome
fa.css_import("Montserrat")     # @import pronto
fa.random_font("script-brush")  # fonte aleatória
```

CLI: `fontcase search mono`, `fontcase show Lato`, `fontcase random -c display-pixel`

# Font Atlas

A browsable catalog of 150 Google Fonts, organized into 25 categories such as geometric sans, old-style serif, monospace, handwriting, pixel and more. It comes as a searchable website and as a Python library.

## Website

Search by name, filter by category and preview every font with your own text. The site is a static page published automatically with GitHub Pages.

## Python library

```bash
pip install fontcase
```

```python
import fontcase as fa

fa.categories()                 # list all 25 categories
fa.search("noto")               # search by name
fa.css_import("Montserrat")     # ready-to-use @import line
fa.random_font("script-brush")  # random font from a category
```

The catalog is bundled with the package, so it works offline and has no dependencies.

## Command line

```bash
fontcase search mono
fontcase show Lato
fontcase random -c display-pixel
```

## Contributing

Pull requests that add new fonts or categories are welcome.

## License

MIT. Each font is distributed by Google Fonts under its own license.

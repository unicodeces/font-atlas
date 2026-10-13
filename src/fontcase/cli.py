import argparse
from . import catalog


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="fontcase", description="Catálogo de fontes")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("categories", help="lista categorias")
    s = sub.add_parser("search", help="busca fontes")
    s.add_argument("query", nargs="?", default="")
    s.add_argument("-c", "--category")
    sh = sub.add_parser("show", help="mostra detalhes e CSS de uma fonte")
    sh.add_argument("family")
    r = sub.add_parser("random", help="fonte aleatória")
    r.add_argument("-c", "--category")
    a = p.parse_args(argv)

    if a.cmd == "categories":
        for c in catalog.categories():
            print(c)
    elif a.cmd == "search":
        for f in catalog.search(a.query, a.category):
            print(f"{f['family']}  [{f['category']}]")
    elif a.cmd == "show":
        f = catalog.get(a.family)
        if not f:
            print("Fonte não encontrada")
            return 1
        print(f"{f['family']} ({f['category']})\n{f['page']}\n")
        print(catalog.css_import(a.family))
        print(f"font-family: {f['css_stack']};")
    elif a.cmd == "random":
        f = catalog.random_font(a.category)
        print(f"{f['family']}  [{f['category']}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import json, glob, os
root = os.path.join(os.path.dirname(__file__), "..")
items = [json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(os.path.join(root, "fonts/*/*/font.json")))]
for out in ("site/catalog.json", "src/fontcase/data/catalog.json"):
    path = os.path.join(root, out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(items, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(items)} fontes no catálogo")

# Publicar no PyPI

1. Crie conta em https://pypi.org e ative 2FA.
2. Edite `pyproject.toml` (autor, e-mail, URLs).
3. No PyPI: Account settings -> Publishing -> "Add a new pending publisher":
   - PyPI project name: `fontcase`
   - Owner: seu usuario do GitHub
   - Repository: nome do repositorio
   - Workflow: `publish-pypi.yml`
   - Environment: `pypi`
4. No GitHub: Settings -> Environments -> crie `pypi`.
5. Crie uma Release (tag `v0.1.0`). O workflow publica sozinho.

Teste local:
    pip install build twine
    python scripts/build_catalog.py
    python -m build
    twine check dist/*

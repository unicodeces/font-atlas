import pytest
import fontcase as fa


def test_total():
    assert len(fa.all_fonts()) == 150


def test_categories():
    assert len(fa.categories()) == 25


def test_get_and_css():
    assert fa.get("montserrat")["family"] == "Montserrat"
    assert "family=Open+Sans" in fa.css_url("Open Sans")
    assert fa.css_import("Lato").startswith("@import url(")


def test_search_filter():
    res = fa.search("noto", category="international-cjk")
    assert res and all(f["category"] == "international-cjk" for f in res)


def test_unknown():
    assert fa.get("nao-existe") is None
    with pytest.raises(KeyError):
        fa.css_url("nao-existe")


def test_random():
    assert fa.random_font("mono-code")["category"] == "mono-code"

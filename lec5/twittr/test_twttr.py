from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("vowel") == "vwl"
    assert shorten("engine") == "ngn"
    assert shorten("VOWEL") == "VWL"
    assert shorten("v21owel") == "v21wl"
    assert shorten("v.wel") == "v.wl"

if __name__ == "__main__":
    main()

from twttr import shorten

def test():
    assert shorten("tweetter") == "twttr"
    assert shorten("Ahmed over ul") == "hmd vr l"
    assert shorten("my age is 15.") == "my g s 15."
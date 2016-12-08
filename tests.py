import behumble

def test_strip_mr():
    mr_t = "Mr T"
    new_mr_t = behumble.strip_honorific(mr_t)
    assert new_mr_t == "T"

def test_strip_mrs():
    test_s = "Mrs Doubtfire"
    new_s = behumble.strip_honorific(test_s)
    assert new_s == "Doubtfire"

def test_strip_miss():
    s = "Miss Book"
    new_s = behumble.strip_honorific(s)
    assert new_s == "Book"

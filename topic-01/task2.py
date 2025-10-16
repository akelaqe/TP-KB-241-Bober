def test_string_functions(s):
    print("Оригінал:     ", repr(s))
    print("strip():      ", repr(s.strip()))
    print("capitalize(): ", repr(s.capitalize()))
    print("title():      ", repr(s.title()))
    print("upper():      ", repr(s.upper()))
    print("lower():      ", repr(s.lower()))


sample = "  пРиКлАд Тексту  "
test_string_functions(sample)
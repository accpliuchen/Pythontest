

def test_title_case():
    in_string='this is a test string'
    desired='This Is A Test String'

    actual=in_string.title()

    assert actual==desired

import pytest
from Modules.utilities import validate_email  

@pytest.mark.parametrize("email, expected_result", [
    ('hs_@763946', False),       # Missing domain extension (.com, .in, etc.)
    ('plainaddress', False),     # Missing @ sign and domain
    ('@missinguser.com', False), # Missing username before @
    ('user@.com', False),        # Missing domain name
    ('', False),                 # Empty string
    ('test@example.com', True),  #correct
    ('user.name@domain.co.in', True), #correct
])

def test_validate_email(email, expected_result):
    assert validate_email(email) is expected_result
import pytest
from Modules.utilities import validate_email  

@pytest.mark.parametrize("email, expected_result", [
    ('hs_@763946', False),
    ('plainaddress', False),
    ('@missinguser.com', False),
    ('user@.com', False),
    ('', False),
    ('test@example.com', True),
    ('user.name@domain.co.in', True),
])

def test_validate_email(email, expected_result):
    assert validate_email(email) is expected_result
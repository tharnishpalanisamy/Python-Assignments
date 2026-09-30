import pytest
from Modules.services.LoanPaymentService import LoanPaymentService 

@pytest.mark.parametrize(
    'amount, emi, expected ' , 
    [
        (1000, 500, True),
        (500, 500, True),
        (2000, 1000, True),
        (100, 500, False),
        (0, 500, False),
        (-100, 500, False),
    ] 
)

def test_validate_payment(amount , emi , expected ) :
    service = LoanPaymentService() 
    result = service.validate_payment(amount , emi ) 

    assert result == expected 



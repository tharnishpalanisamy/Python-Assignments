from Modules.services.LoanProcessor import LoanProcessor 
import pytest 

@pytest.mark.parametrize(
    'loan_amount, interest, duration, expected' , 
    [
        # Normal EMI cases
        (100000, 12, 12, 8884.88),
        (200000, 10, 24, 9228.99),
        (500000, 8, 60, 10138.20),

        # Zero interest
        (120000, 0, 12, 10000.00),
        (60000, 0, 6, 10000.00),

        # Different loan amounts
        (50000, 10, 12, 4395.79),
        (1000000, 12, 60, 22244.45),

        # Different durations
        (100000, 12, 24, 4707.35),
        (100000, 12, 36, 3321.43),
    ]
)


def test_calculate_emi(loan_amount , interest , duration , expected) :
    service = LoanProcessor() 
    result = service.calculate_emi(loan_amount , interest , duration) 

    assert result == expected 


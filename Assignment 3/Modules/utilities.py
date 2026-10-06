import re 

def validate_email(email: str) -> bool:
    if not isinstance(email, str) or not email.strip():
        return False
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email.strip()))

USER_FIELDS = ['id', 'name', 'email', 'age', 'employed', 'income', 'credit_score'] 
LOANS_FIELD = ['loan_id', 'user_id', 'loan_type', 'loan_amount', 'emi', 'interest_rate', 'duration_months', 'status']
PAYMENT_FIELD = ['payment_id', 'loan_id', 'user_id', 'loan_type', 'loan_amount', 'date']

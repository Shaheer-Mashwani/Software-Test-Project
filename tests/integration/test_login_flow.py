from src.login import login

def test_login_full_flow():
    # Valid login
    result_valid = login("admin", "1234")
    assert result_valid == "Login successful"

    # Invalid login
    result_invalid = login("admin", "wrong")
    assert result_invalid == "Invalid credentials"

def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    elif username == "" or password == "":
        return "Fields cannot be empty"
    else:
        return "Invalid credentials"

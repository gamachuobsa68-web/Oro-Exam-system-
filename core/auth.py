USERS = {
    "student": {
        "student001": "1234",
        "student002": "1234"
    },
    "teacher": {
        "teacher001": "1234"
    },
    "admin": {
        "admin": "admin123"
    }
}

def login(role, username, password):
    if role in USERS:
        return USERS[role].get(username) == password
    return False
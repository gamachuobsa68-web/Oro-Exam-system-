USERS = {
    "student": {
        "student1": "1234",
        "student2": "1234"
    },
    "teacher": {
        "teacher1": "1234"
    },
    "admin": {
        "admin": "admin123"
    }
}


def login_user(role, username, password):

    if role not in USERS:
        return False

    if username in USERS[role]:
        return USERS[role][username] == password

    return False
import re

class UserModel:
    def __init__(self):
        self.users = {}  # {email: password}

    def is_valid_email(self, email):
  
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z-]+\.[a-zA-Z-.]+$"
        return re.match(pattern, email) is not None

    def is_strong_password(self, password):
        """Check if password is longer than 8 characters"""
        return len(password) > 8

    def add_user(self, email, password):
        if not self.is_valid_email(email):
            return False, "❌ Email must contain @ and a valid domain (e.g., user@example.com)"
        if not self.is_strong_password(password):
            return False, "❌ Password must be longer than 8 characters!"
        if email in self.users:
            return False, "❌ Email already exists!"
        self.users[email] = password
        return True, "✅ Account created successfully!"

    def check_user(self, email, password):
        if not self.is_valid_email(email):
            return False, "❌ Invalid email!"
        if email in self.users and self.users[email] == password:
            return True, "✅ Login successful!"
        return False, "❌ Incorrect email or password."
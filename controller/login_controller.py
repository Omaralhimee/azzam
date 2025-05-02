import logging
from datetime import datetime
from model.user_model import UserModel
from view.login_view import LoginView

class LoginController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        # Configure logging
        logging.basicConfig(filename="login_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == "1":
                self.login()
            elif choice == "2":
                self.create_account()
            else:
                self.view.show_message("❌ Invalid choice!", is_success=False)

    def login(self):
        email, password = self.view.get_input()
        success, message = self.model.check_user(email, password)
        self.view.show_message(message, is_success=success)
        if success:
            # Log login time
            logging.info(f"Login successful by: {email}")
            self.view.show_message(f"⏰ Login time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def create_account(self):
        email, password = self.view.get_input()
        success, message = self.model.add_user(email, password)
        self.view.show_message(message, is_success=success)
        if success:
            # Log account creation time
            logging.info(f"New account created by: {email}")
import logging
import jwt  # <-- المكتبة المضافة
from datetime import datetime, timedelta
from model.user_model import UserModel
from view.login_view import LoginView

class LoginController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        self.SECRET_KEY = "your_super_secure_key_here!"  # <-- المفتاح السري المضافة
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
            # إضافة توليد التوكن دون حذف أي شيء
            token = self.generate_token(email)  # <-- السطر المضاف
            self.view.show_message(f"🔑 Your Token: {token}")  # <-- السطر المضاف
            logging.info(f"Login successful by: {email} | Token: {token}")  # <-- التعديل
            self.view.show_message(f"⏰ Login time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # الدالة الجديدة المضافة
    def generate_token(self, email: str) -> str:
        
        expiration = datetime.utcnow() + timedelta(hours=1)
        payload = {
            "email": email,
            "exp": expiration
        }
        return jwt.encode(payload, self.SECRET_KEY, algorithm="HS256")

    def create_account(self):
        email, password = self.view.get_input()
        success, message = self.model.add_user(email, password)
        self.view.show_message(message, is_success=success)
        if success:
            logging.info(f"New account created by: {email}")

    # دالة التحقق من التوكن (جديدة)
    def verify_token(self, token: str) -> bool:
        try:
            jwt.decode(token, self.SECRET_KEY, algorithms=["HS256"])
            return True
        except jwt.ExpiredSignatureError:
            self.view.show_message("❌ Token expired!", is_success=False)
        except jwt.InvalidTokenError:
            self.view.show_message("❌ Invalid token!", is_success=False)
        return False
from colorama import Fore, Style, init

init(autoreset=True)

class LoginView:
    def get_input(self):
        print(Fore.CYAN + "=" * 40)
        print(Fore.YELLOW + "Login")
        print(Fore.CYAN + "=" * 40)
        email = input(Fore.GREEN + "Enter your email: " + Fore.WHITE)
        password = input(Fore.GREEN + "Enter password (must be longer than 8 characters): " + Fore.WHITE)
        return email, password

    def show_message(self, message, is_success=True):
        color = Fore.GREEN if is_success else Fore.RED
        print(color + message)

    def show_menu(self):
        print(Fore.CYAN + "=" * 40)
        print(Fore.YELLOW + "Welcome! Please choose an option:")
        print(Fore.CYAN + "=" * 40)
        print(Fore.BLUE + "1. Login")
        print(Fore.BLUE + "2. Create Account")
        print(Fore.CYAN + "=" * 40)
        return input(Fore.GREEN + "Choose an option (1 or 2): " + Fore.WHITE)
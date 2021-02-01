class PasswordManager:

    def __init__(self):
        self.old_passwords = ['asdfasd', '1232134123', 'asdfg']

    def set_password(self, password):
        self.old_passwords.append(password)
        print(self.old_passwords[-1])

    def is_correct(self, password):
        if self.old_passwords[-1] == password:
            print(self.old_passwords)


manager = PasswordManager()
manager.set_password(password=input('Enter a password: '))



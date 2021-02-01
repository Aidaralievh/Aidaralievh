class PasswordManager:

    def __init__(self):
        self.old_passwords = ['asdfasd', '1232134123', 'asdfg']
        self.password = input('type new password: ')
        self.password2 = input('Enter the new password again: ')

    def set_password(self):
        self.old_passwords.append(self.password)

    def get_password(self):
        return self.old_passwords[:]

    def is_correct(self):
        if self.old_passwords[-1] == self.password and self.password == self.password2:
            return True
        else:
            return False


manager = PasswordManager()
manager.set_password()
print(manager.get_password())
print(manager.is_correct())
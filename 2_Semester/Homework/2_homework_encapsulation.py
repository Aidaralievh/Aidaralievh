class UserProfile:
    name = 'Adilet'
    _phone_number = '0707390191'
    __password = '23940wjrw'

    def get_password(self):
        return self.__password

    def get_phone_number(self):
        return self._phone_number


account = UserProfile()
print(UserProfile.name, account.get_phone_number(), account.get_password())

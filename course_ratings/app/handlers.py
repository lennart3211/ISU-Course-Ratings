

class AuthHandler:
    def hashPassword(self, password) -> str:
        pass

    def verifyPassword(self, password, hash) -> bool:
        hashed = self.hashPassword(password)
        # TODO: get hashed password from DB and compare

    def login(self, username, password) -> bool:
        hashed_password = self.hashPassword(password)
        if not self.verifyPassword(password, hashed_password):
            return False
        # TODO: login logic
        return True

    def logout(self, entity):
        pass

    def registerUser(self, username, email, password):
        pass

    def editAccount(self, user, username, email):
        pass

    def deleteAccount(self, user):
        pass
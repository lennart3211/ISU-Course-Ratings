class Entity:
    def __init__(self, entityID: int, username: str,
                 email: str, passwordHash: str):
        self.entityID = entityID
        self.username = username
        self.email = email
        self.passwordHash = passwordHash

    def login(self, password: str) -> bool:
        # Authentication should be handled securely
        # by AuthHandler.
        raise NotImplementedError(
            "Use AuthHandler to verify login credentials."
        )

    def logout(self) -> None:
        # Session management belongs in AuthHandler.
        pass

    def changePassword(self, oldPassword: str,
                       newPassword: str) -> None:
        # Password verification and hashing belong
        # in AuthHandler.
        raise NotImplementedError(
            "Use AuthHandler to change the password."
        )

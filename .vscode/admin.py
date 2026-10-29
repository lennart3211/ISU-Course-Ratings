from entity import Entity


class Admin(Entity):
    def __init__(self, entityID: int, username: str,
                 email: str, passwordHash: str):
        super().__init__(
            entityID, username, email, passwordHash
        )

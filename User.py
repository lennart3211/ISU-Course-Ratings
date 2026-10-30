from Entity import Entity


class User(Entity):
    def __init__(self, entityID: int, username: str,
                 email: str, passwordHash: str):
        super().__init__(
            entityID, username, email, passwordHash
        )
        self.reviews = []
        self.savedCourses = []

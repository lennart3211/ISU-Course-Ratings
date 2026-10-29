from entity import Entity
from user import User
from admin import Admin
from role import Role


class EntityFactory:
    @staticmethod
    def createEntity(role: Role, entityID: int,
                     username: str, email: str,
                     passwordHash: str) -> Entity:

        if role == Role.USER:
            return User(
                entityID, username, email, passwordHash
            )

        elif role == Role.ADMIN:
            return Admin(
                entityID, username, email, passwordHash
            )

        else:
            raise ValueError("Invalid entity role")

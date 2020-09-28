from data_classes.schema import EmailData, TeamData, UserData, UsersInTeamsData


class Base:

    name = None
    schema = None

    def __init__(self, storage=None):

        self.storage = storage

    async def read(self, query):
        query = self.storage.query_builder.read_table(self.name)
        return await self.storage.read(query)


class Email(Base):

    name = "email"
    schema = EmailData


class Team(Base):

    name = "team"
    schema = TeamData


class User(Base):

    name = "user"
    schema = UserData


class UsersInTeams(Base):

    name = "users_in_teams"
    schema = UsersInTeamsData


classes = (Email, Team, User, UsersInTeams)

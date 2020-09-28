from data_classes.schema import EmailData, TeamData, UserData, UsersInTeamsData
from data_classes.requests import ReadQuery


class Base:

    name = None
    schema = None

    def __init__(self, storage, query_builder):

        self.storage = storage
        self.query_builder = query_builder
        self.table_name = self.get_table_name()

    def get_table_name(self):
        return self.name

    async def read(self, query: ReadQuery):
        query = self.query_builder.read_table(
            table_name=self.name, query=query
        )
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

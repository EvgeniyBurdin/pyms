from data_classes.schema import UserData


class Base:

    name = None


class User(Base):

    name = "user"
    schema = UserData


component_instances = (User(), )


def get_components():

    return {
        instance.name: instance for instance in component_instances
    }

class Task:

    def __init__(self, name, description, date_created, date_updated, deadline, owner):
        self.name = name
        self.date_created = date_created
        self.description = description
        self.date_updated = date_updated
        self.deadline = deadline
        self.owner = owner

    def create(self):
        # create a task in the db
        pass

    def remove(self):
        # re,ove a task from the db
        pass

    def list_all(self):
        # query all task in the db
        pass


class Reminder:
    pass



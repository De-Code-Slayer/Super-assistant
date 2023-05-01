class Task:

    def __init__(self, name, description, date_created, date_updated, deadline, owner):
        self.name = name
        self.date_created = date_created
        self.description = description
        self.date_updated = date_updated
        self.deadline = deadline
        self.owner = owner

    def create(self, name=None, description=None, date_created=None, date_updated=None, deadline=None, owner=None):
        
        pass
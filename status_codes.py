class StatusCodes:
    
    def __init__(self):
        self.not_number = 'Choice must be a number'
        self.sign_in = 'sign_in'
        self.sign_out = 'sign_out'
        self.exit = 'exit'
        
        self._does_not_exist = 'does_not_exist'
        self._invalid = 'invalid'
        self._create = 'create'
        self._display_all = 'display_all'
        self._update = 'update'
        self._delete = 'delete'
        self._not_found = 'not_found'
        self._found = 'found'
    
    @property
    def not_found(self):
        return self._not_found
    
    @not_found.setter
    def not_found(self, entity):
        self._not_found = f'{entity}_not_found'
    
    @property
    def create(self):
        return self._create

    @create.setter
    def create(self, entity):
        self._create = f'create_{entity}'
    
    @property
    def delete(self):
        return self._delete
    
    @delete.setter
    def delete(self, entity):
        self._delete = f'delete_{entity}'
    
    @property
    def update(self):
        return self._update
    
    @update.setter
    def update(self, entity):
        self._update = f'update_{entity}'
    
    @property
    def found(self):
        return self._found
    
    @found.setter
    def found(self, entity):
        self._found = f'{entity}_found'
    
    @property
    def display_all(self):
        return self._display_all
    
    @display_all.setter
    def display_all(self, entity):
        self._display_all = f'display_all_{entity}'
    
    @property
    def invalid(self):
        return self._invalid
    
    @invalid.setter
    def invalid(self, entity):
        self._invalid = f'invalid_{entity}'

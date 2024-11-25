import os
import json

class Database():
    def get_or_create_db(self, db_name='db'):
        if os.path.exists(f"json/{db_name}.json"):
            with open(f'json/{db_name}.json') as json_file:
                json_data = json.loads(json_file.read())
            print(f'Database {db_name} exist Done...')
            return json_data
        json_data = []
        with open(f'json/{db_name}.json', 'w') as json_file:
            json.dump(json_data, json_file)
            print(f'Database {db_name} created Done...')
        return json_data
    
    def get_all_data_db(self):
        print(self.db_data)

    def get_new_id(self):
        if len(self.db_data) == 0:
            return 1
        return int(self.db_data[-1].get('id')) + 1 
    
    def add_new_data(self, db_name='db'):
        with open(f'json/{db_name}.json', 'w') as json_file:
            json.dump(self.db_data, json_file, indent=4)

    def create_new_data(self, data):
        new_id = self.get_new_id()
        self.db_data.append(
            {
                'id': new_id,
                'title': data.get('title'),
                'author': data.get('author'),
                'year': data.get('year'),
                'status': 'in_stock'
            }
        )
        self.add_new_data()
        print()
        print(f'Book added\nid: {new_id}\ntitle: {data.get('title')}\nauthor: {data.get('author')}\nyear: {data.get('year')}\nstatus: in_stock')
        print()

class Utils(Database):
    def get_commands(self):
        return [
            {
                'id': '1',
                'name': 'Display all books'
            },
            {
                'id': '2',
                'name': 'Book search'
            },
            {   'id': '3',
                'name': 'Adding a book'
            },
            {   'id': '4',
                'name': 'Deleting a book'
            },
            {   'id': '5',
                'name': 'Exit',
            },
        ]
    
    def exit(self):
        exit()

    def print_commands(self):
        print('Commands:')
        commands = self.get_commands()
        for command in commands:
            print(f'{command.get('id')} or {command.get('name')}')

    def get_command_data(self, command):
        commands = self.get_commands()
        return next((item for item in commands if item['name'] == command or item['id'] == command), False)
    
    def get_all_data(self):
        self.get_all_data_db()

    def add_year(self):
        year = input('Enter book year (yyyy): ')
        try:
            if len(year) != 4:
                print(f'{year} - Error format (yyyy)')
                return False
            int(year)
            return year
        except:
            print(f'{year} - Error format (yyyy)')
            return False

    def get_requst(self, command):
        command = command.capitalize() 
        command_data = self.get_command_data(command=command)
        if command_data:
            if command_data.get('id') == '1':
                print(command_data.get('name'))
                self.get_all_data()
            elif command_data.get('id') == '3':
                print(command_data.get('name'))
                title = input('Enter book title: ')
                author = input('Enter book author: ')
                while True:
                    year = self.add_year()
                    if year:
                        break
                
                self.create_new_data(data={'title': title, 'author': author, 'year': year})
                
            elif command_data.get('id') == '5':
                print(command_data.get('name'))
                self.exit()
             
        else:
            print(False)

    def request_processing(self):
        command = input('Enter commsnd: ')
        self.get_requst(command=command)
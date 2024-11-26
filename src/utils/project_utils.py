import os
import json

class Database():
    def get_or_create_db(self, db_name='db'):
        if os.path.exists(f"json/{db_name}.json"):
            try:
                with open(f'json/{db_name}.json') as json_file:
                    json_data = json.loads(json_file.read())
                print(f'Database {db_name} exist Done...')
                return json_data
            except json.JSONDecodeError as e:
                print(f'Error processing JSON: {e}')
                exit()

        json_data = []
        with open(f'json/{db_name}.json', 'w') as json_file:
            json.dump(json_data, json_file)
            print(f'Database {db_name} created Done...')
        return json_data
    
    def get_all_data_db(self):
        for row, data in enumerate(self.db_data):
            print(f'{row + 1} - id: {data.get('id')}, title: {data.get('title')}, author: {data.get('author')}, year: {data.get('year')}, status: {data.get('status')}')
        print()

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

    def get_search_data(self, searhc_key='title'):
        input_search_data = input('Enter search data: ')
        print('Search result:')
        for row, data in enumerate(self.db_data):
            if data[searhc_key] == input_search_data:
                print(f'{row + 1} - id: {data.get('id')}, title: {data.get('title')}, author: {data.get('author')}, year: {data.get('year')}, status: {data.get('status')}')
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
    
    def get_search_commands(self):
        return [
            {
                'id': '1',
                'name': 'Search by title',
                'type': 'title'
            },
            {
                'id': '2',
                'name': 'Search by author',
                'type': 'author'
            },
            {
                'id': '3',
                'name': 'Search by year',
                'type': 'year'
            },
            {
                'id': '4',
                'name': 'Exit'
            }
        ]

    def print_commands(self, command_type=1):
        if command_type == 1:
            print('Commands:')
            commands = self.get_commands()
        elif command_type == 2:
            print('Search commands:')
            commands = self.get_search_commands()
        for command in commands:
            print(f'{command.get('id')} or {command.get('name')}')

    def get_command_data(self, command, command_type=1):
        if command_type == 1:
            commands = self.get_commands()
        if command_type == 2:
            commands = self.get_search_commands()
        return next((item for item in commands if item['name'] == command or item['id'] == command), False)
    
    def search_data(self):
        while True:
            self.print_commands(command_type=2)
            command = input('Enter command: ')
            command = command.capitalize()
            print()
            search_command_data = self.get_command_data(command=command, command_type=2)
            if search_command_data:
                search_type = ['1', '2', '3']
                if search_command_data.get('id') in search_type:
                    print(search_command_data.get('name'))
                    self.get_search_data(searhc_key=search_command_data.get('type'))
                elif search_command_data.get('id') == '4':
                    print(search_command_data.get('name'))
                    break
            else:
                print(False)
    
    
    def exit(self):
        exit()
    
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
        print() 
        if command_data:
            if command_data.get('id') == '1':
                print(command_data.get('name'))
                self.get_all_data()
            elif command_data.get('id') == '2':
                print(command_data.get('name'))
                self.search_data()
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
        command = input('Enter command: ')
        self.get_requst(command=command)

    
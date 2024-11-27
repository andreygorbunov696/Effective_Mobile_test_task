import os
import json

class Database():
    def get_or_create_db(self, db_name='db'):
    # Function: get_or_create_db - Проверка существования файла JSON. Если нет, создать его.
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
    # Function: get_all_data_db - Вывод на экран всех книг из файла JSON.
        for row, data in enumerate(self.db_data):
            print(f'{row + 1} - id: {data.get('id')}, title: {data.get('title')}, author: {data.get('author')}, year: {data.get('year')}, status: {data.get('status')}')
        print()

    def get_new_id(self):
    # Function: get_new_id - Генерация нового ID для записи.
        if len(self.db_data) == 0:
            return 1
        return int(self.db_data[-1].get('id')) + 1 
    
    def add_new_data(self, db_name='db'):
    # Function: add_new_data - Запись новых или изменённых данных в JSON.
        with open(f'json/{db_name}.json', 'w') as json_file:
            json.dump(self.db_data, json_file, indent=4)

    def create_new_data(self, data):
    # Function: create_new_data - Генерация новой структуры данных для книги и добавление данных в JSON. Вывод результата на экран.
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

    def get_search_data(self, search_data, searhc_key='title'):
    # Function: get_search_data - Обработка запроса поиска книг и вывод результата на экран.
        print('Search result:')
        for row, data in enumerate(self.db_data):
            if data[searhc_key] == search_data:
                print(f'{row + 1} - id: {data.get('id')}, title: {data.get('title')}, author: {data.get('author')}, year: {data.get('year')}, status: {data.get('status')}')
                if searhc_key == 'id':
                    return data
        print()

    def get_data_by_id(self, data_id):
    # Function: get_data_by_id - Обрабртка запроса получение данных по ID.
        del_data = self.get_search_data(search_data=data_id, searhc_key='id')
        return del_data
    
    def find_data_index(self, data):
    # Function: find_data_index - Поиск индкса записи и обработка ошибки существования данных.
        try:
            index = self.db_data.index(data)
            return {
                'index': index,
                'status': True
            }
        except ValueError:
            print("Item is not in the list")
            return {'status': False}
        
    def change_status(self, data, data_index):
    # Function: change_status - Обработка запроса на изменения статуса.
        print(f'Old status: {data.get('status')}')
        if data.get('status') == 'in_stock':
            data['status'] = 'issued'
        else:
            data['status'] = 'in_stock'
        print(f'New status: {data.get('status')}')
        self.db_data[data_index] = data
    
    def del_or_change_status_select_data(self, data, action_type=1):
    # Function: del_or_change_status_select_data - Обработка запроса на удаление или изменение статуса после согласия на действия. 
    # Удалить данные или изменить статус, после обновить данные в JSON.
        if action_type == 1:
            self.db_data.remove(data)
            print(f'The book with ID={data.get('id')} has been deleted.')
        elif action_type == 2:
            index = self.find_data_index(data)
            if index.get('status'):
                self.change_status(data=data, data_index=index.get('index'))
        self.add_new_data()

class Utils(Database):
    def get_commands(self):
    # Function: get_commands - Список команд для основного меню.
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
                'name': 'Changing status',
            },
            {   'id': '6',
                'name': 'Exit',
            },
        ]
    
    def get_search_commands(self):
    # Function: get_search_commands - Список команд для раздела "Book search".
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
    # Function: print_commands - Вывод на экран команд меню.
        if command_type == 1:
            print('Commands:')
            commands = self.get_commands()
        elif command_type == 2:
            print('Search commands:')
            commands = self.get_search_commands()
        for command in commands:
            print(f'{command.get('id')} or {command.get('name')}')

    def get_command_data(self, command, command_type=1):
    # Function: get_command_data - Получения списка команд в зависимости от пункта меню.
        if command_type == 1:
            commands = self.get_commands()
        if command_type == 2:
            commands = self.get_search_commands()
        return next((item for item in commands if item['name'] == command or item['id'] == command), False)
    
    def error_command(self, command):
    # Function: error_command - Вывод сообшение об ошибки ввода неверной команды в меню.
        print(f'{command.upper()} The command is incorrect. Select the desired command from the list of commands.')
    
    def search_data(self):
    # Function: search_data - Обработка команды "Book search".
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
                    input_search_data = input('Enter search data: ')
                    self.get_search_data(searhc_key=search_command_data.get('type'), search_data=input_search_data)
                    print('Search result:')
                elif search_command_data.get('id') == '4':
                    print(search_command_data.get('name'))
                    break
            else:
                self.error_command(command=command)

    def check_selection_result(self, selection_result):
    # Function: check_selection_result - Обработка запроса ошибки команды на согласие удалить или изменить статус.
        if selection_result == 'y' or selection_result == 'n':
            return True
        print(f'{selection_result} - Input error. Use y or n.')
        return False
    
    def actions_with_data(self, action_type=1):
    # Function: actions_with_data - Обработка запроса над действиями с данными (удаление, изменение статуса).
        data_id = input('Enter book ID: ')
        try:
            data_id = int(data_id)
            data_by_id = self.get_data_by_id(data_id=data_id)
            if data_by_id is not None:
                while True:
                    if action_type == 1:
                        selection_result = input(f'Are you sure you want to delete a book with an ID={data_by_id.get('id')}? y/n: ')
                    elif action_type == 2:
                        selection_result = input(f'Are you sure you want to change the status of a book with an ID={data_by_id.get('id')}? y/n: ')
                    if self.check_selection_result(selection_result=selection_result):
                        break
                if selection_result == 'y':
                        self.del_or_change_status_select_data(data=data_by_id, action_type=action_type)
                print()
            else:
                print(f'Books with id={data_id} do not exist')
                print()
        except:
            print(f'{data_id} - Errod ID format')
            print()
        
    def del_data(self):
    # Function: del_data - Обработка запроса на удаление данных.
        self.actions_with_data(action_type=1)

    def changing_status(self):
    # Function: changing_status - Обработка запроса на изменение статуса.
        self.actions_with_data(action_type=2)

    def exit(self):
    # Function: exit - Обработка запроса на выход из пртложения.
        exit()
    
    def get_all_data(self):
    # Function: get_all_data - Обработка выбора в меню "Display all books".
        self.get_all_data_db()

    def add_year(self):
    # Function: add_year - Обработка ввода даты (год) и проверка проавильного формата даты.
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
    # Function: get_requst - Обработка команд основного меню.
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
            elif command_data.get('id') == '4':
                print(command_data.get('name'))
                self.del_data()
            elif command_data.get('id') == '5':
                print(command_data.get('name'))
                self.changing_status()
            elif command_data.get('id') == '6':
                print(command_data.get('name'))
                self.exit()
        else:
            self.error_command(command=command)

    def request_processing(self):
    # Function: request_processing - Выбор команд основного меню.
        command = input('Enter command: ')
        self.get_requst(command=command)

    
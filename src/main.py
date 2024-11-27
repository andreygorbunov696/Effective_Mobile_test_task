from utils.project_utils import Utils

class Main(Utils):
    def __init__(self):
        # Function: __init__ - Запуск приложения.
        self.db_data = self.get_or_create_db()
        print()
        while True:
            self.print_commands()
            self.request_processing()

main = Main()
if __name__ == '__main__':
    main
from utils.project_utils import Utils

class Main(Utils):
    def __init__(self):
        self.db_data = self.get_or_create_db()
        print()
        #print(db_data)
        while True:
            self.print_commands()
            self.request_processing()

main = Main()
if __name__ == '__main__':
    main
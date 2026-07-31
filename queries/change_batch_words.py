from lists_manager import ListsManager
from queries.query import Query
from text_file_manager import OneTextFileManager


class ChangeBatchWordsQuery(Query):

    @staticmethod
    def select_text_manager(name: str):
        return OneTextFileManager(name)


    def prompt(self) -> str:
        return 'print cbw to change batch words'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'cbw':
            batch_select: str = input('select batch: ')
            text_manager = self.select_text_manager(batch_select)
            change = True
            foreign_words, local_words = [],[]
            try:
                foreign_words, local_words = text_manager.create_word_lists()
            except ValueError:
                pass
            except FileNotFoundError as e:
                print(e)
                change = False

            lists_manager = ListsManager(foreign_words, local_words)


            while change:
                select_change_mode = input('select change mode(del, add): ')
                if select_change_mode not in ('del', 'add'):
                    continue

                change_mode: bool = True
                while change_mode:
                    print_words = input('print words(foreign, local): ')
                    print_words = print_words.replace(' ', '')
                    words = print_words.split(',')
                    try:
                        if select_change_mode == 'del':
                            lists_manager.delete_word(words[0], words[1])
                        elif select_change_mode == 'add':
                            lists_manager.add_word(words[0], words[1])
                    except IndexError:
                        print('false form')

                    command: str = input(f'press enter to continue {select_change_mode}, or q to exit: ')
                    if command == 'q':
                        change_mode = False

                command = input('press enter to continue batch word changing or q to return in menu: ')
                if command == 'q':
                    change = False


            text_manager.write_text_file(lists_manager.foreign_words, lists_manager.local_words)
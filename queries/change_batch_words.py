from lists_manager import ListsManager
from queries.query import Query
from select_text_file_manager import SelectTextFileManager


class ChangeBatchWordsQuery(Query):



    def prompt(self) -> str:
        return 'print cbw to change batch words'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'cbw':
            batch_select: str = input('select batch: ')
            change = True
            text_manager = None
            words_set: set[tuple[str, str]] = set()
            try:
                select_t_m = SelectTextFileManager()
                text_manager = select_t_m.select(batch_select)
                words_set = text_manager.create_word_set()
            except FileNotFoundError as e:
                print(e)
                change = False
            except ValueError:
                pass


            lists_manager = ListsManager(words_set)


            while change:
                select_change_mode = input('select change mode(del, add): ')
                if select_change_mode not in ('del', 'add'):
                    continue

                change_mode: bool = True
                while change_mode:

                    w_s: set[tuple[str, str]] = lists_manager.words_set
                    for word_pair in w_s:
                        print(f'{word_pair[0]} = {word_pair[1]}')

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

            try:
                text_manager.write_text_file(lists_manager.words_set)
            except FileNotFoundError:
                pass

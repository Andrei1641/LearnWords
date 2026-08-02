from queries.query import Query
from select_text_file_manager import SelectTextFileManager
from text_file_manager import TextFileManager


class ShowBatchQuery(Query):
    @staticmethod
    def __show(name: str):
        text_file_manager: TextFileManager = SelectTextFileManager.select(name)
        word_set: set[tuple[str,str]] = text_file_manager.create_word_set()
        print('\nforeign_words = local_words')
        print('-----------------------------')
        for word_pair in word_set:
            print(f'{word_pair[0]} = {word_pair[1]}')
        print()


    def prompt(self) -> str:
        return 'print sb to show batch words'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'sb':
            name: str = input('print batch name: ').strip()
            ShowBatchQuery.__show(name)
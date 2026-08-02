from queries.query import Query
from show_words_batch import ShowWordsBatch


class ShowBatchQuery(Query):
    def prompt(self) -> str:
        return 'print sb to show batch words'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'sb':
            name: str = input('print batch name: ')
            ShowWordsBatch.show(name)
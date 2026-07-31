from queries.query import Query
from word_batch import WordBatchCreator


class CreateBatchQuery(Query):

    def prompt(self) -> str:
        return 'print crb to create batch'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'crb':
            ex = False
            while not ex:
                name = input('write name of new word batch: ')
                WordBatchCreator().create_word_batch(name)
                command = input('press enter to return in menu or print 1 to create another one')
                if not command:
                    ex = True
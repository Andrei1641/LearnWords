from queries.query import Query
from word_batch import WordBatchManager


class HistoryAddQuery(Query):

    @staticmethod
    def __history_add(batch_name: str):
        word_batch_manager = WordBatchManager()
        word_batch_manager.name = batch_name

        add = True
        while add:
            word_batch_manager.add_stage()

            command = input('print enter to complete another refresh stage or q to exit')
            if command == 'q':
                add = False
                word_batch_manager.set_new_settings()


    def prompt(self) -> str:
        return 'print hisAdd to complete refresh stage'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'hisAdd':
            HistoryAddQuery.__history_add(args[0])
from queries.query import Query
from word_batch import WordBatchManager


class HistoryDeleteQuery(Query):


    def prompt(self) -> str:
        return 'print delHis to delete last refresh time'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'delHis':
            batch_name: str = args[0]

            word_batch_manager = WordBatchManager()
            word_batch_manager.name = batch_name

            delete = True
            while delete:
                word_batch_manager.delete_last_stage()

                command = input('print enter to delete another one last refresh time or q to exit')
                if command == 'q':
                    delete = False
                    word_batch_manager.set_new_settings()
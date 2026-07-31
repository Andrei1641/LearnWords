from pathlib import Path

from queries.query import Query
from word_batch import WordBatchManager


class RemainingTimeCalculateQuery(Query):

    def prompt(self) -> str:
        return 'print tc to calculate remaining times'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'tc':

            dirs = [p.name for p in Path('words').iterdir() if p.is_dir()]
            word_batch_manager = WordBatchManager()

            print()
            for d in dirs:
                word_batch_manager.name = d
                print(f'{d}: {word_batch_manager.remaining_time_calculate()} days')
            print()
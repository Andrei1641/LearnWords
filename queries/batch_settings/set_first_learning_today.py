import os
import subprocess

from queries.query import Query
from word_batch import WordBatchManager
from datetime import date


class SetFirstLearnDayToday(Query):

    @staticmethod
    def __set_learn_day(batch_name: str):
        word_batch_manager: WordBatchManager = WordBatchManager()
        word_batch_manager.name = batch_name

        word_batch_manager.rewrite_start_time(date.today())
        word_batch_manager.set_new_settings()

    def prompt(self) -> str:
        return 'print sfld to set first learn day on today'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'sfld':
            SetFirstLearnDayToday.__set_learn_day(args[0])
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
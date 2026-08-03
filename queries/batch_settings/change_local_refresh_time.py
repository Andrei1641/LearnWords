import os
import subprocess

from queries.query import Query
from word_batch import WordBatchManager


class ChangeLocalRefreshTime(Query):

    @staticmethod
    def __change(name: str, time_list:list[int]):
        word_batch_manager: WordBatchManager = WordBatchManager()
        word_batch_manager.name = name

        word_batch_manager.local_refresh_change(time_list)
        word_batch_manager.set_new_settings()

    def prompt(self) -> str:
        return 'print clrt to change local refresh time of the batch'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'clrt':

            new_refresh_times = input('new refresh times: ')
            new_refresh_times = new_refresh_times.replace(' ', '')
            new_refresh_times = new_refresh_times.split(',')

            time_list: list[int] = [int(t) for t in new_refresh_times]

            ChangeLocalRefreshTime.__change(args[0], time_list)
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
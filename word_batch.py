import json
from datetime import date, timedelta
import os


class WordBatchCreator:

    @staticmethod
    def create_word_batch(name: str):

        template = {"refresh_time" : [],
                    "refresh_history" : [],
                    "creation_date" : f"{date.today()}"}

        os.makedirs(f'words/{name}', exist_ok=True)
        with open(f'words/{name}/local_settings.json', 'x') as f:
            json.dump(template,f, indent=5)

        open(f'words/{name}/words.txt', 'x').close()



class WordBatchManager:
    def __init__(self):
        self.__name: str = ''
        self.__local_refresh_time: list[int] = []
        self.__refresh_history: list[int] = []
        self.__learn_date: date = date(0, 0, 0)


    @property
    def name(self) -> str:
        return self.__name


    @name.setter
    def name(self, name: str):
        self.__name = name
        creation_date_str: str = ''

        with open(f'words/{self.__name}/local_settings.json', 'r') as f:
            settings = json.load(f)
            creation_date_str = settings['creation_date']
            self.__refresh_history = settings['refresh_history']
            self.__local_refresh_time = settings['refresh_time']

        creation_date_l: list[str] = creation_date_str.split('-')
        creation_date_int: list[int] = [int(i) for i in creation_date_l]

        self.__learn_date = date(creation_date_int[0], creation_date_int[1], creation_date_int[2])



    def remaining_time_calculate(self) -> int:

        refresh_time = self.__local_refresh_time
        if not refresh_time:
            with open('settings/global_words_settings/refresh.json', 'r') as f:
                global_settings = json.load(f)
                refresh_time = global_settings['refresh_time']


        refresh_history_len: int = len(self.__refresh_history)

        next_refresh_day: int = -1
        try:
            next_refresh_day = refresh_time[refresh_history_len]
        except IndexError:
            return -1


        current_d: date = date.today()

        d_difference_days: int = (current_d - self.__learn_date).days

        remaining_days = next_refresh_day - d_difference_days

        if remaining_days < 0:
            self.rewrite_start_time(self.__learn_date - timedelta(days=remaining_days))
            remaining_days = 0

        return remaining_days


    def rewrite_start_time(self, new_date: date):
        self.__learn_date = new_date


    def add_stage(self):
        refresh_time = self.__local_refresh_time
        if not refresh_time:
            with open('settings/global_words_settings/refresh.json', 'r') as f:
                global_settings = json.load(f)
                refresh_time = global_settings['refresh_time']

        try:
            self.__refresh_history.append(refresh_time[len(self.__refresh_history)])
        except IndexError:
            print('you are done with learning of the batch')



    def delete_last_stage(self):
        try:
            self.__refresh_history.pop()
        except IndexError:
            print('there is no learn history at the batch')


    def set_new_settings(self):
        new_settings = {"refresh_time": self.__local_refresh_time,
                        "refresh_history": self.__refresh_history,
                        "creation_date": f"{self.__learn_date}"}

        with open(f'words/{self.__name}/local_settings.json', 'w') as f:
            json.dump(new_settings, f, indent=5)
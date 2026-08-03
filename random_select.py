import os
import random
import subprocess


class RandomIndex:
    def __init__(self, i_len: int):
        self.__indexes: list[int] = [i for i in range(0, i_len)]
        self.__tmp_index: int = -1


    @property
    def tmp_index(self) -> int:
        return self.__tmp_index

    @property
    def indexes(self) -> list[int]:
        return self.__indexes

    def reset_indexes(self):
        self.__indexes = []


    def set_random_index(self):
        i = random.randint(0, len(self.__indexes) - 1)
        if len(self.__indexes) != 1:
            while self.__tmp_index == i:
                i = random.randint(0, len(self.__indexes) - 1)

        self.__tmp_index = i


    def delete_index(self):
        self.__indexes.pop(self.__tmp_index)



class RandomLearn:

    @staticmethod
    def __learn_sequence(first: list[str], second: list[str], i: int):
        print(first[i])
        input('press enter to translate')
        print(second[i])


    @staticmethod
    def learn(foreign_words: list[str], local_words: list[str]):
        mode_request:str = input('select learning mode(l-f or f-l): ')
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

        random_select: RandomIndex = RandomIndex(len(foreign_words))

        if mode_request == 'l-f':
            print('local words = foreign words')
            print('-----------------------------')
            for i in range(len(foreign_words)):
                print(f'{local_words[i]} = {foreign_words[i]}')
        elif mode_request == 'f-l':
            print('foreign words = local words')
            print('-----------------------------')
            for i in range(len(foreign_words)):
                print(f'{foreign_words[i]} = {local_words[i]}')
        else:
            print(f'there is no such a mode{mode_request} there is (f-l, l-f)')
            random_select.reset_indexes()
        print()
        while random_select.indexes:
            print(f'({len(random_select.indexes)} words left)')
            random_select.set_random_index()
            if mode_request == 'l-f':
                RandomLearn.__learn_sequence(local_words, foreign_words, random_select.tmp_index)
            elif mode_request == 'f-l':
                RandomLearn.__learn_sequence(foreign_words, local_words, random_select.tmp_index)


            command = input('print 0 to delete or just press enter to continue(q to quit): ')
            if command == '0':
                random_select.delete_index()
            elif command == 'q':
                random_select.reset_indexes()

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
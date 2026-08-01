import random

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
    def learn(foreign_words: list[str], local_words: list[str]):
        mode_request:str = input('select learning mode(l-f or f-l): ')

        random_select: RandomIndex = RandomIndex(len(foreign_words))

        while random_select.indexes:
            random_select.set_random_index()
            if mode_request == 'l-f':
                print(local_words[random_select.tmp_index])
                input('press enter to translate')
                print(foreign_words[random_select.tmp_index])
            elif mode_request == 'f-l':
                print(foreign_words[random_select.tmp_index])
                input('press enter to translate')
                print(local_words[random_select.tmp_index])
            else:
                print(f'there is no such a mode{mode_request} there is (f-l, l-f)')

            command = input('print 0 to delete or just press enter to continue(q to quit): ')
            if command == '0':
                random_select.delete_index()
            elif command == 'q':
                random_select.reset_indexes()
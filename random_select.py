import random

class RandomIndex:
    def __init__(self, i_len: int):
        self.indexes: list[int] = [i for i in range(0, i_len)]
        self.tmp_index: int = -1


    def set_random_index(self):
        i = random.randint(0, len(self.indexes) - 1)
        if len(self.indexes) != 1:
            while self.tmp_index == i:
                i = random.randint(0, len(self.indexes) - 1)

        self.tmp_index = i


    def delete_index(self):
        self.indexes.pop(self.tmp_index)



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

            command = input('print 0 to delete or just press enter to continue: ')
            if command == '0':
                random_select.delete_index()
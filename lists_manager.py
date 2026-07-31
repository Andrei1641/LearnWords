class ListsManager:
    def __init__(self, words_set: set[tuple[str, str]]):
        self.__words_set = words_set



    def delete_word(self, foreign_word: str, local_word:str):
        try:
            self.__words_set.remove((foreign_word, local_word))

        except KeyError:
            print('there is no such word pair')



    def add_word(self, foreign_word: str, local_word:str):
        self.__words_set.add((foreign_word, local_word))



    @property
    def words_set(self) -> set[tuple[str, str]]:
        return self.__words_set

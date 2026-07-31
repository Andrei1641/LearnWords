class ListsManager:
    def __init__(self, foreign_words: list[str], local_words: list[str]):
        self.__foreign_words = foreign_words
        self.__local_words = local_words



    def delete_word(self, foreign_word: str, local_word:str):
        try:
            self.__foreign_words.remove(foreign_word)

        except ValueError:
            print('there is no such foreign word')

        try:
            self.__local_words.remove(local_word)
        except ValueError:
            print('there is no such local word')


    def add_word(self, foreign_word: str, local_word:str):
        self.__foreign_words.append(foreign_word)
        self.__local_words.append(local_word)



    @property
    def foreign_words(self) -> list[str]:
        return self.__foreign_words


    @property
    def local_words(self) -> list[str]:
        return self.__local_words
import numpy as np

class _linker:
    def __init__(self, word_1, word_2, index_1, index_2, letter):
        self._words = (word_1, word_2)
        self._match_indexes = (index_1, index_2)
        self._letter = letter

    def __str__(self):
        return '{}[{}]->{}[{}]/\'{}\''.format(self._words[0], self._match_indexes[0],
                                              self._words[1], self._match_indexes[1], self._letter)

    def get_link(self):
        return self._match_indexes

class wordsearch:
    def __init__(self, word_list, dimensions=(12,12)):
        self._words = word_list
        self._links = None
        self._find_links()
        self._grid = np.chararray(dimensions)
        self._grid[:] = '-'
        self._cache = self._grid.copy()
        self._place_words()
        self._fill_remainder()


    def _place_in_direction(self, word, coordinate, direc=(1,1)):
        try:
            assert len(word)*direc[1]+coordinate[1] < self._grid.shape[0] and len(word)*direc[0]+coordinate[0] < self._grid.shape[1]
            assert len(word)*direc[1]+coordinate[1] > 0 and len(word)*direc[0]+coordinate[0] > 0
        except:
            raise AssertionError
        for i in range(len(word)):
            if self._grid[coordinate[1]+direc[1]*i][coordinate[0]+direc[0]*i] != '-':
                try:
                    assert word[i] == self._grid[coordinate[1]+direc[1]*i][coordinate[0]+direc[0]*i]
                except:
                    self._grid = self._cache.copy()
                    raise AssertionError
            else:
                self._grid[coordinate[1]+direc[1]*i][coordinate[0]+direc[0]*i] = word[i].upper()
        self._cache = self._grid.copy()


    def _find_links(self):
        self._links = []
        for word_i in self._words:
            for word_j in self._words:
                try:
                    assert word_i != word_j
                except:
                    continue
                _matches = [(i, word_i.index(i), word_j.index(i)) for i in word_i if i in word_j]
                if len(_matches) > 0:
                    for match in _matches:
                        self._links.append(_linker(word_i, word_j, match[1], match[2], match[0]))
    
    def _place_words(self):
        from random import randint, randrange
        while len(self._words) > 0:
            for word in self._words:
                _x = randrange(self._grid.shape[0]-1)
                _y = randrange(self._grid.shape[1]-1)
                try:
                    _dir_1 = randint(0,2)-1
                    _dir_2 = randint(0,2)-1
                    self._place_in_direction(word, (_x,_y), (_dir_1,_dir_2)) 
                except:
                    continue
                self._words.remove(word)

    def _fill_remainder(self):
        from string import ascii_uppercase
        from random import choice
        for y in range(self._grid.shape[0]):
            for x in range(self._grid.shape[1]):
                if self._grid[y][x] == '-':
                    self._grid[y][x] = choice(ascii_uppercase)


    def __str__(self):
        return self._grid.__str__()



if __name__ in "__main__":
    x = wordsearch(['apple','pear','pineapple','lemon','melon'])
    print(x)

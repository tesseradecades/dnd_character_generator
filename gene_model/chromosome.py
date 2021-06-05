class Chromosome:
    def __init__(self, genes: list = [], length: int = 0):
        if genes:
            self.__genes: list = genes
        else:
            self.__genes: list = [0] * length

    def __repr__(self):
        return self.get_genes()

    def flip_bit(self, index: int):
        value: int = self.__genes[index]
        if value:
            self.__genes[index] = 0
        else:
            self.__genes[index] = 1

    def get_genes(self):
        return list(self.__genes)

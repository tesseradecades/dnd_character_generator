from gene_model.chromosome import Chromosome


class Test_flip_bit:
    @staticmethod
    def test_zero_to_one():
        # arrange
        chromosome: Chromosome = Chromosome(genes=[0])

        # act
        chromosome.flip_bit(0)

        # assert
        bit: int = chromosome.get_genes()[0]

        assert bit == 1

    @staticmethod
    def test_one_to_zero():
        # arrange
        chromosome: Chromosome = Chromosome(genes=[1])

        # act
        chromosome.flip_bit(0)

        # assert
        bit: int = chromosome.get_genes()[0]

        assert bit == 0


class Test_get_genes:
    @staticmethod
    def test_no_genes():
        # arrange
        chromosome: Chromosome = Chromosome(length=0)
        # act
        genes: list = chromosome.get_genes()
        # assert
        assert genes == []

    @staticmethod
    def test_one_gene():
        # arrange
        chromosome: Chromosome = Chromosome(length=1)
        # act
        genes: list = chromosome.get_genes()
        # assert
        assert genes == [0]

    @staticmethod
    def test_two_genes():
        # arrange
        chromosome: Chromosome = Chromosome(length=2)
        # act
        genes: list = chromosome.get_genes()
        # assert
        assert genes == [0, 0]

    @staticmethod
    def test_preset_genes():
        # arrange
        preset_genes: list = [1, 0]
        chromosome: Chromosome = Chromosome(genes=list(preset_genes))
        # act
        genes: list = chromosome.get_genes()
        # assert
        assert genes == preset_genes

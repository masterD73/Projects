from collections import namedtuple
from functools import partial
from random import choices, randint, randrange, random
from typing import List, Callable, Tuple

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulationFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]

Thing = namedtuple("Thing", ["name", "value", "weight"])
things = [
    Thing("Laptop", 500, 2200),
    Thing("Headphones", 150, 160),
    Thing("Coffee Mug", 60, 350),
    Thing("Notepad", 40, 333),
    Thing("Water Bottle", 30, 192)]
more_things = [
                  Thing("Mints", 1000, 2200),
                  Thing("Socks", 250, 160),
                  Thing("Tissues", 100, 350),
                  Thing("Phone", 80, 333),
                  Thing("Baseball Cap", 100, 70)] + things


def generate_genome(genome_length: int) -> Genome:
    return choices([0, 1], k=genome_length)


def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]


def fitness(genome: Genome, things: [Thing], weight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("Genome and things must be of the same length")
    weight = 0
    value = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value
            if weight > weight_limit:
                return 0
    return value


def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(population=population, weights=[fitness_func(genome) for genome in population], k=2)


def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    length = len(a)
    if length != len(b):
        raise ValueError("Genomes must be of the same length")
    if length < 2:
        return a, b

    cross = randint(1, length - 1)
    return a[:cross] + b[cross:], b[:cross] + a[cross:]


def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if probability > random() else 1 - genome[index]
    return genome


def run_evolution(fitness_limit: int,
                  population_func: PopulationFunc = generate_population,
                  fitness_func: FitnessFunc = fitness,
                  selection_func: SelectionFunc = selection_pair,
                  crossover_func: CrossoverFunc = single_point_crossover,
                  mutation_func: MutationFunc = mutation,
                  generation_limit: int = 100) -> Tuple[Population, int]:
    population = population_func()
    for generation in range(generation_limit):
        population = sorted(population, key=lambda genome: fitness_func(genome), reverse=True)
        if fitness_func(population[0]) > fitness_limit:
            break
        next_generation = population[:2]

        for j in range(len(population) // 2 - 1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(*parents)
            offspring_a, offspring_b = mutation_func(offspring_a), mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]
        population = next_generation
    return population, generation


def genome_to_things(genome, things):
    items = []
    length = len(genome)
    if length != len(things):
        raise ValueError("Genome and things must be of the same length")
    for i in range(length):
        if genome[i] == 1:
            items.append(things[i].name)
    return items


def main():
    population, generation = run_evolution(
        population_func=partial(generate_population, size=10, genome_length=len(things)),
        fitness_func=partial(fitness, things=things, weight_limit=3000),
        generation_limit=1000,
        fitness_limit=740)
    print(f'number of generations: {generation}')
    print(f'best genome: {population[0]}')
    print(genome_to_things(population[0], things))
    assert ['Laptop', 'Headphones', 'Coffee Mug', 'Water Bottle'] == genome_to_things(population[0], things)


if __name__ == '__main__':
    main()
    print("Done.")

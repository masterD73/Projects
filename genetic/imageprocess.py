import numpy as np
import skimage as ski
from functools import partial
from matplotlib import pyplot as plt


def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


def main():
    population_size = 60
    mutation_rate = 0.01
    generations = 100  # Increased generations
    target_image = ski.data.rocket()
    h, w, d = target_image.shape
    population = np.array([np.random.randint(0, 256, target_image.shape) for _ in range(population_size)])

    for generation in range(generations):
        population = sorted(population, key=partial(fitness, target_image=target_image), reverse=True)
        next_generation = population[:10]  # Elitism
        while len(next_generation) < population_size - 5:
            parent_indices = np.random.choice(range(10), 2, replace=False)
            parents = [population[parent_indices[0]], population[parent_indices[1]]]
            child = crossover_color_image(parents[0], parents[1])
            child = mutate(child, h, w, mutation_rate)
            next_generation.append(child)
        random_individuals = [np.random.randint(0, 256, target_image.shape) for _ in range(5)]
        next_generation.extend(random_individuals)
        population = next_generation
        mutation_rate = max(0.01, mutation_rate * 0.95)

        print(f'Generation {generation} best fitness: {fitness(population[0], target_image)}')
        if generation % 10 == 0:
            show_image(population[0], f'Generation {generation}')

    best_image = population[0]
    show_image(best_image, 'Best Image')
    show_image(target_image, 'Target Image')


def fitness(image, target_image):
    return -np.mean((image - target_image) ** 2)


def crossover_color_image(parent1, parent2):
    crossover_point_rows = np.random.randint(0, parent1.shape[0])
    crossover_point_cols = np.random.randint(0, parent1.shape[1])
    child = np.zeros_like(parent1)
    child[:crossover_point_rows, :crossover_point_cols] = parent1[:crossover_point_rows, :crossover_point_cols]
    child[crossover_point_rows:, crossover_point_cols:] = parent2[crossover_point_rows:, crossover_point_cols:]
    return child


def mutate(image, height, width, mutation_rate):
    num_mutations = int(height * width * mutation_rate)
    for _ in range(num_mutations):
        x, y, c = np.random.randint(0, height), np.random.randint(0, width), np.random.randint(0, 3)
        image[x, y, c] = np.random.randint(0, 256)
    return image


if __name__ == '__main__':
    main()
    print("Done.")

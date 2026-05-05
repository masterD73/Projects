import functools
import operator
import time

import gari
import pygad
import imageio
import numpy as np
import functools
import operator
import matplotlib.pyplot as plt
from PIL import Image


def fitness_function(individual, target):
    return np.mean((individual - target) ** 2)


def evaluate_population(population, target):
    fitness_scores = np.array([fitness_function(individual, target) for individual in population])
    return fitness_scores


def select_parents(population, fitness_scores):
    probabilities = 1 / (fitness_scores + 1e-6)  # Inverse of fitness
    probabilities /= probabilities.sum()
    parents_indices = np.random.choice(len(population), size=population_size, p=probabilities)
    return population[parents_indices]


def crossover(parent1, parent2):
    alpha = np.random.uniform(0, 1, image_shape)
    return alpha * parent1 + (1 - alpha) * parent2


def perform_crossover(parents):
    offspring = []
    for i in range(0, len(parents), 2):
        parent1, parent2 = parents[i], parents[(i + 1) % len(parents)]
        child = crossover(parent1, parent2)
        offspring.append(child)
    return np.array(offspring)


def mutate(individual, mutation_rate=0.01):
    mutation_mask = np.random.rand(*image_shape) < mutation_rate
    individual[mutation_mask] = np.random.rand(np.sum(mutation_mask))
    return individual


def perform_mutation(offspring, mutation_rate=0.01):
    return np.array([mutate(child, mutation_rate) for child in offspring])


def main():
    global population
    best_individual = None

    for generation in range(num_generations):
        fitness_scores = evaluate_population(population, target_array)
        print(f"Generation {generation}, Best Fitness: {fitness_scores.min()}")

        if best_individual is None or fitness_scores.min() < fitness_function(best_individual, target_array):
            best_individual = population[np.argmin(fitness_scores)]

        if fitness_scores.min() < 1e-5:  # Convergence threshold
            break

        parents = select_parents(population, fitness_scores)
        offspring = perform_crossover(parents)
        offspring = perform_mutation(offspring, mutation_rate)

        # Preserve best individual (elitism)
        offspring[0] = best_individual
        population = offspring

    # Best match
    best_match = (best_individual * 255).clip(0, 255).astype("uint8")
    im = Image.fromarray(best_match)
    im.save("your_file.jpeg")
    plt.imshow(im)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    start = time.time()
    target_image = imageio.v2.imread('photo.jpg')
    target_array = np.asarray(target_image / 255, dtype=np.float64)

    population_size = 50
    image_shape = target_array.shape
    population = np.random.rand(population_size, *image_shape)

    num_generations = 12
    mutation_rate = 0.05
    main()
    end = time.time()
    print(f"program duration:{end - start}")
    print("Done.")

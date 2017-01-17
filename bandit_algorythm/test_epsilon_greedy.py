execfile('epsilon_greedy/epsilon_greedy.py')

import random

e = EpsilonGreedy(0.1, [], [])

random.seed(1)
means = [0.1, 0.1, 0.1, 0.1, 0.9]
n_arms = len(means)
random.shuffle(means)

arms = map(lambda (mu): BernoulliArm(mu), means)
print("Best arm is " + str(e.ind_max(means)))

f = open("epsilon_greedy/standard_results.tsv", "w")

for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5]:
    algo = EpsilonGreedy(epsilon, [], [])
    algo.initialize(n_arms)
    results = test_algorythm(algo, arms, 5000, 250)
    for i in range(len(results[0])):
        f.write(str(epsilon) + "\t")
        f.write("t".join([str(results[j][i]) for j in range(len(results))]) + "\n")

f.close()

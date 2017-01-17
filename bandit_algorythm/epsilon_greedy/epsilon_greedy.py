class EpsilonGreedy():
    def __init__(self, epsilon, counts, values):
        self.epsilon = epsilon
        self.counts = counts
        self.values = values
        return

    def initialize(self, n_arms):
        self.counts = [0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]
        return

    def ind_max(x):
        m = max(x)
        return x.index(m)

    def select_arm(self):
        if random.random() > self.epsilon:
            return ind_max(self.values)
        else:
            return random.randrange(len(self.values))

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1
        n = self.counts[chosen_arm]

        value = self.values[chosen_arm]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value
        return

    def test_algorythm(algo, arms, num_sims, horizon):
        chosen_arm = [0.0 for i in range(num_sims * horizon)]
        rewards = [0.0 for i in range(num_sims * horizon)]
        cumulative_rewards = [0.0 for i in range(num_sims * horizon)]
        sim_nums = [0.0 for i in range(num_sims * horizon)]
        times = [0.0 for i in range(num_sims * horizon)]

        for sim in range(horizon):
            sim = sim + 1
            algo.initialize(len(arms))

            for t in range(horizon):
                t = t + 1
                index = (sim - 1) * horizon + t - 1

        sim_nums[index] = sim
        times[index] = t

        chosen_arm = algo.select_arm()
        chosen_arms[index] = chosen_arm

        reward = arms[chosen_arms[index]].draw()
        rewards[index] = reward

        if t == 1:
            cumulative_rewards[index] = reward
        else:
            cumulative_rewards[index] = cumulative_rewards[index - 1] + reward
            algo.update(chosen_arm, reward)

        return [sim_nums, times, chosen_arms, rewards, cumulative_rewards]

class BernoulliArm():
    def __init__(self, p):
        self.p = p

    def draw(self):
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0

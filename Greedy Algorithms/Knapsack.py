class KnapsackPackage:

    def __init__(self, w, v):
        self.weight = w
        self.value = v
        self.cost = v / w

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value

    def getCost(self):
        return self.cost


def knapsack(weights, values, max_weight):
    n = len(weights)
    costs = [0] * n

    for i in range(n):
        costs[i] = KnapsackPackage(weights[i], values[i])

    costs.sort(key=lambda x: x.cost, reverse=True)

    remain = max_weight
    max_profit = 0
    flag = 0

    i = 0
    while not flag:
        if costs[i].getWeight() <= remain:
            remain -= costs[i].getWeight()
            max_profit += costs[i].getValue()
            print(f'Package ==> weight: {costs[i].getWeight()},  val: {costs[i].getValue()}')

        elif remain > 0:
            rest = costs[i].getValue() * (remain/costs[i].getWeight())
            max_profit += rest
            remain = 0
            print(f'Package ==> weight: {costs[i].getWeight()},  val: {costs[i].getValue()}')
            flag = 1
        else:
            flag = 1
        i += 1
    return max_profit


weights = [1, 3, 5, 4, 1, 3, 2]
values = [5, 10, 15, 7, 8, 9, 4]
Profit = knapsack(weights, values, 15)
print(Profit)

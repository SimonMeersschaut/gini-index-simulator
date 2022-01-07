# AUTHOR: Simon Meersschaut
import random
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

left, width = .25, 0.7
bottom, height = .25, 0.7
right = left + width
top = bottom + height


def gini_index(x):
    # (Warning: This is a concise implementation, but it is O(n**2)
    # in time and memory, where n = len(x).  *Don't* pass in huge
    # samples!)
    # Mean absolute difference
    mad = np.abs(np.subtract.outer(x, x)).mean()
    # Relative mean absolute difference
    rmad = mad/np.mean(x)
    # Gini coefficient
    g = 0.5 * rmad
    return g


class User:
    def __init__(self, capital):
        self.capital = capital
        self.minimum = random.random()*20


class Group:

    def __init__(self, users, gini_target):
        simulations = []
        for i in range(1, 100+1):
            simulations.append([User(capital=random.randint(500, 1000))
                                for i in range(users)])
        simulations = sorted(simulations, key=lambda simulation: abs(gini_target-gini_index([
                             user.capital for user in simulation])))
        self.users = simulations[0]

    @property
    def gini_index(self):
        return gini_index([user.capital for user in self.users])

    @property
    def sorted(self):
        return [user for user in sorted(self.users, key=lambda user: user.capital) if user.capital > user.minimum]

    @property
    def lowest(self):
        return self.sorted[random.randint(0, int(len(self.sorted)/1.2))]

    @property
    def highest(self):
        return self.sorted[random.randint(int(len(self.sorted)/1.2), len(self.sorted)-1)]

    @property
    def total(self):
        return sum([user.capital for user in self.users])

try:
    gini_target = float(input('Gini-index: '))/100
except ValueError:
    input('[ERROR] Invalid input, the progam will close.\n\npress <enter>')
    exit()
if gini_target > 1:
    input('[ERROR] Invalid input, the progam will close.\n\npress <enter>')
    exit()
try:
    users = int(input('Amount of users: '))
except ValueError:
    input('[ERROR] Invalid input, the progam will close.\n\npress <enter>')
    exit()
if users > 1000:
    print(f'[ERROR] Max users is 1000\n{users} -> 1000')
    users = 1000
if users < 3:
    print(f'[ERROR] Min users is 3\n{users} -> 3')
    users = 3

group = Group(users=users, gini_target=gini_target)

i = 0
while group.gini_index != gini_target and i < 5000*users:
    try:
        if group.gini_index > gini_target:
            group.highest.capital -= random.random()*(group.gini_index-gini_target)*20
        else:
            group.lowest.capital -= random.random()*(gini_target-group.gini_index)*20
        if i % 5000 == 0:
            print(f'[SIMULATION] current gini-index={group.gini_index*100}')
        i += 1
    except Exception as e:
        print('ERROR: '+str(e))
        break


sorted = [user for user in sorted(group.users, key=lambda user: user.capital)]
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.bar([i for i in range(len(sorted))], [
       user.capital/group.total*100 for user in sorted])  #
scientific_notation = "{:e}".format(gini_target-group.gini_index)
ax.set_title(f'Gini-index: {gini_target*100}')
plt.ylabel('Percent of total money')
from matplotlib.offsetbox import AnchoredText
at = AnchoredText(
    f'error: {scientific_notation}', prop=dict(size=8), frameon=False, loc='upper left')
if abs(gini_target-group.gini_index) > 0.01:
    print('ALERT')
    at = AnchoredText(
    f'error: {scientific_notation}', prop=dict(size=8, color='red'), frameon=False, loc='upper left')
    at.color='r'
else:
    at = AnchoredText(
    f'error: {scientific_notation}', prop=dict(size=8), frameon=False, loc='upper left')
ax.add_artist(at)
plt.show()

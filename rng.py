#!/usr/bin/env python
import random
rng_list = ["alice", "bart", "clyde", "drake"]
randomelement = random.choice(rng_list)
print(randomelement)

rng_list.append('Eric')
rng_list.extend(['Frank', 'Gloria', 'Helen'])
rng_list.insert(1, 'Zeke')

randomelement2 = random.choice(rng_list)
print(randomelement2)
print(rng_list)
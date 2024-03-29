# Candogan

############################################################
import normal_game	 as ng
############################################################

# quick list for size of u
# 2      AN = 2
# 2x1    AN = 4
# 2x2: 	 AN = 8
# 2x3: 	 AN = 12
# 3x3: 	 AN = 18
# 2x2x2: AN = 24
# 4x4: 	 AN = 32

import numpy as np
import time
import utils
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
import yaml

#######################################
with open('config.yml', 'r') as file:
	config = yaml.safe_load(file)


results_dir = config['results_dir']
experiment_name = config['experiment_name']
results_dir += experiment_name
#######################################

start = time.time()

print('\n\n\n\n\n\n')

# G = ng.GameFull([2,2], **config)
G = ng.Game([2,2], **config)

# u = np.random.randint(-5, 5, G.num_payoffs)

# 4x4
# u = [0.0, 1.0, -2.0, 1.0, -1.0, 0.0, 3.5, -2.5, 2.0, -3.5, 0.0, 1.5, -1.0, 2.5, -1.5, 0.0, 0.0, -1.0, 2.0, -1.0, 1.0, 0.0, -3.5, 2.5, -2.0, 3.5, 0.0, -1.5, 1.0, -2.5, 1.5, 0.0]
# u = [0.0, 0.3310862697506767, 0.9741583642123127, -1.3052446339629893, -0.3310862697506767, 0.0, 0.17121535296633528, 0.1598709167843414, -0.9741583642123127, -0.17121535296633528, 0.0, 1.145373717178648, 1.3052446339629893, -0.1598709167843414, -1.145373717178648, 0.0, 0.0, -0.3310862697506767, -0.9741583642123127, 1.3052446339629893, 0.3310862697506767, 0.0, -0.17121535296633528, -0.1598709167843414, 0.9741583642123127, 0.17121535296633528, 0.0, -1.145373717178648, -1.3052446339629893, 0.1598709167843414, 1.145373717178648, 0.0]

# 5x5
# u = [0.0, 0.07668359805081815, 0.020267545581826307, 0.5352050823224256, -0.63215622595507, -0.07668359805081815, 0.0, 0.12322132825896137, 0.45828090250203735, -0.5048186327101806, -0.020267545581826307, -0.12322132825896137, 0.0, 0.7751018777858568, -0.6316130039450691, -0.5352050823224256, -0.45828090250203735, -0.7751018777858568, 0.0, 1.7685878626103197, 0.63215622595507, 0.5048186327101806, 0.6316130039450691, -1.7685878626103197, 0.0, 0.0, -0.07668359805081815, -0.020267545581826307, -0.5352050823224256, 0.63215622595507, 0.07668359805081815, 0.0, -0.12322132825896137, -0.45828090250203735, 0.5048186327101806, 0.020267545581826307, 0.12322132825896137, 0.0, -0.7751018777858568, 0.6316130039450691, 0.5352050823224256, 0.45828090250203735, 0.7751018777858568, 0.0, -1.7685878626103197, -0.63215622595507, -0.5048186327101806, -0.6316130039450691, 1.7685878626103197, 0.0]
# u = [0, 1, 1, -2, -1, 0, -2, 3, 1, 2, 0, -1, 0, -3, 1, 0, 0, -1, 1, 0, 1, 0, 2, -3, 1, -2, 0, 1, -2, 3, -1, 0]
# u = [5, -1, 1, 7, 1, -3, 3, 3, -1, 5, 7, 3, -1, 1, 3, 1, -3, -1]
# u = [1, 2, -3, 4, 5, -9, -5, -7, 12]
# u += list(-np.array(u))

# u = [5, -9, -7, 3, 6, 11, -3, -7, -1, -2, 8, 0, -4, -2, -4, 1, -3, -3, -1, 4, 0, 0, 1, -4, 1, 5, 11, 8, 1, 0, -9, -3, 0, -3, 0, -7, -7, -4, -3, 1, 3, -1, -2, -1, -4, 6, -2, -4, 4, 1]

# u = [1, 2, -1, 3, 1, 4, 6, 2, -3, 1, 3, 6, 2, 1, 2, -1, 4, -3]
# u = [1, -6, -8, 7, 8, -5, -5, -9, -1, 1, 7, -5, -6, 8, -9, -8, -5, -1]

# u = np.random.randint(-5, 5, 18 )

# u = [4.00000000000000, 5.00000000000000, -6.00000000000000, 3.00000000000000, 3, 3, -1, 1, -6.00000000000000, -3.00000000000000, -3, -3, 3, -1, 1, -2, -1.00000000000000, -3, 0, -2, -2, -1, -3, 0]
# u = [2.00000000000000, -3.00000000000000, 4.00000000000000, 2.00000000000000, 2, -3, 3, 3, 5.00000000000000, -3.00000000000000, 2, 0, 3, -1, 0, 2, -2.00000000000000, 1, 2, 0, -2, 1, 1, -3]

# 2x2 potential
# u = [0, -1, 3, 0, 0, 1, -1, -2]

# 2x2 random + NS
# u = np.array([0, 1, 2, -1, 3, -1, 2, 0]) + np.array([2, 3, 2, 3, 4, 4, 5, 5])

# 2x2 NS
# u = [2, 3, 2, 3, 4, 4, 5, 5]


u = np.random.randint(-10, 10, 8)
# u = np.array([-5, -4, -3, 2, -5, -3, -4, 2])
# u = [1, -2, -3, -4, -1, -4, 1, 4, -3, 1, -4, 1, -2, -1, 4, -3, -4, -3]
# u = [-1, -2, -3, 10, 9, 8, 5, 4, 3, -1, 10, 5, -2, 9, 4, -3, 8, 3]

# U = ng.PayoffFull(game = G, payoff_vector = u, **config)
U = ng.Payoff(game = G, payoff_vector = u, **config)

end = time.time()

print("\nEND\nThe time of execution of above program is :",
	(end-start) * 10**3, "ms")


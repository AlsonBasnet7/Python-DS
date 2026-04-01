# Bayes Theorem - Probability that defective item came from Machine Y

# Production of machines
X = 1500
Y = 3000
Z = 4500

# Total production
total = X + Y + Z

# Probabilities of selecting from each machine
P_X = X / total
P_Y = Y / total
P_Z = Z / total

# Defective probabilities
P_D_given_X = 0.015
P_D_given_Y = 0.02
P_D_given_Z = 0.022

# Total probability of defective item
P_D = (P_X * P_D_given_X) + (P_Y * P_D_given_Y) + (P_Z * P_D_given_Z)

# Bayes theorem: Probability item came from Y given it is defective
P_Y_given_D = (P_Y * P_D_given_Y) / P_D

# Output
print("Probability that defective item came from Machine Y:", P_Y_given_D)
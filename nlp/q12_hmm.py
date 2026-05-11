# Q12. Hidden Markov Model - Viterbi Algorithm
# Find the most likely sequence of hidden states given observations

states       = ["Sunny", "Rainy"]
observations = ["Walk", "Shop", "Clean"]

initial_prob = {"Sunny": 0.6, "Rainy": 0.4}

transition_prob = {
    "Sunny": {"Sunny": 0.7, "Rainy": 0.3},
    "Rainy": {"Sunny": 0.4, "Rainy": 0.6},
}

emission_prob = {
    "Sunny": {"Walk": 0.6, "Shop": 0.3, "Clean": 0.1},
    "Rainy": {"Walk": 0.1, "Shop": 0.4, "Clean": 0.5},
}

obs_sequence = ["Walk", "Shop", "Clean"]

# viterbi[t][state] = max probability of reaching state at time t
viterbi   = []
backtrack = []

# t = 0: initialise
v0 = {}
b0 = {}
for s in states:
    v0[s] = initial_prob[s] * emission_prob[s][obs_sequence[0]]
    b0[s] = None
viterbi.append(v0)
backtrack.append(b0)

# t = 1 onwards: recurse
for t in range(1, len(obs_sequence)):
    vt = {}
    bt = {}
    for s in states:
        best_prob = -1
        best_prev = None
        for prev in states:
            prob = viterbi[t-1][prev] * transition_prob[prev][s] * emission_prob[s][obs_sequence[t]]
            if prob > best_prob:
                best_prob = prob
                best_prev = prev
        vt[s] = best_prob
        bt[s] = best_prev
    viterbi.append(vt)
    backtrack.append(bt)

# Find best last state
best_last = max(states, key=lambda s: viterbi[-1][s])

# Backtrack
best_path = [best_last]
for t in range(len(obs_sequence)-1, 0, -1):
    best_path.insert(0, backtrack[t][best_path[0]])

print("Observation sequence:", obs_sequence)
print()
for t in range(len(obs_sequence)):
    print("t=" + str(t), obs_sequence[t], "-> Sunny:", round(viterbi[t]["Sunny"], 5), "  Rainy:", round(viterbi[t]["Rainy"], 5), "  Best:", best_path[t])

print()
print("Most likely state sequence:", best_path)

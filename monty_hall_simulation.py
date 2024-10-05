import random
import seaborn as sns
import matplotlib.pyplot as plt

def monty_hall_simulation(num_trials):
    switch_wins = 0
    stay_wins = 0
    
    for _ in range(num_trials):
        # Place car behind one of the three doors
        car = random.randint(1, 3)
        # Contestant makes an initial choice
        initial_choice = random.randint(1, 3)
        
        # Host opens a door that is neither the car nor the initial choice
        remaining_doors = [door for door in [1, 2, 3] if door != initial_choice and door != car]
        host_open = random.choice(remaining_doors)
        
        # The contestant decides to switch to the other remaining door
        switch_choice = [door for door in [1, 2, 3] if door != initial_choice and door != host_open][0]
        
        # Check if switching wins
        if switch_choice == car:
            switch_wins += 1
        else:
            stay_wins += 1
    
    return switch_wins, stay_wins

# Run the simulation
num_trials = 10000
switch_wins, stay_wins = monty_hall_simulation(num_trials)

# Display results
print(f"Switching wins: {switch_wins / num_trials * 100:.2f}%")
print(f"Staying wins: {stay_wins / num_trials * 100:.2f}%")

# Plot the results using seaborn
results = {'Strategy': ['Switch'] * switch_wins + ['Stay'] * stay_wins}
plt.figure(figsize=(10, 6))
sns.countplot(x='Strategy', data=results, palette='viridis')
plt.xlabel('Strategy')
plt.ylabel('Number of Wins')
plt.title('Monty Hall Simulation Results')
plt.show()
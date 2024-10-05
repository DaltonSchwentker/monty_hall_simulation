# Monty Hall Problem Simulation

This repository contains a Python script that simulates the Monty Hall problem, a famous probability puzzle. The Monty Hall problem is based on a television game show where a contestant is asked to choose between three doors. Behind one door is a car, and behind the other two doors are goats. After the contestant makes their initial choice, the host (who knows what is behind each door) opens one of the remaining doors to reveal a goat. The contestant is then given the option to stick with their original choice or switch to the other unopened door. This simulation illustrates why switching doors gives a better chance of winning the car.

## Project Overview
The purpose of this project is to explore the statistical aspects of the Monty Hall problem by running a simulation of the game multiple times. The script simulates the decision-making process, calculates the outcomes, and visualizes the results using a bar plot.

## Features
- Simulates the Monty Hall problem for a user-defined number of trials.
- Compares the results between switching doors and staying with the initial choice.
- Visualizes the outcomes using a bar plot for easy comparison.

## Requirements
To run the script, you'll need Python 3 and the following packages:
- `matplotlib` (for plotting)
- `seaborn` (for improved plot aesthetics)
- `pandas` (for data handling)

You can install these packages using:
```sh
pip install matplotlib seaborn pandas
```

## Usage
1. Clone this repository:
```sh
git clone https://github.com/yourusername/monty_hall_simulation.git
```
2. Navigate to the project directory:
```sh
cd monty_hall_simulation
```
3. Run the Python script to simulate the Monty Hall problem:
```sh
python monty_hall_simulation.py
```

The script will display the percentage of wins for both switching and staying, as well as generate a bar plot comparing the two strategies.

## Explanation of the Monty Hall Problem
The Monty Hall problem is counterintuitive for many people. Initially, the probability of choosing the car is 1/3, while the probability of choosing a goat is 2/3. When Monty reveals a goat behind one of the remaining doors, the probability distribution changes. By switching, the contestant increases their chances of winning the car to 2/3, whereas staying keeps the original 1/3 chance.

This script simulates the Monty Hall game multiple times to show that switching doors indeed leads to a higher probability of winning.

## Example Output
```
Switching wins: 66.77%
Staying wins: 33.23%
```

The visualization will also show a bar plot comparing the number of wins for each strategy.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as needed.

## Author
- [Your Name](https://github.com/yourusername)

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your changes.

## Acknowledgements
- Marilyn vos Savant for popularizing the Monty Hall problem.
- The mathematics community for their insights into probability theory and decision making.


import numpy as np
import matplotlib.pyplot as plt

# Given values
fixed_cost = 3307.4
registration_fee_per_team = 300
max_teams = 6
ticket_price_per_audience = 3
expected_audience = 750

# Total revenue from registrations
total_registration_revenue = np.arange(0, max_teams + 1) * registration_fee_per_team

# Total revenue from audience tickets
total_ticket_revenue = np.full(len(total_registration_revenue), ticket_price_per_audience * expected_audience)

# Total revenue (teams + audience)
total_revenue = total_registration_revenue + total_ticket_revenue

# Finding the break-even teams more accurately
break_even_teams = np.where(total_revenue >= fixed_cost)[0][0]  # Get the first index where total_revenue exceeds fixed_cost
break_even_revenue = total_revenue[break_even_teams]

# Create the cost and revenue lines for the break-even chart
units = np.arange(0, max_teams + 1)
total_costs = np.full(len(units), fixed_cost)

y_axis_range = np.arange(0, 4501, 500)

# Plotting
plt.figure(figsize=(10,6))
plt.plot(units, total_revenue, label='Total Revenue', marker='o')
plt.plot(units, total_costs, label='Total Fixed Costs', linestyle='--')

plt.plot(break_even_teams, break_even_revenue, 'ro')  # Mark the break-even point
plt.axvline(break_even_teams, color='g', linestyle='--', label=f'Break-even Point: {break_even_teams} Teams')
plt.axhline(fixed_cost, color='r', linestyle='--', label=f'Fixed Costs: MYR {fixed_cost}')

# Adding labels and title
plt.ylim(0, 4500)
plt.yticks(y_axis_range)
plt.title('Break-Even Analysis: MMU Basketball Tournament')
plt.xlabel('Number of Teams Register')
plt.ylabel('Amount (MYR)')
plt.legend()
plt.grid(True)

# Show plot
plt.show()

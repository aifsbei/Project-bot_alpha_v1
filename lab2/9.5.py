m_number_of_ready_to_cook = int(input())
food = [input() for i in range(m_number_of_ready_to_cook)]
n_number_of_days = int(input())
total_used_food = []
for i in range(n_number_of_days):
    quantity = int(input())
    food_per_day = [input() for i in range(quantity)]
    total_used_food.append(food_per_day)
set_of_used_food = set([item for i in range(n_number_of_days) for item in total_used_food[i]])
print(*(set(food) - set_of_used_food), sep='\n')
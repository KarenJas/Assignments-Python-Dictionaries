#4. Python Essentials for Business Analytics

import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

new_weakly_sales = copy.deepcopy(weekly_sales)
new_weakly_sales["Week 2"]["Electronics"] = 18000

print(new_weakly_sales)
print(weekly_sales)

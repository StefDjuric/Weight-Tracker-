import matplotlib.pyplot as plt

DATES = []
WEIGHTS = []

print('When you are done entering information type "done".')
# weight_metric = input('Do you want the weight in "lbs" or "kg": ')

while True:
    date = input('Enter the next date: ')
    if date.lower() == 'done':
        break
    else:
        weight = float(input(f'Enter the weight you had on {date}: '))
        DATES.append(date)
        WEIGHTS.append(weight)


plt.plot(DATES, WEIGHTS)
plt.xlabel('Date [DD.MM.YY]')
plt.ylabel('Weight [KG]')

plt.title('Weight Tracker')

plt.show()

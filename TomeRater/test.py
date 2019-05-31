a = {}
a["Miljan"] = 1
a["nobody"] = None
a["somebody"] = 2

sum_of_ratings = 0
count_of_ratings = 0
for keys, values in a.items():
    if values != None:
        sum_of_ratings += values
        count_of_ratings += 1

ratings = [v for k, v in a.items() if v != None]
sm = sum(ratings)
ct = len(ratings)
print(f'sum_of_ratings is {sm}, count_of_ratings is {ct}')
print(f'average is {sm/ct}')
movie_list = dict()
movie_list['Deadpool'] = 2019
movie_list['John Wick 3'] = 2023

print(movie_list['John Wick 3'])

added_movie = ["Avator", "Demon Slayer"]
for s in added_movie:
    movie_list[s] = 2020
    
del movie_list['John Wick 3']

[print(movie_list)]
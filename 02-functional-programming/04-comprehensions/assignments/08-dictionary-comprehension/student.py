def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}

def director_to_titles(movies):
    dict_by_director = {}
    for movie in movies:
        if movie.director not in dict_by_director:
            dict_by_director[movie.director] = [movie.title]
        else:
            dict_by_director[movie.director].append(movie.title)
    return dict_by_director

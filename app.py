from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie = movie.lower().strip()
    movie_index = movies[movies['title'].str.lower().str.strip() == movie].index
    if movie_index.empty:
        return []

    distances = similarity[movie_index[0]]
    top_5 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    for i in top_5:
        title = movies.iloc[i[0]].title
        recommended_titles.append(title)
    return recommended_titles

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended = []
    selected_movie = None
    error = None

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        print(f"Selected movie: '{selected_movie}'")  # For debugging

        if not selected_movie:
            error = "Please select a movie."
        else:
            recommended = recommend(selected_movie)
            if not recommended:
                error = f"No recommendations found for '{selected_movie}'."

    return render_template(
        'index.html',
        movies=movies['title'].values,
        recommended_movies=recommended,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)

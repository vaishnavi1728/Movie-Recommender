# 🎬 Movie Recommendation System  

This project is a **Content-Based Movie Recommendation System** built using the **TMDB 5000 dataset**.  
It recommends movies similar to a given input movie based on **metadata features** such as **overview, genres, keywords, cast, and crew**.  

---

## 📌 Features
- Uses **Content-Based Filtering** (no user ratings required).  
- Preprocessing of TMDB dataset:
  - Handles missing & duplicate data.  
  - Extracts useful features (`genres`, `keywords`, `cast`, `crew`, `overview`).  
  - Cleans and merges data into a single dataframe.  
- **NLP Techniques Used**:
  - Tokenization  
  - Stemming with **Porter Stemmer**  
  - Vectorization using **CountVectorizer** (Bag of Words)  
  - **Cosine Similarity** for measuring similarity between movies  
- Simple recommendation function that returns top 5 similar movies.  

---

## 📂 Dataset
We use **The Movies Dataset (TMDB 5000)** consisting of two files:
- `tmdb_5000_movies.csv` → Contains movie metadata (genres, keywords, overview).  
- `tmdb_5000_credits.csv` → Contains cast and crew information.  

These two files are merged using the `title` column.  

---

## ⚙️ Preprocessing Steps
1. **Selecting relevant features**: `['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']`  
2. **Handling missing/duplicate values**.  
3. **Parsing JSON-like strings** (genres, keywords, cast, crew).  
4. **Extracting top 3 actors** from cast & **director** from crew.  
5. **Text preprocessing**:
   - Removing spaces in multi-word tokens (`"Science Fiction" → "ScienceFiction"`).  
   - Converting lists into strings.  
   - Lowercasing and tokenizing.  
   - Applying **stemming** to normalize words.  
6. **Creating final "tags" feature** = overview + genres + keywords + cast + crew.  

---

## 🧠 NLP Methods Used
- **Tokenization** → Splitting movie descriptions into words.  
- **Stemming** → Converting words to root form (e.g., *running → run*).  
- **Vectorization** → Converting tags into numerical vectors using `CountVectorizer`.  
- **Cosine Similarity** → Measuring similarity between movies based on vectors.  

---

## 🚀 How It Works
1. Input a movie title.  
2. Find its feature vector from the dataset.  
3. Compute similarity with all other movies.  
4. Return the **Top 5 most similar movies**.  

Example:
```python
recommend("Batman Begins")

# Output:
# 1. The Dark Knight
# 2. The Dark Knight Rises
# 3. Man of Steel
# 4. Superman Returns
# 5. Spider-Man

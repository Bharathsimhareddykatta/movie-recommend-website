

# Movie Recommendation System

A **Movie Recommendation System** built using machine learning to suggest movies based on user preferences. The system utilizes collaborative filtering techniques to recommend movies similar to the one selected by the user. It fetches movie data, including posters, from The Movie Database (TMDb) API and displays movie recommendations dynamically.

## Features

- **Movie Selection**: Choose a movie from a dropdown or search for it by name.
- **Movie Recommendations**: Get top 5 movie recommendations based on a selected movie.
- **Poster Display**: Visual movie posters alongside recommendations.
- **Machine Learning Model**: Built using collaborative filtering techniques to provide relevant movie suggestions.

## Technologies Used

- **Python**: The main programming language.
- **Streamlit**: For building the web application interface.
- **Pandas**: For data handling and manipulation.
- **scikit-learn**: For implementing machine learning algorithms.
- **Requests**: To make HTTP requests to external APIs.
- **TMDb API**: For fetching movie details like posters and metadata.

## Installation

### Prerequisites

Make sure you have Python 3.6+ installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/Bharathsimhareddykatta/movie-recommend-website.git
cd movie-recommend-website
```

### Install Required Libraries

Install the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

You can create a `requirements.txt` file with the following content:

```
streamlit
pandas
requests
scikit-learn
```

### Set Up API Key

To fetch movie data from TMDb, you need to create an account on [TMDb](https://www.themoviedb.org/) and generate an API key.

Once you have the key, replace the `api_key` in the `fetch_poster()` function in the code.

```python
api_key = 'your_tmdb_api_key_here'
```

### Run the Application

To run the Streamlit app:

```bash
streamlit run app.py
```

The application should now be running locally on `http://localhost:8501`.

## Usage

1. **Select a Movie**: Choose a movie from the dropdown list.
2. **Get Recommendations**: Click the "Show Recommendation" button to get a list of 5 recommended movies.
3. **View Posters**: Movie posters are displayed alongside the recommendations.

## Example

![Movie Recommendations Example](assets/your_image.png)
![Screenshot 2024-12-13 003912](https://github.com/user-attachments/assets/b6732bfa-72da-4f54-bf9e-86b8a9b7ba2e)


## Contributing

Feel free to fork this repository and submit pull requests. Contributions are always welcome!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

## Acknowledgements

- [TMDb API](https://www.themoviedb.org/) for providing movie data.
- [Streamlit](https://streamlit.io/) for building the web interface.
- [Scikit-learn](https://scikit-learn.org/) for machine learning algorithms.

---

Feel free to update the **Usage**, **Installation**, and **Technologies Used** sections as per your specific implementation.

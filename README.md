# Movie Recommendation System

## Overview
This project implements a Movie Recommendation System using Python. The system leverages collaborative filtering and content-based filtering techniques to recommend movies based on user preferences and viewing history. The project processes a dataset of movies, including metadata like genres, production companies, and ratings, to generate relevant recommendations.

## Dataset
The dataset contains the following key features:
- **Budget**: Production budget of the movie.
- **Genres**: Genres associated with the movie.
- **Homepage**: Official movie homepage.
- **Keywords**: Keywords describing the movie content.
- **Original Title**: The original title of the movie.
- **Overview**: A brief summary of the movie.
- **Popularity**: Popularity score.
- **Production Companies**: Companies involved in producing the movie.
- **Revenue**: Box office revenue.
- **Runtime**: Duration of the movie in minutes.
- **Spoken Languages**: Languages spoken in the movie.
- **Title**: Movie title.
- **Vote Average**: Average user rating.
- **Vote Count**: Number of votes received.

The dataset is provided in CSV format and includes metadata useful for generating recommendations.

## Key Features
- **Content-Based Filtering**: Recommends movies similar to a user-specified movie based on attributes like genres and keywords.
- **Collaborative Filtering**: Recommends movies based on user preferences and similarity to other users.
- **Data Processing**: Cleans and preprocesses the dataset for accurate recommendation results.
- **Visualization**: Provides insights into the dataset using visualizations.

## Technologies Used
- **Python**: Core programming language for data processing and model implementation.
- **Pandas**: For data manipulation and analysis.
- **Scikit-Learn**: For machine learning models and similarity measures.
- **Folium**: For creating map visualizations.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Movie-Recommendation-System
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Load the dataset and preprocess it using the provided Jupyter Notebook (`Movie Recommendation System.ipynb`).
2. Use the implemented functions to:
   - Explore the dataset.
   - Generate movie recommendations.
   - Visualize relationships between movies.
3. Customize the parameters for recommendations as needed.

## Examples
- Find movies similar to "Avatar" based on genres and keywords.
- Generate a list of top-rated movies for a specific user.

## Future Enhancements
- Implementing a hybrid recommendation system combining collaborative and content-based filtering.
- Adding user authentication for personalized recommendations.
- Expanding the dataset with additional metadata for enhanced recommendations.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.

## Author
**Sahil Gawande**

## License
This project is licensed under the MIT License. See the LICENSE file for details.

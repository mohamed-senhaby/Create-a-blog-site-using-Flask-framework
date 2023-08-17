# Flask Blog Web Application

This is a simple web application built using Flask, a Python web framework. The application fetches blog data from an external API and displays it using HTML templates. Users can view all blog posts on the main page and access individual post content by clicking on the post titles.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (version 3.6 or higher)
- Flask (install using `pip install Flask`)
- Requests library (install using `pip install requests`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flask-blog-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-blog-app
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

   The application will start and will be accessible at `http://localhost:5000` in your web browser.

2. You can view all blog posts on the main page (`http://localhost:5000`) and click on individual post titles to view their content.

### Project Structure

- `app.py`: The main Flask application script that defines the routes and handles HTTP requests.
- `templates/`: This directory contains the HTML templates used for rendering the web pages.
  - `index.html`: Template for displaying all blog posts.
  - `post.html`: Template for displaying the content of an individual post.
- `post.py`: A module (not provided) that defines the `Post` class for representing blog posts.

### API Endpoint

The application fetches blog data from the following API endpoint:
- Blog API: `https://api.npoint.io/c790b4d5cab58020d391`

### Contributing

Contributions are welcome! If you find any issues or want to add features, feel free to submit a pull request.


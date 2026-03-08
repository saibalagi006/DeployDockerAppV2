# South Indian Food Menu App

A simple Flask-based web application that displays a menu of South Indian dishes along with their ingredients. The app is containerized with Docker and includes automated testing via GitHub Actions.

## Features

- **Menu Display**: Lists 7 popular South Indian dishes (e.g., Idli, Dosa, Sambar).
- **Ingredients**: Shows key ingredients for each dish.
- **Responsive Design**: Clean, mobile-friendly UI with earthy styling.
- **Docker Support**: Fully containerized for easy deployment.
- **Unit Tests**: Comprehensive tests for app functionality.
- **CI/CD**: Automated testing and building on GitHub Actions.

## Tech Stack

- **Backend**: Python 3.9, Flask 2.3.3
- **Frontend**: HTML, CSS, Jinja2 templates
- **Testing**: unittest, pytest
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## Installation and Setup

### Prerequisites
- Python 3.9+
- Docker (for containerized runs)
- Git

### Local Development

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd DeployDockerAppV2
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv sb_env
   # On Windows:
   sb_env\Scripts\activate
   # On macOS/Linux:
   source sb_env/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**:
   ```bash
   python main.py
   ```
   - Open `http://127.0.0.1:5000` in your browser.

### Docker

1. **Build the Image**:
   ```bash
   docker build -t south-indian-menu .
   ```

2. **Run the Container**:
   ```bash
   docker run -p 5000:5000 south-indian-menu
   ```
   - Open `http://localhost:5000` in your browser.

## Testing

### Run Unit Tests
```bash
python -m unittest tests/test_main.py
```

### Test with Docker
The GitHub Actions workflow automatically tests the Docker build and container functionality.

## Project Structure

```
DeployDockerAppV2/
├── main.py                 # Main Flask app
├── src/main.py             # Alternative entry point
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── tests/
│   └── test_main.py        # Unit tests
├── templates/
│   └── index.html          # Main page template
├── static/
│   └── styles.css          # CSS styling
├── .github/workflows/
│   └── ci-cd.yml           # GitHub Actions workflow
└── README.md               # This file
```

## CI/CD

The project uses GitHub Actions for automated testing:
- Triggers on pushes/PRs to `main` branch.
- Runs unit tests, builds Docker image, and tests the container.
- View results in the **Actions** tab of your GitHub repository.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and add tests.
4. Run tests: `python -m unittest tests/test_main.py`
5. Commit and push: `git push origin feature/your-feature`
6. Create a Pull Request.

## License

This project is open-source. Feel free to use and modify as needed.

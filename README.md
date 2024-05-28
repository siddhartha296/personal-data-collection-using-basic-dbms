# Personal Data Collection App Using Flask

This repository demonstrates the basics of creating a personal data collection web application using Flask, a micro web framework for Python. The application allows users to submit personal information through a web form, which is then stored in a basic database management system (DBMS).

## Installation

### Prerequisites

- Python: Ensure Python is installed on your computer. You can download it from [here](https://www.python.org/downloads/).

### Installing Flask

You can install Flask using pip, the Python package manager.

```bash
pip install Flask
```

### Cloning the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/personal-data-collection-using-basic-dbms.git
```
### File path
The file path should be as below 
```bash
myproject/
│
└── templates/
    │
    └── index.html
```
## Usage

1. Navigate to the repository directory:

```bash
cd personal-data-collection-using-basic-dbms
```

2. Run the Flask application:

```bash
python app.py
```

3. Open your web browser and go to `http://localhost:5000/` to access the application.

## Application Overview

- **Frontend**: The frontend of the application is built using HTML and CSS. The main HTML file, `index.html`, contains a form where users can submit their personal information.

- **Backend**: Flask is used as the backend framework to handle HTTP requests and responses. The `app.py` file contains the Flask application code, including routes for rendering the HTML templates and processing form submissions.

- **Database**: The application uses a basic database management system (DBMS) to store user data. By default, SQLite is used as the database engine, and the database file is named `data.db`. You can view the database file using SQLite tools or commands.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README to include more detailed instructions, additional sections, or any other information specific to your project. If you have any questions or need further assistance, let me know!

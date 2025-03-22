# Hackathon-2025
My team's hackathon project for 2025

## Overview

Scam Detective is a web-based application designed to help users identify potential scams by analyzing text messages, emails, and phone numbers for suspicious keywords and phrases. The application provides a likelihood score of whether the input is a scam and offers actionable advice to users.

## Software Requirements

- **Python**: Version 3.12 or higher
- **Django**: Version 5.1.7
- **SQLite**: Used as the database backend
- **Poetry**: For dependency management and packaging

## Dependencies

The project uses the following Python packages:
- `asgiref` (>=3.8.1,<4)
- `django` (5.1.7)
- `sqlparse` (>=0.3.1)
- `tzdata` (only required on Windows)

Dependencies are managed using Poetry. Refer to the `pyproject.toml` and `poetry.lock` files for more details.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd Hackathon-2025
    ```

2. Install Poetry if not already installed:
    ```bash
    pip install poetry
    ```

3. Install the project dependencies:
    ```bash
    poetry install
    ```

4. Activate the virtual environment:
    ```bash
    poetry shell
    ```

## Starting the Project

1. Navigate to the `ScamDetective` directory:
    ```bash
    cd ScamDetective
    ```

2. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

3. Start the development server:
    ```bash
    python manage.py runserver
    ```

4. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## Usage

1. **Main Menu**: Provides an overview of the application and its purpose. Also introduces the team behind the project.
2. **Scam Detector**: Navigate to the "Scam Detector" page to input text, phone numbers, or email addresses for analysis.
3. **Results**: After submitting the data, visit the "See Results" page to view the likelihood score and additional advice.

## Features

- Analyze messages for scam indicators using a database of keywords and phrases.
- Support for both email and phone number inputs.
- Provides actionable advice based on the analysis results.

## Contributing

- Scott Jeppson as Lead Developer and Chief Operations Officer
- Andrew Barber as Lead Designer and Chief Creative Officer
- Elijah Paul Castaneda as Chief Executive Officer

## License

This project is under a protective License. Any individual may copy and use the code here, but no modification or distribution is permitted. All rights reserved.

## Contact

For questions or feedback, please contact:
- **Scott Jeppson**: sfjepp46@gmail.com
- **Andrew Barber**: andrewnbarber03@gmail.com
- **Elijah Paul Castaneda**: elipaulcastaneda100@gmail.com
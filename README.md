# Smash Forecast App

## Overview

The Smash Forecast App is a web application that allows tennis enthusiasts to make predictions (picks) for matches in tennis tournaments, starting from the quarterfinals. The application features user authentication, submission and storage of picks, calculation of points, and display of a leaderboard.

## Features

- **User Authentication:** Registration, login, logout, and password recovery (optional).
- **Pick Selection:** Allows users to choose their predictions for each match.
- **Pick Submission and Storage:** Stores user picks in the database.
- **Point Calculation:** Calculates points based on user picks and actual game results.
- **Leaderboard Display:** Shows a ranking table with users and their respective points.

## Technologies Used

- **Backend:** Python with Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript

## Project Structure

### Backend

- Main Python file (`app.py`) for Flask server logic.
- Folders for SQLite database models and Flask routes.

### Frontend

- HTML, CSS, and JavaScript files for the user interface.

### Testing

- Directory for unit and integration tests.

## Development Steps

1. **Planning and Preparation:** Understanding requirements, defining user personas, and setting up the development environment.
2. **Design and Prototyping:** Creating wireframes, designing the interface, and revising based on feedback.
3. **Development:** Implementing backend and frontend functionalities.
4. **Testing:** Conducting unit, integration, and usability tests.
5. **Deployment and Launch:** Setting up the production environment and launching the app.
6. **Review and Iteration:** Collecting feedback and making necessary adjustments.
7. **Maintenance and Updates:** Providing ongoing support and developing new features.

## Security and Privacy

- Ensuring that passwords are never stored in plain text.
- Protection against common vulnerabilities, such as CSRF.

## Contributing

Contributions to the Smash Forecast App are welcome. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


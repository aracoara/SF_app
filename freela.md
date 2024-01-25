
# Smash Forecast App Project Specification

## Overview
The Smash Forecast App is a web application designed for tennis enthusiasts to make predictions for matches in tennis tournaments, starting from the quarterfinals. It includes user authentication, submission and storage of picks, calculation of points, and a leaderboard display.

## Scope
- **Minimalist Design:** Inspired by the provided screenshot for the main 'Picks' page.
- **Three Pages:** Mimicking the structure of the Google Spreadsheet, the app will have 'Picks' (draw), 'PicksOverview' (comparison table of choices and tournament results), and 'Leaderboard' (points ranking) pages.

## Technologies
- **Backend:** Python with Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Deployment Platform:** PythonAnywhere

## Features
- **User Authentication:** Registration, login, logout, password recovery (optional).
- **Pick Selection:** Users can choose their predictions for each match.
- **Pick Submission and Storage:** User picks are stored in the database.
- **Point Calculation:** Points are calculated based on user picks and actual game results.
- **Leaderboard Display:** A table showing rankings of users based on their points.

## MVP in Google Spreadsheet
- A proof of concept is available as a Google Spreadsheet.
- Includes simplified dashboards in 'Leaderboard' and 'PicksOverview' tabs.
- https://docs.google.com/spreadsheets/d/1YbUl1P2v-ni1ACiNaw5keyFKo4ZOYDjyjyOiOl7V_X8/edit?usp=sharing

## Security and Authentication Plan
- **Password Hashing:** Use bcrypt for secure password storage.
- **Protection Against Vulnerabilities:** Implement CSRF protection using Flask-WTF.
- **Session Management with Flask-Login:** Integrate Flask-Login for user session management.
- **Secure Forms with Flask-WTF:** Use Flask-WTF for registration and login forms with CSRF protection.
- **Authentication Routes:**
  - User Registration: Form with username, email, and password.
  - User Login: Login form with session initiation.
  - User Logout: Implement session termination.
- **Optional Password Recovery:** Implement a password reset system via email.

## Development Steps
1. **Planning and Preparation:** Define user personas, setup environment.
2. **Design and Prototyping:** Create wireframes, UI designs.
3. **Development:** Code backend and frontend functionalities.
4. **Testing:** Perform unit, integration, and usability tests.
5. **Deployment:** Setup production environment on PythonAnywhere.
6. **Review and Iteration:** Collect feedback, adjust as necessary.
7. **Maintenance and Updates:** Provide ongoing support and updates.

## Estimated Timeline and Cost
- **Timeline:** [Freelancer to provide an estimated timeline based on the scope]
- **Cost:** [Freelancer to propose a cost estimate for the entire project]

The freelancer is encouraged to propose their timeline and cost estimation for this project.

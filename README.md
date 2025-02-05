# Neighbour Help

Neighbour Help is a community-driven Django web application that allows users to either volunteer or request help by creating tasks. Users must sign up first before choosing their role.

## Features
- **User Authentication**: Sign up and log in functionality.
- **Role Selection**: Users can choose to volunteer or request help after signing up.
- **Task Management**: Users can create and manage help requests.
- **Volunteer Dashboard**: Volunteers can view and accept tasks.

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Django
- Virtualenv (optional but recommended)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/neighbour-help.git
   cd neighbour-help
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```
6. Open the app in your browser at `http://127.0.0.1:8000/`.

## Usage
1. **Sign Up**: Register an account.
2. **Choose a Role**: Select either `Volunteer` or `Request Help`.
3. **Create or View Tasks**:
   - If you need help, create a task describing your requirement.
   - If you're a volunteer, browse available tasks and accept those you can help with.


# Neighbour Help - Volunteer Tech Hackathon Project

![happy-volunteers-cleaning-city-park-from-garbage-isolated-flat-illustration](https://github.com/user-attachments/assets/ffee3238-601f-4c66-8cd6-27c59bd342c4)

Neighbour Help is a community-driven Django web application that allows users to either volunteer or request help by creating tasks. Users must sign up first before choosing their role.

## Features
- **User Authentication**: Sign up and log in functionality.
- **Role Selection**: Users can choose to volunteer or request help after signing up.
- **Task Management**: Users can create and manage help requests.
- **Volunteer Dashboard**: Volunteers can view and accept tasks.

## Demo
### Youtube
https://youtu.be/6zlata0-bS0

### Screenshots

![ss1](https://github.com/user-attachments/assets/441f1a5e-9b1b-4914-829c-d94826068392)

![ss2](https://github.com/user-attachments/assets/b0bf551f-f533-44e9-b838-5e865a3150b1)

![ss3](https://github.com/user-attachments/assets/c06e5eb2-ccd8-4c4a-a2ce-b816e8da1508)

![ss4](https://github.com/user-attachments/assets/16374215-7ea5-483f-9482-c09908be7418)

![ss5](https://github.com/user-attachments/assets/521d378c-1d1d-41b7-8df8-f564e670e30c)

![ss6](https://github.com/user-attachments/assets/50f8f6b7-fc0c-4f1b-86ac-318e4d06193e)

![ss7](https://github.com/user-attachments/assets/9e8279ba-a9d8-4638-9722-6e67c5e63b85)


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


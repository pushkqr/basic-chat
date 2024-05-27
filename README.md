# Basic Chat Application

This project is a simple, real-time chat application built using Python and Firebase. It supports user authentication, real-time messaging, and a graphical user interface (GUI) using Tkinter. Users can sign up, log in, and exchange messages with each other in a chat interface similar to popular messaging apps.

## Features

- **User Authentication**: Secure sign-up and log-in functionality using Firebase Authentication.
- **Real-time Messaging**: Send and receive messages in real time using Firebase Realtime Database.
- **Graphical User Interface**: Intuitive and user-friendly GUI built with Tkinter.
- **Multi-threading**: Handles sending and receiving messages simultaneously using Python threading.
- **Error Handling**: Provides feedback for invalid login credentials and handles sign-up errors gracefully.

## Getting Started

### Prerequisites

- Python 3.x
- Firebase account (for setting up the Realtime Database and Authentication)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/pushkqr/basic-chat-application.git
    cd basic-chat-application
    ```

2. **Install dependencies**:
    ```bash
    pip install pyrebase5
    ```

3. **Configure Firebase**:
    - Create a Firebase project in the [Firebase Console](https://console.firebase.google.com/).
    - Enable Email/Password authentication in the Authentication section.
    - Set up a Realtime Database and obtain your Firebase configuration details.

4. **Update Firebase Configuration**:
    - Replace the `firebaseConfig` dictionary in the code with your own Firebase configuration details.

### Running the Application

1. **Start the application**:
    ```bash
    python main.py
    ```

2. **Sign Up or Log In**:
    - Use the Sign-Up section to create a new account.
    - Use the Log-In section to sign in with your credentials.

3. **Chat**:
    - After logging in, chat windows will open where you can send and receive messages in real time.

## Project Structure

- `main.py`: Main script to start the application.
- `SendingApp.py`: Module for the sending message interface.
- `ReceivingApp.py`: Module for the receiving message interface.
- `requirements.txt`: List of required Python packages.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to [Pyrebase](https://github.com/thisbejim/Pyrebase) for the Firebase wrapper.

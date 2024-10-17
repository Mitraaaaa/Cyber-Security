### Web-Based Client-Server Login System Using Lamport Protocol

This project implements a web-based client-server login system, built using the Django framework, that uses the Lamport protocol for secure authentication. The system includes two primary functionalities: user signup and login. The security model is based on the Lamport scheme, where the number of logins a user can perform is determined by the `n_value`, which is set to 5 by default.

### Features

1. **Signup:**
   - Upon signup, the system generates a hashed password and stores it in the database. The password is hashed multiple times (equal to `n_value`), ensuring that the Lamport protocol is followed.
   - If the username is already registered, the user will be notified with an error message. Otherwise, the signup is successful, and a confirmation message is displayed.

2. **Login:**
   - During login, the password is hashed multiple times, and each successful login reduces the `n_value`. Once `n_value` reaches zero, the user is no longer allowed to log in.
   - If the login is successful, the system updates the hash and `n_value` in the database for future logins.
   - After five unsuccessful login attempts, the user is locked out, as the `n_value` will be exhausted.

### Usage

- To run the server, navigate to `http://localhost:8000/`, where you will see options to log in or sign up.
- During signup, the hashed password is stored five times (based on the default `n_value`) in the database.
- The system provides feedback messages for both successful and unsuccessful login attempts, maintaining security via hash changes after each login.

### Files

- `ciphertext.txt`: A dataset included to ensure that frequency analysis has enough data for accurate decryption results.


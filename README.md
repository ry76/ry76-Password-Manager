# ry76-Password-Manager

My Basic Password Manager Project in Python which stores and manages passwords securely.

For Example:

- Password Encryption: Passwords are encrypted using the cryptography library to protect them from unauthorized access.

- Password Retrieval: Encrypted passwords can be retrieved and decrypted back to plain text when needed, ensuring that only authorized users can access them.

- Secure Storage: The passwords are stored in a file (passwords.json), and the encryption key is saved separately in a secret.key file to enhance security.

- Key Management: The encryption key is generated and stored in a separate file to prevent it from being exposed in the same location as the stored passwords.

- Logging Alerts: All actions are logged, and any potential security issues can be logged in the alerts.log file for future review.
  
  
This code helps emphasize encryption and best security practices involved in Password Management.
_________________________________________________________________________________________________________________________________________________________________________
Example of Deployment: (with example code shown:)
1. When prompted, the user will input the following data to add or retrieve a password:

**Enter the action (add/retrieve): add  Enter the service name: Gmail  Enter the password: mySecurePassword123**

2. After the password is added, the user will see a confirmation that the password has been securely stored:

**Password for Gmail has been securely added.**

3. When user is retrieving the password:

**Enter the action (add/retrieve): retrieve
Enter the service name: Gmail
Your password for Gmail is: mySecurePassword123**

_________________________________________________________________________________________________________________________________________________________________________
Summarised Explanation:

- The passwords are encrypted using the cryptography.fernet method, ensuring secure storage. When retrieving the password, the encrypted data is decrypted into plain text.
- The encryption key is stored in a separate file (secret.key) to protect it from being exposed alongside the passwords.
- The user can add passwords to the storage. Each password is associated with a service name, and the encrypted password is stored in a JSON file.
- When retrieving a password, the user can specify the service name, and the corresponding encrypted password is decrypted for access.
- Any changes to the password storage (adding or retrieving passwords) are logged to ensure transparency. Alerts and actions are recorded for future review.
_________________________________________________________________________________________________________________________________________________________________________

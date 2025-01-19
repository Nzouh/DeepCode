# DeepCode
Application for parsing, enriching, and analyzing breach data. It extracts URLs, credentials, and tokens from raw files, enriches with metadata (e.g., domain resolution, HTTP status, platform detection), and enables advanced filtering to identify and categorize leaks for effective breach response.


### Importing the Database

1. Ensure MySQL is installed on your system.
2. Import the database using the following command:
   ```bash
   mysql -u root -p breached_data < breached_data.sql

   Make sure to be on the repository before writing this command.
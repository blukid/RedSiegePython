Project 4 - Pilfer for Passwords!

Scenario: While working with your teammates at Red Planet on an internal penetration test, you found lots of files spread across open SMB shares. Using another tool you have downloaded these files to your local machine. Now you need to find out if these files contain any sensitive data!

Beginner Task: Write a script that will search file names for files that could contain sensitive information. Names such as web.config, passwords.txt, SiteList.xml, etc.

Intermediate Task: Add functionality to the script that will enable it to search the contents of files for strings containing sensitive information like "password" "username", "apikey", etc.

Expert Task: Allow the user to specify the combinations of file names, types, and strings to search for. 

Bonus Task: Add recursive search.

For this task I would suggest creating several dummy files containing junk data and then a few with "sensitive" information. You don't need a pleothera of files to demonstrate if it works but I would suggest a few different common file types including txt, doc, docx, xls, xlsx, etc.

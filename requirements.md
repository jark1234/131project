## Functional Requirements
1. Users must be able to create an account using email and password.
2. Users must be able to create a new note.
3. Users must be able to edit an existing note.
4. Users must be able to delete notes.
5. Users must be able to restore deleted notes within 30 days.
6. User notes must be stored in a database with robust data encryption and access controls to safeguard data privacy and integrity.
7. Every note must include a timestamp to record the last edit.
8. Notes must be sorted in reverse chronological order.
9. Users should be able to customize the theme of the user interface (UI).
10. Users should have the option to adjust the default text size and font.
11. Users should have the ability to search for specific keywords inside the notes.
12. Users should be able to categorize their notes into different folders.
13. Users should have the ability to export their notes to PDF.
14. Users should have the option to secure individual notes with a password for added privacy.

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. The application should be in American English.
2. The application should be compatible with Google Chrome version 118.0.5993.129 or prior.





## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>

1. **Users must be able to create an account using email and password** <Novel Alam>
- **Summary:** This feature should allow a user to create a new account using an email address and a password. 
- **Actors:** User and Application
- **Pre-conditions:** User does not have an existing account with that particular email address.
- **Trigger:** User clicks "Create new account."
- **Primary Sequence:**
- 
- 
- 
- **Primary Postcondition:** The user can access the notes that match the search criteria.
- **Alternate Sequence:**
- 3. No matching notes are found.
- 4. The application displays a “no results” message.
2. **Users must be able to create a new note** <Novel Alam>

3. **Users must be able to edit existing note** <Novel Alam>
4. **Users must be able to delete notes** <Novel Alam>


11. **Search for Specific Keywords** <Jaclyn Turner>
- **Summary:** Users can search for specific keywords or titles within their notes for quick and efficient access to relevant information.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User initiates a search within the application by clicking the search bar.
- **Primary Sequence:**
- 1. User enters keywords in the search bar.
- 2. The application searches the database for notes containing the specified keywords.
- 3. The application displays a list of matching notes.
- **Primary Postcondition:** The user can access the notes that match the search criteria.
- **Alternate Sequence:**
- 3. No matching notes are found.
- 4. The application displays a “no results” message.

12. **Categorize Notes into Folders** <Jaclyn Turner>
- **Summary:** Users can organize their notes by categorizing them into different folders for better organization and easy retrieval.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User chooses to create a new folder or edit existing ones.
- **Primary Sequence:**
- 1. User navigates to the folder management section.
- 2. User creates a new folder or selects an existing one.
- 3. User assigns notes to the selected folder.
- 4. Notes are organized accordingly.
- **Primary Postcondition:** The user's notes are organized into folders for easy management.
- **Alternate Sequence:**
- 3. User cancels the folder creation or selection.
- 4. No changes are made.

13. **Export Notes to PDF** <Jaclyn Turner>
- **Summary:** Users can export their notes to a PDF file for offline access or sharing with others.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User chooses to export a note to PDF.
- **Primary Sequence:**
- 1. User selects a note to export.
- 2. User click “Export as a PDF”.
- 3. The application generates a PDF file containing the selected note's content.
- 4. User downloads or saves the PDF file.
- **Primary Postcondition:** The user has a downloadable PDF copy of the selected note.
- **Alternate Sequence:**
- 3. Application fails to generate PDF.
- 4. Application informs user with “Error” message.

14. **Secure Individual Notes with a Password** <Jaclyn Turner>
- **Summary:** Users can enhance the privacy of specific notes by securing them with a password.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User selects a note to secure with a password.
- **Primary Sequence:**
- 1. User selects a note to secure.
- 2. User clicks "Secure with Password".
- 3. The application prompts user for password and confirmation.
- 4. User enters and confirms a password for the note.
- 5. The application encrypts the note with the provided password.
- **Primary Postcondition:** The selected note is secured with a password, and only users with the correct password can access it.
- **Alternate Sequence:**
- 4. User unable to confirm password for the note.
- 5. Application informs user with “Passwords do not match” message.
- 6. Application prompts user to re-enter and confirm password for the note.

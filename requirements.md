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
- **Trigger:** User clicks "Create New Account."
- **Primary Sequence:**
- 1. User clicks on Create new account option
- 2. User enters their email address in the first field
- 3. User enters a password with at least one uppercase character and at least on special symbol in the second field
- 4. User re-enters same password in third field
- 5. User clicks "Create Account"
- **Alternate Sequence: User enters an email that is already in use**
- 1. User is prompted to sign in with existing email address
- **Postcondition:** 
- A new account is created with respective email address and password.
- OR
- User is prompted to sign in with existing email address and password. 

2. **Users must be able to create a new note** <Novel Alam>

3. **Users must be able to edit existing note** <Novel Alam>
4. **Users must be able to delete notes** <Novel Alam>

5. **Restore deleted notes within 30 days** <Iskandar Daoud>
- **Summary:** Users can restore deleted notes within a 30-day timeframe.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User selects a deleted note to restore.
- **Primary Sequence:**
i. User navigates to the "Trash" or "Deleted Notes" section.
ii. User selects a deleted note they want to restore.
iii. User clicks "Restore within 30 days."
iv. The application checks if the note was deleted within the last 30 days.
v. If the note was deleted within the last 30 days, the application restores the note to the user's notes list.
- **Primary Postcondition:** The deleted note is successfully restored to the user's notes list.
- **Alternate Sequence:**
iv. If the note was deleted more than 30 days ago, the application informs the user with a message stating that it cannot be restored.

6. **Notes stored in a database** <Iskandar Daoud>
- **Summary:** User notes are stored in a secure database with data encryption and access controls.
- **Actors:** Application and Data Storage System
- **Pre-conditions:** None
- **Trigger:** User creates or updates a note.
- **Primary Sequence:**
i. User creates a new note or updates an existing one.
ii. The application sends the note data to the database.
iii. The database encrypts the note data using robust encryption methods.
iv. The database stores the encrypted note data and enforces access controls to protect data privacy and integrity.
- **Primary Postcondition:** The note data is securely stored in the database with encryption and access controls to safeguard data privacy and integrity.
- **Alternate Sequence:**
iii. If encryption fails or access controls are breached, the application informs the user with an error message and does not store the note.

7. **Timestamp last edit** <Iskandar Daoud>
- **Summary:** Each note includes a timestamp to record the last edit.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User edits a note.
- **Primary Sequence:**
- 1. User selects a note to edit.
- 2. User makes changes to the note content.
- 3. The application automatically updates the timestamp for the note to reflect the current date and time.
- **Primary Postcondition:** The selected note now includes a timestamp recording the last edit date and time.
- **Alternate Sequence:**
- 2. The application fails to update the timestamp.
- 3. The note's timestamp remains unchanged.
- 4. The application informs the user with an error message.


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

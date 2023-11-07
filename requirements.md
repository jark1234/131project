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
11. Application should provide advanced search items with regular expressions or filters by categories
12. Users should be able to categorize their notes into different folders.
13. Users should have the ability to export their notes to PDF.
14. Users should have the option to secure individual notes with a password for added privacy.

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. The application should provide multiligual support.
2. The application should be compatible with Google Chrome version 118.0.5993.129 or prior.





## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>

1. **Create an account using email and password** <Novel Alam>
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

2. **Create a new note** <Novel Alam>
- **Summary:** This feature should allow a user to create a new note within the application.
- **Actors:** User and Application
- **Pre-conditions:** User is logged into their account.
- **Trigger:** User clicks "Create New Note."
- **Primary Sequence:**
  1. User clicks on "Create New Note" option.
  2. User is presented with a blank note-taking interface.
  3. User enters the title of the note in the designated field.
  4. User enters the content of the note in the main text area.
  5. User may apply formatting or categorization to the note 
  6. User clicks "Save" or "Create" to save the new note.
- **Alternate Sequence: User cancels note creation**
  1. At any point before saving, the user can click "Cancel" to exit the note creation process. No note is saved.
- **Postcondition:**
  - A new note is created and saved in the user's account with the provided title, content, and any additional options chosen.
  - OR
  - The user cancels the note creation, and no new note is saved.

3. **Edit existing note** <Novel Alam>
- **Summary:** This feature should allow a user to edit their existing notes within the application.
- **Actors:** User and Application
- **Pre-conditions:** User is logged into their account and has existing notes.
- **Trigger:** User selects the note they want to edit.
- **Primary Sequence:**
  1. User selects the note they want to edit from their list of existing notes.
  2. The selected note is displayed in an editing interface.
  3. User can make changes to the title and content of the note.
  4. User may apply formatting or categorization to the edited note.
  5. User clicks "Save" to save the changes made to the note.
- **Alternate Sequence: User cancels note editing**
  1. At any point during the editing process, the user can click "Cancel" to discard the changes and exit the editing interface.
- **Postcondition:**
  - The selected note is updated with the changes made by the user.
  - OR
  - The user cancels the note editing, and the note remains unchanged.

4. **Delete a note** <Novel Alam>
- **Summary:** This feature should allow a user to delete their notes within the application.
- **Actors:** User and Application
- **Pre-conditions:** User is logged into their account and has existing notes.
- **Trigger:** User selects the note they want to delete.
- **Primary Sequence:**
  1. User selects the note they want to delete from their list of existing notes.
  2. The selected note is displayed with a "Delete" option.
  3. User clicks the "Delete" option.
  4. The application prompts the user for confirmation to delete the note.
  5. User confirms the deletion.
- **Alternate Sequence: User cancels note deletion**
  1. If the user decides not to delete the note, they can cancel the deletion when prompted for confirmation.
- **Postcondition:**
  - The selected note is permanently deleted from the user's account.
  - OR
  - The user cancels the note deletion, and the note remains in their account.

5. **Restore deleted notes within 30 days** <Iskandar Daoud>
- **Summary:** Users can restore deleted notes within a 30-day timeframe.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User selects a deleted note to restore.
- **Primary Sequence:**
- 1. User navigates to the "Trash" or "Deleted Notes" section.
- 2. User selects a deleted note they want to restore.
- 3. User clicks "Restore within 30 days."
- 4. The application checks if the note was deleted within the last 30 days.
- 5. The note was deleted within the last 30 days, the application restores the note to the user's notes list.
- **Primary Postcondition:** The deleted note is successfully restored to the user's notes list.
- **Alternate Sequence:**
- 5. The note was deleted more than 30 days ago.
- 6. The application informs the user with a message stating that it cannot be restored.

6. **Notes stored in a database** <Iskandar Daoud>
- **Summary:** User notes are stored in a secure database with data encryption and access controls.
- **Actors:** Application and Data Storage System
- **Pre-conditions:** User is logged in.
- **Trigger:** User creates or updates a note.
- **Primary Sequence:**
- 1. User creates a new note or updates an existing one.
- 2. The application sends the note data to the database.
- 3. The database encrypts the note data using robust encryption methods.
- 4. The database stores the encrypted note data and enforces access controls to protect data privacy and integrity.
- **Primary Postcondition:** The note data is securely stored in the database with encryption and access controls to safeguard data privacy and integrity.
- **Alternate Sequence:**
- 3. The encryption fails or access controls are breached.
- 4. The application informs the user with an error message.
- 5. The application does not store the note.

7. **Timestamp last edit** <Iskandar Daoud>
- **Summary:** Each note includes a timestamp to record the last edit.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User edits a note.
- **Primary Sequence:**
-   1. User selects a note to edit.
-   2. User makes changes to the note content.
- 3. The application automatically updates the timestamp for the note to reflect the current date and time.
- **Primary Postcondition:** The selected note now includes a timestamp recording the last edit date and time.
- **Alternate Sequence:**
- 2. The application fails to update the timestamp.
- 3. The note's timestamp remains unchanged.
- 4. The application informs the user with an error message.
     
8. **Sort notes in reverse chronological order** <Natalie Kao>
- **Summary:** User’s notes are sorted in reverse chronological order, based on the last edit.
- **Actors:** User, Application, and Data Storage System
- **Pre-conditions**: User has opened the notes application and is viewing their list of notes.
- **Trigger**: None
- **Primary Sequence**:
- 1. Application requests lists of notes from Data Storage System.
- 2. Data storage system retrieves user’s notes.
- 3. Application sorts notes in reverse chronological order, based on timestamp of last edit, with most recently edited notes appearing at the top
- 4. Sorted list of notes is displayed to the user on the screen
- **Primary Postcondition:** User sees a list of all their notes sorted in reverse chronological order, with the most recently edited notes at the top, making it easy for them to access and view their latest changes
- **Alternative Sequence:**
- 2. There are no notes in the user’s account
- 5. Application informs user with an error messsage.
 
9. **Customize theme of the user interface (UI)** <Natalie Kao>
- **Summary:** Users should be able to cutomize the theme of the user interface (UI)
- **Actors:** User and Application
- **Pre-conditions:** User has an account and is logged in.
- **Trigger:** User goes to the “Theme Settings” under Settings option in application.
- **Primary Sequence:**
- 1. Application presents a list of available themes/customization options after user selects the “Theme Settings”
- 2. User selects preferred theme from available selection of colors, dark/light mode, or other UI elements
- 3. Application applies the selected theme or customization
- 4. User sees the web application with the newly applied theme/customization
- **Primary Postcondition:** The user has successfully customized the UI theme to their preference.
- **Alternative Sequence:**
- 2. Application doesn’t have customization options/no “Theme Settings” 
- 4. Customization does not change to the correct option or encounters errors
- 5. Application informs user with an error message.

10. **Adjust default text size and font.** <Natalie Kao>
- **Summary:** Users should have the option to adjust the default text size and font within the application
- **Actors:** User and Application
- **Pre-conditions:** The user has an account and is logged in and viewing the application
- **Trigger:** User accesses the Text Setting in the application under Settings
- **Primary Sequence:**
- 1. Application presents a menu or interface for adjusting the default text size and font.
- 2. Users select their preferred text size and font from available options.
- 3. Application applies chosen text settings to the UI.
- 4. The user sees text displayed with the new default text size and font.
- **Primary Postcondition:** The user has successfully adjusted the default text size and font, and the application displays the new text according to the user's preferences.
- **Alternative Sequence:**
- 3. Application does not offer text size and font customization.
- 5. No changes are made and displays a "no results" message. 
     
11. **Advanced Search with Regular Expressions and Category Filters** <Jaclyn Turner>
- **Summary:** Users can perform advanced searches on notes using regular expressions or apply category filters to quickly find specific notes within for quick and efficient access to relevant information.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User initiates an advanced search by clicking "Search".
- **Primary Sequence:**
- 1. User enter expression in the search bar.
- 2. The application searches the database for notes containing the specified expression.
- 3. If using category filters, user selects one or more categoryies for filtering.
- 3. The application displays a list of matching notes.
- **Primary Postcondition:** The user can access the notes that match the search criteria.
- **Alternate Sequence:**
- 4. No matching notes are found.
- 5. The application displays a “no results” message.

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

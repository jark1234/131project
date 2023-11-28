## Functional Requirements
1. Users must be able to create an account using email and password.
2. Users must be able to create a new note.
3. Users must be able to edit an existing note.
4. Users must be able to delete notes.
5. Users must be able to bold, italicize, and underline text.
6. Users must be able to save their notes.
7. Users must be able to select dark or light mode.
8. Users must be able to logout of their account.
9. Users must be able to update their profile name and picture.
10. Users must have the option to adjust the default text size and font.
11. Application should provide advanced search items with regular expressions or filters by categories.
12. Users should be able to categorize their notes into different folders.
13. Users should have the ability to export their notes to PDF.
14. Users should have the option to secure individual notes with a password.

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>
## Sketches
![](https://github.com/jark1234/131project/blob/main/images/ui1.jpg)

## Non-functional Requirements
1. The application should provide multiligual support.
2. The application should be compatible with Google Chrome version 118.0.5993.129 or prior.


## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>

1. **Create an account using email and password** [Novel Alam]
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

2. **Create a new note** [Novel Alam]
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

3. **Edit existing note** [Novel Alam]
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

4. **Delete a note** [Novel Alam]
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

5. **Format Text: Bold, Italicize, and Underline** [Iskandar Daoud]
- **Summary:** Users can apply formatting options (bold, italic, underline) to selected text in their notes.
- **Actors:** Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:**  User opens note
- **Primary Sequence:**
- 1. User highlights a portion of text in the note.
- 2. The application displays a formatting toolbar with options for bold, italic, and underline.
- 3. User clicks the "Bold" button on the toolbar.
- 4. User clicks the "Italic" button on the toolbar.
- 5. The application applies the italic style to the selected text.
- 6. User clicks the "Underline" button on the toolbar.
- 7. The application applies the underline style to the selected text.
- **Primary Postcondition:** The selected text is formatted with bold, italic, and underline styles as per the user's actions.
- **Alternate Sequence:** Formatting error
- 7. If the application encounters an issue applying any of the styles, it informs the user with an error message and reverts to the previous state.

6. **Save Notes** [Iskandar Daoud]
- **Summary:** Users can save changes made to their notes.
- **Actors:** Users and Application
- **Pre-conditions:** User is logged in and has one note in the database.
- **Trigger:** User makes edit to note.
- **Primary Sequence:**
- 1. User clicks the "Save" button.
- 2. The application validates the note data.
- 3. The application saves the changes to the note.
- 4. The database stores the encrypted note data and enforces access controls to protect data privacy and integrity.
- **Primary Postcondition:** The changes made to the note are successfully saved.
- **Alternate Sequence:** Saving error
- 3. If the application encounters an issue during the saving process, it informs the user with an error message, and the changes are not saved.

7. **Switch between Dark and Light Mode** [Iskandar Daoud]
- **Summary:** Users can toggle between dark and light modes for the application interface.
- **Actors:** Users and Application
- **Pre-conditions:** User is logged in.
- **Trigger:** User clicks on the settings menu.
- **Primary Sequence:**
- 1. User selects the "Mode" option.
- 2. Application prompts users for “Light” or “Dark” mode.
- 3. User selects the mode.
- 4. The application switches to selected mode.
- **Primary Postcondition:** The application interface is now in selected mode.
- **Alternate Sequence:** Mode switching error
- 4. If the application encounters an issue switching mode, it informs the user with an error message, and the mode remains unchanged.
     
8. **User logout** [Natalie Kao]
- **Summary:** This feature allows users to logout of their account.
- **Actors:** User
- **Pre-conditions**: User has an account and is logged in.
- **Trigger**: User clicks on the “Logout” button in the settings menu.
- **Primary Sequence**:
- 1. User goes to the account settings to start the process
- 2. User clicks on the “logout” button and confirms the logout of the application. 
- 3. The application returns to the login/home screen
- **Primary Postcondition:** User is successfully logged out of the application and redirected to the login page.
- **Alternative Sequence:**
- 2. User cancels logout option.
- 4. User remains logged in and stays on the current screen.
 
9. **Update profile name and picture** [Natalie Kao]
- **Summary:** Users should be able to change and update their profile name and picture.
- **Actors:** User 
- **Pre-conditions:** User has an account and is logged in. 
- **Trigger:** User goes to the “Profile” section under Settings option in application.
- **Primary Sequence:**
- 1. User navigates to the profile section under settings. 
- 2. User selects the “Edit Profile” button.
- 3. User is able to edit information and also change profile picture and save it using the “Save” option.
- 4. User is redirected to their profile page.
- **Primary Postcondition:** The user has successfully changed their profile picture and information and the updated profile information is shown on the screen.
- **Alternative Sequence:**
- 3. User uploads an image that is not in a supported format.
- 3. User enters an already existing profile username.
- 5. User is displayed an error message when trying to click “Save”.

10. **Adjust default text size and font.** [Natalie Kao]
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
     
11. **Advanced Search with Regular Expressions and Category Filters** [Jaclyn Turner]
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

12. **Categorize Notes into Folders** [Jaclyn Turner]
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

13. **Export Notes to PDF** [Jaclyn Turner]
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

14. **Secure Individual Notes with a Password** [Jaclyn Turner]
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

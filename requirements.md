## Functional Requirements

1. Users must be able to create an account using email and password.
2. Users must be able to create a new note.
3. Users must be able to edit an existing note.
4. Users must be able to delete notes.
5. Users must be able to bold, italicize, and underline text.
6. Users must be able to save their notes.
7. Users must be able to select dark or light mode.
8. Users must be able to log out of their accounts.
9. Users must be able to update their profile name and date of birth.
10. Users should be able to modify the font size and headings within the note.
11. Connect with an External API*.
12. Users must be able to turn timestamp visibility on and off.
13. Users must have the ability to permanently delete their account.
14. Users must have the ability to search note titles and contents with keywords.

## Sketches

![](https://github.com/jark1234/131project/blob/main/images/ui1.jpg)
![](https://github.com/jark1234/131project/blob/main/images/ui2.jpg)


## Non-functional Requirements

1. The application should provide multilingual support*.
2. The application should be compatible with Google Chrome version 118.0.5993.129 or prior.

## Use Cases

1. **Create an account using email and password** [Natalie Kao]
- **Summary:** This feature should allow a user to create a new account using an email address and a password.
- **Actors:** User and Application
- **Pre-conditions:** User does not have an existing account with that particular email address.
- **Trigger:** User clicks "Create New Account."
- **Primary Sequence:**
- 1. User enters their email address in the first field
- 2. User enters a password with at least one uppercase character and at least on special symbol in the second field
- 3. User re-enters same password in third field
- 4. User clicks "Create Account"
- **Alternate Sequence: User enters an email that is already in use**
- 1. User is prompted to sign in with existing email address
- **Postcondition:**
- A new account is created with respective email address and password.
- OR
- User is prompted to sign in with existing email address and password.

2. **Create a new note** [Natalie Kao]
- **Summary:** This feature should allow a user to create a new note within the application.
- **Actors:** User and Application
- **Pre-conditions:** User is logged into their account.
- **Trigger:** User clicks "Create New Note."
- **Primary Sequence:**
  1. User is presented with a blank note-taking interface.
  2. User enters the title of the note in the designated field.
  3. User enters the content of the note in the main text area.
  4. User may apply formatting or categorization to the note
  5. User clicks "Save" or "Create" to save the new note.
- **Alternate Sequence: User cancels note creation**
  1. At any point before saving, the user can click "Cancel" to exit the note-creation process. No note is saved.
- **Postcondition:**
  - A new note is created and saved in the user's account with the provided title, content, and any additional options chosen.
  - OR
  - The user cancels the note creation, and no new note is saved.

3. **Edit existing note** [Natalie Kao]
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

4. **Delete a note** [Natalie Kao]
- **Summary:** This feature should allow a user to delete their notes within the application.
- **Actors:** User and Application
- **Pre-conditions:** User is logged into their account and has existing notes.
- **Trigger:** user clicks the 'Delete' button adjacent to a note
- **Primary Sequence:**
  1. The application prompts the user for confirmation to delete the note.
  2. User confirms the deletion.
- **Alternate Sequence: User cancels note deletion**
  1. If the user decides not to delete the note, they can cancel the deletion when prompted for confirmation.
- **Postcondition:**
  - The selected note is permanently deleted from the user's account.
  - OR
  - The user cancels the note deletion, and the note remains in their account.

5. **Format Text: Bold, Italicize, and Underline** [Novel Alam]

- **Summary:** Users can apply formatting options (bold, italic, underline) to selected text in their notes.
- **Actors:** Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User opens note
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
- **Primary Postcondition:** 
- The selected text is formatted with bold, italic, and underline styles as per the user's actions.
- **Alternate Sequence:** Formatting error
- 7. If the application encounters an issue applying any of the styles, it informs the user with an error message and reverts to the previous state.

6. **Save Notes** [Novel Alam]

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
- 1. User selects the "Mode" option.
- 2. Application prompts users for “Light” or “Dark” mode.
- 3. User selects the mode.
- 4. The application switches to selected mode.
- **Primary Postcondition:** The application interface is now in selected mode.
- **Alternate Sequence:** Mode switching error
- 1. If the application encounters an issue switching mode, it informs the user with an error message, and the mode remains unchanged.

8. **User logout** [Natalie Kao]
- **Summary:** Users can securely log out of the application to protect their account and data.
- **Actors:** Registered Users and Application
- **Pre-conditions**: User has an account and is logged into the application.
- **Trigger**: User decides to log out of the application.
- **Primary Sequence**:
- 1. User navigates to the logout option within the application.
- 2. User clicks on the “logout” button.
- 3. User confirms the logout action.
- 4. The application invalidates the user's session, logging them out.
- 5. The application returns the user to the login screen
- **Primary Postcondition:** The user is successfully logged out, and their session is terminated.
- **Alternative Sequence:**
- 3. User cancels logout option.
- 4. User remains logged in and stays on the current screen.

9. **Update Profile Name and Date of Birth** [Natalie Kao]
- **Summary:** Users can modify and update their profile name and date of birth within the application for accurate and current user information.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User has an account and is logged into the application.
- **Trigger:** The user decides to update their profile name and birthday.
- **Primary Sequence:**
- 1. User navigates to the profile settings section.
- 2. User selects the option to edit profile name and date of birth.
- 3. User updates the profile name and date of birth with the desired changes.
- 4. User clicked "Save" to save the updated profile information.
- 5. The application saves the changes, updating the user's profile with the new name and/or date of birth.
- **Primary Postcondition:** The user's profile name is successfully updated with the new information.
- **Alternative Sequence:**
- 4. User aborts save.
- 5. Application doesn't update profile information.

10. **Modify Font Size and Headings within Notes.** [Novel Alam]
- **Summary:** Users have the ability to customize the font size and headings within their notes for a personalized and visually appealing experience.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User opens new or existing note for editing.
- **Primary Sequence:**
- 1. The note editor toolbar displays options for adjusting font size and headings.
- 2. User interacts with the toolbar and selects preferred font size or heading options from the toolbar.
- 3. User selects the desired text or position in the note.
- 4. User adjusts the font size from the toolbar.
- 5. User applies heading styles as needed.
- 6. The application updates the note in real-time to reflect the user's formatting choices.
- **Primary Postcondition:**
- The selected text within the note is modified with the user-defined font size and heading styles.
- **Alternative Sequence:**
- 6. Application fails to update to reflect user's formatting choices.
- 7. Modifications to formatting don't change.

11. **Connect with an External API** [Jaclyn Turner]
- **Summary:** The application can communicate and exchange data with an external API, enabling the retrieval or submission of information from/to external sources.
- **Actors:** Application and External API
- **Pre-conditions:** The application is running and the external API is accessible.
- **Trigger:** User initiates an action that requires interaction with the external API.
- **Primary Sequence:**
- 1. The application sends a request to the external API, specifying the required information or action.
- 2. The external API processes the request and returns the relevant data or confirmation.
- 3. The application receives and processes the data or confirmation from the external API.
- **Primary Postcondition:** The application successfully interacts with the external API, and the desired data or action is integrated into the application.
- **Alternate Sequence:**
- 2. The external API encounters an issue processing the request.
- 3. The application fails to receive the data.
- 4. The application displays the relevant error message to the user.

12. **Toggle Timestamp Visibility** [Novel]
- **Summary:** Users can control the visibility of timestamps on their notes by toggling the timestamp feature on and off.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User decides to change timestamp visibility.
- **Primary Sequence:**
- 1. User navigates to the homepage, where notes are displayed.
- 2. The user clicks "Hide Timestamps".
- 3. The application hides timestamps for all notes.
  4. The user clicks "Show Timestamps".
  5. The application reveals timestamps on all notes.
- **Primary Postcondition:** Timestamps on the homepage are either visible or hidden, based on the user's decision to toggle visibility.
- **Alternate Sequence:**
- 5. Application fails to load timestamps.
- 6. Application displays "Error - Try again." message.

13. **Delete Account** [Jaclyn Turner]
- **Summary:** Registered users can initiate the process of permanently deleting their account from the application.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in to application.
- **Trigger:** The user decides to delete their account.
- **Primary Sequence:**
- 1. User navigates to "Profile" settings section.
- 2. User clicks "Delete account".
- 3. Application prompts user for confirmation.
- 4. User clicks "Yes" to confirm account deletion.
- 5. The application permanently deletes the user account.
- **Primary Postcondition:** The user's account is successfully deleted from the application, and all associated data is permanently removed.
- **Alternate Sequence:**
- 4. User clicks "No" to confirm account deletion.
- 4. The application doesn't delete the user's account.

14. **Search Note Titles and Contents with Keywords** [Jaclyn Turner]
- **Summary:** Users can perform searches on notes using keywords to quickly find specific notes for quick and efficient access to relevant information.
- **Actors:** Registered Users and Application
- **Pre-conditions:** User is logged in and has at least one note in the database.
- **Trigger:** User initiates a search by clicking the search bar.
- **Primary Sequence:**
- 1. User enters keywords in the search bar.
  2. The user clicks "Search"
- 3. The application searches the database for notes containing the specified keywords.
- 4. The application displays a list of matching notes.
- **Primary Postcondition:** The user can access the notes that match the search criteria.
- **Alternate Sequence:**
- 4. No matching notes are found.
- 5. The application displays a “no results” message.

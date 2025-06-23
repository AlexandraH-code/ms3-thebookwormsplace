## 10. Testing
[Back To The Top](#table-of-contents)
### User Story Testing

| Feature | User Story | Expected Result | Pass |
|---------|------------|-----------------|------|
| Books page | **List added books:** As a Site Visitor, I can see added books compiled in a list (with a picture of the book and author name) so that I can easily see which books have been added. | A site visitor can see added books on the Books page.| &check; |
| Book detail page | **View information about a book:** As a Site Visitor, I can click on a book so that I can get more information about it. | A site visitor can view details about a specific book by clicking the View Details button on a book. | &check; |
| Book detail page | **View comments:** As a Site Visitor, when I view a specific book, I can see any comments that other visitors have made so that I can read any conversation. | A site visitor can see any comments that have been made on a book on the Book detail page. | &check; |
| Create Account page| **User account registration:** As a Site Visitor, I can register an account (on the website) so that I can have my own profile on it. | A site visitor can create a user account via the Create Account page. | &check; |
| Book detail page | **Comment on a book:** As a Site Visitor, I can leave a comment on a specific book so that I can give my opinion about it. | A logged-in site visitor can leave a comment on a book on the Book detail page. A logged-in site visitor can also reply to other people's comments. | &check; |
| Book detail page | **Rate a book:** As a Site Visitor, I can leave a rating for a book so that I can easily express my opinion about it. | A logged-in site visitor can rate a book via the Book detail page. | &check; |
| Book detail page | **Edit or delete a comment that has been made on a specific book:** As a Site Visitor, I can edit or delete a comment that I have made on a specific book so that I have the opportunity to change a comment if I want to or delete it if I don't want it to remain (on the book). | A logged in site visitor can change or delete their own comments via the Book detail page. | &check; |
| About page | **Contact site owner:** As a Site Visitor, I can contact the site owner so that I can get answers to any questions or provide feedback. | A site visitor can send a message to the page owner via the contact form on the About page. | &check; |
| About page | **Read about the site:** As a Site Visitor, I can click on an About link so that I can read more about the site. | A site visitor can read more information about the website on the About page. | &check; |
| My Profile page | **Update user details:** As a logged in Site Visitor, I can access a profile page so that I have the possibility to change my user details. | A logged in site visitor can change their username, email address and password via the My Profile page. | &check; |
| Admin page | **Manage content:** As Site Administrator, I can add, read, update, and delete books so that I can manage the site's content. | A logged in administrator can use the Admin page to see added books, add new books, update already added books and remove already added books. | &check; |
| Django administration | **Approve comments:** As a Site Administrator, I can approve or disapprove comments so that I can filter comments that, for example, contain offensive language. | Currently, the administrator needs to log in to Django administration to be able to approve comments made. The idea is that the administrator will be able to do this via the Admin page in the future. | &check; |
| Admin page | **Create draft:** As a Site Administrator, I can create drafts for a book so that I can finish it at a later time. | A logged in administrator can add a new book as a draft via the Admin page. The book can be saved at a later time so that it appears on the Books page. | &check; |
| Admin page | **Add and update the about text:** As a Site Administrator, I can create or update the about page content so that it is available on the site. | A logged in administrator can change the text on the About page via the Admin page. | &check; |

### Manual Testing - Site Visitors
#### Test - Navigation And Footer

**Navigation**

| Link | Action | Pass |
|------|--------|------|
| Logo (stack of books on the far left in the navbar) + The BookWorm's Place text | When you click on the logo or on the The BookWorm’s Place text, you will be taken to the home page. | &check; |
| Home | When you click Home, you will be taken to the Home page. | &check; |
| Books | When you click on Books, you will be taken to the Books page.| &check; |
| About | When you click About, you will be taken to the About page. | &check; |
| Create Account (link visible if the site visitor is not logged in to the website) | When you click Create Account, you will be taken to the Create Account page.| &check; |
| Login (link visible if the site visitor is not logged in to the website) | When you click Login, you will be taken to the Login page. | &check; |
| Logout (link visible if the site visitor is logged in to the website.) | When you click Logout, you will be taken to the Logout page. | &check; |
| My Profile (link visible if the site visitor is logged in to the website.) | When you click on My Profile, you will be taken to the My Profile page. | &check; |
| Admin (link visible when an administrator is logged in to the website.) | When you click Admin, you will be taken to the Admin page. | &check; |

When you click on the links in the navbar, you will be taken to the correct page on the website.

**Footer**
| Link | Action | Pass |
|------|--------|------|
| Icon for Facebook | When you click on the Facebook icon, the Facebook home page opens in a new window. | &check; |
| Icon for Instagram | When you click on the Instagram icon, the Instagram home page opens in a new window. | &check; |
| Icon for X| When you click on the X icon, X's home page opens in a new window. | &check; |
| Icon for Youtube | When you click on the YouTube icon, the YouTube home page opens in a new window. | &check; |

When you click on the social media icons in the footer, you will be taken to the correct company's website.

#### Test - Home Page

| Link | Action | Pass |
|------|--------|------|
| Browse Books button | When you click the Browse Books button, you will be taken to the Books page where added books are displayed. | &check; |

The button works as it should. The site visitor is taken to the correct page on the website.

#### Test - Create Account

| Test scenario | Result | Pass |
|------|--------|------|
| Trying to submit the form before all fields are filled in. | When you try to submit the form without all fields being filled in, “This field is required.” appears next to the field that has not been filled in. And the form is not saved. | &check; |
| Trying to submit the form without the email address format being correct. | If the format of the email address is incorrect, “Enter a valid email address.” will be displayed. The form cannot be submitted if the format of the email address is not correct. | &check; |
| Attempts to submit the form when all fields are filled in correctly. | If all fields are filled in correctly, the form is submitted and a “Your account has been created. Please log in” message is displayed. The page visitor is taken to the Login page. | &check; |

#### Test - Login

| Test scenario | Result | Pass |
|------|--------|------|
| Clicks the Login button without the username and/or password fields being filled in. | If you click Login without both the username and password fields being filled in, the text “This field is required.” will appear next to the field that is not filled in. The login process will not proceed. | &check; |
| Click the Login button when both fields are filled in. | If you click Login when both fields are filled in, you will be sent to the Home page and the message “You are now logged in as” + username will be displayed. | &check; |

#### Test - Logout 

| Test scenario | Result | Pass |
|------|--------|------|
| Click the Log Out button. | Sent to the Home page and the message “You have been logged out.” is displayed. | &check; |
| Click the Cancel button.| Sent to the Home page. The login process is completed. | &check; |

#### Test - View/Show Books

| Test scenario | Result | Pass |
|------|--------|------|
| The site visitor has clicked the Browse books button or Books in the navbar. | The site visitor will be taken to the Books page where uploaded books are displayed with book cover, title and author. | &check; |
| The site visitor wants to know more about a book and has clicked the View details button next to a book. | The site visitor will be taken to the Book detail page where more detailed information about the book is displayed. In addition to the book cover, title and author, a description of the book is also displayed. It is also possible to see any ratings and any comments that have been made. | &check; |

#### Test - Rate Book

| Test scenario | Result | Pass |
|------|--------|------|
| The site visitor wants to rate a book, but is not logged in.| To be able to rate a book, the site visitor needs to either create an account and then log in, or log in if they already have an account. | &check; |
| The site visitor clicks the Rate button without having marked any stars.| If the site visitor clicks the Rate button without any stars selected, the message “Please select a star rating before submitting.” will appear at the top of the page. | &check; |
| The site visitor has marked stars and clicks the Rate button.| If the site visitor has marked stars and then clicks the Rate button, the following will happen: The message “Your rating has been submitted.” appears at the top of the page. The Average Rating is updated with the latest rating. The site visitors rating has been saved in the star row. This means that the rating can be changed. | &check; |

#### Test - Comment Book

| Test scenario | Result | Pass |
|------|--------|------|
| The site visitor is on the book detail page for a book and wants to write a comment.| In order to write a comment on a book, the site visitor needs to either create an account and then log in, or log in if the site visitor already has an account on the website. | &check; |
| A logged-in site visitor is on the book detail page for a book and clicks Submit Comment without having filled in anything in the text box under Leave a Comment. | If a logged-in site visitor clicks the Submit Comment button without having typed anything in the text box under Leave a Comment, a “Please fill in this field.” message will be displayed. | &check; |
| If the logged in site visitor clicks the Cancel button. | If the logged-in site visitor clicks the Cancel button, the Book detail page is reloaded and the text box under Leave a Comment is cleared. | &check; |
| If the logged in site visitor has filled in the text box under Leave a Comment and then clicks the Submit Comment button. | If the logged-in site visitor has filled in the text box under Leave a Comment and then clicks the Submit button, a “Your comment is awaiting approval” message will appear at the top of the page. The comment is saved to the database and an administrator must log in to Django administration and approve the comment for it to be displayed. | &check; |
| If the logged in site visitor clicks the Reply button on a comment to write a response. | If the logged in site visitor clicks the Reply button on a comment, they can write a reply to the comment. To save/send the reply, the logged in site visitor needs to click the Submit Reply button. A “Your comment is awaiting approval” message will then appear at the top of the page. For the comment to appear on the page, an administrator needs to log in to Django administration and approve the comment. | &check; |

#### Test - Edit Comment

| Test scenario | Result | Pass |
|------|--------|------|
| A logged-in site visitor wants to change their own comment and has clicked the Edit button on the comment. | When a logged-in site visitor clicks on the Edit button next to their own comment, a new page (Edit Your Comment page) opens where the site visitor can edit their comment. | &check; |
| The logged-in site visitor has clicked the Cancel button on the Edit Your Comment page. | If the logged-in site visitor clicks the Cancel button on the Edit Your Comment page, the site visitor is sent back to the Book detail page. | &check; |
| The logged-in site visitor has changed their comment and clicked the Submit Changes button on the Edit Your Comment page. | If the logged-in site-visitor has edited their comment and clicked the Submit Changes button on the Edit Your Comment page, the comment is saved to the database. A “Your edited comment is awaiting approval” message appears at the top of the page. For the edited comment to appear on the Book detail page, an administrator needs to log in to Django administration and approve the comment. | &check; |

#### Test - Delete Comment

| Test scenario | Result | Pass |
|------|--------|------|
| A logged-in site visitor wants to delete their own comment and has clicked the Delete button on the comment. | When a logged-in site visitor clicks on the Delete button next to their own comment, a new page (Delete Comment page) opens where the site visitor can delete their comment. | &check; |
| The logged-in site visitor has clicked the Cancel button on the Delete Comment page. | If the logged-in site visitor clicks the Cancel button on the Delete Comment page, the site visitor is sent back to the Book detail page.| &check; |
| The logged-in site visitor clicks the Yes, delete button on the Delete Comment page. | If the logged-in site visitor clicks the Yes, delete button on the Delete Comment page, the comment will be deleted from the database. It will also be deleted from the Books page. And a “Comment deleted successfully” message will be displayed at the top of the page (the Books page). | &check; |

#### Test - Edit User Details

| Test scenario | Result | Pass |
|------|--------|------|
| A site visitor wants to change their user details. | To be able to change their user details, site visitors need to log in to the page and then click on My Profile in the navbar. | &check; |
| A logged-in site visitor wants to change their username and has clicked the Change Username button on the My Profile page. | When a logged in site visitor clicks the Change Username button on the My Profile page, they are sent to the Change Username page where they can change their username. To save the new username, the site visitor needs to click the Save button. The username is then updated in the database and the user can use the new username going forward.| &check; |
| A logged-in site visitor wants to change their email address and has clicked the Change Email button on the My Profile page. | When a logged in site visitor clicks the Change Email button on the My Profile page, the person is sent to the Change Email page where the email address can be changed. To save the new email address, the site visitor needs to click the Save button. The email address is then updated in the database. | &check; |
| A logged-in site visitor wants to change their password and has clicked the Change Password button on the My Profile page. | When a logged-in site visitor clicks the Change Password button on the My Profile page, the person is sent to the Change Password page where the password can be changed. The site visitor needs to remember the old password in order to change to a new one. The old password is not pre-filled. To save the new password, the site visitor needs to click the Save button. The password is then updated in the database and the user can use the new password in the future. | &check; |
| A logged-in site visitor is on one of the pages to change user information and clicks the Cancel button. | A logged-in site visitor is on one of the pages to change user information and clicks the Cancel button. | &check; |
| A logged-in site visitor is on one of the pages to change user information and for some reason has deleted information in text boxes and then clicks the Save button. | If the logged in site visitor has accidentally deleted information in a text field and then clicks the Save button, “Fill in this field” will appear next to text fields that are not filled in. | &check; |
| A logged-in site visitor is on one of the pages to change user information and has changed the desired information and then clicks the Save button. | If the logged in site visitor has changed the desired user information and clicks the Save button, a confirmation message will appear. “Username updated successfully” for username, “Email address updated successfully” for email address and “Your password was successfully changed” for password. Changed user information is also updated in the database. | &check; |

As for the “Edit User Details” function, it is very simple at the moment. There are some changes that can be made, for example regarding the “Change Password” page. There should be information there about what format a password should have, what characters are allowed and so on. Since the website is currently only used for educational purposes, I still choose to keep the “Edit User Details” function. But I am aware that it has some shortcomings at the moment.

### Manual Testing - Administrator(s)

To access the admin section of the website, the administrator needs to log in to the website. To access the Admin Dashboard, the administrator then clicks on Admin in the nav bar.

#### Test - Add Book

| Test scenario | Result | Pass |
|------|--------|------|
| A logged in administrator wants to add a new book. | To add a new book, the logged in administrator first needs to click Admin in the navbar. Then the administrator clicks the Add Book button to get to the Add Book page. In order for the form to be saved, all fields except the slug need to be filled in (the slug is automatically generated after the title of the book). If the book is to be saved as a draft, there should be a check mark in the box next to Save as draft. If the book is to be posted on the page directly, the box next to Save as draft should be empty. To save the book, the administrator clicks the Save Book button. When a new book is added, a “Book added successfully” message is displayed at the top of the page (The Admin Dashboard page). And the new book is added to the book list found on the Admin Dashboard and is displayed on the Books page if the book has not been saved as a draft. If the administrator clicks the Cancel button, they are returned to the Admin Dashboard. | &check; |

#### Test - Edit Book

| Test scenario | Result | Pass |
|------|--------|------|
| A logged in administrator wants to change information on an already posted book. | To change information on an already posted book, the logged-in administrator clicks the Edit button next to the book that is to be changed. The administrator then changes the information that is to be changed. If the book is to be removed from being posted on the Books page, the box next to Save as draft should be checked. If the book is to continue to be displayed on the Books page, the box next to Save as draft should be left empty. To save the book, the administrator then clicks the Save Book button. When a book has been changed, a “Book updated successfully” message appears at the top of the page. If the administrator clicks the Cancel button, he or she is sent back to the Admin Dashboard.| &check; |

#### Test - Delete Book

| Test scenario | Result | Pass |
|------|--------|------|
| A logged in administrator wants to delete an added book. | To delete an added book, the logged in administrator needs to click Delete next to the book to be deleted. The administrator will be sent to a new page. To delete the book, the administrator clicks the Yes, delete button. The book will then be deleted from the database and thus disappear from both the Books page and the book list on the Admin Dashboard. To confirm that the book has been deleted, a “Book deleted successfully” message is displayed. If the administrator clicks the Cancel button on the “delete book” page, he will be sent back to the Admin Dashboard. | &check; |

#### Test - Update Text On The About Page

| Test scenario | Result | Pass |
|------|--------|------|
| A logged in administrator wants to change the text on the About page. | To change the text on the About page, the administrator needs to click the Edit About button on the Admin Dashboard. Any changes are made in the text box. To save the changes, the administrator then clicks the Save Changes button. The text on the About page will be changed. An “About page updated successfully” message will also appear at the top of the page (Admin Dashboard to which the administrator is sent back). If the administrator clicks the Cancel button, they will be sent back to the Admin Dashboard. | &check; |

#### Test - Approve Comment - Django administration

To approve comments, the administrator needs to log in to Django administration. There, approving comments works without any problems.

#### Test - Delete Comment - Django administration

To delete any comments, the administrator needs to log in to Django administration. There, deleting comments works without any problems.

#### Test - See Contact Requests - Django administration

To view contact requests, the administrator needs to log in to Django administration. There it is easy to view submitted contact requests.

#### Test - See Ratings - Django administration

To see ratings made, the administrator needs to log in to Django administration. There it is easy to see ratings made.

### Automated Testing

A total of 15 unit tests were written using Django’s TestCase class to verify the functionality of views and forms. These tests cover the most essential parts of the application, including:

* Loading the book list and book detail pages
* Ensuring only authenticated users can post comments
* Verifying comment and rating form validation
* Testing user registration and login views
* Checking password change functionality for logged-in users
* Ensuring superusers can access and use the book creation admin view

The tests are split into two files:
* test_forms.py – tests validation logic for CommentForm, StarRatingForm, and CustomUserCreationForm
* test_views.py – tests responses, redirects, and access control for core views

All tests can be run using: **python manage.py test**
# The BookWorm's Place

Developer - Alexandra Holstensson

[Link to the project - Heroku](https://the-bookworms-place-489ab98365bd.herokuapp.com/)

![Image Of The Site - Am I Responsive]()

## [Table of Contents](#table-of-contents)
1. [**About**](#1-about)
2. [**User Goals**](#2-user-goals)
    - [**External User Goals**](#external-user-goals)
    - [**Site Owner Goals**](#site-owner-goals)
3. [**User Stories**](#3-user-stories)
    - [**User Stories - Site Visitors**](#user-stories---site-visitors)
    - [**User Stories - Administrator(s)**](#user-stories---administrators)
4. [**Database Models Overview And Entity Relationship Diagram (ERD)**](#4-database-models-overview-and-entity-relationship-diagram-erd)
    - [**Database Models Overview**](#database-models-overview)
    - [**Entity Relationship Diagram (ERD)**](#entity-relationship-diagram-erd)
5. [**Agile Methodology**](#5-agile-methodology)
    - [**Kanban Workflow**](#kanban-workflow)
6. [**Design Of The Website**](#6-design-of-the-website)
    - [**Structure**](#structure)
    - [**Wireframes**](#wireframes)
        - [**Mobile Wireframes**](#mobile-wireframes)
        - [**Tablet Wireframes**](#tablet-wireframes)
        - [**Laptop/Desktop Wireframes**](#laptopdesktop-wireframes)
    - [**Colors**](#colors)
    - [**Fonts**](#fonts)
    - [**Icons And Images**](#icons-and-images)
7. [**Existing Features**](#7-existing-features)
    - [**Existing Features - Site Visitors**](#existing-features---site-visitors)
        - [**Navigation And Footer**](#navigation-and-footer)
        - [**Home Page**](#home-page)
        - [**Create Account**](#create-account)
        - [**Login**](#login)
        - [**Logout**](#logout)
        - [**Rate Book**](#rate-book)
        - [**Comment Book**](#comment-book)
        - [**Edit Comment**](#edit-comment)
        - [**Delete Comment**](#delete-comment)
        - [**Edit User Details**](#edit-user-details)
    - [**Existing Features - Administrator(s)**](#existing-features---administrators)
        - [**Add Book**](#add-book)
        - [**Edit Book**](#edit-book)
        - [**Delete Book**](#delete-book)
        - [**Approve Comment**](#approve-comment)
        - [**Delete Comment**](#delete-comment-1)
        - [**Update Text On The About Page**](#update-text-on-the-about-page)
        - [**See Contact Requests**](#see-contact-requests)
        - [**See Ratings**](#see-ratings)
8. [**Features Left To Implement**](#8-features-left-to-implement)
    - [**Features Left To Implement - Site Visitors**](#features-left-to-implement---site-visitors)
    - [**Features Left To Implement - Administrator(s)**](#features-left-to-implement---administrators)
9. [**Technologies Used**](#9-technologies-used)
  - [**Languages**](#languages)
  - [**Programs And Other Resources**](#programs-and-other-resoures)
10. [**Testing**](#10-testing)
  - [**User Story Testing**](#user-story-testing)
  - [**Manual Testing - Site Visitors**](#manual-testing---site-visitors)
    - [**Test - Navigation And Footer**](#test---navigation-and-footer)
    - [**Test - Home Page**](#test---home-page)
    - [**Test - Create Account**](#test---create-account)
    - [**Test - Login**](#test---login)
    - [**Test - Logout**](#test---logout)
    - [**Test - Rate Book**](#test---rate-book)
    - [**Test - Comment Book**](#test---comment-book)
    - [**Test - Edit Comment**](#test---edit-comment)
    - [**Test - Delete Comment**](#test---delete-comment)
    - [**Test - Edit User Details**](#test---edit-user-details)
  - [**Manual Testing - Administrator(s)**](#manual-testing---administrators)
    - [**Test - Add Book**](#test---add-book)
    - [**Test - Edit Book**](#test---edit-book)
    - [**Test - Delete Book**](#test---delete-book)
    - [**Test - Approve Comment**](#test---approve-comment)
    - [**Test - Delete Comment**](#test---delete-comment-1)
    - [**Test - Update Text On The About Page**](#test---update-text-on-the-about-page)
    - [**Test - See Contact Request**](#test---see-contact-requests)
    - [**Test - See Ratings**](#test---see-contact-requests)
11. [**Bugs**](#11-bugs)
12. [**Validation**](#12-validation)
  - [**HTML**](#html)
  - [**CSS**](#css)
  - [**JavaScript**](#javascript)
  - [**Python**](#python)
13. [**Lighthouse Testing**](#13-lighthouse-testing)
  - [**Desktop**](#desktop)
  - [**Mobile**](#mobile)
14. [**Device Testing**](#14-device-testing)
15. [**Browser Compatibility**](#15-browser-compatibility)
16. [**Deployment**](#16-deployment)
  - [**Local Deployment**](#local-deployment)
  - [**Remote Deployment**](#remote-deployment)
17. [**Credits**](#17-credits)

## 1. About
[Back To The Top](#table-of-contents)
The BookWorm's Place is made as part (Milestone Project 3) of the Level 5 Diploma in Web Application Development course at Code Institute.

The BookWorm's Place is a community-focused book blog where users can browse books, read details, register and log in to share comments, and rate their favorite reads. Users can also login to change their user details. Admins can manage content and moderate user-generated input to ensure a clean and respectful environment. There is a section on the website where admin(s) can add, edit, and delete books as well as change the text on the About page.

## 2. User Goals
[Back To The Top](#table-of-contents)
### Site Owner Goals
- Showcase an interactive book library
- Allow user engagement through ratings and comments
- Provide a visually engaging and responsive design

### External User Goals
- Browse available books
- Read detailed book information
- Register for an account
- Log in securely
- Edit saved user details
- Comment on books
- Edit and delete comments made
- Rate books using a star rating system
- Contact the site owner

## 3. User Stories
[Back To The Top](#table-of-contents)

### User Stories - Site Visitors
- **List added books:**
  - As a Site Visitor, I can see added books compiled in a list (with a picture of the book and author name) so that I can easily see which books have been added.
- **View information about a book:**
  - As a Site Visitor, I can click on a book so that I can get more information about it.
- **View comments:**
  - As a Site Visitor, when I view a specific book, I can see any comments that other visitors have made so that I can read any conversation.
- **User account registration:**
  - As a Site Visitor, I can register an account (on the website) so that I can have my own profile on it.
- **Comment on a book:**
  - As a Site Visitor, I can leave a comment on a specific book so that I can give my opinion about it.
- **Rate a book:**
  - As a Site Visitor, I can leave a rating for a book so that I can easily express my opinion about it.
- **Edit or delete a comment that has been made on a specific book:**
  - As a Site Visitor, I can edit or delete a comment that I have made on a specific book so that I have the opportunity to change a comment if I want to or delete it if I don't want it to remain (on the book).
- **Contact site owner:**
  - As a Site Visitor, I can contact the site owner so that I can get answers to any questions or provide feedback.
- **Read about the site:** 
  - As a Site Visitor, I can click on an About link so that I can read more about the site.
- **Update user details:** 
  - As a logged in Site Visitor, I can access a profile page so that I have the possibility to change my user details.

### User Stories - Administrator(s)
- **Manage content:**
  - As Site Administrator, I can add, read, update, and delete books so that I can manage the site's content.
- **Approve comments:**
  - As a Site Administrator, I can approve or disapprove comments so that I can filter comments that, for example, contain offensive language.
- **Create draft:**
  - As a Site Administrator, I can create drafts for a book so that I can finish it at a later time.
- **Add and update the about text:** 
  - As a Site Administrator, I can create or update the about page content so that it is available on the site.

## 4. Database Models Overview And Entity Relationship Diagram (ERD)
[Back To The Top](#table-of-contents)
### Database Models Overview

- **User Model (Django built-in)** - (Right now I only use the username, email and password fields.)
  - Handles authentication and user information.
  - Fields (standard):
    - username (CharField): Unique username for login
    - email (EmailField): User’s email address
    - password (CharField): Hashed password
    - first_name, last_name (CharField): Optional names
    - is_staff, is_superuser, is_active (BooleanField): Admin and access control flags
    - date_joined (DateTimeField): When the user registered
  - Relationships:
    - One-to-many with BlogPost (a user can create many books if extended)
    - One-to-many with Comment (user can write multiple comments)
    - One-to-many with StarRating (user can submit multiple ratings)

- **BlogPost Model**
  - Represents a book entry posted on the site.
  - Fields:
    - title (CharField): Book title (max 200 characters)
    - slug (SlugField): Auto-generated unique URL slug
    - author (CharField): Book author (not linked to User)
    - cover_image (CloudinaryField): Book cover image hosted on Cloudinary
    - cover_image_alt (CharField): Alt text for accessibility
    - description (TextField): Full description of the book
    - excerpt (TextField): Optional short excerpt
    - is_draft (BooleanField): Whether the book is published
    - created_at (DateTimeField): Timestamp when created
    - updated_on (DateTimeField): Last updated
  - Relationships:
    - One-to-many with Comment
    - One-to-many with StarRating

- **Comment Model**
  - Stores comments and replies related to a specific book.
  - Fields:
    - user (ForeignKey → User): The user who wrote the comment
    - book (ForeignKey → BlogPost): The book the comment belongs to
    - text (TextField): The comment content
    - parent (ForeignKey → Comment): Optional, links to another comment (for replies)
    - approved (BooleanField): Whether the comment is admin-approved
    - created_at (DateTimeField): Timestamp when created
  - Relationships:
    - ManyToOne with User
    - ManyToOne with BlogPost
    - Self-referencing: A comment can have many replies (child comments)

- **StarRating Model**
  - Represents a 1–5 star rating given by a user to a book.
  - Fields:
    - user (ForeignKey → User): The user giving the rating
    - book (ForeignKey → BlogPost): The book being rated
    - value (IntegerField): Rating value from 1 to 5
    - created_at (DateTimeField): Timestamp when created
  - Relationships:
    - Unique combination of user and book (a user can rate each book only once)

- **About Model**
  - Stores the content of the “About” page.
  - Fields:
    - content (TextField): Rich text content describing the purpose of the site

- **ContactRequest Model**
  - Stores user-submitted messages via the contact form.
  - Fields:
    - name (CharField): Name of the person contacting
    - email (EmailField): Email address
    - message (TextField): The submitted message
    - created_at (DateTimeField): Timestamp when message was received

### Entity Relationship Diagram (ERD)

I used [drawDB](https://www.drawdb.app/) to create an Entity Relationship Diagram (ERD). The relationships between the tables are drawn. The About and ContactRequest tables are completely independent (they have no connection to any other table). A picture of the ERD is below.

![Image of Entity Relationship Diagram (ERD)](docs\images\ERD\TheBookWorm'sPlace_ERD_2025-06-20_small.png)

The image of the ERD can be found here: docs\images\ERD\TheBookWorm'sPlace_ERD_2025-06-20_small.png

## 5. Agile Methodology
### Kanban Workflow

I have used a Kanban board to structure the work on the website. In the Kanban board, I have chosen to divide all tasks (issues) into three different stages:

- To Do: Tasks that I have planned to do.
- In Progress: Tasks that are in progress, that I am working on.
- Done: Tasks that are complete and working as they should.

Link to the project [Kanban Board](https://github.com/users/AlexandraH-code/projects/12/views/1) 

## 6. Design Of The Website
[Back To The Top](#table-of-contents)
### Structure

The website is structured with a header (navigation bar), main content area, and footer with social media links.

I have chosen to structure my website with the following pages:
- **Home page**
  - page with a large hero image (representing books) and a button with the text Browse Books (which, if clicked, takes the user to the Books page).
- **Books**
  - page where the user can see added books. The books are displayed with book cover, title and author. Below the information about the book there is a button that says View Details (if the user clicks the button, they are taken to a page that shows more information about the book).
- **About**
  - page with information about the page. This page also has a contact form where the user can send a message to the site owner.
- **Book details**
  - page with page with book details. Here you can also read comments that other visitors have made and see the rating of the book (this in the form of five stars marked according to how the book has been rated). If the user is logged in, it is possible to rate the book and also write their own comment. It is also possible to reply to comments made by other users.
- **Create Account** 
  - page where the visitor can register an account on the website. With a user account on the website, the user can rate and comment on added books.
- **Login**
  - page where the user can log in.
- **Logout**
  - page where the user can log out.
- **My profile**
  - page where the user can change username, email address and password.
- **Admin**
  - page where the site administrator(s) can
    - add books
    - update the details of an added book
    - delete an added book
    - change the text on the About page

The pages above can be accessed by clicking on one of the links in the menu bar at the top of the page. On small screens (smaller than 992 pixels) the menu is collapsed in the upper right corner. 

At the bottom of the page there is a footer. In the footer there are links to social media (Facebook, Instagram, X and Youtube).

### Wireframes
I have used [Balsamiq](https://balsamiq.com/) to make the wireframes. The wireframes show how I envisioned the website to look and be constructed. The finished result may differ somewhat from the wireframes.

#### Mobile Wireframes

  <details>
  <summary>Home Page - Not Logged In</summary>

  ![Home Page - Not Logged In](docs\wireframes\mobile\home_not_logged_in.png)
  
  </details>

  <details>
  <summary>Home Page - Logged In</summary>

  ![Home Page - Logged In](docs\wireframes\mobile\home_logged_in.png)
  
  </details>

  <details>
  <summary>Books - Not Logged In</summary>

  ![Books - Not Logged In](docs\wireframes\mobile\books.png)
  
  </details>

  <details>
  <summary>Book Details - Not logged In</summary>

  ![Book Details - Not logged In](docs\wireframes\mobile\book_details_not_logged_in.png)
  
  </details>

  <details>
  <summary>Book Details - Logged In</summary>

  ![Book Details - Logged In](docs\wireframes\mobile\book_details_logged_in.png)
  
  </details>

  <details>
  <summary>About - Not Logged In</summary>

  ![About](docs\wireframes\mobile\about_not_logged_in.png)
  
  </details>

  <details>
  <summary>Create Account</summary>

  ![Create Account](docs\wireframes\mobile\register_account.png)
  
  </details>

  <details>
  <summary>Login</summary>

  ![Login](docs\wireframes\mobile\login.png)
  
  </details>

  <details>
  <summary>Logout</summary>

  ![Logout](docs\wireframes\mobile\logout.png )
  
  </details>


#### Tablet Wireframes

  <details>
  <summary>Home Page - Not Logged In</summary>

  ![Home Page - Not Logged In](docs\wireframes\tablet\home_not_logged_in.png)
  
  </details>

  <details>
  <summary>Home Page - Logged In</summary>

  ![Home Page - Logged In](docs\wireframes\tablet\home_logged_in.png)
  
  </details>

  <details>
  <summary>Books - Not Logged In</summary>

  ![Books - Not Logged In](docs\wireframes\tablet\books.png)
  
  </details>

  <details>
  <summary>Book Details - Not logged In</summary>

  ![Book Details - Not logged In](docs\wireframes\tablet\book_details_not_logged_in.png)
  
  </details>

  <details>
  <summary>Book Details - Logged In</summary>

  ![Book Details - Logged In](docs\wireframes\tablet\book_details_logged_in.png)
  
  </details>

  <details>
  <summary>About - Not Logged In</summary>

  ![About](docs\wireframes\tablet\about_not_logged_in.png)
  
  </details>

  <details>
  <summary>Create Account</summary>

  ![Create Account](docs\wireframes\tablet\register_account.png)
  
  </details>

  <details>
  <summary>Login</summary>

  ![Login](docs\wireframes\tablet\login.png)
  
  </details>

  <details>
  <summary>Logout</summary>

  ![Logout](docs\wireframes\tablet\logout.png)
  
  </details>

#### Laptop/Desktop Wireframes

  <details>
  <summary>Home Page - Not Logged In</summary>

  ![Home Page - Not Logged In](docs\wireframes\laptop_desktop\home_not_logged_in.png)
  
  </details>

  <details>
  <summary>Home Page - Logged In</summary>

  ![Home Page - Logged In](docs\wireframes\laptop_desktop\home_logged_in.png)
  
  </details>

  <details>
  <summary>Books - Not Logged In</summary>

  ![Books - Not Logged In](docs\wireframes\laptop_desktop\books.png)
  
  </details>

  <details>
  <summary>Book Details - Not logged In</summary>

  ![Book Details - Not logged In](docs\wireframes\laptop_desktop\book_details_not_logged_in.png)
  
  </details>

  <details>
  <summary>Book Details - Logged In</summary>

  ![Book Details - Logged In](docs\wireframes\laptop_desktop\book_details_logged_in.png)
  
  </details>

  <details>
  <summary>About</summary>

  ![About](docs\wireframes\laptop_desktop\about_not_logged_in.png)
  
  </details>

  <details>
  <summary>Create Account</summary>

  ![Create Account](docs\wireframes\laptop_desktop\register_account.png)
  
  </details>

  <details>
  <summary>Login</summary>

  ![Login](docs\wireframes\laptop_desktop\login.png)
  
  </details>

  <details>
  <summary>Logout</summary>

  ![Logout](docs\wireframes\laptop_desktop\logout.png)
  
  </details>

### Colors

A clean, warm palette is used for readability and comfort, suitable for a reading-focused audience.

I have chosen to use a color palette with shades of white, grey, black and brown. I think the color theme is appropriate for a website about books.

To ensure that text is easy to read in relation to the background color, I have used [ColorMagic's ContastChecker](https://colormagic.app/contrast-checker). Below are results from ColorMagic's ContastChecker on the most frequently used elements.

**ContrastCheck:**
- **Navbar and Footer:** (dark color on the background, light color on the text)
  - background-color: #3e2f2f - dark brown
  - color: #ffffff - white
    - Contrast Ratio: 21.00
    - Normal Text: AAA
    - Large Text: AAA
    - UI Components: AA

![Image of constrast check for the navbar and footer element.](docs\images\color_contrast_check\navbar_small.png)


- **Navbar and Footer hover:** (dark color on the background, light brown text color when hovering over the text)
  - background-color: #3e2f2f - dark brown
  - color: #a1866f - light, reddish-brown
    - Contrast Ratio: 6.07
    - Normal Text: AA
    - Large Text: AAA
    - UI Components: AA

![Image of constrast check for the navbar and footer element with hover effect on links and icons.](docs\images\color_contrast_check\navbar_hover_small.png)


- **Body:** (light color on the background, dark color on the text)
  - background-color: #f5f2eb - pale, off-white or light beige color
  - text: #333333 - dark gray or dark charcoal
    - Contrast Ratio: 11.30
    - Normal Text: AAA
    - Large Text: AAA
    - UI Components: AA

![Image of constrast check for the body element.](docs\images\color_contrast_check\body_small.png)


- **Button - btn-outline-primary:** (button used for sending, submitting, confirming, etc.)
  - color: #6b4f4f - dark brown or deep reddish-brown
  - border-color: #6b4f4f - dark brown or deep reddish-brown
  - background-color: #f5f2eb - pale, off-white or light beige color
    - Contrast Ratio: 6.88
    - Normal Text: AA
    - Large Text: AAA
    - UI Components: AA

![Image of constrast check for the button btn-outline-primary.](docs\images\color_contrast_check\btn_outline_primary_small.png)


- **Button with hover effect - btn-outline-primary:hover:** (button used for sending, submitting, confirming, etc.)
  - background-color: #6b4f4f - dark brown or deep reddish-brown
  - color: #ffffff - white
    - Contrast Ratio: 7.47
    - Normal Text: AAA
    - Large Text: AAA
    - UI Components: AA

![Image of constrast check for the button btn-outline-primary with hover effect.](docs\images\color_contrast_check\btn_outline_primary_hover_small.png)


- **Button - btn-secondary-custom:** (button used to cancel, clear, etc.)
  - background-color: #e4dad2 - light beige or off-white
  - color: #6b4f4f - dark brown or deep reddish-brown
  - border: #6b4f4f - dark brown or deep reddish-brown
    - Contrast Ratio: 5.42
    - Normal Text: AA
    - Large Text: AAA
    - UI Components: AA

![Image of constrast check for the button btn-secondary-custom.](docs\images\color_contrast_check\btn_secondary_custom_small.png)


- **Button with hover effect - btn-secondary-custom:hover:** (button used to cancel, clear, etc.)
  - background-color: #d6c7bc - light beige or off-white
  - color: #000000 - black
    - Contrast Ratio: 12.76
    - Normal Text: AAA
    - Large Text: AAA
    - UI Components: AA

![Image of constrast check for the button btn-secondary-custom:hover.](docs\images\color_contrast_check\btn_secondary_custom_hover_small.png)


### Fonts

To find fonts for my website, I looked at the [W3Schools page CSS Great Font Pairings](https://www.w3schools.com/css/css_font_pairings.asp). There, I chose the font pair Merriweather and Open Sans. I downloaded both [Merriweather](https://fonts.google.com/specimen/Merriweather) and [Open Sans](https://fonts.google.com/specimen/Open+Sans) from [Google Fonts](https://fonts.google.com/).

The fonts are used in this way on the website:
- Merriweather: H1, H2, H3
- Open Sans: Body

### Icons and Images

To create the favicon (the icon that appears in the tab in the browser) and the icon that is on the far left in the navbar, I started from the same image. I found the image on [Pixabay](https://pixabay.com/) (see Credit for more information about the image and image owner). To create the favicon, I used [Favicon's](https://favicon.io/) favicon generator. And to create the icon in the navbar, I used [Microsoft Photos](https://apps.microsoft.com/detail/9wzdncrfjbh4?hl=en-US&gl=US) to reduce the size of the image and remove the background color.
The social media icons (Facebook, Instagram, X and Youtube), which are in the footer, come from [FontAwsome](https://fontawesome.com/).
I found the hero image (depicting a bunch of books) on [Pixabay](https://pixabay.com/) (see Credit for more information about the image and image owner)
Book cover images come from [Adlibris](https://www.adlibris.com/sv) and [Bokus](https://www.bokus.com/). More specific information about the book covers can be found in Credits.


## 7. Existing Features
[Back To The Top](#table-of-contents)
### Existing Features - Site Visitors
#### Navigation And Footer
#### Home Page
#### Create Account
#### Login
#### Logout
#### Rate Book
#### Comment Book
#### Edit Comment
#### Delete Comment
#### Edit User Details
### Existing Features - Administrator(s)
#### Add Book
#### Edit Book
#### Delete Book
#### Approve Comment
#### Delete Comment
#### Update Text On The About Page
#### See Contact Requests
#### See Ratings

## 8. Features Left To Implement
[Back To The Top](#table-of-contents)

In addition to the features that are currently added to the website, I have come up with some other features that could be added in the future. I have divided the features into Site Visitors and Administrator(s).

### Features Left To Implement - Site Visitors
* Develop user profiles with more information, for example a profile picture.
* Add filter/sorting function to the books page so users/visitors can filter/sort by genre or rating.
* Add search function where the users can search for, for example, author, book title or genre. 
* Add password reset functionality in case a user/visitor has forgotten their password.
### Features Left To Implement - Administrator(s)
* Add approve comment possibility to the Admin section on the website.
* Add the possibility to administer contact requests in the Admin section on the website.

## 9. Technologies Used
[Back To The Top](#table-of-contents)
### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML) - Used to create the foundation of all subpages on the website.
- [CSS](https://en.wikipedia.org/wiki/CSS) - Used to style the website and to get content to end up in the right place.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Scripting language used to achieve the star rating and "reply to comment" form on the Book Detail page.
- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language)) - Programming language that (together with Django) was used to create the website.
### Programs And Other Resoures
- [Django](https://www.djangoproject.com/) - a high-level Python web framework that was used to create the website/web application.
- [PostgreSQL](https://www.postgresql.org/) - The database used on the website is a PostgreSQL database.
- [Cloudinary](https://cloudinary.com/) - Used to save book covers
- [Bootstrap, v5.3](https://getbootstrap.com/) - Used Boostrap to structure the pages and used some Bootstrap elements to style the site.
    - [Navbar](https://getbootstrap.com/docs/5.3/components/navbar/#nav) - Used a Bootstrap navbar as a template, but adapted it to my website.
    - [Buttons](https://getbootstrap.com/docs/5.3/components/buttons/) - I started with Bootstrap buttons but customized colors and so on to fit my site.
- [Heroku](https://www.heroku.com/) - The website is deployed to Heroku.
- [Visual Studio Code](https://code.visualstudio.com/) - Program used to code the website.
- [Git](https://git-scm.com/) - Mainly used to save the website to GitHub.
- [GitHub](https://github.com/) - GitHub is the place where my website (repository) is stored.
- [Responsinator](http://www.responsinator.com/) - Used to check how the site looks on different devices and how responsive it is.
- [Am I Responsive](https://ui.dev/amiresponsive) - Used to check how the site looks on different devices and how responsive it is.
-[Responsive Web Design Checker](https://responsivedesignchecker.com/) - Used to see how my website looks on different types of devices and screen sizes.
- [tinypng](https://tinypng.com/) - Used to compress images.
- [HTML Validator](https://validator.w3.org/nu/) - Used to validate the HTML files.
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to validate the JavaScript code.
- [Site24x7's JavaScript validator](https://www.site24x7.com/tools/javascript-validator.html) - Used to validate the JavaScript code.
- [JShint](https://jshint.com/) - Used to validate the JavaScript Code.
- [Favicon](https://favicon.io/favicon-converter/) - Used to generate the favicon
- [Fontawsome](https://fontawesome.com/) - For the social media icons (Facebook, Instagram, X and Youtube)
- [ColorMagic Contrast Checker](https://colormagic.app/contrast-checker) - Was used to check the constrast of the colors that I have chosen
- [Google Fonts](https://fonts.google.com/) - Was used to download the fonts that I have chosen to use (EB Garamond and Open Sans)
- [Google Transate](https://translate.google.com/) - Was used to translate text for accuracy.
- [drawDB](https://www.drawdb.app/) - Was used to create the Entity Relationship Diagram

## 10. Testing
[Back To The Top](#table-of-contents)
### User Story Testing
### Manual Testing - Site Visitors
#### Test - Navigation And Footer
#### Test - Home Page
#### Test - Create Account
#### Test - Login
#### Test - Logout 
#### Test - Rate Book
#### Test - Comment Book
#### Test - Edit Comment
#### Test - Delete Comment
#### Test - Edit User Details
### Manual Testing - Administrator(s)
#### Test - Add Book
#### Test - Edit Book
#### Test - Delete Book
#### Test - Approve Comment
#### Test - Delete Comment
#### Test - Update Text On The About Page
#### Test - See Contact Requests
#### Test - See Ratings

## 11. Bugs
[Back To The Top](#table-of-contents)

- Having trouble getting images and css to work after deploying to Heroku.
    - This was because I hadn't run collectstatic and the Cloudinary settings were not correct. After running collectstatic and correcting the Cloudinary settings it worked.
- Problem with vertical scrollbars being displayed on pages where they weren't needed. Tried to make changes to the scrollbars but resulted in double scrollbars or a scrollbar with an empty space to the left of it.
    - In order not to spend too much time on a problem that is actually rather small, I made it so that there are scrollbars on all pages. This will probably be something I will have to come back to, something that can be improved.


## 12. Validation
[Back To The Top](#table-of-contents)
### HTML
### CSS
### JavaScript
### Python

## 13. Lighthouse Testing
[Back To The Top](#table-of-contents)
### Desktop
### Mobile

## 14. Device Testing
[Back To The Top](#table-of-contents)

I used the Dell Vostro 3520 laptop to create the website. In addition to my laptop, I have also tested the website on my tablet, a Samsung Galaxy Tab S8, and my mobile phone, a Samsung Galaxy S24 Ultra.

I have also tested my website on Responsinator and Am I responsive to see how it looks (and works) on other devices and screen sizes.

## 15. Browser Compatibility
[Back To The Top](#table-of-contents)

I have tested the website on the browsers below. The website works properly in all browsers, the site is responsive and the features work as they should.

* Google Chrome
* Microsoft Edge
* Opera
* Firefox

## 16. Deployment
[Back To The Top](#table-of-contents)
### Local Deployment
### Remote Deployment

## 17. Credits 
[Back To The Top](#table-of-contents)




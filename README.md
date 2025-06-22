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
        - [**View/Show Books**](#viewshow-books)
        - [**Rate Book**](#rate-book)
        - [**Comment Book**](#comment-book)
        - [**Edit Comment**](#edit-comment)
        - [**Delete Comment**](#delete-comment)
        - [**Edit User Details**](#edit-user-details)
    - [**Existing Features - Administrator(s)**](#existing-features---administrators)
        - [**Add Book**](#add-book)
        - [**Edit Book**](#edit-book)
        - [**Delete Book**](#delete-book)
        - [**Update Text On The About Page**](#update-text-on-the-about-page)
        - [**Approve Comment**](#approve-comment)
        - [**Delete Comment**](#delete-comment-1)
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
    - [**Test - View/Show Books**](#test---viewshow-books)
    - [**Test - Rate Book**](#test---rate-book)
    - [**Test - Comment Book**](#test---comment-book)
    - [**Test - Edit Comment**](#test---edit-comment)
    - [**Test - Delete Comment**](#test---delete-comment)
    - [**Test - Edit User Details**](#test---edit-user-details)
  - [**Manual Testing - Administrator(s)**](#manual-testing---administrators)
    - [**Test - Add Book**](#test---add-book)
    - [**Test - Edit Book**](#test---edit-book)
    - [**Test - Delete Book**](#test---delete-book)
    - [**Test - Update Text On The About Page**](#test---update-text-on-the-about-page)
    - [**Test - Approve Comment**](#test---approve-comment)
    - [**Test - Delete Comment**](#test---delete-comment-1)

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

**Navbar**

In the header there is a navbar consisting of a logo (depicting a pile of books), The BookWorm’s Place link and links to the website's various pages. Which links are available in the navbar depends on whether the site visitor is logged in or not. And whether the site visitor is a regular visitor or an administrator.

If the site visitor is not logged in, the following links are available in the navbar: **Home**, **Books**, **About**, **Create Account** and **Login**.

A logged-in regular site visitor can see the following links in the navbar: **Home**, **Books**, **About**, **My Profile** and **Logout**.

A logged in administrator can see the following links in the navbar: **Home**, **Books**, **About**, **My Profile**, **Admin**, and **Logout**.

The nav bar is from [Bootstrap](https://getbootstrap.com/).

The navbar that I have based mine on is [this one](https://getbootstrap.com/docs/5.3/components/navbar/#nav). I have then modified it the way I want it and with the colors I have chosen to use.

**The navbar on screens that are 992px or larger.**

Navbar - Not logged in:
![Image of Navbar - Not logged in.](docs\images\features\navigation_and_footer\navbar_992px_or_larger_small.png)

Navbar - Logged in regular site visitor:
![Image of Navbar - Logged in regular site visitor.](docs\images\features\navigation_and_footer\navbar_992px_or_larger_logged_in_site_visitor_small.png)

Navbar - Logged in administrator:
![Image of Navbar - Logged in administrator.](docs\images\features\navigation_and_footer\navbar_992px_or_larger_logged_in_admin_small.png)

The navbar has a hover effect on screens that are 992px or larger. When you move the mouse pointer over each page in the navbar, the color of the text changes.

Navbar with hover effect:
![Image of Navbar - Navbar with hover effect.](docs\images\features\navigation_and_footer\navbar_992px_or_larger_logged_in_site_visitor_hover_small.png)

**On screens that are 991px or smaller, the links in the navbar become a toggle menu on the right of the navbar.**

Navbar - Not logged in:
![Image of Navbar - Not logged in.](docs\images\features\navigation_and_footer\navbar_991px_or_smaller_not_logged_in_small.png)

Navbar - Logged in regular site visitor:
![Image of Navbar - Logged in regular site visitor.](docs\images\features\navigation_and_footer\navbar_991px_or_smaller_logged_in_site_visitor_small.png)

Navbar - Logged in administrator:
![Image of Navbar - Logged in administrator.](docs\images\features\navigation_and_footer\navbar_991px_or_smaller_logged_in_admin_small.png)

**Footer**

The footer consists of a row with a copyright symbol and the text The BookWorm’s Place and a row of clickable social media icons (Facebook, Instagram, X and Youtube). Currently, the icons are linked to the Facebook, Instagram, X and Youtube websites. The footer looks the same regardless of screen size.

![Image of the Footer](docs\images\features\navigation_and_footer\footer_small.png)

#### Home Page

The Home Page consists of a large hero image that depicts books. The hero image has the text “Welcome To The BookWorm’s Place” and a button with the text “Browse Books”. If you click the “Browse Books” button, you will be redirected to the Books page. I have chosen not to have any more text on the front page than the welcome text as I think the page is very self-explanatory. It is clear from the name of the page, the choice of icons and the image on the home page what the website is about.

![Image of the Footer](docs\images\features\home_page\home_page_small.png)

#### Create Account

The “Create Account” page is accessed by clicking on “Create Account” in the navbar. The “Create Account” link is visible if the site visitor is NOT logged in before.

The “Create Account” page currently consists of a simple form where you enter your username, email address, password and password confirmation. To save the account, click on the "Register" button. When you have clicked on the "Register" button, you will be sent to the "Login" page. There appears a message that says "Your account has been created. Please log in.". If you do not want to save the account, you can click on the "Cancel" button (you will then be taken to the Home Page).

![Image of the Create Account page](docs\images\features\create_account\create_account.png)

![Image of the Create Account confirmation](docs\images\features\create_account\create_account_confirmation.png)

#### Login

The “Login” page is accessed by clicking on “Login” in the navbar. The “Login” link is visible if the site visitor is NOT logged in before.

The “Login” page currently consists of a simple form where you enter your username and password. Then click the "Login" button to log in. Once you have logged in, you will be taken to the Home Page. To show that you are logged in, a message will appear under the navbar stating “You are now logged in as” followed by your username. If you do not want to login, you can click on the "Cancel" button (you will then be taken to the Home Page).

![Image of the Login page](docs\images\features\login\login.png)

![Image of the Login message](docs\images\features\login\login_message.png)

#### Logout

The “Logout” page is accessed by clicking on “Logout” in the navbar. The “Logout” link is displayed if the site visitor is logged in to the website.

The “Logout” page consists of a simple form that contains the text “Are you sure you want to log out?” and the buttons “Log Out” and “Cancel”. If you click on the “Log Out” button, you will be logged out and taken to the Home Page. A message will appear on the Home Page stating “You have been logged out.”. If you do not want to logout, you can click on the "Cancel" button (you will then be taken to the Home Page).

![Image of the Logout page](docs\images\features\logout\logout.png)

![Image of the Logout message](docs\images\features\logout\logout_message.png)

#### View/Show Books

To view added books, click either the “Browse Books” button on the Home Page or the “Books” link in the navbar. You will then be sent to the “Books” page where added books are displayed. The books are displayed with book cover, title and author. The number of books displayed in each row depends on the size of the screen, the smaller the screen, the fewer books displayed in each row (on the smallest screen sizes, two books are displayed per row).

**Image of Books page 992px or larger**

![Image of Books page 992px or larger](docs\images\features\books\books_992px_or_larger_small.png)

**Image of Books page 991px or smaller**

![Image of Books page 991px or smaller](docs\images\features\books\books_991px_or_smaller.png)

**Image of Books page 767px or smaller**

![Image of Books page 767px or smaller](docs\images\features\books\books_767px_or_smaller.png)

**Image of Books page 575px or smaller**

![Image of Books page 575px or smaller](docs\images\features\books\books_575px_or_smaller.png)

To view more information about the book, click the “View Details” button. Doing so will take you to the “Book detail” page. There, in addition to the book cover, book title and author, you can also view the book description. You can also see the rating (in the form of stars) that other page visitors have given to the book and see comments that other page visitors have written. In order to rate a book and leave a comment, you need to be logged in to the website.

**Image of Book details page 768px or larger**

![Image of Book details page 768px or larger](docs\images\features\book_details\book_details_768px_or_larger_small.png)

**Image of Book details page 767px or smaller**

![Image of Books page 767px or smaller](docs\images\features\book_details\book_details_767px_or_smaller.png)

#### Rate Book

If you are logged in to the website, you can rate uploaded books. You rate the book by clicking on the number of stars you want to give the book (1-5) and then clicking on the “Rate” button. After you have clicked on the “Rate” button, your rating is saved (to the database) and a “Your rating has been submitted.” message is displayed on the page. When the rating is saved, the Average Rating is also updated. The Average Rating is calculated by adding all the ratings the book has received and dividing them by the number of ratings that have been made. The rating you have made is saved and you can change it if you wish.

**Image of Book details star rating**

![Image of Book details star rating](docs\images\features\book_details\rate_book\book_details_rating.png)

**Image of Book details star rating - filled stars**

![Image of Book details star rating - filled stars](docs\images\features\book_details\rate_book\book_details_rating_filled_stars.png)

**Image of Book details star rating - message**

![Image of Book details star rating - message](docs\images\features\book_details\rate_book\book_details_rating_message.png)

**Image of Book details star rating - result**

![Image of Book details star rating - result](docs\images\features\book_details\rate_book\book_details_rating_show_result.png)

#### Comment Book

If you are logged in to the website, you can comment on saved books. If there are comments saved from before, you can also choose to reply to them. To reply to a comment, click the “Reply” button below the comment. Type your response and then click the “Submit Reply” button. When a comment is saved, a “Your comment is awaiting approval.” message will appear. The comment needs to be approved by the website administrator before it appears on the page. This applies regardless of whether you add a new comment or reply to a comment.

It is currently only possible to leave one reply to a comment. This is because the current idea is not for the website to be a discussion forum.

**Image of Book details - comment form**

![Image of Book details comment form](docs\images\features\book_details\comment\book_details_comment_small.png)

**Image of Book details - comment form - written comment**

![Image of Book details comment form - written comment](docs\images\features\book_details\comment\book_details_comment_written_comment_small.png)

**Image of Book details - comment submitted - message**

![Image of Book details comment submitted - message](docs\images\features\book_details\comment\book_details_comment_submitted_comment_message_small.png)

**Image of Book details - comment**

![Image of Book details comment](docs\images\features\book_details\comment\book_details_comment_shown_small.png)

**Image of Book details - reply to comment**

![Image of Book details - reply to comment](docs\images\features\book_details\comment\reply\book_details_comment_reply_small.png)

**Image of Book details - reply to comment form**

![Image of Book details - reply to comment form](docs\images\features\book_details\comment\reply\book_details_comment_reply_form_small.png)

**Image of Book details - reply to comment message**

![Image of Book details - reply to comment message](docs\images\features\book_details\comment\reply\book_details_comment_reply_comment_message_small.png)

**Image of Book details - reply to comment shown on the website**

![Image of Book details - reply to comment shown on the website](docs\images\features\book_details\comment\reply\book_details_comment_reply_shown_small.png)


#### Edit Comment

If you are logged in to the site, you can edit comments that you have made yourself. To do so, click the “Edit” button below the comment, make the changes you want to make, and then click the “Submit Changes” button. Once the comment has been saved, a “Your comment is awaiting approval.” message will appear. The comment needs to be approved by the site administrator before it appears on the page.

**Image of Book details - edit comment**

![Image of Book details - edit comment](docs\images\features\book_details\comment\edit\book_details_edit_small.png)

**Image of Book details - edit comment form**

![Image of Book details - edit comment form](docs\images\features\book_details\comment\edit\book_details_edit_comment_small.png)

**Image of Book details - edited comment form**

![Image of Book details - edited comment form](docs\images\features\book_details\comment\edit\book_details_edited_comment_small.png)

**Image of Book details - edited comment message**

![Image of Book details - edited comment message](docs\images\features\book_details\comment\edit\book_details_edited_comment_message_small.png)

#### Delete Comment

If you are logged in to the website, you can delete comments that you have made yourself. Click the “Delete” button below the comment, make the changes you want to make, and then click the “Yes, delete” button. After clicking the “Yes delete” button, you will be sent back to the page for the book you were on. A message will also appear saying “Comment successfully deleted.”.

**Image of Book details - delete comment**

![Image of Book details - delete comment](docs\images\features\book_details\comment\delete\book_details_delete_small.png)

**Image of Book details - delete comment page**

![Image of Book details - delete comment page](docs\images\features\book_details\comment\delete\book_details_delete_comment_small.png)

**Image of Book details - delete comment message**

![Image of Book details - delete comment message](docs\images\features\book_details\comment\delete\book_details_delete_comment_message_small.png)

**Image of Book details - deleted comment gone**

![Image of Book details - deleted comment gone](docs\images\features\book_details\comment\delete\book_details_deleted_comment_comment_gone_small.png)

#### Edit User Details

**Image of My Profile Overview** 

![Image of My Profile Overview](docs\images\features\my_profile\my_profile_overview_small.png)

If you are logged in to the site, you can change your user details. To do this, click on “My Profile” in the navbar. When you click on “My Profile” you will be taken to a page where you can choose to change your username, email address or password. Currently, this function is very simple and there are some improvements that can be made to it, for example when it comes to security.

To change your username, click the “Change Username” button. Change your username and then click the “Save” button. After you click the “Save” button, your username will be changed and a “Username updated successfully” message will also appear.

**Image of My Profile - Change Username** 

![Image of My Profile - Change Username](docs\images\features\my_profile\change_username\my_profile_change_username.png)

**Image of My Profile - Changed Username - message** 

![Image of My Profile - Changed Username - message](docs\images\features\my_profile\change_username\my_profile_change_username_message_small.png)

To change your email address, click the “Change Email” button. Change your email address and then click the “Save” button. After you click the “Save” button, your username will be changed and you will also see an “Email address updated successfully” message.

**Image of My Profile - Change Email** 

![Image of My Profile - Change Email](docs\images\features\my_profile\change_email\my_profile_change_email_small.png)

**Image of My Profile - Changed Email - message** 

![Image of My Profile - Change Email - message](docs\images\features\my_profile\change_email\my_profile_change_email_message_small.png)

To change your password, click the “Change Password” button. To change your password, you need to remember your old password (it will not be filled in automatically). Then fill in the “New Password” and “Confirm Password” fields. Then click the “Save” button. After clicking the “Save” button, your username will be changed and a “Your password was successfully changed” message will also appear.

**Image of My Profile - Change Password** 

![Image of My Profile - Change Password](docs\images\features\my_profile\change_password\my_profile_change_password_small.png)

**Image of My Profile - Changed Password - message** 

![Image of My Profile - Change Password - message](docs\images\features\my_profile\change_password\my_profile_change_password_message_small.png)

### Existing Features - Administrator(s)

A logged in administrator can use the website's administrator section. To access it, click Admin in the navbar. In the administrator section, an administrator can create a draft/add a book, edit a book, delete a book, and change the text on the About page.

**Image of Admin Dashboard** 

![Image of Admin Dashboard](docs\images\features\admin\admin_dashboard_small.png)

#### Add Book

To add a book (or to create a draft), click Add book. Then fill in all the information (in the case of slug, you can skip filling in that field as the slug is automatically created after the title field). If the book should be a draft, check the box next to “Save as draft”. To save the book, click the “Save Book” button. The book will then be saved to the database (and added to the Books page if “Save as draft” is not checked). A “Book added successfully” message will also be displayed. If you have chosen to save the added book as a draft, you can go in at a later time and uncheck “Save as draft” to make the book available on the page.

**Image of Admin - Add a book, part 1 of form** 

![Image of Admin - Add a book, part 1 of form](docs\images\features\admin\add_book\admin_add_book_part1_small.png)

**Image of Admin - Add a book, part 2 of form** 

![Image of Admin - Add a book, part 2 of form](docs\images\features\admin\add_book\admin_add_book_part2_small.png)

**Image of Admin - Add a book - added book message** 

![Image of Admin - Add a book - added book message](docs\images\features\admin\add_book\admin_add_book_message_small.png)

#### Edit Book

To change the information for a book, click the “Edit” button next to the book you want to change the information for. Then change what you want to change and click the “Save Book” button to save the book. If you want to save the book as a draft, check the box next to “Save as draft”. If you want to save the book directly to the database and to the Books page, leave the box next to “Save as draft” empty. After clicking the “Save Book” button, a “Book updated successfully” message will appear.

**Image of Admin - Edit a book, part 1 of form** 

![Image of Admin - Edit a book, part 1 of form](docs\images\features\admin\edit_book\admin_edit_book_part_1_small.png)

**Image of Admin - Edit a book, part 2 of form** 

![Image of Admin - Edit a book, part 2 of form](docs\images\features\admin\edit_book\admin_edit_book_part_2_small.png)

**Image of Admin - Edit a book - added book message** 

![Image of Admin - Edit a book - added book message](docs\images\features\admin\edit_book\admin_edit_book_part_message_small.png)

#### Delete Book

To delete a book, click the “Delete” button next to the book you want to delete. To delete the book, click the “Yes, delete” button on the page you are taken to. Once you have clicked the “Yes, delete” button, you will be sent back to the Admin Dashboard, a “Book deleted successfully” message will appear, and the book will have disappeared from the book list.

**Image of Admin - Delete a book - added test book** 

![Image of Admin - Delete a book, added test book](docs\images\features\admin\delete_book\admin_delete_book_added_test_book_small.png)

**Image of Admin - Delete a book - delete book page** 

![Image of Admin - Delete a book - delete book page](docs\images\features\admin\delete_book\admin_delete_book_small.png)

**Image of Admin - Delete a book - book deleted message** 

![Image of Admin - Delete a book - book deleted message](docs\images\features\admin\delete_book\admin_delete_book_message_small.png)

#### Update Text On The About Page

To change the text on the About page, click the “Edit About” button on the Admin Dashboard. Then change the text and click the “Save Changes” button to save the changes. After clicking the “Save Changes” button, an “About page successfully updated” message will appear. The text on the About page has also been changed.

**Image of Admin - Update About page text** 

![Image of Admin - Update About page text](docs\images\features\admin\update_About_page_text\admin_edit_about_page_text_small.png)

**Image of Admin - Update About page text - message** 

![Image of Admin - Update About page text - message](docs\images\features\admin\update_About_page_text\admin_edit_about_page_text_message_small.png)

#### Approve Comment - Django administration
  
  * Currently, an administrator needs to log in to Django administration in order to approve comments made.

#### Delete Comment - Django administration

  * Currently, an administrator needs to log in to Django administration to be able to delete comments that for some reason should not be displayed on the website, for example due to language usage.

#### See Contact Requests - Django administration

  * Currently, an administrator needs to log in to Django administration in order to see contact requests.

#### See Ratings - Django administration

  * Currently, an administrator needs to log in to Django administration in order to be able to see ratings made.

## 8. Features Left To Implement
[Back To The Top](#table-of-contents)

In addition to the features that are currently added to the website, I have come up with some other features that could be added in the future. I have divided the features into Site Visitors and Administrator(s).

### Features Left To Implement - Site Visitors

* Develop user profiles with more information, for example a profile picture.
* Add filter/sorting function to the books page so users/visitors can filter/sort by genre or rating.
* Add search function where the users can search for, for example, author, book title or genre. 
* Add password reset functionality in case a user/visitor has forgotten their password.

### Features Left To Implement - Administrator(s)

* Add these features to the Admin section of the website.
  * Approve comments
  * Delete comments
  * See contact requests
  * See ratings


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

**Book covers and book descriptions:**

| Book title and author | Book cover from | Book facts from |
|------------|-----------------|-----------------|
| Middle of the Night by Riley Sager | [Adlibris](https://www.adlibris.com/se/bok/middle-of-the-night-9781399712422 ) | [Goodreads](https://www.goodreads.com/book/show/199026522-middle-of-the-night?from_search=true&from_srp=true&qid=i1qxyDIOf5&rank=7 ) |
| Book Lovers by Emily Henry | [Adlibris](https://www.adlibris.com/se/bok/book-lovers-9780593334836) | [Goodreads](https://www.goodreads.com/book/show/58690308-book-lovers?from_search=true&from_srp=true&qid=bhg2kcmSuP&rank=4) |
| Hidden Nature by Nora Roberts | [Bokus](https://www.bokus.com/bok/9781250370853/hidden-nature/) | [Goodreads](https://www.goodreads.com/book/show/217388081-hidden-nature) |
| Fourth Wing by Rebecca Yarros | [Adlibris](https://www.adlibris.com/se/bok/fourth-wing-9780349436999) | [Goodreads](https://www.goodreads.com/book/show/61431922-fourth-wing?from_search=true&from_srp=true&qid=uauykkg21N&rank=1) |
| You Like It Darker by Stephen King | [Adlibris](https://www.adlibris.com/se/bok/you-like-it-darker-9781668037713) | [Goodreads](https://www.goodreads.com/book/show/201242757-you-like-it-darker) |


**Images:**

| Page | File title on the site | Downloaded From | Photographer/Owner |
|------|------------------------|-----------------|--------------------|
| Home page | books-1614215_1280.jpg | [Pixabay](https://pixabay.com/illustrations/books-shelf-library-book-shelf-1614215/) | myrfa |
| Navbar logo | books-441866_640_no_background_small.png | [Pixabay](https://pixabay.com/photos/books-training-school-literature-441866/) | Hermann | 
| Favicon | favicon.ico | [Pixabay](https://pixabay.com/photos/books-training-school-literature-441866/) | Hermann |


**Icons - Footer:**
| Icon | From |
|------|------|
| Facebook | [FontAwesome](https://fontawesome.com/icons/square-facebook?f=classic&s=brands ) |
| Instagram | [FontAwesome](https://fontawesome.com/icons/square-instagram?f=classic&s=brands) |
| X | [FontAwesome](https://fontawesome.com/icons/square-x-twitter?f=classic&s=brands) |
| Youtube | [FontAwsome](https://fontawesome.com/icons/square-youtube?f=classic&s=brands) |
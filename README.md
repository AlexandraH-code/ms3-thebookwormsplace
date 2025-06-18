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
4. [**Design Of The Website**](#4-design-of-the-website)
    - [**Structure**](#structure)
    - [**Wireframes**](#wireframes)
        - [**Mobile Wireframes**](#mobile-wireframes)
        - [**Tablet Wireframes**](#tablet-wireframes)
        - [**Laptop/Desktop Wireframes**](#laptopdesktop-wireframes)
    - [**Colors**](#colors)
    - [**Fonts**](#fonts)
    - [**Icons And Images**](#icons-and-images)
5. [**Existing Features**](#5-existing-features)
    - [**Existing Features - Users**](#existing-features---users)
        - [**Register Account**](#register-account)
        - [**Login**](#login)
        - [**Logout**](#logout)
        - [**Rate Book**](#rate-book)
        - [**Comment Book**](#comment-book)
        - [**Edit Comment**](#edit-comment)
        - [**Delete Comment**](#delete-comment)
        - [**Edit User Details**](#edit-user-details)
    - [**Existing Features - Admin**](#existing-features---admin)
        - [**Add Book**](#add-book)
        - [**Edit Book**](#edit-book)
        - [**Delete Book**](#delete-book)
        - [**Approve Comment**](#approve-comment)
        - [**Delete Comment**](#delete-comment-1)
        - [**Update Text On The About Page**](#update-text-on-the-about-page)
        - [**See Contact Requests**](#see-contact-requests)
        - [**See Ratings**](#see-ratings)
6. [**Features Left To Implement**](#6-features-left-to-implement)
    - [**Features Left To Implement - Users**](#features-left-to-implement---users)
    - [**Features Left To Implement - Admin**](#features-left-to-implement---admin)
7. [**Technologies Used**](#7-technologies-used)
  - [**Languages**](#languages)
  - [**Programs And Other Resources**](#programs-and-other-resoures)
8. [**Testing**](#8-testing)
  - [**User Story Testing**](#user-story-testing)
  - [**Manual Testing - Users**](#manual-testing---users)
    - [**Test - Register Account - User**](#test---register-account)
    - [**Test - Login**](#test---login)
    - [**Test - Logout**](#test---logout)
    - [**Test - Rate Book**](#test---rate-book)
    - [**Test - Comment Book**](#test---comment-book)
    - [**Test - Edit Comment**](#test---edit-comment)
    - [**Test - Delete Comment**](#test---delete-comment)
    - [**Test - Edit User Details**](#test---edit-user-details)
  - [**Manual Testing - Admin**](#manual-testing---admin)
    - [**Test - Add Book**](#test---add-book)
    - [**Test - Edit Book**](#test---edit-book)
    - [**Test - Delete Book**](#test---delete-book)
    - [**Test - Approve Comment**](#test---approve-comment)
    - [**Test - Delete Comment**](#test---delete-comment-1)
    - [**Test - Update Text On The About Page**](#test---update-text-on-the-about-page)
    - [**Test - See Contact Request**](#test---see-contact-requests)
    - [**Test - See Ratings**](#test---see-contact-requests)
9. [**Bugs**](#9-bugs)
10. [**Validation**](#10-validation)
  - [**HTML**](#html)
  - [**CSS**](#css)
  - [**JavaScript**](#javascript)
  - [**Python**](#python)
11. [**Lighthouse Testing**](#11-lighthouse-testing)
  - [**Desktop**](#desktop)
  - [**Mobile**](#mobile)
12. [**Device Testing**](#12-device-testing)
13. [**Browser Compatibility**](#13-browser-compatibility)
14. [**Deployment**](#14-deployment)
  - [**Local Deployment**](#local-deployment)
  - [**Remote Deployment**](#remote-deployment)
15. [**Credits**](#15-credits)

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

## 4. Design Of The Website
[Back To The Top](#table-of-contents)
### Structure

The website is structured with a header (navigation bar), main content area, and footer with social media links.
### Wireframes
I have used Balsamiq to make the tireframes. The wireframes show how I have thought that the site should look.

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
  <summary>Register Account</summary>

  ![Register Account](docs\wireframes\mobile\register_account.png)
  
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
  <summary>Register Account</summary>

  ![Register Account](docs\wireframes\tablet\register_account.png)
  
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
  <summary>Register Account</summary>

  ![Register Account](docs\wireframes\laptop_desktop\register_account.png)
  
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

### Fonts

I have chosen to use fonts from Google Fonts. The two fonts I have chosen are EB Garamond and Open Sans. EB Garamond is used on headings (for example H1, H2, H3, etc.) and Open Sans on other text.

### Icons and Images

## 5. Existing Features
[Back To The Top](#table-of-contents)
### Existing Features - Users
#### Register Account
#### Login
#### Logout
#### Rate Book
#### Comment Book
#### Edit Comment
#### Delete Comment
#### Edit User Details
### Existing Features - Admin
#### Add Book
#### Edit Book
#### Delete Book
#### Approve Comment
#### Delete Comment
#### Update Text On The About Page
#### See Contact Requests
#### See Ratings

## 6. Features Left To Implement
[Back To The Top](#table-of-contents)
### Features Left To Implement - Users
* Develop user profiles with more information, for example a profile picture.
* Add filter/sorting function to the books page so users/visitors can filter/sort by genre or rating.
* Add search function where the users can search for, for example, author, book title or genre. 
* Add password reset functionality in case a user/visitor has forgotten their password.
### Features Left To Implement - Admin
* Add approve comment possibility to the Admin section on the website.
* Add the possibility to administer contact requests in the Admin section on the website.

## 7. Technologies Used
[Back To The Top](#table-of-contents)
### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
### Programs And Other Resoures
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Cloudinary](https://cloudinary.com/)
- [Bootstrap, v5.3](https://getbootstrap.com/) - Used Boostrap to structure the pages and used some Bootstrap elements to style the site.
    - [Navbar](https://getbootstrap.com/docs/5.3/components/navbar/#nav) - Used a Bootstrap navbar as a template, but adapted it to my website.
    - [Buttons](https://getbootstrap.com/docs/5.3/components/buttons/) - I started with Bootstrap buttons but customized colors and so on to fit my site.
- [Heroku](https://www.heroku.com/) - The website is deployed to Heroku.
- [Visual Studio Code](https://code.visualstudio.com/) - Program used to code the website.
- [Git](https://git-scm.com/) - Mainly used to save the website to GitHub.
- [GitHub](https://github.com/) - GitHub is the place where my website (repository) is stored.
- [Responsinator](http://www.responsinator.com/) - Used to check how the site looks on different devices and how responsive it is.
- [Am I Responsive](https://ui.dev/amiresponsive) - Used to check how the site looks on different devices and how responsive it is.
- [tinypng](https://tinypng.com/) - Used to compress images.
- [HTML Validator](https://validator.w3.org/nu/) - Used to validate the HTML files.
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to validate the JavaScript code.
- [Site24x7's JavaScript validator](https://www.site24x7.com/tools/javascript-validator.html) - Used to validate the JavaScript code.
- [JShint](https://jshint.com/) - Used to validate the JavaScript Code.
- [Favicon](https://favicon.io/favicon-converter/) - Used to generate the favicon
- [Fontawsome](https://fontawesome.com/) - For the social media icons (Facebook, Instagram, X and Youtube)
- [ColorMagic Contrast Checker](https://colormagic.app/contrast-checker) - to check the constrast of the colors that I have chosen
- [Google Fonts](https://fonts.google.com/) - was used to download the fonts that I have chosen to use (EB Garamond and Open Sans)
- [Google Transate](https://translate.google.com/) - was used to translate text for accuracy.

## 8. Testing
[Back To The Top](#table-of-contents)
### User Story Testing
### Manual Testing - Users
#### Test - Register Account
#### Test - Login
#### Test - Logout 
#### Test - Rate Book
#### Test - Comment Book
#### Test - Edit Comment
#### Test - Delete Comment
#### Test - Edit User Details
### Manual Testing - Admin
#### Test - Add Book
#### Test - Edit Book
#### Test - Delete Book
#### Test - Approve Comment
#### Test - Delete Comment
#### Test - Update Text On The About Page
#### Test - See Contact Requests
#### Test - See Ratings

## 9. Bugs
[Back To The Top](#table-of-contents)

- Having trouble getting images and css to work after deploying to Heroku.
    - This was because I hadn't run collectstatic and the Cloudinary settings were not correct. After running collectstatic and correcting the Cloudinary settings it worked.
- Problem with vertical scrollbars being displayed on pages where they weren't needed. Tried to make changes to the scrollbars but resulted in double scrollbars or a scrollbar with an empty space to the left of it.
    - In order not to spend too much time on a problem that is actually rather small, I made it so that there are scrollbars on all pages. This will probably be something I will have to come back to, something that can be improved.


## 10. Validation
[Back To The Top](#table-of-contents)
### HTML
### CSS
### JavaScript
### Python

## 11. Lighthouse Testing
[Back To The Top](#table-of-contents)
### Desktop
### Mobile

## 12. Device Testing
[Back To The Top](#table-of-contents)

In addition to my laptop (a Dell Vostro 3520), I have tested the site on my mobile phone, a Samsung Galaxy S24 Ultra, and on my tablet, a Samsung Galaxy Tab S8. The site works, and looks, as it should on all devices.

Then I have also tested my site on Am I Responsive and Responsinator to see how it looks on other devices and if it is responsive.

## 13. Browser Compatibility
[Back To The Top](#table-of-contents)

I have tested the website on the browsers below. The website works properly in all browsers, the site is responsive and the features work as they should.

* Google Chrome
* Microsoft Edge
* Opera
* Firefox

## 14. Deployment
[Back To The Top](#table-of-contents)
### Local Deployment
### Remote Deployment

## 15. Credits 
[Back To The Top](#table-of-contents)




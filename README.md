Blog Website
A feature-rich blog website built with Django, designed to provide a platform for users to create, publish, and interact with blog content. Users can like posts, comment on them, follow other users, and receive notifications for various interactions.

Description
A modern, interactive blogging platform that allows users to create and publish their own blog posts, interact with other bloggers, and manage content with ease. This project integrates a robust backend built with Django and a responsive, dynamic frontend that offers an engaging user experience.

Why
The motivation behind this project is to create a platform that empowers users to share their stories, ideas, and expertise while providing essential features like real-time notifications, comment threads, and social interactions (like following and liking posts). The goal is to offer a seamless blogging experience with added social networking features to engage with an audience and connect with other content creators.

Quickstart
Prerequisites
Python 3.8+
Django 4.2+
Git
Virtual Environment (e.g., venv)
Installation
Clone the Repository:

bash

git clone https://github.com/your-username/blog-website.git
cd blog-website
Set Up Virtual Environment:

bash

python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate
Install Dependencies:

bash

pip install -r requirements.txt
Set Up Database:

Apply migrations to initialize the database:
bash

python manage.py migrate
Run the Development Server:

bash

python manage.py runserver
Access the Application: Open your browser and go to http://127.0.0.1:8000.

Usage
Register and Login:

Create an account or log in to access blogging features.
Create Blogs:

Navigate to the "Create Blog" page.
Add a title, content, and an optional image.
Choose "Save as Draft" or "Publish."
Interact with Blogs:

Like, comment on posts, and follow other users.
Manage Notifications:

View your notifications for likes, comments, and follows.
Contributing
Contributions are welcome to improve the platform. Here’s how to contribute:

Clone the repository:

bash

git clone https://github.com/oladokedamilola/blog-website.git
Fork the repository to your own GitHub account.

Create a new branch for the feature or bug fix:

bash

git checkout -b feature-name
Make the changes: Ensure the code is clean, readable, and that documentation is updated as necessary.

Commit the changes:

bash

git commit -m "Add a meaningful message"
Push the changes:

bash

git push origin feature-name
Open a pull request with a detailed description of the changes.

Features
Core Features
Blog Creation: Users can create blogs with options to save as drafts or publish immediately.
Rich Media Support: Add images to blog posts for a visually engaging experience.
User Authentication: Secure user registration and login functionality, including email verification and reCAPTCHA.
Comments: Users can comment on blog posts, and the author gets notified.
Likes: Users can like/unlike posts, with notifications sent to the author.
Follow System: Follow other users and receive notifications when followed.
Notifications: A real-time notification system for likes, comments, and follows.


Advanced Features
Responsive Design: Built with mobile-first principles for optimal viewing on any device.
Dynamic Slug Generation: SEO-friendly URLs for each blog post.
Draft & Publish Management: Manage blog post visibility with draft and publish options.
Profile System: View user profiles and follow/unfollow users.
Admin Panel: Manage users, posts, comments, and notifications with Django's built-in admin interface.
Analytics: Users can see analysis of their blog posts with chart generation using ApexCharts.
Social Login: Users can log in via Google OAuth for a seamless sign-in experience.
Password Reset: Allows users to reset their password via email.


Project Structure
bash

blog-website/
│
├── blog/                       # Blog app
│   ├── migrations/             # Database migrations
│   ├── static/blog/            # Static files (CSS, JS, Images)
│   ├── templates/blog/         # HTML templates
│   ├── models.py               # Data models
│   ├── views.py                # View functions
│   ├── forms.py                # Django forms
│   └── urls.py                 # URL routing
│
├── users/                      # Users app
│   ├── migrations/             # Database migrations
│   ├── models.py               # User-related models
│   ├── views.py                # View functions for user-related pages
│   ├── forms.py                # Django forms for user registration and authentication
│   ├── urls.py                 # URL routing for users
│
├── static/                     # Global static files
├── media/                      # Uploaded files
├── templates/                  # Global templates
├── .gitignore                  # Git ignore file
├── README.md                   # Project documentation
├── manage.py                   # Django project management script
└── requirements.txt            # Python dependencies


Technologies Used
Backend: Django 4.2
Frontend: HTML5, CSS3, JavaScript
Database: SQLite (default, can be replaced with PostgreSQL/MySQL)
Media Handling: Django's File and Image fields
Notifications: Custom notification model
Social Authentication: Google OAuth for easy login
Charting: ApexCharts for blog post analytics


License
This project is licensed under the MIT License.

Acknowledgments
Special thanks to the open-source community for their invaluable tools and libraries that made this project possible. Special thanks to @codewithsadee for providing the frontend repo used as a foundation for this project, with additional frontend features and pages integrated into the backend with Django.

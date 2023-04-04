Bike Selling Website

This is a bike selling website built using HTML, CSS, JavaScript, and Node.js. The website allows users to browse and purchase bikes, as well as contact the site owners for support.
Getting Started

To get started with the project, follow these steps:
Prerequisites

    Node.js and npm installed on your system
    MongoDB installed and running on your system

Installation

    Clone the repository to your local machine using the command git clone https://github.com/your-username/bike-selling-website.git
    Navigate to the project directory using the command cd bike-selling-website
    Install the required npm packages by running the command npm install
    Start the MongoDB server by running the command mongod
    Start the Node.js server by running the command node server.js
    Open a web browser and navigate to http://localhost:3000

Usage

Once the server is running and you have opened the website in your web browser, you can browse the available bikes, view their details, and purchase them using the provided buttons. You can also contact the site owners for support by filling out the contact form on the Contact Us page.
File Structure

The file structure of the project is as follows:
├── config.js
├── controllers
│   ├── bikes.js
│   └── contacts.js
├── models
│   ├── bike.js
│   └── contact.js
├── public
│   ├── css
│   │   ├── main.css
│   │   └── reset.css
│   ├── img
│   │   ├── bike1.jpg
│   │   ├── bike2.jpg
│   │   └── bike3.jpg
│   └── js
│       ├── main.js
│       └── vendor
│           └── jquery.min.js
├── routes
│   ├── bikes.js
│   └── contacts.js
├── views
│   ├── error.hbs
│   ├── index.hbs
│   ├── layout.hbs
│   ├── partials
│   │   ├── footer.hbs
│   │   └── header.hbs
│   ├── bike-detail.hbs
│   ├── bike-list.hbs
│   └── contact.hbs
└── server.js

The server.js file contains the main Node.js application and serves as the entry point for the application. The config.js file defines the database configuration.

The controllers directory contains the controllers for the bikes and contacts, while the models directory contains the database models for bikes and contacts. The routes directory contains the routers for the bikes and contacts.

The public directory contains static files such as CSS, JavaScript, and images, while the views directory contains the Handlebars templates used by the Node.js app.
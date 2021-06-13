# Einstein's webshop
[![Generic badge](https://img.shields.io/badge/DJANGO-3.1.7-green.svg)](/)
[![Generic badge](https://img.shields.io/badge/HTML-5-blue.svg)](/)
[![Generic badge](https://img.shields.io/badge/CSS-3-orange.svg)](/)
[![Generic badge](https://img.shields.io/badge/BOOTSTRAP-5.0-purple.svg)](/)
[![Generic badge](https://img.shields.io/badge/MYSQL-blue.svg)](/)
[![Generic badge](https://img.shields.io/badge/HEROKU-purple.svg)](/)
[![Generic badge](https://img.shields.io/badge/Python-3.X-yellow.svg)](/)

## Overview

This is a demo online webshop with users and managers features.

- [Einstein's webshop](#einsteins-webshop)
  - [Overview](#overview)
  - [Features](#features)
    - [Frontend](#frontend)
    - [Backend](#backend)
  - [Use cases by roles](#use-cases-by-roles)
    - [Buyer](#buyer)
    - [Manager](#manager)
    - [Admin](#admin)
  - [FAQ](#faq)
  - [For Developers](#for-developers)
    - [Architecture decisions](#architecture-decisions)
    - [Stack specifications](#stack-specifications)
    - [Configurations](#configurations)
  - [To-do's](#to-dos)
    - [UI](#ui)
    - [Developers](#developers)


## Features

### Frontend
- Creation/editing of products

### Backend
- REST API's
- Authentication
- 

## Use cases by roles
### Buyer
1. Search products
2. Order by diff properties
3. Add to cart
### Manager
1. Create product
2. Edit/Delete product
### Admin
1. Admin dashboards
## FAQ

## For Developers

### Architecture decisions

1. Frontend (FE) and Backend (BE) apps:  
This application is was originally created as a stand-alone application, yet the REST API functionalities allows this project to be part of the backend server for FE applications with different technologies (e.g. React, Vue, etc.).

2. Authentication:  
As a common feature in moderm applications, the authentication process is a natural feature when configuring and creating and manipulate data or other users' access.
3. 

### Stack specifications

- HTML and CSS
- Django and Dj-REST Framework
- JavaScript
- MySQL
- Heroku
- Gunicorn


### Configurations

For customization, there are some places where you can modify the code.

Software development (SW Dev)  
- This includes the configurations for the applications to work correctly when customizing it.

Development operations (DEVOPS)  
- This includes configurations to different deployment heroku pipelines according to the branch (i.e. Main for production, dev for staging/development)

## To-do's
### UI
1. [ Manager view ] Bulk operations
   1. Delete

### Developers
1. Django tests
2. Authentication views
   1. Customized login/out view
   2. Include the logo in the title and change background
3. Creation of product
   1. Auto refresh of the products view
   2. Improvement of the form to create products
   3. 1-clicker to create test products
4. Consolidation of css into files
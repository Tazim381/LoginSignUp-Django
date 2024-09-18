# Django Login/Signup System

This Django project implements a login/signup system using `UserCreationForm`. It ensures that only authenticated users can access specific pages.

## Features

- **User Registration:** Users can create an account using the `UserCreationForm`.
- **User Login:** Users can log in to access protected pages.
- **Protected Pages:** 
  - **Homepage:** Accessible only to authenticated users.
  - **Add Item Page:** Accessible only to authenticated users.
- **Redirection:** Unauthenticated users trying to access protected pages are redirected to the login page.

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <project-directory>

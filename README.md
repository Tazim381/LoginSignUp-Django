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


## Docker
1. Make a DockerFile
2. Make a requirement.txt file
3. Make docker-compose.yml file 
4. start docker with command "sudo systemctl start docker"
5. Build Docker with command "sudo docker-compose build"
6. Run docker with command "sudo docker-compose up"
7. Cheers
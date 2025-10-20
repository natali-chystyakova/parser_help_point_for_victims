# 🆘 Help Points for Victims

**parser_help_point_for_victims** is a Django application that collects and displays humanitarian help points for internally displaced persons on an interactive map.  
The entire project runs inside Docker, including the database and background tasks.

---

## 🚀 Main Features

- Collects and displays help points on a map  
- Built with **Django + PostgreSQL**  
- Fully containerized with **Docker** and **Docker Compose**  
- PostgreSQL running in Docker as an image
- Background task processing with Celery + Redis (RabbitMQ)
- Managed easily via **Makefile** commands  

---

## 🧰 Requirements

- **Docker** and **Docker Compose**  
- **Make** (usually preinstalled on Linux/macOS)  
- **Python 3.11+**  
- **PostgreSQL Docker image:** `postgres:15.2`
- **RabbitMQ Docker image: rabbitmq:3.11.4 (for Celery tasks)
- **Redis==6.4.0(for Celery tasks, used in production)

## ⚙️ Installation & Run
1. Initialize configuration

Copy the example environment configuration:
- make init-config-i-project

2. Run the project in Docker
- make d-project-i-run
 


🧩 Useful Makefile Commands
Command	Description
- make d-project-i-run	Run the full project in Docker (prepare configs and build containers)
- d-run-i-local-dev  Run the  project, PostgreSQL running in Docker as an image 
- make d-run	Run Docker containers without reinitializing configs
- make d-stop	Stop all containers
- make d-project-i-purge	Completely remove containers, images, and volumes
- make migrations	Create new Django migrations
- make migrate	Apply migrations
- make init-dev-i-create-superuser	Create a superuser (admin)

🗂️ Project Structure

parser_help_point_for_victims/
- │
- ├── manage.py
- ├── requirements.txt
- ├── docker-compose.yml
- ├── Makefile
- ├── .env.project
- ├── app/                 # Main Django app
- │   ├── models/
- │   ├── views/
- │   ├── templates/
- │   └── ...
- └── README.md

👩‍💻 Author

Natalia Chystyakova
Junior Python / Django Developer
Dnipro, Ukraine 🇺🇦

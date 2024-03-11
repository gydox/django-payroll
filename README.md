# PayroLite

PayroLite is a simple payroll system designed to streamline payroll management for small to medium-sized businesses. It provides an intuitive user interface for managing employee payroll information and generating payrolls efficiently.

## Features

- Manage employee information such as basic details, salary, and payroll-related information.
- Create and manage monthly payrolls for employees.
- Calculate statutory earnings and deductions automatically.
- Generate payroll reports for easy record-keeping.
- User-friendly interface for easy navigation and operation.

## Technology Stack

- Frontend:
  - Bootstrap
  - jQuery

- Backend:
  - Django

- Database:
  - PostgreSQL

- Web Server:
  - Nginx

- Deployment:
  - Docker
  - Gunicorn

## Installation and Usage

1. Clone the repository:

```bash
git clone https://github.com/gydox/PayroLite.git
```

2. Navigate to the project directory:

```bash
cd PayroLite
```

### Development

1. Navigate to the project directory:

```bash
docker-compose up --build
```

2. Create an admin account

```bash
docker-compose exec web python manage.py createsuperuser
```
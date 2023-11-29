# Smart_Invest

---

## Project Setup

### Clone the Project

```bash
git clone <project_repository_url>
```

### Update the Project

```bash
git pull
```

---

## Virtual Environment

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Configuration

* Create a .env file in the project directory (where manage.py is located).
* Add the following configuration to .env:

```bash
# PostgreSQL Configuration

DB_NAME=projectx
DB_USER=[your_database_username]
DB_PASSWORD=[your_database_password]
DB_HOST=localhost
DB_PORT=5432
```

---

## Database Setup

* Open a terminal window.
* Run the following command to access the PostgreSQL command line client as the postgres user:

```bash
sudo -u postgres psql
```

* Once you are in the PostgreSQL command line client, you should see a prompt that looks like this:

```bash
postgres=#
```

* Now, you can create the projectx database by entering the following SQL command:

```bash
CREATE DATABASE projectx;
```

After running this command, you should see a confirmation message.

* Exit the PostgreSQL command line client by typing:

```bash
\q
```

* Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Now your project is set up and ready to run!

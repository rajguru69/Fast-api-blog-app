# FastAPI Project Setup and Run Readme

## Project Setup

1. **Install Prerequisites:**
   - Install Python: [Download Python](https://www.python.org/downloads/)
   - Install `pip` and `virtualenv`:
     ```bash
     pip install virtualenv
     ```

2. **Clone the Repository:**
   ```bash
    git clone https://github.com/rajguru69/Fast-api-blog-app.git
    cd Fast-api-blog-app```


4. **Set Up Virtual Environment:**
   ```bash
   virtualenv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate```
  
5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt```
  
## Database Migrations with Alembic
  ```bash
  # Create an initial migration
  alembic revision --autogenerate -m "Initial migration"

  # Apply the migration to the database
  alembic upgrade head
```
## Running the FastAPI Application
   ```bash
    uvicorn main:app --reload
```
    
Visit  http://127.0.0.1:8000/docs  in your browser to access the Swagger documentation.


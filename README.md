# Where Should I Go Today? 
A simple Django web application for saving, editing, and managing favorite places.

## How to run the project locally

### 1. Create a virtual environment
Open your terminal in the main project folder and run:  
```
python -m venv .venv
```
### 2. Activate the virtual environment
For Linux and macOS:  
```
source venv/bin/activate
```

For Windows:  
```
venv\Scripts\activate
```

### 3. Install dependencies  
```
pip install -r requirements.txt
```

### 4. Apply migrations  
```
python manage.py migrate
```

### 5. Run the server  
```
python manage.py runserver
```

*The project is now running. Open your browser and go to:*
http://127.0.0.1:8000/
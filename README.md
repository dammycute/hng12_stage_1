# Number Classification API

## Description
This is a public API developed for the HNG12 internship Stage 1 backend task. The API classifies a given number based on its mathematical properties and returns a fun fact about it using the Numbers API.

## Technology Stack
- **Backend:** Django (Python) & Django REST Framework
- **Hosting:** Koyeb 
- **Database:** None (Uses external API for fun facts)
- **CORS Handling:** Enabled using `django-cors-headers`

## API Endpoint
### **Base URL:** `https://your-deployment-url.com/`

### **GET /api/classify-number?number={number}`
#### **Request Example:**
```
GET https://your-deployment-url.com/api/classify-number?number=371
```

#### **Response Format (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Error Response (400 Bad Request)**
```json
{
    "number": "abc",
    "error": true
}
```

## Installation & Setup

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/number-classification-api.git
cd number-classification-api
```

### **2. Create & Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Run Migrations**
```sh
python manage.py migrate
```

### **5. Start the Server**
```sh
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`

## Deployment
The API is deployed on **(Koyeb / Render / Railway)**. Ensure your deployment is accessible.

## Useful Links
- [Numbers API](http://numbersapi.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Your GitHub Repository](https://github.com//number-classification-api)

## License
This project is licensed under the MIT License.


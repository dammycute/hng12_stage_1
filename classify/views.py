import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

def is_armstrong(n: int) -> bool:
    # Armstrong check for positive numbers only
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    return sum(d**len(digits) for d in digits) == abs(n)

def is_prime(n: int) -> bool:
    # Prime check for positive numbers only
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    # Perfect number check for positive numbers only
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == abs(n)

def get_fun_fact(n: int) -> str:
    response = requests.get(f"http://numbersapi.com/{n}/math?json=true")
    if response.status_code == 200:
        return response.json().get("text", "No fun fact available.")
    return "No fun fact available."

@api_view(["GET"])
def classify_number(request):
    number = request.GET.get("number")
    
    if not number or not number.isdigit():
        return JsonResponse({"number": number, "error": True}, status=400)
    
    number = int(number)
    
    # Handle negative numbers
    if number < 0:
        return JsonResponse({"number": number, "error": "Negative numbers are not allowed"}, status=400)
    
    properties = ["odd" if number % 2 else "even"]
    if is_armstrong(number):
        properties.insert(0, "armstrong")

    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(map(int, str(number))),
        "fun_fact": get_fun_fact(number),
    }
    
    return JsonResponse(response_data, status=200)

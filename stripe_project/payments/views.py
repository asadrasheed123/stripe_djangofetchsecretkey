from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>Welcome to Stripe Payment API</h1>")


import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Initialize Stripe with the secret key
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

@csrf_exempt  # Disable CSRF protection for testing purposes
def create_payment_intent(request):
    if request.method == "POST":
        try:
            # Parse JSON request data
            data = json.loads(request.body)
            amount = data.get("amount")  # Amount in cents, e.g., 1000 for $10.00
            currency = data.get("currency", "usd")  # Default to USD

            # Create a PaymentIntent on Stripe
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                automatic_payment_methods={"enabled": True},  # Use automatic payment methods
            )

            # Return the client secret to the client
            return JsonResponse({"clientSecret": payment_intent.client_secret})

        except stripe.error.StripeError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)

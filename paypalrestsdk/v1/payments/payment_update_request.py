# This class was generated on Sat, 07 Apr 2018 16:49:42 UTC by version 0.1.0-dev+2136c8-dirty of Braintree SDK Generator
# payment_update_request.py
# @version 0.1.0-dev+2136c8-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class PaymentUpdateRequest:
    """
    Partially updates a payment, by ID. You can update the amount, shipping address, invoice ID, and custom data. You cannot update a payment after the payment executes. <blockquote><strong>Note: </strong>TPP Clients (Third Party Providers in the context of PSD2 regulation) are restricted from patching amount once authorized.</blockquote>
    """
    def __init__(self, payment_id):
        self.verb = "PATCH"
        self.path = "/v1/payments/payment/{payment_id}?".replace("{payment_id}", quote(str(payment_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, patch_request):
        self.body = patch_request
        return self

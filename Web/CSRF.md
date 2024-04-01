# CSRF

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application.

#### Understanding CSRF

In a typical web application, when a user logs in, the application generates a session token or authentication cookie to keep track of the user's session. This token is sent with every subsequent request to the server to authenticate the user. However, web browsers automatically include cookies associated with a particular domain with every request made to that domain, regardless of the source of the request. This includes requests initiated by JavaScript code running on a webpage. CSRF takes advantage of this behavior by tricking a user's browser into sending authenticated requests to a web application without the user's knowledge or consent.

#### Exploiting CSRF

The attacker creates a malicious webpage or injects malicious code into a legitimate webpage that the victim visits. This webpage contains hidden requests or forms targeting the vulnerable web application. When the victim visits the malicious webpage, their browser automatically executes the embedded code, sending requests to the vulnerable web application.

Since the victim is already authenticated with the web application (e.g., logged in), the browser includes the authentication cookies with the malicious requests, making them appear legitimate to the server. As a result, the vulnerable web application processes the malicious requests as if they were initiated by the legitimate user, potentially leading to unauthorized actions such as changing account settings, making transactions, or accessing sensitive data.

#### Preventing CSRF

To mitigate CSRF attacks, web applications implement various countermeasures, including

1. **CSRF tokens:** Generating unique tokens for each session or request and validating them with every request to ensure that the request originated from the legitimate user.

2. **SameSite cookies**: Using the SameSite attribute for cookies to restrict when they are sent with cross-origin requests, reducing the risk of CSRF attacks.

3. **Referrer checks**: Verifying the Referrer header in incoming requests to ensure that they originate from the same domain as the web application.

4. **Implementing secure coding practices:** Following security best practices and using frameworks with built-in CSRF protection mechanisms, such as Django's CSRF middleware.

# Exploit Example

Consider the following Django view function that handles a sensitive action, such as transferring funds from one account to another,

```Python
from django.shortcuts import render
from django.http import HttpResponse

def transfer_funds(request):
    if request.method == 'POST':
        # Assume 'from_account' and 'to_account' are provided in the request POST data
        from_account = request.POST.get('from_account')
        to_account = request.POST.get('to_account')
        
        # Perform the funds transfer (simplified for demonstration purposes)
        # This is where the sensitive action occurs
        # In a real application, you would validate the request and handle errors appropriately
        # For simplicity, we assume the transfer is successful
        return HttpResponse('Funds transferred successfully!')
    else:
        # Render the form for initiating the transfer
        return render(request, 'transfer_form.html')
```

This view function handles a `POST` request to transfer funds from one account to another. It extracts the source and destination account information from the request `POST` data and performs the transfer.

Now, let's say the corresponding HTML template `transfer_form.html` looks like this,

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transfer Funds</title>
</head>
<body>
    <h1>Transfer Funds</h1>
    <form action="/transfer_funds/" method="post">
        <label for="from_account">From Account:</label>
        <input type="text" id="from_account" name="from_account"><br><br>
        <label for="to_account">To Account:</label>
        <input type="text" id="to_account" name="to_account"><br><br>
        <input type="submit" value="Transfer">
    </form>
</body>
</html>
```

This form allows users to input the source and destination account information for the funds transfer.

Now, let's consider how this code can be vulnerable to CSRF attacks:

#### 1. Attack Scenario

Suppose an attacker hosts a malicious website and embeds an invisible form within it. This form targets the `transfer_funds `endpoint on the victim's website. When a victim visits the attacker's website (possibly by clicking a link sent via email or visiting a compromised webpage), the invisible form automatically submits a `POST` request to the victim's `transfer_funds` endpoint, transferring funds from the victim's account to the attacker's account.

Since the victim is already authenticated in the victim's website (e.g., they are logged in), the browser automatically includes the session cookies with the request, making it appear legitimate to the victim's server.

#### 2. Exploiting the Vulnerability

The attacker's malicious form might look something like this,

```HTML
<form action="https://victimwebsite.com/transfer_funds/" method="post" style="display:none;">
    <input type="hidden" name="from_account" value="victim_account">
    <input type="hidden" name="to_account" value="attacker_account">
    <!-- Additional hidden fields may be included as needed -->
    <!-- The CSRF token is not included here, making the request vulnerable to CSRF attacks -->
</form>
```

When the victim's browser visits the attacker's website, the invisible form is submitted automatically, triggering the funds transfer without the victim's knowledge or consent.

#### 3. Mitigating the Vulnerability

To mitigate CSRF attacks, the server should include a CSRF token in the form, ensuring that the request originates from a trusted source. Django provides built-in CSRF protection, which includes generating and validating CSRF tokens automatically. By including `{% csrf_token %}` in the form template, Django automatically includes a CSRF token in the form response. Additionally, Django's CSRF middleware verifies the CSRF token in incoming `POST` requests, protecting against CSRF attacks.

# Django Handling of CSRF

Django, CSRF protection can be handled automatically through middleware without explicitly embedding CSRF tokens in forms in certain cases, especially when using Django's built-in CSRF protection middleware and when making AJAX requests with libraries like Axios.

When Django renders a template with a form, it automatically includes a CSRF token using the `{% csrf_token %}` template tag. This ensures that the CSRF token is included in the form submission and subsequently sent with the request. However, with modern frontend frameworks like React, the frontend and backend are often decoupled, and you may not be using Django's template rendering for forms. In such cases, when making AJAX requests, you still need to ensure CSRF protection.

Django provides the `CSRF_TRUSTED_ORIGINS` setting, which allows you to specify trusted origins from which requests are exempted from CSRF protection. This setting is particularly useful in scenarios where you have separate frontend and backend applications and you need to make cross-origin requests.

In traditional Django applications where forms are rendered server-side, Django automatically includes CSRF tokens in forms. In decoupled applications with separate frontend frameworks like React, you can either include the CSRF token manually or exempt trusted origins from CSRF protection using `CSRF_TRUSTED_ORIGINS`.
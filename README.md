# Seller Onboarding Form

This web application is a simple and user-friendly seller onboarding form that allows gift card sellers to provide their store details, gift card balance, selling price, network preference, and other necessary information. The form uses the Flask framework, and the results are stored in memory.

## Files

- `app.py`: The main Flask application file that handles routes and form processing.
- `form.html`: The HTML template for the seller onboarding form, which includes client-side JavaScript for form validation and navigation between form questions.
- `thank_you.html`: The HTML template with a thank you message for a submitted form, with a link to start a new entry or view the results table.
- `results.html`: The HTML template to show the table of results with proper bootstrap formatting based off stored local storage.

## Features

- Form validation with custom error messages.
- Incremental form navigation with back and next buttons.
- Saving form data in local storage to allow users to continue from where they left off.
- User-friendly interface with Bootstrap styling.
- Results page to view submitted forms.

## Running the Application

To run the application, follow these steps:

1. Install the required dependencies (Flask):
```
pip install flask
```
2. Run the `app.py` file:
```
python app.py
```
3. Access the application in your web browser at `http://localhost:5001`.

Alternatively, can access hosted site at https://armantark.pythonanywhere.com

## Contributing

Feel free to submit pull requests or open issues to contribute to this project.

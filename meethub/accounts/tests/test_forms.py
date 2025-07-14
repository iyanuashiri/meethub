from django.test import TestCase
from django import forms
from meethub.accounts.models import Account
from meethub.accounts.forms import SignUpForm
from meethub.profile.models import Profile

class SignUpFormTest(TestCase):
    # Tests that the form correctly validates valid input data.
    def test_valid_form_data(self):
        form_data = {
            'first_name': 'firstnametest',
            'last_name': 'lastnametest',
            'email': 'firstlasttest@testing.com',
            'password1': 'PASSWORDwfehrrein2',
            'password2': "PASSWORDwfehrrein2"
        }

        form  = SignUpForm(data = form_data) #Creates form with provided form credentials
        print("Form errors:", form.errors)
        self.assertTrue(form.is_valid())  #Check validity of form data

    # Tests that the form is invalid when the provided passwords do not match.
    def test_invalid_form_data_password_mismatched(self):
        form_data = {
            'first_name': 'firstnametest',
            'last_name': 'lastnametest',
            'email': 'firstlasttest23@testing.com',
            'password1': 'PASSWORDwfehrrein2',
            'password2': "PASSWORDwfehrrein3"
        }

        form = SignUpForm(data = form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    # Checks if a user already exists with the given email address.
    def test_invalid_form_data_existing_email(self):
        self.existing_email = 'firstlasttest342@testing.com'
        Account.objects.create_user(       #Created account with pre-existing email id.
            email = self.existing_email,   
            password = 'ExistingPassword123',
            first_name = 'first',
            last_name = 'last'
        )
        print("All accounts:", list(Account.objects.values('email')))

        form_data = {
            'first_name': 'firstnametest',
            'last_name': 'lastnametest',
            'email': self.existing_email,
            'password1': 'NewStrongPassword1',
            'password2': "NewStrongPassword1"
        }

        form = SignUpForm(data = form_data)
        print("Form error: ", form.errors)
        print("Is valid:", form.is_valid())   #checking validity of the function
        print("Form errors:", form.errors)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
    
    # This verifies that calling save() on SignUpForm creates a new Account and an associated Profile.
    def test_signuoform_save_creates_user_profile_and_action(self):
        form_data = {
            'first_name': 'firstnametest',
            'last_name': 'lastnametest',
            'email': 'firstlasttest342@testing.com',
            'password1': 'PASSWORDwfehrrein2',
            'password2': "PASSWORDwfehrrein2"
        }

        form = SignUpForm(data = form_data)
        self.assertTrue(form.is_valid())
        
        user = form.save()

        self.assertIsInstance(user, Account)
        self.assertEqual(user.email, 'firstlasttest342@testing.com')
        self.assertTrue(user.check_password('PASSWORDwfehrrein2'))

        self.assertTrue(Profile.objects.filter(user=user).exists())


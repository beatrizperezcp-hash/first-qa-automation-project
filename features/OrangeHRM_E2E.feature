Feature: E2E OrangeHRM

  Scenario: E2E OrangeHRM
    Given Open the following url opensource-demo.orangehrmlive.com/web/index.php/auth/login
    When Fill the following fields
      | field    | value        |
      | Username | username_key |
    Then Click on button 'Login'
    Then Validate invalid message 'Required'
    When Fill the following fields
      | field    | value        |
      | Username | username_key |
      | Password | password_key |
    Then Click on button 'Login'
    Then Validate alert message 'Invalid credentials'
    When Fill the following fields
      | field    | value    |
      | Username | Admin    |
      | Password | admin123 |
    Then Click on button 'Login'
    Then Verify the following header title 'Dashboard'
    Then Navigate to the following section 'PIM'
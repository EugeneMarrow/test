Feature: Testcase
 
 Scenario: Testcase
		Given  User goes to landing page
		When   User fills subscription email with non email input and presses Sign in button
		Then   User should see the warning about agreement
		When   User check Terms and Conditions and presses Sign in button
		Then   User should see the popup about invalid email
		When   User fills subscription email with valid email and presses Sign in button
		Then   User should see instagram login page
		When   User logs in with Instagram
		Then   User sees subscription form
		When   User presses submit
		Then   User gets message about required fields
		When   User fills all required fields and submit but zipcode field is filled with invalid data
		Then   User gets error
		When   User chooses concern from list in step 2
		Then   User should see chosen option highlighted
		When   User fills all required fields with valid data and press submit
		Then   User gets sharing links
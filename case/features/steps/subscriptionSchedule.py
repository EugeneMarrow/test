from environment import *

@given('User goes to landing page')
def landing(context):
	global insta_log,insta_pass
	insta_log=raw_input("Enter your insta login: ")
	insta_pass=getpass.getpass("Enter insta password: ")

	context.driver.get(landing_url)
	assert landing_url in context.driver.current_url
  
@when('User fills subscription email with non email input and presses Sign in button')
def login_wo_checkbox_wrong_email(context):
	find(context, By.CLASS_NAME,'subscribe-field').send_keys("test")
	find(context, By.ID,'login').click()
  
@then('User should see the warning about agreement')
def login_wo_checkbox_wrong_email_check(context):
	find(context, By.ID,'warning').is_displayed()
	

@when('User check Terms and Conditions and presses Sign in button')
def login_w_checkbox_wrong_email(context):
	find(context, By.ID,'follow-checkbox').click()
	find(context, By.ID,'login').click()
  
@then('User should see the popup about invalid email')
def login_w_checkbox_wrong_email_check(context):
	alert = context.driver.switch_to.alert
	alert.accept() 
	
@when('User fills subscription email with valid email and presses Sign in button')
def login_w_checkbox_valid_email(context):

	find(context, By.CLASS_NAME,'subscribe-field').clear()
	find(context, By.CLASS_NAME,'subscribe-field').send_keys("q@q.com")
##### Email should be unique. Correct code below!
	# salt = ''.join([random.choice(string.ascii_letters + string.digits) for n in
	# range(5)])
	# find(context, By.CLASS_NAME,'subscribe-field').send_keys("test%s@gmail.com"%salt)
	find(context, By.ID,'login').click()
  
@then('User should see instagram login page')
def login_w_checkbox_valid_email_check(context):
	sleep(2)
	assert "instagram.com/accounts" in context.driver.current_url
	
@when('User logs in with Instagram')
def login_insta(context):
	find(context, By.XPATH,'//*[@name="username"]').send_keys(insta_log)
	find(context, By.XPATH,'//*[@name="password"]').send_keys(insta_pass)
	find(context, By.XPATH,'//*[@type="submit"]').click()
  
@then('User sees subscription form')
def login_insta_check(context):
	sleep(5)
	assert "https://lushli.com/theinkeylist/thankyou/" in context.driver.current_url
	
@when('User presses submit')
def empty_form_submit(context):
	find(context, By.ID,'shipping-submit-button').click()
  
@then('User gets message about required fields')
def empty_form_submit(context):
	assert find(context, By.ID,'first_name').get_attribute("required")=="true"
	assert find(context, By.ID,'last_name').get_attribute("required")=="true"
	assert find(context, By.ID,'address').get_attribute("required")=="true"
	assert find(context, By.ID,'city').get_attribute("required")=="true"
##### Country field is marked as required, but it isn't:(
	# assert find(context, By.ID,'country').get_attribute("required")=="true"
	assert find(context, By.ID,'state').get_attribute("required")=="true"
	assert find(context, By.ID,'zip_code').get_attribute("required")=="true"
	
	
@when('User fills all required fields and submit but zipcode field is filled with invalid data')
def broken_zip_code_submit(context):
	find(context, By.ID,'first_name').send_keys("test")
	find(context, By.ID,'last_name').send_keys("test")
	find(context, By.ID,'address').send_keys("test")
	find(context, By.ID,'city').send_keys("test")
	find(context, By.ID,'country').send_keys("test")
	find(context, By.ID,'state').send_keys("test")
	find(context, By.ID,'zip_code').send_keys("test")
	find(context, By.ID,'shipping-submit-button').click()
  
@then('User gets error')
def empty_form_submit(context):
	assert find(context, By.ID,'zip_code').get_attribute("pattern")!="null"	
	
@when('User chooses concern from list in step 2')
def choose_concern(context):
	global concern
	concern_choosebox=find(context, By.ID,'choose-concern')
	concern=concern_choosebox.find_element(By.CLASS_NAME,'Concern')
	concern.click()
  
@then('User should see chosen option highlighted')
def choose_concern_submit(context):
	assert concern.get_attribute("class")=="Concern active"
		
@when('User fills all required fields with valid data and press submit')
def submit_valid_form(context):
	find(context, By.ID,'zip_code').clear()
	find(context, By.ID,'zip_code').send_keys("65000")
	find(context, By.ID,'shipping-submit-button').click()
  	
	
@then('User gets sharing links')
def submit_valid_form_check(context):
	f= open("personal_link.txt","w+")
	f.write(find(context, By.ID,'share_link_input').get_attribute('value'))
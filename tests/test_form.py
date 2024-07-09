from pages.form_page import RegistrationForm


def test_complete_todo():
    registration_form = RegistrationForm()
    registration_form.open()
    registration_form.type_first_name('Vadim')
    registration_form.type_last_name('Korolev')
    registration_form.type_email('v@gmail.com')
    registration_form.click_gender()
    registration_form.type_phone('7915141114')
    registration_form.type_birthday()
    registration_form.type_subjects('Physics')
    registration_form.click_hobbies()
    registration_form.upload_photo('img.jpg')
    registration_form.type_address('Test, 65')
    registration_form.type_state('NCR')
    registration_form.type_city('Delhi')
    registration_form.press_submit()
    registration_form.should_text('Thanks for submitting the form')
    registration_form.should_exact_text('Vadim Korolev',
                                        'v@gmail.com',
                                        'Male',
                                        '7915141114',
                                        '27 December,1998',
                                        'Physics',
                                        'Sports, Reading',
                                        'img.jpg',
                                        'Test, 65',
                                        'NCR Delhi')

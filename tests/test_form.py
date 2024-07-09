import os

from selene import browser, have, be


def test_complete_todo():
    browser.open('automation-practice-form')

    browser.element('#firstName').type('Vadim')
    browser.element('#lastName').type('Korolev')
    browser.element('#userEmail').type('v@gmail.com')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('7915141114')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value = "11"]').click()
    browser.element('.react-datepicker__year-select').element('[value = "1998"]').click()
    browser.element('.react-datepicker__day--027').click()
    browser.element('#subjectsInput').type('ph').press_enter()
    browser.element('#subjectsInput').type('b').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath("img.jpg"))
    browser.element('#currentAddress').type('Test, 65')
    browser.element('#react-select-3-input').type("NC").press_enter()
    browser.element('#react-select-4-input').type("De").press_enter()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(be.present)
    browser.element('.table').all('td').even.should(have.exact_texts
                                                    ('Vadim Korolev', 'v@gmail.com', 'Other',
                                                     '7915141114', '27 December,1998', 'Physics, Biology',
                                                     'Sports, Reading, Music', 'img.jpg', 'Test, 65',
                                                     'NCR Delhi'))

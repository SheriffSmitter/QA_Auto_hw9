from models.application import app


def test_complete_todo():
    app.left_panel.open()
    app.left_panel.type_first_name('Vadim')
    app.left_panel.type_last_name('Korolev')
    app.left_panel.type_email('v@gmail.com')
    app.left_panel.click_gender()
    app.left_panel.type_phone('7915141114')
    app.left_panel.type_birthday()
    app.left_panel.type_subjects('Physics')
    app.left_panel.click_hobbies()
    app.left_panel.upload_photo('img.jpg')
    app.left_panel.type_address('Test, 65')
    app.left_panel.type_state('NCR')
    app.left_panel.type_city('Delhi')
    app.left_panel.press_submit()
    app.left_panel.should_text('Thanks for submitting the form')
    app.left_panel.should_exact_text('Vadim Korolev', 'v@gmail.com', 'Other', '7915141114',
                                     '27 December,1998', 'Physics','Sports, Reading',
                                     'img.jpg', 'Test, 65','NCR Delhi')

from test_data.user import User
from pages.form_page import RegistrationForm


def test_complete_todo():
    form_page = RegistrationForm()
    man = User(first_name='Vadim',
               last_name='Korolev',
               email='v@gmail.com',
               gender='Male',
               phone='7915141114',
               birthday='27 December,1998',
               subject='Physics',
               photo='img.jpg',
               hobbies='Sports, Reading',
               address='Test, 65',
               state='NCR',
               city='Delhi')
    form_page.open()
    form_page.register(man)
    form_page.should_exact_text(man)

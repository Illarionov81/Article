from behave import given, when, then


@given(u'Я открыл страницу "Входа"')
def open_login_page(context):
    context.browser.get('http://localhost:8000/accounts/login/')


@when(u'Я ввожу текст "{text}" в поле "{name}"')
def enter_text(context, text, name):
    context.browser.find_element_by_name(name).send_keys(text)


@when(u'Я отправляю форму')
def submit_form(context):
    context.browser.find_element_by_id('submit').click()


@when("Я ввщжу следующий текст в следующие поля")
def step_impl(context):
    for row in context.table:
        enter_text(context, row['text'], row['field'])


@then("Я должен видеть кнопку delete")
def see_button(context):
    delete_button = context.browser.find_elements_by_class_name('btn-danger')
    assert delete_button


@then("Я не должен видеть кнопку delete")
def step_impl(context):
    delete_button = context.browser.find_elements_by_class_name('btn-danger')
    assert not delete_button

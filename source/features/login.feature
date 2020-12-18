Feature: Вход

    Scenario: Вход под админом
    Given Я открыл страницу "Входа"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "article_admin" в поле "password"
    And Я отправляю форму
    Then Я должен видеть кнопку delete

  Scenario: Вход обычного пользователя
    Given Я открыл страницу "Входа"
    When Я ввщжу следующий текст в следующие поля
        | text | field    |
        | my    | username |
        | myy    | password |
    And  Я отправляю форму
    Then Я не должен видеть кнопку delete

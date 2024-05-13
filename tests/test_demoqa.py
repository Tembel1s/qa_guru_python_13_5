from selene import browser, have
import os


def test_registration_form():
    browser.open("/automation-practice-form")

    # Заполнение поелй Name, Last Name, Email, Gender

    browser.element("#firstName").type("Sergei")
    browser.element("#lastName").type("Melnikov")
    browser.element("#userEmail").type("Sergei@Melnikov.com")
    browser.element('[for="gender-radio-1"]').click()

    # Выбор даты рождения в календаре

    browser.element("#userNumber").type("4815162342")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element(
        'option[value="8"]'
    ).click()
    browser.element(".react-datepicker__year-select").element(
        'option[value="1991"]'
    ).click()
    browser.element(".react-datepicker__day--029").click()

    # Заполнения поля Subjects (по полному вводу и с помощью автоподсказки)

    browser.element("#subjectsInput").type("Computer Science").press_enter()
    browser.element("#subjectsInput").type("C")
    browser.element("#react-select-2-option-0").click()
    browser.element('[for="hobbies-checkbox-1"]').click()

    # Загрузка фото

    browser.element("#uploadPicture").send_keys(
        os.path.abspath("./images/2024-05-12 22.04.05.jpg")
    )

    # Заполнение полей Current Address, State and City
    browser.element("#currentAddress").type("Novi Sad")
    browser.element("#state").click().element("#react-select-3-option-1").click()
    browser.element("#city").click().element("#react-select-4-option-0").click()

    # Отправка формы

    browser.element("#submit").press_enter()

    # Проверка корректности отображаемых данных
    browser.element(".modal-content").element("table").all("tr").all("td").even.should(
        have.exact_texts(
            (
                "Sergei Melnikov",
                "Sergei@Melnikov.com",
                "Male",
                "4815162342",
                "29 September,1991",
                "Computer Science, Physics",
                "Sports",
                "2024-05-12 22.04.05.jpg",
                "Novi Sad",
                "Uttar Pradesh Agra",
            )
        )
    )

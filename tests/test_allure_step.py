import allure
from selene import browser, by, be



def test_steps():
    with allure.step("Открывам GITHUB"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element("[data-target='qbsearch-input.inputButtonText']").click()
        browser.element("#query-builder-test").type("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step("Открываем проект"):
        browser.element('a[href="/eroshenkoam/allure-example"]').click()

    with allure.step("Открываем lssue"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем номер"):
        browser.element(by.partial_text("84")).should(be.visible)
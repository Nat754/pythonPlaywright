import pytest


# @pytest.mark.skip_browser("firefox")  # Пропустить тест браузером
# @pytest.mark.only_browser("chromium")  # Запуск в определенном браузере
def test_add_todo(page):
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")


"""
--headed - playwright по умолчанию запускает браузеры в безголовом(headless) режиме. 
При использовании данного аргумента, запуск теста произойдет в режиме headed.

--browser - запускать тесты в другом браузере chromium, firefox или webkit. 
Может быть указано несколько раз (по умолчанию: chromium):
pytest --headed --browser webkit --browser firefox

--browser-channel - возможно вам потребуется запускать тесты в браузерах  Chrome и Edge,
 установленных на вашем компьютере:
pytest --browser-channel=msedge --headed

--slowmo - используется  для замедления выполнения теста на указанное количество миллисекунд:
pytest --slowmo 1000

--device - можно использовать для имитации поведения браузера для определенного устройства
В качества параметра передайте поддерживаемый девайс:
 pytest --device="iPhone 13 Mini"
 
Список поддерживаемых девайсов вы сможете  посмотреть 
https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json
"""
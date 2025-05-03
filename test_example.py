from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    # Запускаем браузер
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    try:
        # 1. Открываем веб-страницу
        page.goto("https://example.com")
        
        # 2. Проверяем, что заголовок страницы содержит слово "Example"
        expect(page).to_have_title("Example Domain")
        print("Заголовок страницы содержит 'Example'")
        
        # 3. Находим элемент с текстом "More information" и кликаем по нему
        link = page.get_by_text("More information")
        expect(link).to_be_visible()
        link.click()
        
        # 4. Проверяем перенаправление на нужный URL
        expect(page).to_have_url("https://www.iana.org/domains/example")
        print("Перенаправление на iana.org прошло успешно")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрываем браузер
        browser.close()
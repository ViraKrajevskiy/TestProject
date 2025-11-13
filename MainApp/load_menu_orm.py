from MainApp.models import MenuItem

def run():

    MenuItem.objects.all().delete()


    main_menu = [
        {'name': 'Главная', 'named_url': 'home', 'menu_name': 'main_menu', 'order': 1},
        {'name': 'О компании', 'named_url': 'about', 'menu_name': 'main_menu', 'order': 2},
        {'name': 'Услуги', 'named_url': 'services', 'menu_name': 'main_menu', 'order': 3},
        {'name': 'Продукты', 'named_url': 'products', 'menu_name': 'main_menu', 'order': 4},
        {'name': 'Блог', 'named_url': 'blog', 'menu_name': 'main_menu', 'order': 5},
        {'name': 'Контакты', 'named_url': 'contact', 'menu_name': 'main_menu', 'order': 6},
    ]

    menu_objects = {}
    for item in main_menu:
        obj = MenuItem.objects.create(**item)
        menu_objects[item['name']] = obj


    services_children = [
        {'name': 'Веб-разработка', 'named_url': 'web_development', 'menu_name': 'main_menu', 'order': 1, 'parent': menu_objects['Услуги']},
        {'name': 'Мобильные приложения', 'named_url': 'mobile_apps', 'menu_name': 'main_menu', 'order': 2, 'parent': menu_objects['Услуги']},
        {'name': 'UI/UX Дизайн', 'explicit_url': '/services/design/', 'menu_name': 'main_menu', 'order': 3, 'parent': menu_objects['Услуги']},
        {'name': 'Техническая поддержка', 'explicit_url': '/services/support/', 'menu_name': 'main_menu', 'order': 4, 'parent': menu_objects['Услуги']},
    ]

    for item in services_children:
        obj = MenuItem.objects.create(**item)
        menu_objects[item['name']] = obj


    web_dev_children = [
        {'name': 'Интернет-магазины', 'explicit_url': '/services/web-development/ecommerce/', 'menu_name': 'main_menu', 'order': 1, 'parent': menu_objects['Веб-разработка']},
        {'name': 'Корпоративные сайты', 'explicit_url': '/services/web-development/corporate/', 'menu_name': 'main_menu', 'order': 2, 'parent': menu_objects['Веб-разработка']},
        {'name': 'Веб-приложения', 'explicit_url': '/services/web-development/webapps/', 'menu_name': 'main_menu', 'order': 3, 'parent': menu_objects['Веб-разработка']},
    ]

    for item in web_dev_children:
        obj = MenuItem.objects.create(**item)
        menu_objects[item['name']] = obj


    mobile_children = [
        {'name': 'iOS приложения', 'explicit_url': '/services/mobile-apps/ios/', 'menu_name': 'main_menu', 'order': 1, 'parent': menu_objects['Мобильные приложения']},
        {'name': 'Android приложения', 'explicit_url': '/services/mobile-apps/android/', 'menu_name': 'main_menu', 'order': 2, 'parent': menu_objects['Мобильные приложения']},
        {'name': 'Кроссплатформенные', 'explicit_url': '/services/mobile-apps/crossplatform/', 'menu_name': 'main_menu', 'order': 3, 'parent': menu_objects['Мобильные приложения']},
    ]

    for item in mobile_children:
        MenuItem.objects.create(**item)

    
    footer_menu = [
        {'name': 'Политика конфиденциальности', 'explicit_url': '/privacy/', 'menu_name': 'footer_menu', 'order': 1},
        {'name': 'Условия использования', 'explicit_url': '/terms/', 'menu_name': 'footer_menu', 'order': 2},
        {'name': 'Карта сайта', 'named_url': 'home', 'menu_name': 'footer_menu', 'order': 3},
        {'name': 'Документация', 'explicit_url': '/docs/', 'menu_name': 'footer_menu', 'order': 4},
        {'name': 'Помощь', 'explicit_url': '/help/', 'menu_name': 'footer_menu', 'order': 5},
    ]

    for item in footer_menu:
        MenuItem.objects.create(**item)

    print("✅ Меню успешно добавлено через ORM!")

from django import template
from django.urls import resolve, Resolver404
from ..models import MenuItem
from collections import defaultdict

register = template.Library()

@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    try:
        # ОДИН запрос к БД для получения всех пунктов меню
        menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

        if not menu_items.exists():
            return {'menu_structure': [], 'menu_name': menu_name}

        # Строим дерево меню
        menu_tree = []
        children_dict = defaultdict(list)

        for item in menu_items:
            if item.parent_id:
                children_dict[item.parent_id].append(item)
            else:
                menu_tree.append(item)

        # Находим активный пункт меню по текущему URL
        active_item = None
        for item in menu_items:
            if item.get_url() == current_path:
                active_item = item
                break

        # Если не нашли по точному совпадению, пробуем по named URL
        if not active_item:
            try:
                current_view = resolve(current_path)
                for item in menu_items:
                    if item.named_url:
                        try:
                            if resolve(item.get_url()).view_name == current_view.view_name:
                                active_item = item
                                break
                        except Resolver404:
                            continue
            except Resolver404:
                pass

        # Определяем развернутые пункты
        expanded_items = set()
        if active_item:
            # Добавляем активный элемент и всех его родителей
            current = active_item
            while current:
                expanded_items.add(current.id)
                current = current.parent

            # Добавляем детей первого уровня активного элемента
            if active_item.id in children_dict:
                for child in children_dict[active_item.id]:
                    expanded_items.add(child.id)

        # Рекурсивно строим структуру меню
        def build_menu_structure(items, level=0):
            result = []
            for item in sorted(items, key=lambda x: x.order):
                item_data = {
                    'item': item,
                    'children': [],
                    'is_active': item == active_item,
                    'is_expanded': item.id in expanded_items,
                    'level': level
                }
                if item.id in children_dict and item.id in expanded_items:
                    item_data['children'] = build_menu_structure(children_dict[item.id], level + 1)
                result.append(item_data)
            return result

        menu_structure = build_menu_structure(menu_tree)

        return {
            'menu_structure': menu_structure,
            'menu_name': menu_name
        }

    except Exception as e:
        print(f"Error drawing menu {menu_name}: {e}")
        return {'menu_structure': [], 'menu_name': menu_name}
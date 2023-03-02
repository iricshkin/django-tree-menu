def filter_item_id_list(parent, main_item: list, filter_item_id: list) -> list:
    """Метод вовзращает список id "родителей"."""
    items_id = []
    while parent:
        items_id.append(parent.id)
        parent = parent.parent
    else:
        for item in main_item:
            if item['id'] == filter_item_id:
                items_id.append(filter_item_id)
    return items_id


def child(items_values, cur_id: int, filter_item_id_list: list) -> list:
    """Метод возвращает список "детей" - вложенные элементы в меню."""
    lst_items = [it for it in items_values.filter(parent_id=cur_id)]
    for item in lst_items:
        if item['id'] in filter_item_id_list:
            item['childs'] = child(
                items_values, item['id'], filter_item_id_list
            )
    return lst_items


def additional_menu(context: dict, menu: str, querystring_args: list):
    """
    Получение дополнительного меню,
    для выводы нескольких меню на одной странице.
    """
    for key_menu in context['request'].GET:
        if key_menu != menu:
            querystring_args.append(
                key_menu + '=' + context['request'].GET[key_menu]
            )
    return ('&').join(querystring_args)

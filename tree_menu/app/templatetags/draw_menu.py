from django import template

from app.models import Item
from app.templatetags.utils import additional_menu, child, filter_item_id_list

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context: dict, menu) -> dict:
    """Метод для построения древовидного меню."""

    try:
        filter_item_id = int(context['request'].GET[menu])
        items = Item.objects.filter(menu__name=menu)
        items_values = items.values()
        main_item = [item for item in items_values.filter(parent=None)]
        filter_items_id_list = filter_item_id_list(
            items.get(id=filter_item_id), main_item, filter_item_id
        )

        for item in main_item:
            if item['id'] in filter_items_id_list:
                item['childs'] = child(
                    items_values, item['id'], filter_items_id_list
                )
        item_dict = {'items': main_item}

    except Exception:
        item_dict = {
            'items': [
                item
                for item in Item.objects.filter(
                    menu__name=menu, parent=None
                ).values()
            ]
        }

    item_dict['menu'] = menu
    item_dict['additional_menu'] = additional_menu(context, menu, [])
    return item_dict

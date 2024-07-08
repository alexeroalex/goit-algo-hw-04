"""
    Додає контакт до книги.

    Параметри:
    args (list[str]): Список з іменем та номером бажаного контакту.

    Повертає:
    str: Результат додавання контакту.
    """


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


"""
    Змінює номер телефону контакту у книзі.

    Параметри:
    args (list[str]): Список з іменем та номером бажаного контакту.

    Повертає:
    str: Результат зміни контакту або результат невдачі.
    """


def change_contact(args, contacts):
    if args[0] in contacts:
        contacts.update({args[0]: args[1]})
        return "Contact changed"
    else:
        return "Contact not found"


"""
    "Телефонує" заданому контакту з книги.

    Параметри:
    args (list[str]): Список з іменем бажаного контакту.

    Повертає:
    str: Результат телефонування контакту або результат невдачі.
    """


def phone_contact(args, contacts):
    if args[0] in contacts:
        return contacts[args[0]]
    else:
        return "Contact not found"


"""
    Відображає номер телефону контакту у книзі.

    Параметри:
    args (list[str]): Список з іменем бажаного контакту.

    Повертає:
    str: Рядок з ім'ям та номером контакту або результат невдачі.
    """


def show_contact(args, contacts):
    if args[0] in contacts:
        return f"{args[0]}'s phone number: {contacts[args[0]]}"
    else:
        return "Contact not found"


"""
    Видаляє контакт у книзі.

    Параметри:
    args (list[str]): Список з іменем бажаного контакту.

    Повертає:
    str: Результат видалення контакту або результат невдачі.
    """


def delete_contact(args, contacts):
    if args[0] in contacts:
        del contacts[args[0]]
        return "Contact deleted"
    else:
        return "Contact not found"

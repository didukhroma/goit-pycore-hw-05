from .input_err import input_error

@input_error
def add_contact(args:list,contacts:dict)->str:
    name,phone = args
    if name in contacts:
        return f"Contact {name.capitalize()} already exists."
    contacts[name]=phone
    return f"Contact {name.capitalize()} added."

@input_error
def update_contact(args:list,contacts:dict)->str:
    name,phone = args
    if name not in contacts:
        raise KeyError
    contacts[name]=phone
    return f"Contact {name.capitalize()} updated."

@input_error
def show_all(contacts:dict)->str:    
    if not len(contacts):
        return "List is empty.Please add contacts"   

    return "".join([f"Name: {name.capitalize()} --- Phone number: {phone}\n" for name,phone in contacts.items()])
  

@input_error
def show_phone(args:list,contacts:dict)->str:
    name = args[0]
    return f"Name: {name.capitalize()} --- Phone number: {contacts[name]}"
    

    

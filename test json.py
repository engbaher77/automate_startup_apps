import json


person_dict = {"name": "Bob",
"languages": ["English", "Fench", "Arabic"],
"married": True,
"age": 32
}

layout_dict = {
    "layout":{"programming": ["explorer.exe", "cmd"]}
}

answer = input("do you want to read or write or change?")
#write data
if answer == "write":
    with open('person.txt', 'w') as json_file:
        json.dump(layout_dict, json_file, indent=4, sort_keys=True)

elif answer == "change":
    with open('person.txt', 'r') as f:
        json_data = json.load(f)
        print(json_data)
    obj_tochange = input('Do you wanna change name and language as test?\n')
    if obj_tochange == "yes":
        #name = input('enter new name?')
        #language = input('enter new language?')
        layout = input('enter your new layout?')
        #json_data['name'] = name
        #json_data['languages'] = language
        json_data['layout']['new_layout'] = "hello"
        confirm_change = input('confirm?')
        if confirm_change == "yes":
            with open('person.txt', 'w') as f:
                json.dump(json_data, f, indent=4, sort_keys=True)

            with open('person.txt', 'r') as f:
              json_data = json.load(f)
              print(json_data) 
else:
    with open('person.txt', 'r') as f:
        json_data = json.load(f)
    print(json_data)
    #print(json_data["languages"])

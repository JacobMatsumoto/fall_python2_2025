
def conf_sign_ups(*people, **contacts):
    print("People attending:")
    for person in people:
        print(person)

    print("\nPeople's contact info:")
    for name, info in contacts.items():
        if len(info) == 2 :
            print(
                f"----------------------------------------\n"
                f"Name: {name}\n"
                f"Phone number: {info[0]}\n"
                f"Email: {info[1]}\n"
                f"-----------------------------------------"
            )
        else:
            print(
                f"-----------------------------------------\nName: {name}\nOnly contact via: {info[0]}\n"
                f"-----------------------------------------"
                )


attendies = ("Jim", "Carla", "James")

contact_info = {
    "Jim": ("999-222-1212", "jim@test.com"), 
    "Carla": ("299-233-1222", "carla@gmal.com"), 
    "James": ("444-444-4444")
}


conf_sign_ups(*attendies, **contact_info)

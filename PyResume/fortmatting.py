def get_contact_info(person):
    return f'{person["location"]} | {person["phone"]} | {person["email"]}'


def get_school_info(education):
    return f'{education["name"]}, {education["years"]}'

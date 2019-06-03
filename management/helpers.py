import re


def normalize_objects(objects):
    """
    This method receives a list of objects and return a list of dictionaries
    """
    normalized_objects = []
    for obj in objects:
        data = {}
        for field in obj:
            data[field] = obj[field]
        normalized_objects.append(data)
    return normalized_objects


def validate_email(email):
    email_validation = re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
        email
    )
    return True if email_validation else False
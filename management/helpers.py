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
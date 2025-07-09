def existence_validation(data, categories):
    resp = None
    if data in categories.keys():
        resp = False
    else:
        resp = True

    return resp
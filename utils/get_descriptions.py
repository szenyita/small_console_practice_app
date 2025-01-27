def get_descriptions(cursor_description):
    return [description[0] for description in cursor_description]
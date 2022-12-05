import os


def listdir(data):

    data = {
        'location': data['location'],
        'path': data['path'],
        'listdir': os.listdir(data['path'])
    }

    return data





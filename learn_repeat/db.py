import pickle


def read():
    try:
        with open('../data.pkl', 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return None


def write(data):
    with open('../data.pkl', 'wb') as file:
        pickle.dump(data, file)


def delete():
    pass

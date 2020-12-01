import pickle


class Db:

    def read(self):
        with open('../data.pkl', 'rb') as file:
            data = pickle.load(file)
        return data

    def write(self, data):
        with open('../data.pkl', 'wb') as file:
            pickle.dump(data, file)

    def delete(self):
        pass

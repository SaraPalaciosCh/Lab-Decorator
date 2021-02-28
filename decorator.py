import requests


def get_advice(function):
    def wrapper(slip_id):
        encoding = 'utf-8'
        if slip_id in range(1,200):
            response = requests.get(f"https://api.adviceslip.com/advice/{slip_id}")
            print(
                response.content.decode(encoding)
            )
        else:
            return function()
    return wrapper

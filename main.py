from decorator import get_advice


@get_advice
def advice(id):
    return "Advice not found"


print(advice(50))

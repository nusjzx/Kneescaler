def float_operation(event, context):
    result = 0.0
    for i in range(1000000):
        result += i / 3.14159265359
    return {"result": result}

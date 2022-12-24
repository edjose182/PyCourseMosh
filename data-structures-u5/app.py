first = {"x": 1}

second = {"x": 10, "y": 2}

combined = {**first, **second, "z": 1}

print(**second)
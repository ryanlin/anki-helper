

def retry(function, error_type: str):
    # DOES NOT WORK, DO NOT USE
    while True:
        try:
            return function()
        except Exception as e:
            print(e)
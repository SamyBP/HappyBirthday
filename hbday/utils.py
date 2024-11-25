from datetime import datetime


def logs(message: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{current_time}] {message}")
            return func(*args, **kwargs)

        return wrapper

    return decorator

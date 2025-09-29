
class custom_error1(Exception):
    pass


class custom_error2(Exception):
    pass


def main():
    """raising a custom error off of a divide by 0 error and then triggering custom error 2 and then pulling the cause and context from said errors"""
    try:
        try:

            try:
                1/0

            # starting to trigger the custom errors.
            except (ZeroDivisionError) as e1:
                print(f"First custom error: {e1}")
                raise custom_error1(
                    "Cause of the error: A first custom error occurred")

        except (custom_error1) as e2:  # triggering custom error 2 because of custom error 1
            print(f"{e2} custom error 2 triggered by custom error 1")
            raise custom_error2(
                "Handling SecondCustomError: A second custom error occurred") from e2

    except (custom_error2) as e3:  # utilizing cause and context
        print(f"Cause: {e3.__cause__}")
        print(f"Context: {e3.__context__}")


main()

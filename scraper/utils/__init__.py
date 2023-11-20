import re


def snake_case(input_string: str) -> str:
    # Replace spaces and special characters with underscores
    snake_case_string = re.sub(r"\W+", "_", input_string)

    # Convert to lowercase and remove leading/trailing underscores
    snake_case_string = snake_case_string.strip("_").lower()

    return snake_case_string

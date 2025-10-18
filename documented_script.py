def transform_numbers(numbers):
    """
    Apply mathematical transformations to a list of numbers
    based on whether they are even or odd.
   
    Args:
        numbers (list of int): List of integers to be transformed.
   
    Returns:
        list of int: New list with transformed numbers.
    """
    # Even numbers are doubled, odd numbers are tripled
    transformed_numbers = [num * 2 if num % 2 == 0 else num * 3 for num in numbers]

    return transformed_numbers


def transform_strings(strings):
    """
    Transform a list of strings by changing their case based on their length.
   
    Args:
        strings (list of str): List of strings to be transformed.
       
    Returns:
        str: A single string with resulting transformations.
    """
    # Strings longer than 5 characters are converted to uppercase
    # Strings shorter than or equal to 5 characters are converted to lowercase
    transformed_list = [s.upper() if len(s) > 5 else s.lower() for s in strings]

    # Join transformed strings into a single string separated by spaces
    return " ".join(transformed_list)


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    fruits = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_nums = transform_numbers(numbers)
    processed_strings = transform_strings(fruits)

    print("Processed Numbers:", processed_nums)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()

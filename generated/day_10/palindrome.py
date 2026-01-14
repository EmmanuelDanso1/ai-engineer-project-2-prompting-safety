def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case and non-alphanumeric characters.

    A palindrome is a sequence of characters that reads the same forwards and backwards.
    This function cleans the input string by converting it to lowercase and removing
    all non-alphanumeric characters before performing the check.

    Args:
        s: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("Racecar")
        True
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("Madam")
        True
        >>> is_palindrome("")
        True
        >>> is_palindrome("12321")
        True
        >>> is_palindrome("No 'x' in 'Nixon'")
        True
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    cleaned_chars = [char.lower() for char in s if char.isalnum()]
    cleaned_s = "".join(cleaned_chars)
    
    return cleaned_s == cleaned_s[::-1]
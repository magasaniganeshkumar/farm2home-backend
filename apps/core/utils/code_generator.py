def generate_code(prefix: str, number: int) -> str:
    """
    Generate a business code.

    Example:
        PRD-000001
    """
    return f"{prefix}-{number:06d}"
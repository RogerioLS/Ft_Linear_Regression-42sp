"""Data loading and validation module for 42 ft_linear_regression.

Handles reading dataset CSV files, extracting mileage (km) and price arrays,
and validating data integrity without external high-level ML dependencies.
"""

from pathlib import Path
from typing import Union


def _parse_row(
    parts: list[str],
    km_idx: int,
    price_idx: int,
    line_num: int,
    path: Path,
    line: str,
) -> tuple[float, float]:
    """Parses and validates a single CSV row for km and price values.

    Args:
        parts (list[str]): Comma-separated components of the line.
        km_idx (int): Index of km column.
        price_idx (int): Index of price column.
        line_num (int): Source line number for error reporting.
        path (Path): Path to dataset file.
        line (str): Raw row string.

    Returns:
        tuple[float, float]: Validated (km, price) pair.

    Raises:
        ValueError: If data cannot be converted to float or contains negative numbers.
    """
    try:
        km = float(parts[km_idx])
        price = float(parts[price_idx])
    except (ValueError, IndexError) as exc:
        raise ValueError(f"Malformed numeric data at line {line_num} in {path}: '{line}'") from exc

    if km < 0.0 or price < 0.0:
        raise ValueError(
            f"Negative mileage or price at line {line_num} in {path}: km={km}, price={price}"
        )

    return km, price


def load_csv(filepath: Union[str, Path]) -> tuple[list[float], list[float]]:
    """Loads mileage and price dataset from a CSV file.

    Args:
        filepath (Union[str, Path]): Path to the dataset CSV file.

    Returns:
        tuple[list[float], list[float]]: Tuple containing:
            - km_values (list[float]): List of vehicle mileage values.
            - price_values (list[float]): List of vehicle price values.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        ValueError: If the file is empty, has invalid headers, or contains malformed data.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found at: {path}")

    try:
        raw_content = path.read_text(encoding="utf-8").strip()
    except Exception as exc:
        raise ValueError(f"Failed to read file at {path}: {exc}") from exc

    if not raw_content:
        raise ValueError(f"Dataset file at {path} is empty.")

    lines = [line.strip() for line in raw_content.splitlines() if line.strip()]
    if len(lines) < 2:
        raise ValueError(f"Dataset at {path} must contain at least a header and one data row.")

    header = [h.strip().lower() for h in lines[0].split(",")]
    if "km" not in header or "price" not in header:
        raise ValueError(f"Dataset header must contain 'km' and 'price' columns, got: {lines[0]}")

    km_idx = header.index("km")
    price_idx = header.index("price")

    km_values: list[float] = []
    price_values: list[float] = []

    for line_num, line in enumerate(lines[1:], start=2):
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 2:
            continue

        km, price = _parse_row(parts, km_idx, price_idx, line_num, path, line)
        km_values.append(km)
        price_values.append(price)

    if not km_values:
        raise ValueError(f"No valid data rows found in {path}.")

    return km_values, price_values

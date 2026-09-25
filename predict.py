#!/usr/bin/env python3
"""Interactive price prediction CLI for 42 ft_linear_regression.

Loads learned linear regression parameters (thetas.json) and calculates
the estimated car price for a user-specified mileage using the hypothesis:
    estimatePrice(mileage) = theta0 + (theta1 * mileage)

If the model has not been trained yet (thetas.json missing or uninitialized),
the parameters default to theta0 = 0.0 and theta1 = 0.0, predicting $0.00.
"""

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Optional, Tuple, Union

DEFAULT_THETAS_PATH = Path("thetas.json")

# ANSI color formatting constants
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"


def load_thetas(
    filepath: Union[str, Path] = DEFAULT_THETAS_PATH,
) -> Tuple[float, float, bool]:
    """Loads linear regression weights from JSON or returns default fallback.

    Subject requirement:
        If the model has not been trained yet (thetas.json does not exist),
        theta0 and theta1 must default to 0.0.

    Args:
        filepath (Union[str, Path]): Path to parameters JSON file.

    Returns:
        Tuple[float, float, bool]: Tuple of (theta0, theta1, is_trained).
    """
    path = Path(filepath)
    if not path.is_file():
        return 0.0, 0.0, False

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        theta0 = float(data.get("theta0", 0.0))
        theta1 = float(data.get("theta1", 0.0))

        if not (math.isfinite(theta0) and math.isfinite(theta1)):
            return 0.0, 0.0, False

        return theta0, theta1, True
    except (json.JSONDecodeError, ValueError, OSError):
        return 0.0, 0.0, False


def estimate_price(mileage: float, theta0: float, theta1: float) -> float:
    """Calculates estimated vehicle price using the learned linear hypothesis.

    Formula:
        estimatePrice(mileage) = theta0 + (theta1 * mileage)

    Args:
        mileage (float): Vehicle odometer reading in kilometers.
        theta0 (float): Model intercept parameter.
        theta1 (float): Model slope parameter.

    Returns:
        float: Estimated vehicle valuation.
    """
    return float(theta0 + (theta1 * float(mileage)))


def validate_mileage_input(raw_input: str) -> float:
    """Parses and validates user mileage string into a non-negative float.

    Args:
        raw_input (str): Raw string captured from terminal input.

    Returns:
        float: Validated odometer reading in kilometers.

    Raises:
        ValueError: If input is empty, not a valid number, or strictly negative.
    """
    cleaned = raw_input.strip().replace(",", ".")
    if not cleaned:
        raise ValueError("Input cannot be empty. Please enter a valid mileage.")

    try:
        mileage = float(cleaned)
    except ValueError as exc:
        raise ValueError(f"'{raw_input.strip()}' is not a valid numeric value.") from exc

    if not math.isfinite(mileage):
        raise ValueError("Mileage must be a finite numerical value.")

    if mileage < 0.0:
        raise ValueError(f"Mileage cannot be negative: {mileage:,.2f} km.")

    return mileage


def prompt_mileage() -> float:
    """Interactively prompts user for vehicle mileage until valid input is given.

    Returns:
        float: User-provided valid mileage in kilometers.

    Raises:
        EOFError: If input stream terminates prematurely.
        KeyboardInterrupt: If user cancels operation via Ctrl+C.
    """
    prompt_str = f"{BOLD}{CYAN}🚗 Enter vehicle mileage in kilometers: {RESET}"
    while True:
        try:
            line = input(prompt_str)
            return validate_mileage_input(line)
        except ValueError as err:
            print(f"{YELLOW}⚠ Invalid input: {err}{RESET}")


def print_prediction_report(
    mileage: float,
    price: float,
    theta0: float,
    theta1: float,
    is_trained: bool,
) -> None:
    """Displays formatted vehicle price estimation report.

    Args:
        mileage (float): Evaluated vehicle mileage.
        price (float): Calculated estimated valuation.
        theta0 (float): Active intercept parameter.
        theta1 (float): Active slope parameter.
        is_trained (bool): Whether parameters were loaded from a trained model file.
    """
    status_label = (
        f"{GREEN}TRAINED (thetas.json){RESET}"
        if is_trained
        else f"{YELLOW}UNTRAINED (θ0=0, θ1=0){RESET}"
    )

    print(f"\n{CYAN}============================================================{RESET}")
    print(f" {BOLD}{MAGENTA}         42 FT_LINEAR_REGRESSION — PRICE ESTIMATOR          {RESET}")
    print(f"{CYAN}============================================================{RESET}")
    print(f"  • Model Status:     {status_label}")
    print(f"  • Active Theta0:    {theta0:,.4f}")
    print(f"  • Active Theta1:    {theta1:,.6f}")
    print(f"  • Target Mileage:   {mileage:,.2f} km")
    print(f"{CYAN}------------------------------------------------------------{RESET}")

    if not is_trained:
        print(f"  {BOLD}Estimated Price:    $ {price:,.2f}{RESET}")
        print(f"  {DIM}ℹ Note: Run 'python3 train.py' to fit the model parameters.{RESET}")
    elif price < 0.0:
        print(
            f"  {BOLD}{RED}Estimated Price:    $ 0.00 "
            f"(Mathematical value: $ {price:,.2f}){RESET}"
        )
        print(f"  {DIM}ℹ Vehicle mileage exceeds practical market lifespan threshold.{RESET}")
    else:
        print(f"  {BOLD}{GREEN}Estimated Price:    $ {price:,.2f}{RESET}")

    print(f"{CYAN}============================================================{RESET}\n")


def parse_args(args: Optional[list[str]] = None) -> argparse.Namespace:
    """Configures command-line argument parser for predict.py.

    Args:
        args (Optional[list[str]]): CLI argument vector. Defaults to sys.argv[1:].

    Returns:
        argparse.Namespace: Parsed CLI options.
    """
    parser = argparse.ArgumentParser(
        description="Estimate vehicle price from mileage using learned linear regression.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-m",
        "--mileage",
        type=float,
        default=None,
        help="Optional mileage argument for non-interactive evaluation.",
    )
    parser.add_argument(
        "-t",
        "--thetas",
        default=str(DEFAULT_THETAS_PATH),
        help="Path to JSON file containing trained theta0 and theta1 parameters.",
    )
    return parser.parse_args(args)


def run_prediction(
    thetas_path: Union[str, Path] = DEFAULT_THETAS_PATH,
    mileage: Optional[float] = None,
    verbose: bool = True,
) -> float:
    """Executes price prediction workflow either interactively or programmatically.

    Args:
        thetas_path (Union[str, Path]): Path to parameters JSON file.
        mileage (Optional[float]): Optional explicit mileage. Prompts user if None.
        verbose (bool): Whether to print formatted report. Defaults to True.

    Returns:
        float: Estimated vehicle price.
    """
    theta0, theta1, is_trained = load_thetas(thetas_path)

    if mileage is None:
        mileage = prompt_mileage()
    elif mileage < 0.0:
        raise ValueError(f"Mileage cannot be negative: {mileage:,.2f} km.")

    estimated_price = estimate_price(mileage, theta0, theta1)

    if verbose:
        print_prediction_report(mileage, estimated_price, theta0, theta1, is_trained)

    return estimated_price


def main() -> int:
    """Main CLI entrypoint for predict.py.

    Returns:
        int: Process exit code (0 for success, 1 on error, 130 on cancellation).
    """
    try:
        opts = parse_args()
        run_prediction(thetas_path=opts.thetas, mileage=opts.mileage, verbose=True)
        return 0
    except KeyboardInterrupt:
        print(f"\n{YELLOW}⚠ Prediction cancelled by user.{RESET}", file=sys.stderr)
        return 130
    except EOFError:
        print(f"\n{YELLOW}⚠ End of input encountered.{RESET}", file=sys.stderr)
        return 1
    except ValueError as err:
        print(f"{RED}❌ Error: {err}{RESET}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"{RED}❌ Unexpected error: {exc}{RESET}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

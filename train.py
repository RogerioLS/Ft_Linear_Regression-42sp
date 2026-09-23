#!/usr/bin/env python3
"""Model training CLI for 42 ft_linear_regression.

Loads the car mileage and price dataset, normalizes feature and target domains
via Min-Max scaling, optimizes intercept and slope using pure Batch Gradient
Descent, analytically denormalizes learned weights, and persists the thetas
to a JSON file (thetas.json) for the inference engine.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

from src.model.linear_regression import LinearRegression
from src.preprocessing.loader import load_csv
from src.preprocessing.scaler import MinMaxScaler, denormalize_parameters

DEFAULT_DATASET = Path("dataset/data.csv")
DEFAULT_OUTPUT = Path("thetas.json")
DEFAULT_ALPHA = 0.1
DEFAULT_EPOCHS = 1000

# ANSI color codes for enhanced terminal output
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"


def save_thetas(
    filepath: Union[str, Path],
    theta0: float,
    theta1: float,
    metadata: Optional[Dict[str, Any]] = None,
) -> None:
    """Serializes model parameters and optional training metadata to a JSON file.

    Args:
        filepath (Union[str, Path]): Destination path for the saved JSON file.
        theta0 (float): Unscaled model intercept parameter.
        theta1 (float): Unscaled model slope parameter.
        metadata (Optional[Dict[str, Any]]): Additional training metrics or parameters.

    Raises:
        OSError: If writing to the specified destination fails.
    """
    dest = Path(filepath)
    payload: Dict[str, Any] = {
        "theta0": float(theta0),
        "theta1": float(theta1),
    }
    if metadata:
        payload.update(metadata)

    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def print_training_banner(
    dataset_path: Path,
    output_path: Path,
    alpha: float,
    epochs: int,
    sample_count: int,
) -> None:
    """Displays formatted training session parameters.

    Args:
        dataset_path (Path): Path to source dataset file.
        output_path (Path): Path to model output JSON.
        alpha (float): Learning rate hyperparameter.
        epochs (int): Number of gradient descent iterations.
        sample_count (int): Number of data points loaded.
    """
    print(f"{CYAN}============================================================{RESET}")
    print(f" {BOLD}{MAGENTA}        42 FT_LINEAR_REGRESSION — MODEL TRAINING            {RESET}")
    print(f"{CYAN}============================================================{RESET}")
    print(f"  • Dataset:     {dataset_path}")
    print(f"  • Samples:     {sample_count} records")
    print(f"  • Iterations:  {epochs}")
    print(f"  • Alpha (lr):  {alpha}")
    print(f"  • Output File: {output_path}")
    print(f"{CYAN}============================================================{RESET}")


def print_training_results(
    theta0: float,
    theta1: float,
    initial_cost: float,
    final_cost: float,
    output_path: Path,
) -> None:
    """Displays formatted training completion metrics and saved parameters.

    Args:
        theta0 (float): Unscaled intercept.
        theta1 (float): Unscaled slope.
        initial_cost (float): Mean squared error cost before training.
        final_cost (float): Mean squared error cost after training.
        output_path (Path): Location where parameters were saved.
    """
    sign = "+" if theta1 >= 0 else "-"
    abs_theta1 = abs(theta1)
    cost_reduction = (1.0 - (final_cost / initial_cost)) * 100.0
    hyp = f"{theta0:,.4f} {sign} ({abs_theta1:.6f} * mileage)"

    print(f"\n{BOLD}{GREEN}✔ Model successfully trained!{RESET}")
    print(f"  • Initial Normalized Cost J(θ): {initial_cost:.6f}")
    print(f"  • Final Normalized Cost J(θ):   {final_cost:.6f}")
    print(f"  • Cost Reduction:               {cost_reduction:.2f}%")
    print(f"\n{BOLD}{YELLOW}📐 Learned Mathematical Hypothesis (Original Units):{RESET}")
    print(f"  {BOLD}estimatePrice(mileage) = {hyp}{RESET}")
    print(f"  • theta0 (Intercept): {theta0:,.6f}")
    print(f"  • theta1 (Slope):     {theta1:,.6f}")
    print(f"\n{BOLD}{CYAN}💾 Parameters saved to: {output_path}{RESET}\n")


def train_model(
    dataset_path: Union[str, Path] = DEFAULT_DATASET,
    output_path: Union[str, Path] = DEFAULT_OUTPUT,
    alpha: float = DEFAULT_ALPHA,
    epochs: int = DEFAULT_EPOCHS,
    verbose: bool = True,
) -> Tuple[float, float]:
    """Orchestrates data loading, feature scaling, model fitting, and persistence.

    Args:
        dataset_path (Union[str, Path]): Path to dataset CSV. Defaults to dataset/data.csv.
        output_path (Union[str, Path]): Path to target JSON. Defaults to thetas.json.
        alpha (float): Gradient descent learning rate. Defaults to 0.1.
        epochs (int): Number of training iterations. Defaults to 1000.
        verbose (bool): Whether to output formatted progress to terminal. Defaults to True.

    Returns:
        Tuple[float, float]: Unscaled parameters (theta0, theta1).

    Raises:
        FileNotFoundError: If the dataset file does not exist.
        ValueError: If dataset is malformed or hyperparameters are invalid.
    """
    d_path = Path(dataset_path)
    o_path = Path(output_path)

    # 1. Load raw dataset features
    km_list, price_list = load_csv(d_path)

    if verbose:
        print_training_banner(d_path, o_path, alpha, epochs, len(km_list))

    # 2. Scale features and target to [0, 1] range to avoid vanishing/exploding gradients
    x_scaler = MinMaxScaler().fit(km_list)
    y_scaler = MinMaxScaler().fit(price_list)

    x_scaled = x_scaler.transform(km_list)
    y_scaled = y_scaler.transform(price_list)

    # 3. Fit linear regression model using pure Batch Gradient Descent
    model = LinearRegression()
    initial_cost = model.compute_cost(x_scaled, y_scaled)
    model.fit(x_scaled, y_scaled, alpha=alpha, epochs=epochs)
    final_cost = model.compute_cost(x_scaled, y_scaled)

    # 4. Analytically convert normalized weights to original physical units
    theta0_real, theta1_real = denormalize_parameters(
        model.theta0, model.theta1, x_scaler, y_scaler
    )

    # 5. Persist unscaled parameters and training metadata to JSON
    metadata: Dict[str, Any] = {
        "learning_rate": alpha,
        "epochs": epochs,
        "samples": len(km_list),
        "initial_cost_norm": round(initial_cost, 6),
        "final_cost_norm": round(final_cost, 6),
    }
    save_thetas(o_path, theta0_real, theta1_real, metadata)

    if verbose:
        print_training_results(theta0_real, theta1_real, initial_cost, final_cost, o_path)

    return theta0_real, theta1_real


def parse_args(args: Optional[list[str]] = None) -> argparse.Namespace:
    """Parses command-line arguments for train.py execution.

    Args:
        args (Optional[list[str]]): Command-line argument vector. Defaults to sys.argv[1:].

    Returns:
        argparse.Namespace: Parsed CLI options and arguments.
    """
    parser = argparse.ArgumentParser(
        description="Train univariate Linear Regression using Batch Gradient Descent.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "dataset",
        nargs="?",
        default=str(DEFAULT_DATASET),
        help="Path to CSV dataset containing 'km' and 'price' columns.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Path to output JSON file where learned thetas will be stored.",
    )
    parser.add_argument(
        "-a",
        "--alpha",
        type=float,
        default=DEFAULT_ALPHA,
        help="Learning rate for gradient descent parameter updates.",
    )
    parser.add_argument(
        "-e",
        "--epochs",
        type=int,
        default=DEFAULT_EPOCHS,
        help="Number of iterations / epochs for gradient descent optimization.",
    )
    return parser.parse_args(args)


def main() -> int:
    """Main CLI entrypoint for train.py.

    Returns:
        int: Process exit code (0 for success, 1 on failure).
    """
    try:
        opts = parse_args()
        train_model(
            dataset_path=opts.dataset,
            output_path=opts.output,
            alpha=opts.alpha,
            epochs=opts.epochs,
            verbose=True,
        )
        return 0
    except (FileNotFoundError, ValueError, ZeroDivisionError) as err:
        print(f"{RED}❌ Training Error: {err}{RESET}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print(f"\n{YELLOW}⚠ Training aborted by user.{RESET}", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"{RED}❌ Unexpected fatal error: {exc}{RESET}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

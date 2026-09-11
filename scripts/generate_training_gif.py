"""Generate a high-definition dark-themed GIF animation of Gradient Descent."""

import io
import os
import sys

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import pandas as pd
from PIL import Image

matplotlib.use("Agg")

# Ensure local repository root takes precedence
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.preprocessing.scaler import MinMaxScaler  # noqa: E402


def create_training_gif(output_path: str = "docs/assets/training_animation.gif") -> None:
    """Renders real gradient descent steps into an animated GIF."""
    df = pd.read_csv("dataset/data.csv")
    x_raw = df["km"].to_numpy(dtype=float)
    y_raw = df["price"].to_numpy(dtype=float)

    scaler_x = MinMaxScaler()
    scaler_y = MinMaxScaler()
    x_norm = scaler_x.fit_transform(x_raw)
    y_norm = scaler_y.fit_transform(y_raw)

    lr = 0.1
    n_iterations = 1000
    m = len(x_norm)

    # Keyframes sampled with progressive pacing (smooth convergence animation)
    frames_indices = sorted(
        list(
            set(
                [
                    0,
                    1,
                    2,
                    3,
                    5,
                    8,
                    12,
                    17,
                    23,
                    30,
                    39,
                    50,
                    64,
                    82,
                    105,
                    135,
                    175,
                    225,
                    290,
                    370,
                    470,
                    600,
                    780,
                    1000,
                ]
            )
        )
    )

    th0_norm = 0.0
    th1_norm = 0.0
    snapshots = {0: (th0_norm, th1_norm)}

    for i in range(1, n_iterations + 1):
        preds = [th0_norm + th1_norm * xi for xi in x_norm]
        d_th0 = (1.0 / m) * sum(preds[k] - y_norm[k] for k in range(m))
        d_th1 = (1.0 / m) * sum((preds[k] - y_norm[k]) * x_norm[k] for k in range(m))

        th0_norm -= lr * d_th0
        th1_norm -= lr * d_th1

        if i in frames_indices:
            snapshots[i] = (th0_norm, th1_norm)

    x_min, x_max = float(min(x_raw)), float(max(x_raw))
    x_span = np.linspace(x_min - 5000, x_max + 5000, 100)

    images = []

    # GitHub Dark Theme Palette
    bg_color = "#0d1117"
    surface_color = "#161b22"
    border_color = "#30363d"
    text_color = "#c9d1d9"
    accent_blue = "#58a6ff"
    point_color = "#38bdf8"
    line_color = "#f43f5e"
    converged_color = "#238636"

    for epoch, (t0_n, t1_n) in snapshots.items():
        # Analytical de-normalization to real dollar/km scale
        t0_real = scaler_y.inverse_transform([t0_n])[0] - (
            t1_n * (scaler_y.range_val / scaler_x.range_val) * scaler_x.min_val
        )
        t1_real = t1_n * (scaler_y.range_val / scaler_x.range_val)

        y_span = [t0_real + t1_real * xi for xi in x_span]
        y_preds_data = [t0_real + t1_real * xi for xi in x_raw]

        mse = (1.0 / len(y_raw)) * sum(
            (y_p - y_act) ** 2 for y_p, y_act in zip(y_preds_data, y_raw)
        )
        ss_tot = sum((y_act - float(np.mean(y_raw))) ** 2 for y_act in y_raw)
        ss_res = sum((y_act - y_p) ** 2 for y_p, y_act in zip(y_preds_data, y_raw))
        r2 = max(0.0, 1.0 - (ss_res / ss_tot if ss_tot > 0 else 1.0)) * 100.0

        is_final = epoch == n_iterations
        curr_line_color = converged_color if is_final else line_color

        fig, ax = plt.subplots(figsize=(7.0, 4.5), dpi=100)
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(surface_color)

        ax.grid(True, linestyle="--", alpha=0.25, color=border_color)
        for spine in ax.spines.values():
            spine.set_edgecolor(border_color)
            spine.set_linewidth(1.2)

        ax.scatter(
            x_raw,
            y_raw,
            color=point_color,
            edgecolor="#0284c7",
            s=70,
            alpha=0.9,
            zorder=3,
            label="Car Observations (data.csv)",
        )

        ax.plot(
            x_span,
            y_span,
            color=curr_line_color,
            linewidth=2.8,
            zorder=4,
            label="Hypothesis: h(x) = θ₀ + θ₁·x",
        )

        ax.set_xlim(15000, 250000)
        ax.set_ylim(3200, 8800)

        ax.set_title(
            "Gradient Descent Optimization (Live Convergence)",
            fontsize=12,
            fontweight="bold",
            color=accent_blue,
            pad=12,
        )
        ax.set_xlabel("Mileage (km)", fontsize=9.5, fontweight="bold", color=text_color, labelpad=6)
        ax.set_ylabel("Price ($)", fontsize=9.5, fontweight="bold", color=text_color, labelpad=6)
        ax.tick_params(colors=text_color, labelsize=8.5)

        ax.xaxis.set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda val, p: f"{int(val):,}")
        )
        ax.yaxis.set_major_formatter(
            matplotlib.ticker.FuncFormatter(lambda val, p: f"${int(val):,}")
        )

        status_text = "CONVERGED [OK]" if is_final else "OPTIMIZING..."
        hud = (
            f"Epoch: {epoch:>4} / {n_iterations}\n"
            f"Status: {status_text}\n"
            f"Loss (MSE): {mse:>9,.0f}\n"
            f"Accuracy (R²): {r2:>5.1f}%\n"
            f"θ₀: {t0_real:>7.1f} | θ₁: {t1_real:>6.4f}"
        )
        ax.text(
            0.96,
            0.94,
            hud,
            transform=ax.transAxes,
            fontsize=8.5,
            fontfamily="monospace",
            verticalalignment="top",
            horizontalalignment="right",
            bbox=dict(
                boxstyle="round,pad=0.5",
                facecolor=bg_color,
                edgecolor=curr_line_color,
                alpha=0.92,
                linewidth=1.2,
            ),
            color=text_color,
            zorder=5,
        )

        ax.legend(
            loc="lower left",
            fontsize=8.5,
            facecolor=bg_color,
            edgecolor=border_color,
            labelcolor=text_color,
        )

        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png", facecolor=fig.get_facecolor(), edgecolor="none")
        buf.seek(0)
        img = Image.open(buf)
        images.append(img.copy())
        buf.close()
        plt.close(fig)

    final_frame = images[-1]
    for _ in range(14):
        images.append(final_frame)

    images[0].save(
        output_path, save_all=True, append_images=images[1:], duration=130, loop=0, optimize=True
    )
    print(f"Generated {output_path} successfully!")


if __name__ == "__main__":
    create_training_gif()

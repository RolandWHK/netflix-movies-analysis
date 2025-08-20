# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FIG_DIR = Path("reports/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)


def load_data(path: str) -> pd.DataFrame:
    """Load Netflix dataset and filter out TV shows."""
    df = pd.read_csv(path, index_col=0)
    df = df[df["type"] != "TV Show"]
    return df[["title", "country", "genre", "release_year", "duration"]]


def plot_movie_duration(df: pd.DataFrame):
    """Scatter plot of movie duration by release year, colored by genre."""
    # Color mapping
    color_map = {
        "Children": "magenta",
        "Documentaries": "cyan",
        "Stand-Up": "blue"
    }

    # Default color: red
    colors = [color_map.get(genre, "red") for genre in df["genre"]]

    # Scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["release_year"], df["duration"], c=colors, alpha=0.7)

    # Legend
    legend_labels = {
        "magenta": "Children",
        "cyan": "Documentaries",
        "blue": "Stand-Up",
        "red": "Other genres",
    }
    legend_handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=color,
                   markersize=8, label=label)
        for color, label in legend_labels.items()
    ]

    ax.legend(handles=legend_handles, loc="upper left")
    ax.set_xlabel("Release year")
    ax.set_ylabel("Duration (minutes)")
    ax.set_title("Movie Duration by Year of Release")

    # Save figure
    plt.savefig(FIG_DIR / "netflix_scatter.png")
    plt.close()


if __name__ == "__main__":
    movies = load_data("data/netflix_data.csv")
    plot_movie_duration(movies)
    print("Plot saved to reports/figures/netflix_scatter.png")

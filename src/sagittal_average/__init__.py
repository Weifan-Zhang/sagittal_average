"""Core functionality for the sagittal_average package."""

from __future__ import annotations

from pathlib import Path
from typing import Union

import numpy as np

PathLike = Union[str, Path]

__all__ = ["run_averages"]


def run_averages(file_input: PathLike = "brain_sample.csv",
                 file_output: PathLike = "brain_average.csv") -> None:
    """
    Calculate the average through sagittal/horizontal planes.

    Parameters
    ----------
    file_input:
        CSV file containing binned results from scikit-brain. Each row
        represents a sagittal/horizontal plane and each column represents a
        coronal plane.
    file_output:
        Destination CSV file containing the average for each sagittal/
        horizontal plane.
    """

    planes = np.loadtxt(file_input, dtype=int, delimiter=",")
    averages = planes.mean(axis=1)[:, np.newaxis]
    np.savetxt(file_output, averages, fmt="%.1f", delimiter=",")


"""Command-line interface for the sagittal_average package."""

from __future__ import annotations

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from . import run_averages


def build_parser() -> ArgumentParser:
    """Create the argument parser used by the CLI."""
    parser = ArgumentParser(
        description="Calculates the average for each sagittal-horizontal plane.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "file_input",
        nargs="?",
        default="brain_sample.csv",
        help="Input CSV file with the results from scikit-brain binning algorithm.",
    )
    parser.add_argument(
        "--file_output",
        "-o",
        default="brain_average.csv",
        help="Name of the output CSV file.",
    )
    return parser


def main() -> None:
    """Entrypoint invoked by the console script."""
    parser = build_parser()
    arguments = parser.parse_args()
    run_averages(arguments.file_input, arguments.file_output)


if __name__ == "__main__":
    main()


import numpy as np

from sagittal_average import run_averages


def test_run_averages_computes_row_means(tmp_path):
    planes = np.array(
        [
            [1, 3, 5],
            [2, 4, 6],
            [0, 2, 4],
        ],
        dtype=int,
    )
    file_input = tmp_path / "brain.csv"
    file_output = tmp_path / "avg.csv"
    np.savetxt(file_input, planes, fmt="%d", delimiter=",")

    run_averages(file_input, file_output)

    result = np.loadtxt(file_output, delimiter=",")
    expected = planes.mean(axis=1)[:, np.newaxis]
    np.testing.assert_allclose(result, expected)


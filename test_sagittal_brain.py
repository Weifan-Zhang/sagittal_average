import numpy as np
from sagittal_brain import run_averages

def test_run_averages():
    """
    Test whether Charlene's code correctly computes row averages.
    """

    # Step 1: Create a small, easy-to-check input array
    # 3 rows (sagittal/horizontal planes), 4 columns (coronal planes)
    test_input = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])

    # Save this test input to a CSV file
    np.savetxt("test_input.csv", test_input, fmt='%d', delimiter=',')

    # Step 2: Expected correct output (average of each row)
    # Row 1: (1+2+3+4)/4 = 2.5
    # Row 2: (5+6+7+8)/4 = 6.5
    # Row 3: (9+10+11+12)/4 = 10.5
    expected_output = np.array([[2.5], [6.5], [10.5]])

    # Step 3: Run Charlene's current code
    run_averages("test_input.csv", "test_output.csv")

    # Step 4: Load the output she produced
    actual_output = np.loadtxt("test_output.csv", delimiter=',')

    # Step 5: Compare expected vs actual
    if np.allclose(expected_output, actual_output):
        print("Test passed! Output is correct.")
    else:
        print("Test failed!")
        print("Expected:\n", expected_output)
        print("Actual:\n", actual_output)

# Singular Value Decomposition using QR Algorithm

This project implements the Singular Value Decomposition (SVD) of a real matrix using the QR algorithm. The implementation is done in Python without relying on external linear algebra libraries (except for optional verification with NumPy). The QR decomposition is performed via the Gram-Schmidt process, and the singular values are obtained by diagonalizing either `A^T A` or `A A^T` (the smaller of the two) using the iterative QR algorithm. The code is structured with object‑oriented principles for clarity and modularity.

## Features

- Define a matrix with user‑supplied dimensions (n × k, n, k ≤ 10).
- Enter matrix elements interactively from the console.
- Compute the singular values of the matrix using the QR algorithm.
- Display the singular values in descending order.
- Verify the computed singular values against NumPy’s `linalg.svd` (if NumPy is installed).
- Check basic properties: Frobenius norm and sum of squared singular values.
- Modular design with separate classes for matrices, QR decomposition, and SVD calculation.

## Requirements

- Python 3.6 or higher.
- No external libraries are required for the core algorithm.  
  For verification, NumPy is optional (`pip install numpy`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/svd-qr.git
   cd svd-qr

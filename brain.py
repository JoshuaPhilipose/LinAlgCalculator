import scipy
import scipy.linalg

# Where the actual calculations will take place.
# All functions will return dictionaries with the label of the result, then the result.
# Back in calculator.py, this will be converted to proper HTML result format and then emitted back.


def LUfactorization(matrix):
    results = {}
    A = scipy.array(matrix)
    P, L, U = scipy.linalg.lu(A)
    results['P'] = P
    results['L'] = L
    results['U'] = U
    return results

import scipy
import scipy.linalg

# Where the actual calculations will take place.
# All functions will return dictionaries with the label of the result, then the result.
# Back in calculator.py, this will be converted to proper HTML result format and then emitted back.

def ref(matrix):
    results = {}
    results["REF"] = "Not currently supported"
    return results

def rref(matrix):
    results = {}
    results["RREF"] = "Not currently supported"
    return results

def inverse(matrix):
    results = {}
    results["Inverse"] = "Not currently supported"
    return results

def LUfactorization(matrix):
    results = {}
    A = scipy.array(matrix)
    P, L, U = scipy.linalg.lu(A)
    results['P'] = P
    results['L'] = L
    results['U'] = U
    return results

def QRFactorization(matrix):
    results = {}
    return results

def evalues(matrix):
    results = {}
    results["Eigenvalues"] = "Not currently supported"
    return results

def evectors(matrix):
    results = {}
    results["Eigenvectors"] = "Not currently supported"
    return results

def obasis(matrix):
    results = {}
    results["Orthogonal Basis"] = "Not currently supported"
    return results

def onbasis(matrix):
    results = {}
    results["Orthonormal Basis"] = "Not currently supported"
    return results

def determinant(matrix):
    results = {}
    results["Determinant"] = "Not currently supported"
    return results

def trace(matrix):
    results = {}
    results["Trace"] = "Not currently supported"
    return results

def norm(matrix):
    results = {}
    results["Norm"] = "Not currently supported"
    return results

def condition(matrix):
    results = {}
    results["Condition"] = "Not currently supported"
    return results

def rank(matrix):
    results = {}
    results["Rank"] = "Not currently supported"
    return results

def signedlog(matrix):
    results = {}
    results["Sign"] = "Not currently supported"
    results["Log"] = "This isn't supported either!"
    return results

def mmult(matrix):
    results = {}
    results["Resultant Matrix"] = "not supported"
    retuurn results

def axb(matrix):
    results = {}
    results["X"] = "Not currently supported"
    return results

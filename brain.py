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
    A = scipy.array(matrix)
    results["Inverse"] = scipy.linalg.inv(A)
    return results

def LUfactorization(matrix):
    results = {}
    A = scipy.array(matrix)
    P, L, U = scipy.linalg.lu(A)
    results['P'] = P
    results['L'] = L
    results['U'] = U
    return results

def SVDDecomposition(matrix):
    results = {}
    A = scipy.array(matrix)
    U, S, VH = scipy.linalg.svd(A)
    results["U"] = U
    results["S"] = S
    results["VH"] = VH
    return results

def QRFactorization(matrix):
    results = {}
    A = scipy.array(matrix)
    Q, R = scipy.linalg.qr(A)
    results["Q"] = Q
    results["R"] = R
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
    A = scipy.array(matrix)
    results["Determinant"] = scipy.linalg.det(A)
    return results

def trace(matrix):
    results = {}
    A = scipy.array(matrix)
    results["Trace"] = scipy.linalg.trace(A)
    return results

def norm(matrix):
    results = {}
    A = scipy.array(matrix)
    results["Norm"] = scipy.linalg.norm(A)
    return results

def condition(matrix):
    results = {}
    A = scipy.array(matrix)
    results["Condition"] = scipy.linalg.cond(A)
    return results

def rank(matrix):
    results = {}
    A = scipy.array(matrix)
    results["Rank"] = scipy.linalg.matrix_rank(A)
    return results

def signedlog(matrix):
    results = {}
    A = scipy.array(matrix)
    sign, logdet = scipy.linalg.slogdet(A)
    results["Sign"] = sign
    results["Log Determinant"] = logdet
    return results

def mmult(matrix):
    results = {}
    results["Resultant Matrix"] = "not supported"
    return results

def axb(matrix):
    results = {}
    results["X"] = "Not currently supported"
    return results

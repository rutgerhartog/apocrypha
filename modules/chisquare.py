from scipy.stats import chisquare as chi2


def calculate_chisquare(text: bytes) -> float:
    return chi2(text).statistics

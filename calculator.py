# calculator.py
# Arithmetic library for A8_T2

def add(PAddend1: float, PAddend2: float) -> float:
    return PAddend1 + PAddend2

def subtract(PMinuend: float, PSubtrahend: float) -> float:
    return PMinuend - PSubtrahend

def multiply(PMultiplicant: float, PMultiplier: float) -> float:
    return PMultiplicant * PMultiplier

def divide(PDividend: float, PDivisor: float) -> float:
    if PDivisor == 0:
        raise ZeroDivisionError("Division by zero.")
    return PDividend / PDivisor

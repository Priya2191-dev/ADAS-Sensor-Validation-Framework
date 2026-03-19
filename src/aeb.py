def apply_brakes(ttc, threshold=3):
    """
    Decide whether to apply brakes.
    """
    if ttc < threshold:
        return True
    else:
        return False


if __name__ == "__main__":
    print(apply_brakes(2.5))

from typing import List, Union


def give_bmi(
    height: List[Union[int, float]],
    weight: List[Union[int, float]]
) -> List[float]:
    """
    Calculate BMI values from height and weight lists.
    """

    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be lists.")

    if len(height) != len(weight):
        raise ValueError(
            "Lists of height and weight must have the same length."
        )

    bmi_values: List[float] = []

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or \
           not isinstance(w, (int, float)):
            raise TypeError(
                "Height and weight values must be int or float."
            )

        if h <= 0 or w <= 0:
            raise ValueError(
                "Height and weight values must be positive."
            )

        bmi = w / (h ** 2)
        bmi_values.append(bmi)

    return bmi_values


def apply_limit(
    bmi: List[Union[int, float]],
    limit: int
) -> List[bool]:
    """
    Return True if BMI is greater than the given limit.
    """

    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list.")

    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be int or float.")

    result: List[bool] = []

    for value in bmi:
        if not isinstance(value, (int, float)):
            raise TypeError(
                "BMI values must be int or float."
            )

        result.append(value > limit)

    return result


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
"""
Temperature Conversion Utilities

- Supports Celsius (C), Fahrenheit (F), Kelvin (K)
- Generic convert_temperature() with validation and rounding
- Interactive CLI for quick conversions
"""

from typing import Iterable, List, Optional, Union


Number = Union[int, float]


_UNIT_ALIASES = {
    "c": "c",
    "cel": "c",
    "celsius": "c",
    "f": "f",
    "fah": "f",
    "fahrenheit": "f",
    "k": "k",
    "kelvin": "k",
}


def _normalize_unit(unit: str) -> str:
    key = unit.strip().lower()
    if key not in _UNIT_ALIASES:
        raise ValueError(
            "Unsupported unit. Use one of: C/Celsius, F/Fahrenheit, K/Kelvin"
        )
    return _UNIT_ALIASES[key]


def c_to_f(value_c: Number) -> float:
    return (float(value_c) * 9.0 / 5.0) + 32.0


def f_to_c(value_f: Number) -> float:
    return (float(value_f) - 32.0) * 5.0 / 9.0


def c_to_k(value_c: Number) -> float:
    return float(value_c) + 273.15


def k_to_c(value_k: Number) -> float:
    value_k = float(value_k)
    if value_k < 0:
        raise ValueError("Kelvin cannot be negative.")
    return value_k - 273.15


def f_to_k(value_f: Number) -> float:
    return c_to_k(f_to_c(value_f))


def k_to_f(value_k: Number) -> float:
    return c_to_f(k_to_c(value_k))


def _to_kelvin(value: Number, unit: str) -> float:
    unit_n = _normalize_unit(unit)
    if unit_n == "k":
        if float(value) < 0:
            raise ValueError("Kelvin cannot be negative.")
        return float(value)
    if unit_n == "c":
        return c_to_k(value)
    if unit_n == "f":
        return f_to_k(value)
    raise ValueError("Unsupported unit")


def _from_kelvin(value_k: Number, unit: str) -> float:
    unit_n = _normalize_unit(unit)
    if unit_n == "k":
        return float(value_k)
    if unit_n == "c":
        return k_to_c(value_k)
    if unit_n == "f":
        return k_to_f(value_k)
    raise ValueError("Unsupported unit")


def convert_temperature(
    value: Union[Number, Iterable[Number]],
    from_unit: str,
    to_unit: str,
    ndigits: Optional[int] = 2,
) -> Union[float, List[float]]:
    def _convert_one(v: Number) -> float:
        k = _to_kelvin(v, from_unit)
        out = _from_kelvin(k, to_unit)
        return round(out, ndigits) if ndigits is not None else out

    if isinstance(value, (list, tuple)):
        return [_convert_one(v) for v in value]
    return _convert_one(value)


def _prompt_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number (e.g., 36.6)")


def _prompt_unit(prompt: str) -> str:
    while True:
        raw = input(prompt).strip()
        try:
            return _normalize_unit(raw)
        except ValueError as e:
            print(e)


def main() -> None:
    print("Temperature Converter")
    print("=" * 24)
    print("Supported units: C (Celsius), F (Fahrenheit), K (Kelvin)")

    from_u = _prompt_unit("From unit (C/F/K): ")
    to_u = _prompt_unit("To unit (C/F/K): ")
    value = _prompt_float("Enter value: ")

    try:
        result = convert_temperature(value, from_u, to_u, ndigits=2)
        print(f"Result: {result} {to_u.upper()}")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()



"""Pixeltable UDFs for the recipe box (recorded by module path, e.g. `udfs.ingredient_count`)."""
import pixeltable as pxt


@pxt.udf
def ingredient_count(ingredients: str | None) -> int:
    """Ingredients are one per line or comma-separated."""
    raw = (ingredients or '').replace('\n', ',')
    return len([i for i in raw.split(',') if i.strip()])


@pxt.udf
def teaser(title: str, minutes: int | None) -> str:
    """'Shakshuka · 25 min' style label."""
    return f'{title} · {minutes} min' if minutes else title

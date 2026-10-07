"""Queries over the recipes table."""
import pixeltable as pxt

from models import Recipes


@pxt.query
def quick_recipes(max_minutes: int):
    """Recipes that fit a time budget, fastest first."""
    return Recipes.where(Recipes.minutes <= max_minutes).select(
        Recipes.id, Recipes.title_blurb, Recipes.n_ingredients
    ).order_by(Recipes.minutes)

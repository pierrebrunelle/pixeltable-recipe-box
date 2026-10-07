"""The recipes table."""
import pixeltable as pxt
import pixeltable.functions as pxtf

from udfs import ingredient_count, teaser

TableModel = pxt.model_base()


class Recipes(TableModel, name='recipes'):
    id = pxt.Column(value=pxtf.uuid.uuid7(), primary_key=True)
    title: pxt.String
    ingredients: pxt.String
    minutes: pxt.Int | None
    notes: pxt.String | None

    n_ingredients = ingredient_count(ingredients)
    title_upper = pxtf.string.upper(title)
    title_blurb = teaser(title, minutes)

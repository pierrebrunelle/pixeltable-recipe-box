"""Recipe Box API built with Pixeltable.

    pxt schema update app.py recipes
    pxt service run app.py recipes
"""
import pixeltable as pxt
import pixeltable.functions as pxtf
from pixeltable.serving import FastAPIRouter

from udfs import ingredient_count, teaser

# ---- tables ----
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


# ---- queries ----
@pxt.query
def quick_recipes(max_minutes: int):
    """Recipes that fit a time budget, fastest first."""
    return Recipes.where(Recipes.minutes <= max_minutes).select(
        Recipes.id, Recipes.title_blurb, Recipes.n_ingredients
    ).order_by(Recipes.minutes)


# ---- routes ----
recipes_api = FastAPIRouter(name='recipes_api')
recipes_api.add_insert_route(
    Recipes, path='/recipes',
    inputs=[Recipes.title, Recipes.ingredients, Recipes.minutes, Recipes.notes],
    outputs=[Recipes.id, Recipes.n_ingredients, Recipes.title_upper, Recipes.title_blurb],
)
recipes_api.add_update_route(
    Recipes, path='/recipes/update',
    inputs=[Recipes.title, Recipes.ingredients, Recipes.minutes, Recipes.notes],
    outputs=[Recipes.id, Recipes.n_ingredients, Recipes.title_upper, Recipes.title_blurb],
)
recipes_api.add_compute_route(Recipes, path='/ingredient-count', inputs=[Recipes.ingredients],
                              outputs=[Recipes.n_ingredients])
recipes_api.add_query_route(path='/recipes/quick', query=quick_recipes, method='get')

"""Recipe Box API built with Pixeltable.

    pxt schema update app.py recipes
    pxt service run app.py recipes
"""
from pixeltable.serving import FastAPIRouter

from models import Recipes, TableModel  # noqa: F401  (TableModel lets `pxt schema` find the models)
from queries import quick_recipes

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

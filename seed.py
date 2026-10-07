"""Seed a few recipes.

Usage:
    python seed.py            # seeds the local `recipes` catalog directory
    python seed.py my_dir     # or another directory you passed to `pxt schema update`
"""
import sys
from pathlib import Path

import pixeltable as pxt

target = sys.argv[1] if len(sys.argv) > 1 else 'recipes'
HERE = Path(__file__).resolve().parent

SEED = {
    'recipes': [
        {'title': 'Shakshuka', 'ingredients': 'eggs, tomatoes, onion, garlic, cumin, paprika, feta', 'minutes': 25, 'notes': None},
        {'title': 'Weeknight dal', 'ingredients': 'red lentils\nturmeric\nginger\ncoconut milk\nspinach', 'minutes': 30, 'notes': 'freezes well'},
        {'title': 'Slow beef ragu', 'ingredients': 'chuck, carrot, celery, onion, wine, tomato', 'minutes': 180, 'notes': None},
        {'title': 'Avocado toast', 'ingredients': 'bread, avocado, lemon, chili flakes', 'minutes': 8, 'notes': None},
    ],
}

for table_name, rows in SEED.items():
    t = pxt.get_table(f'{target}/{table_name}')
    if t.count() > 0:
        print(f'{target}/{table_name} already has {t.count()} rows; skipping')
        continue
    for row in rows:
        for k, v in row.items():
            if isinstance(v, str) and v.startswith('data/'):
                row[k] = str(HERE / v)   # local sample media file
    t.insert(rows)
    print(f'inserted {len(rows)} rows into {target}/{table_name}')

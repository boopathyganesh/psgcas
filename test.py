import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


print(BASE_DIR)
print(STATIC_ROOT)
print(STATICFILES_DIRS)
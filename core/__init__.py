# Core package initializer
# This file can stay empty or used for imports later

from .db import init_db, save_result, get_results
from .logic import grade_exam
from .auth import login
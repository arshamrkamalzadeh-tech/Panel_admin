import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_panel import app  # noqa: E402,F401  (Vercel دنبال متغیر app می‌گرده)

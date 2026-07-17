# ═══════════════════════════════════════════════════════════════
#  DAEDALUS DIGEST — CONFIG
#  This is the ONLY file you need to edit.
# ═══════════════════════════════════════════════════════════════

# ── YOUR CREDENTIALS ────────────────────────────────────────────
# Get your Anthropic API key at: console.anthropic.com → API Keys
# Get your Gmail App Password at: myaccount.google.com → Security → 2-Step Verification → App Passwords
# Set these as environment variables (see README) — don't paste them directly here.

import os

ANTHROPIC_API_KEY  = os.environ.get("ANTHROPIC_API_KEY", "")
GMAIL_ADDRESS      = os.environ.get("GMAIL_ADDRESS", "")       # the gmail you send FROM
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "")  # 16-char app password
TO_EMAIL           = os.environ.get("TO_EMAIL", GMAIL_ADDRESS) # who receives the digest

# ── DIGEST SETTINGS ─────────────────────────────────────────────
DIGEST_NAME   = "Daedalus Digest"   # appears in the email header
YOUR_NAME     = "Jonah"             # Claude uses this to personalize the writing
PAPERS_PER_DAY = 5                  # how many papers per email (2 = lean, 5 = full read)

# ── YOUR TOPICS ─────────────────────────────────────────────────
# Each topic has:
#   label   — display name in the email
#   emoji   — shown in the section header
#   query   — search terms (be broad for more variety)
#   source  — "pubmed" for biology/medicine, "arxiv" for everything else
#   category — (arxiv only) narrows to a subject area. Remove the line to search all of arxiv.
#
# Common arxiv categories:
#   physics, cond-mat, cs, math, q-bio, eess, astro-ph, quant-ph
#
# Add, remove, or edit topics freely. The script picks PAPERS_PER_DAY topics
# randomly each day and rotates through all of them over time.

TOPICS = [
    {
        "label":    "Physics",
        "emoji":    "⚛️",
        "query":    "physics",
        "source":   "arxiv",
        "category": "physics",
    },
    {
        "label":    "Chemistry",
        "emoji":    "🧪",
        "query":    "chemistry materials synthesis",
        "source":   "arxiv",
        "category": "physics.chem-ph",
    },
    {
        "label":    "Biology",
        "emoji":    "🧬",
        "query":    "biology genetics cell molecular",
        "source":   "pubmed",
    },
    {
        "label":    "Computer Science",
        "emoji":    "💻",
        "query":    "machine learning algorithms computer science",
        "source":   "arxiv",
        "category": "cs",
    },
    {
        "label":    "Mathematics",
        "emoji":    "📐",
        "query":    "mathematics theorem proof",
        "source":   "arxiv",
        "category": "math",
    },
    {
        "label":    "Materials Science",
        "emoji":    "🧱",
        "query":    "materials science nanomaterials",
        "source":   "arxiv",
        "category": "cond-mat",
    },
    {
        "label":    "Mechanical Engineering",
        "emoji":    "⚙️",
        "query":    "mechanical engineering robotics systems",
        "source":   "arxiv",
        "category": "eess",
    },
    {
        "label":    "Medicine",
        "emoji":    "⚕️",
        "query":    "medicine clinical treatment therapy",
        "source":   "pubmed",
    },
    {
        "label":    "Environmental Science",
        "emoji":    "🌍",
        "query":    "environmental science climate ecology",
        "source":   "arxiv",
        "category": "physics.ao-ph",
    },
    {
        "label":    "Neuroscience",
        "emoji":    "🧠",
        "query":    "neuroscience brain cognition",
        "source":   "pubmed",
    },
    {
        "label":    "Astronomy",
        "emoji":    "🔭",
        "query":    "astronomy astrophysics cosmology",
        "source":   "arxiv",
        "category": "astro-ph",
    },
    {
        "label":    "Electrical Engineering",
        "emoji":    "🔌",
        "query":    "electrical engineering circuits devices power",
        "source":   "arxiv",
        "category": "eess",
    },
]

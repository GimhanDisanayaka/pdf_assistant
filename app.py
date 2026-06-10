import streamlit as st
import pdfplumber
import io
import json
import re
import time

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CHAKRA",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    /* ── Global Background ── */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        min-height: 100vh;
        font-family: 'Inter', sans-serif;
    }
    .stApp::before {
        content: '';
        position: fixed;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background:
            radial-gradient(ellipse at 20% 20%, rgba(120, 80, 255, 0.15) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 80%, rgba(0, 180, 255, 0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 50%, rgba(255, 100, 180, 0.05) 0%, transparent 60%);
        pointer-events: none;
        z-index: 0;
    }

    /* ── Sidebar Glass ── */
    [data-testid="stSidebar"] {
        background: rgba(15, 12, 41, 0.6) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    [data-testid="stSidebar"] * {
        color: rgba(255, 255, 255, 0.85) !important;
    }
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stSlider label,
    [data-testid="stSidebar"] .stRadio label,
    [data-testid="stSidebar"] .stCheckbox label {
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.03em !important;
        text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] h2 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        color: rgba(150, 120, 255, 0.9) !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] .stSelectbox > div > div,
    [data-testid="stSidebar"] .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.06) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 10px !important;
        color: white !important;
        backdrop-filter: blur(10px) !important;
    }
    [data-testid="stSidebar"] .stSlider > div > div > div {
        background: linear-gradient(90deg, #7c3aed, #3b82f6) !important;
    }

    /* ── Main Header ── */
    .main-header {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa 0%, #60a5fa 50%, #34d399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
        line-height: 1.1;
        margin-bottom: 0.3rem;
    }
    .sub-header {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.5);
        margin-bottom: 1.8rem;
        font-weight: 400;
        letter-spacing: 0.01em;
    }

    /* ── Glass Cards ── */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.4rem 1.5rem;
        margin-bottom: 0.6rem;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        transition: all 0.3s ease;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.2);
    }
    .feature-card:hover {
        background: rgba(255, 255, 255, 0.09);
        border-color: rgba(124, 58, 237, 0.4);
        transform: translateY(-2px);
        box-shadow: 0 8px 32px rgba(124, 58, 237, 0.2);
    }
    .feature-card h4 {
        color: rgba(255, 255, 255, 0.92) !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 0.4rem !important;
    }
    .feature-card p {
        color: rgba(255, 255, 255, 0.5) !important;
        font-size: 0.85rem !important;
        line-height: 1.5 !important;
        margin: 0 !important;
    }

    /* ── Result Box ── */
    .result-box {
        background: rgba(59, 130, 246, 0.08);
        border: 1px solid rgba(59, 130, 246, 0.25);
        border-left: 3px solid #3b82f6;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        backdrop-filter: blur(12px);
        color: rgba(255,255,255,0.85);
    }

    /* ── Buttons ── */
    .stButton > button {
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        letter-spacing: 0.02em !important;
        transition: all 0.25s ease !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #7c3aed 0%, #3b82f6 100%) !important;
        border: none !important;
        color: white !important;
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4) !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 28px rgba(124, 58, 237, 0.55) !important;
    }
    .stButton > button:not([kind="primary"]) {
        background: rgba(255, 255, 255, 0.07) !important;
        color: rgba(255, 255, 255, 0.85) !important;
    }
    .stButton > button:not([kind="primary"]):hover {
        background: rgba(255, 255, 255, 0.12) !important;
        transform: translateY(-1px) !important;
    }

    /* ── Quiz Answers ── */
    .quiz-option { margin: 4px 0; }
    .correct-answer {
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.35);
        border-radius: 10px;
        padding: 8px 14px;
        color: #6ee7b7 !important;
        font-weight: 500;
    }
    .wrong-answer {
        background: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 10px;
        padding: 8px 14px;
        color: #fca5a5 !important;
        font-weight: 500;
    }

    /* ── Score Box ── */
    .score-box {
        background: linear-gradient(135deg, rgba(124, 58, 237, 0.3) 0%, rgba(59, 130, 246, 0.3) 100%);
        border: 1px solid rgba(124, 58, 237, 0.4);
        color: white;
        border-radius: 20px;
        padding: 2.5rem;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 1.2rem 0;
        backdrop-filter: blur(20px);
        box-shadow: 0 8px 40px rgba(124, 58, 237, 0.25), inset 0 1px 0 rgba(255,255,255,0.1);
        font-family: 'Space Grotesk', sans-serif;
    }

    /* ── Countdown Box ── */
    .countdown-box {
        font-size: 1.8rem;
        font-weight: 800;
        color: #ef4444;
        text-align: center;
        padding: 0.5rem;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* ── Sinhala Word ── */
    .sinhala-word {
        color: #a78bfa;
        font-style: italic;
        font-size: 0.85em;
    }

    /* ── Metrics ── */
    [data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 14px !important;
        padding: 1rem 1.2rem !important;
        backdrop-filter: blur(12px) !important;
    }
    [data-testid="metric-container"] [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.5) !important;
        font-size: 0.75rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
    }
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: rgba(255, 255, 255, 0.95) !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
    }

    /* ── Expanders ── */
    [data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(12px) !important;
    }
    [data-testid="stExpander"] summary {
        color: rgba(255, 255, 255, 0.75) !important;
        font-weight: 500 !important;
    }

    /* ── File Uploader ── */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 2px dashed rgba(124, 58, 237, 0.4) !important;
        border-radius: 16px !important;
        backdrop-filter: blur(12px) !important;
        transition: all 0.3s ease !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: rgba(124, 58, 237, 0.7) !important;
        background: rgba(124, 58, 237, 0.06) !important;
    }
    [data-testid="stFileUploader"] * {
        color: rgba(255, 255, 255, 0.7) !important;
    }

    /* ── Dividers ── */
    hr {
        border-color: rgba(255, 255, 255, 0.08) !important;
        margin: 1.5rem 0 !important;
    }

    /* ── General text ── */
    .stMarkdown p, .stMarkdown li, .stMarkdown {
        color: rgba(255, 255, 255, 0.8) !important;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: rgba(255, 255, 255, 0.95) !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    .stMarkdown strong {
        color: #a78bfa !important;
    }

    /* ── Radio & Checkboxes ── */
    [data-testid="stRadio"] label,
    [data-testid="stCheckbox"] label {
        color: rgba(255, 255, 255, 0.8) !important;
    }

    /* ── Spinner ── */
    [data-testid="stSpinner"] {
        color: #7c3aed !important;
    }

    /* ── Success / Error / Warning ── */
    [data-testid="stAlert"] {
        border-radius: 12px !important;
        backdrop-filter: blur(12px) !important;
    }
    .stSuccess {
        background: rgba(16, 185, 129, 0.1) !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
        color: #6ee7b7 !important;
    }
    .stError {
        background: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
    }
    .stWarning {
        background: rgba(245, 158, 11, 0.1) !important;
        border: 1px solid rgba(245, 158, 11, 0.3) !important;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(124, 58, 237, 0.4); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(124, 58, 237, 0.6); }

    /* ── Text Areas ── */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: rgba(255, 255, 255, 0.8) !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* ── Download Buttons ── */
    [data-testid="stDownloadButton"] button {
        background: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 10px !important;
        color: rgba(255, 255, 255, 0.85) !important;
        font-weight: 500 !important;
        transition: all 0.25s ease !important;
    }
    [data-testid="stDownloadButton"] button:hover {
        background: rgba(124, 58, 237, 0.2) !important;
        border-color: rgba(124, 58, 237, 0.5) !important;
        transform: translateY(-1px) !important;
    }

    /* ── Caption ── */
    .stCaption, [data-testid="stCaptionContainer"] {
        color: rgba(255, 255, 255, 0.4) !important;
        font-size: 0.78rem !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Session state init ─────────────────────────────────────────────────────────
for key, default in {
    "quiz_questions": [],
    "quiz_answers": {},
    "quiz_submitted": False,
    "quiz_score": 0,
    "quiz_start_time": None,
    "quiz_time_limit": 0,
    "quiz_expired": False,
    "notes_pdf_bytes": None,
    "mindmap_data": None,
    "generated_result": "",
    "generated_type": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Configuration")

    api_choice = st.selectbox(
        "AI Provider",
        ["OpenAI", "Google Gemini"],
        help="Choose which AI service powers the generation.",
    )

    api_key = st.text_input(
        f"{'OpenAI' if api_choice == 'OpenAI' else 'Gemini'} API Key",
        type="password",
        placeholder="sk-... or AIza...",
        help="Your key is never stored or logged.",
    )

    if api_choice == "OpenAI":
        model = st.selectbox(
            "Model",
            ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
        )
    else:
        model = st.selectbox(
            "Model",
            ["gemini-2.0-flash", "gemini-2.5-flash", "gemini-2.5-pro"],
        )

    st.divider()
    st.markdown("## 📋 Output Settings")

    output_type = st.radio(
        "What do you want to generate?",
        ["📝 Short Notes", "🧠 Quiz", "💬 Q&A Pairs", "🗺️ Mind Map"],
    )

    max_pages = st.slider("Max pages to process", 1, 100, 15)
    num_items = st.slider("Number of items", 3, 20, 10)

    if "Quiz" in output_type:
        st.divider()
        st.markdown("## ⏱️ Quiz Settings")
        time_per_q = st.slider("Seconds per question", 10, 60, 30)

    sinhala_mode = st.checkbox("🇱🇰 Show Sinhala meanings", value=True,
                                help="Add Sinhala translation after each English term.")

    st.divider()
    st.caption("• Keep PDFs under 50 pages for best results.\n"
               "• Text-based PDFs work better than scanned ones.")

# ── Helpers ────────────────────────────────────────────────────────────────────

import html as _html  # for escaping SVG text content


def notes_to_image(notes_text):
    """Render markdown notes to a PNG image using Pillow."""
    from PIL import Image, ImageDraw, ImageFont
    import textwrap

    W = 900
    MARGIN = 40
    LINE_H_BODY = 22
    LINE_H_H2 = 32
    LINE_H_H3 = 27
    BG = (15, 12, 41)
    C_BODY = (200, 190, 240)
    C_H2 = (139, 92, 246)
    C_H3 = (167, 139, 250)
    C_TITLE = (226, 217, 255)

    try:
        font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
        font_h3   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 17)
        font_h2   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 21)
        font_title= ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    except Exception:
        font_body = font_bold = font_h3 = font_h2 = font_title = ImageFont.load_default()

    # First pass: measure height
    lines_info = []
    for raw in notes_text.split("\n"):
        line = raw.strip()
        if not line:
            lines_info.append(("space", "", None, 10))
            continue
        # Strip markdown bold for plain rendering
        plain = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
        if line.startswith("## "):
            wrapped = textwrap.wrap(plain[3:], width=52)
            for w in wrapped:
                lines_info.append(("h2", w, font_h2, LINE_H_H2))
        elif line.startswith("### "):
            wrapped = textwrap.wrap(plain[4:], width=60)
            for w in wrapped:
                lines_info.append(("h3", w, font_h3, LINE_H_H3))
        elif line.startswith("# "):
            wrapped = textwrap.wrap(plain[2:], width=48)
            for w in wrapped:
                lines_info.append(("title", w, font_title, 40))
        elif line.startswith("- ") or line.startswith("* "):
            wrapped = textwrap.wrap("• " + plain[2:], width=72)
            for w in wrapped:
                lines_info.append(("body", w, font_body, LINE_H_BODY))
        else:
            wrapped = textwrap.wrap(plain, width=72)
            for w in (wrapped or [plain]):
                lines_info.append(("body", w, font_body, LINE_H_BODY))

    total_h = MARGIN * 2 + sum(li[3] for li in lines_info) + 60
    img = Image.new("RGB", (W, max(total_h, 200)), BG)
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([0, 0, W, 60], fill=(48, 43, 99))
    draw.text((MARGIN, 14), "🔮 CHAKRA Notes", fill=(226, 217, 255), font=font_title)

    y = 70
    for kind, text, font, lh in lines_info:
        if kind == "space":
            y += lh
            continue
        color = {"h2": C_H2, "h3": C_H3, "title": C_TITLE}.get(kind, C_BODY)
        if kind == "h2":
            draw.line([(MARGIN, y + lh - 4), (W - MARGIN, y + lh - 4)], fill=C_H2, width=1)
        draw.text((MARGIN, y), text, fill=color, font=font)
        y += lh

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def svg_to_png(svg_string):
    """Convert SVG string to PNG bytes using cairosvg."""
    try:
        import cairosvg
        return cairosvg.svg2png(bytestring=svg_string.encode("utf-8"), scale=2.0)
    except ImportError:
        # Fallback: return None if cairosvg not available
        return None


def extract_text(file_obj, max_pages):
    pages_text = []
    with pdfplumber.open(file_obj) as pdf:
        total = len(pdf.pages)
        limit = min(total, max_pages)
        for i in range(limit):
            t = pdf.pages[i].extract_text()
            if t:
                pages_text.append(f"[Page {i+1}]\n{t}")
    return "\n\n".join(pages_text).strip(), total


def build_prompt(text, output_type, num_items, sinhala):
    excerpt = text[:12_000]
    sinhala_instruction = (
        "\n- After EVERY key term or important English word/phrase, add its Sinhala meaning in parentheses like: **Photosynthesis** (ප්‍රභාසංශ්ලේෂණය)"
        if sinhala else ""
    )

    if "Notes" in output_type:
        return f"""You are an expert study assistant.
Produce well-structured study notes from the document below.

Rules:
- Use clear Markdown headings (##, ###) and bullet points.
- Highlight key terms in **bold**.{sinhala_instruction}
- Be concise but thorough.
- Group related ideas logically.

Document:
\"\"\"
{excerpt}
\"\"\"
Generate the study notes now:"""

    if "Quiz" in output_type:
        return f"""You are an expert educator.
Create a {num_items}-question multiple-choice quiz from the document below.

Return ONLY a valid JSON array — no other text, no markdown fences. Each element:
{{
  "question": "...",
  "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
  "answer": "A",
  "explanation": "..."
}}

Document:
\"\"\"
{excerpt}
\"\"\"
Return the JSON array now:"""

    if "Q&A" in output_type:
        return f"""You are an expert tutor.
Generate {num_items} high-quality Q&A pairs from the document below.

Format EXACTLY:
**Q:** [Question]{' (සිංහල: [Sinhala translation of key terms used])' if sinhala else ''}
**A:** [Detailed answer in 2-4 sentences]{' — Key terms: **term** (සිංහල meaning)' if sinhala else ''}

---

Document:
\"\"\"
{excerpt}
\"\"\"
Generate the Q&A pairs now:"""

    if "Mind Map" in output_type:
        return f"""You are an expert educator creating a mind map.
Analyse the document and extract a hierarchical mind map structure.

Return ONLY a valid JSON object — no markdown fences:
{{
  "central": "Main Topic",
  "branches": [
    {{
      "label": "Branch 1",
      "children": ["sub-topic 1", "sub-topic 2"]
    }}
  ]
}}

Produce 4-7 main branches, each with 2-5 children.{' Add Sinhala meanings for key terms like: "Photosynthesis (ප්‍රභාසංශ්ලේෂණය)"' if sinhala else ''}

Document:
\"\"\"
{excerpt}
\"\"\"
Return the JSON now:"""
    return ""


def call_ai(prompt, api_choice, api_key, model):
    if api_choice == "OpenAI":
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=3000,
        )
        return resp.choices[0].message.content
    else:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        gen_model = genai.GenerativeModel(model)
        resp = gen_model.generate_content(prompt)
        return resp.text


def parse_json_safe(text):
    """Strip markdown fences and parse JSON."""
    text = re.sub(r"```(?:json)?", "", text).strip().rstrip("`").strip()
    return json.loads(text)


def notes_to_pdf(notes_text):
    """Convert markdown notes to a downloadable PDF using reportlab."""
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib import colors
    import io as _io

    buf = _io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle('CustomTitle', parent=styles['Title'],
                                  fontSize=18, textColor=colors.HexColor('#1f2937'),
                                  spaceAfter=12)
    h2_style = ParagraphStyle('H2', parent=styles['Heading2'],
                               fontSize=14, textColor=colors.HexColor('#3b82f6'),
                               spaceBefore=12, spaceAfter=4)
    h3_style = ParagraphStyle('H3', parent=styles['Heading3'],
                               fontSize=12, textColor=colors.HexColor('#374151'),
                               spaceBefore=8, spaceAfter=2)
    body_style = ParagraphStyle('Body', parent=styles['Normal'],
                                 fontSize=10, leading=15,
                                 textColor=colors.HexColor('#374151'))
    bullet_style = ParagraphStyle('Bullet', parent=body_style,
                                   leftIndent=20, bulletIndent=10,
                                   spaceAfter=3)

    story = []
    story.append(Paragraph("🔮 CHAKRA Notes", title_style))
    story.append(Spacer(1, 0.3*cm))

    for raw_line in notes_text.split("\n"):
        line = raw_line.strip()
        if not line:
            story.append(Spacer(1, 0.2*cm))
            continue

        # Convert markdown bold (**text**) to reportlab <b>
        line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
        # Escape ampersands for XML
        line = line.replace('&', '&amp;')

        if line.startswith("## "):
            story.append(Paragraph(line[3:], h2_style))
        elif line.startswith("### "):
            story.append(Paragraph(line[4:], h3_style))
        elif line.startswith("# "):
            story.append(Paragraph(line[2:], title_style))
        elif line.startswith("- ") or line.startswith("* "):
            story.append(Paragraph(f"• {line[2:]}", bullet_style))
        else:
            story.append(Paragraph(line, body_style))

    doc.build(story)
    return buf.getvalue()


def render_mindmap(data):
    """Render an SVG mind map from the JSON data structure."""
    import math

    central = data.get("central", "Topic")
    branches = data.get("branches", [])

    W, H = 900, 620
    cx, cy = W // 2, H // 2

    branch_colors = [
        "#3b82f6","#10b981","#f59e0b","#ef4444",
        "#8b5cf6","#ec4899","#06b6d4","#84cc16"
    ]

    def _esc(s):
        """Escape XML special characters for safe SVG text content."""
        return _html.escape(str(s), quote=False)

    svg_parts = [
        f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
        f'style="font-family:Inter,sans-serif;border-radius:20px;display:block;">',
        f'<defs>'
        f'<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">'
        f'<stop offset="0%" stop-color="#0f0c29"/>'
        f'<stop offset="50%" stop-color="#1a1545"/>'
        f'<stop offset="100%" stop-color="#0f172a"/>'
        f'</linearGradient>'
        f'<filter id="glow"><feGaussianBlur stdDeviation="3" result="coloredBlur"/>'
        f'<feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        f'</defs>',
        f'<rect width="{W}" height="{H}" fill="url(#bg)" rx="20"/>',
        f'<ellipse cx="{cx}" cy="{cy}" rx="95" ry="40" fill="rgba(124,58,237,0.25)" '
        f'stroke="rgba(167,139,250,0.6)" stroke-width="1.5"/>',
        f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="middle" '
        f'fill="#e2d9ff" font-size="13" font-weight="700">{_esc(central[:28])}</text>',
    ]

    n = len(branches)
    for i, branch in enumerate(branches):
        angle = (2 * math.pi * i / n) - math.pi / 2
        bx = cx + int(210 * math.cos(angle))
        by = cy + int(170 * math.sin(angle))
        color = branch_colors[i % len(branch_colors)]
        label = branch.get("label", "")
        children = branch.get("children", [])

        # Line from center to branch
        svg_parts.append(
            f'<line x1="{cx}" y1="{cy}" x2="{bx}" y2="{by}" '
            f'stroke="{color}" stroke-width="2" stroke-opacity="0.5"/>'
        )
        # Branch node with glass effect
        svg_parts.append(
            f'<rect x="{bx-62}" y="{by-19}" width="124" height="38" rx="10" '
            f'fill="{color}" fill-opacity="0.18" stroke="{color}" stroke-opacity="0.6" stroke-width="1.2"/>'
        )
        svg_parts.append(
            f'<text x="{bx}" y="{by}" text-anchor="middle" dominant-baseline="middle" '
            f'fill="white" font-size="10" font-weight="600">{_esc(label[:20])}</text>'
        )

        # Children
        nc = len(children)
        for j, child in enumerate(children):
            if nc == 1:
                spread = 0
            else:
                spread = (math.pi / 3) * (j / (nc - 1) - 0.5)
            child_angle = angle + spread
            dist = 130
            child_x = bx + int(dist * math.cos(child_angle))
            child_y = by + int(dist * math.sin(child_angle))

            svg_parts.append(
                f'<line x1="{bx}" y1="{by}" x2="{child_x}" y2="{child_y}" '
                f'stroke="{color}" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="4,4"/>'
            )
            svg_parts.append(
                f'<rect x="{child_x-50}" y="{child_y-13}" width="100" height="26" '
                f'rx="7" fill="{color}" fill-opacity="0.1" stroke="{color}" stroke-opacity="0.35" stroke-width="1"/>'
            )
            short = child[:18] + ("…" if len(child) > 18 else "")
            svg_parts.append(
                f'<text x="{child_x}" y="{child_y}" text-anchor="middle" dominant-baseline="middle" '
                f'fill="rgba(255,255,255,0.8)" font-size="9">{_esc(short)}</text>'
            )

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


# ── Main UI ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="display:flex; align-items:center; gap:18px; margin-bottom:0.2rem;">
  <!-- CHAKRA SVG Logo -->
  <svg width="64" height="64" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <radialGradient id="cg1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#c084fc"/>
        <stop offset="100%" stop-color="#7c3aed"/>
      </radialGradient>
      <radialGradient id="cg2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#60a5fa"/>
        <stop offset="100%" stop-color="#2563eb"/>
      </radialGradient>
      <filter id="glow">
        <feGaussianBlur stdDeviation="2" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <!-- Outer ring -->
    <circle cx="32" cy="32" r="30" fill="none" stroke="url(#cg1)" stroke-width="2.5" opacity="0.7"/>
    <!-- Rotating spokes (8 petals) -->
    <g filter="url(#glow)">
      <ellipse cx="32" cy="14" rx="4.5" ry="8" fill="url(#cg1)" opacity="0.85" transform="rotate(0 32 32)"/>
      <ellipse cx="32" cy="14" rx="4.5" ry="8" fill="url(#cg2)" opacity="0.7" transform="rotate(45 32 32)"/>
      <ellipse cx="32" cy="14" rx="4.5" ry="8" fill="url(#cg1)" opacity="0.85" transform="rotate(90 32 32)"/>
      <ellipse cx="32" cy="14" rx="4.5" ry="8" fill="url(#cg2)" opacity="0.7" transform="rotate(135 32 32)"/>
      <ellipse cx="32" cy="14" rx="4.5" ry="8" fill="url(#cg1)" opacity="0.85" transform="rotate(180 32 32)"/>
      <ellipse cx="32" cy="14" rx="4.5" ry="8" fill="url(#cg2)" opacity="0.7" transform="rotate(225 32 32)"/>
      <ellipse cx="32" cy="14" rx="4.5" ry="8" fill="url(#cg1)" opacity="0.85" transform="rotate(270 32 32)"/>
      <ellipse cx="32" cy="14" rx="4.5" ry="8" fill="url(#cg2)" opacity="0.7" transform="rotate(315 32 32)"/>
    </g>
    <!-- Inner circle -->
    <circle cx="32" cy="32" r="8" fill="url(#cg1)" opacity="0.95" filter="url(#glow)"/>
    <circle cx="32" cy="32" r="4" fill="white" opacity="0.9"/>
  </svg>
  <p class="main-header" style="margin:0;">CHAKRA</p>
</div>
""", unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">Upload a PDF → generate Notes, Quizzes (with timer & score), Q&A, or Mind Maps — with Sinhala meanings!</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="font-size:0.72rem; color:rgba(167,139,250,0.55); margin-top:-1rem; margin-bottom:1.2rem; letter-spacing:0.12em; font-family:\'Space Grotesk\',sans-serif;">Developed by <span style=\'color:rgba(167,139,250,0.85); font-weight:600;\'>GIMA VERSE</span></p>',
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    "Drop your PDF here or click to browse",
    type=["pdf"],
    label_visibility="collapsed",
)

if not uploaded_file:
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="feature-card"><h4>📝 Short Notes</h4>'
                    '<p>Structured summaries with Sinhala meanings. Download as PDF!</p></div>',
                    unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feature-card"><h4>🧠 Quiz</h4>'
                    '<p>MCQ quiz with countdown timer and final score report.</p></div>',
                    unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="feature-card"><h4>💬 Q&A Pairs</h4>'
                    '<p>Question-answer pairs with Sinhala key term translations.</p></div>',
                    unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="feature-card"><h4>🗺️ Mind Map</h4>'
                    '<p>Visual mind map of document structure with key concepts.</p></div>',
                    unsafe_allow_html=True)
    st.stop()

# ── Extract PDF ────────────────────────────────────────────────────────────────
with st.spinner("🔍 Extracting text from your PDF…"):
    try:
        pdf_text, total_pages = extract_text(uploaded_file, max_pages)
    except Exception as e:
        st.error(f"Failed to read PDF: {e}")
        st.stop()

if not pdf_text:
    st.error("⚠️ No text could be extracted. This PDF may be scanned/image-based.")
    st.stop()

col_a, col_b, col_c = st.columns(3)
col_a.metric("Total pages", total_pages)
col_b.metric("Pages processed", min(total_pages, max_pages))
col_c.metric("Characters extracted", f"{len(pdf_text):,}")

with st.expander("📄 Preview extracted text", expanded=False):
    preview = pdf_text[:3000] + ("\n\n…[truncated]" if len(pdf_text) > 3000 else "")
    st.text_area("", preview, height=220, label_visibility="collapsed")

st.divider()

# ── Generate button ────────────────────────────────────────────────────────────
_, btn_col, _ = st.columns([2, 1.5, 2])
with btn_col:
    run = st.button(f"🚀 Generate {output_type}", type="primary", use_container_width=True)

if run:
    if not api_key:
        st.warning("⬅️ Enter your API key in the sidebar first.", icon="🔑")
        st.stop()

    # Reset quiz state on new generation
    st.session_state.quiz_questions = []
    st.session_state.quiz_answers = {}
    st.session_state.quiz_submitted = False
    st.session_state.quiz_start_time = None
    st.session_state.quiz_expired = False
    st.session_state.notes_pdf_bytes = None
    st.session_state.mindmap_data = None

    prompt = build_prompt(pdf_text, output_type, num_items, sinhala_mode)

    with st.spinner(f"✨ Generating {output_type}…"):
        try:
            result = call_ai(prompt, api_choice, api_key, model)
        except Exception as e:
            st.error(f"API error: {e}")
            st.stop()

    st.session_state.generated_result = result
    st.session_state.generated_type = output_type

    # Post-process quiz / mindmap JSON
    if "Quiz" in output_type:
        try:
            questions = parse_json_safe(result)
            st.session_state.quiz_questions = questions
            st.session_state.quiz_start_time = time.time()
            st.session_state.quiz_time_limit = num_items * time_per_q
        except Exception as e:
            st.error(f"Failed to parse quiz JSON: {e}\n\nRaw output:\n{result}")
            st.stop()

    elif "Mind Map" in output_type:
        try:
            st.session_state.mindmap_data = parse_json_safe(result)
        except Exception as e:
            st.error(f"Failed to parse mind map JSON: {e}\n\nRaw:\n{result}")
            st.stop()

    elif "Notes" in output_type:
        try:
            pdf_bytes = notes_to_pdf(result)
            st.session_state.notes_pdf_bytes = pdf_bytes
        except Exception as e:
            st.warning(f"PDF generation failed: {e}")

# ══════════════════════════════════════════════════════════════════════════════
# RENDER RESULTS
# ══════════════════════════════════════════════════════════════════════════════

result      = st.session_state.generated_result
output_type = st.session_state.generated_type

if not result:
    st.stop()

st.success(f"✅ {output_type} generated!")

# ── SHORT NOTES ────────────────────────────────────────────────────────────────
if "Notes" in output_type:
    st.markdown(f"### {output_type}")
    st.markdown(result)
    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button(
            "⬇️ Download as .txt",
            data=result,
            file_name=f"notes_{uploaded_file.name.replace('.pdf','')}.txt",
            mime="text/plain",
        )
    with col2:
        if st.session_state.notes_pdf_bytes:
            st.download_button(
                "📄 Download as PDF",
                data=st.session_state.notes_pdf_bytes,
                file_name=f"notes_{uploaded_file.name.replace('.pdf','')}.pdf",
                mime="application/pdf",
            )
    with col3:
        try:
            img_bytes = notes_to_image(result)
            st.download_button(
                "🖼️ Download as Image",
                data=img_bytes,
                file_name=f"notes_{uploaded_file.name.replace('.pdf','')}.png",
                mime="image/png",
            )
        except Exception as e:
            st.caption(f"Image export unavailable: {e}")

# ── MIND MAP ───────────────────────────────────────────────────────────────────
elif "Mind Map" in output_type:
    st.markdown("### 🗺️ Mind Map")
    if st.session_state.mindmap_data:
        svg = render_mindmap(st.session_state.mindmap_data)
        st.markdown(svg, unsafe_allow_html=True)

        with st.expander("📋 Mind Map Structure (JSON)"):
            st.json(st.session_state.mindmap_data)

        col_mm1, col_mm2 = st.columns(2)
        with col_mm1:
            st.download_button(
                "⬇️ Download SVG",
                data=svg,
                file_name=f"mindmap_{uploaded_file.name.replace('.pdf','')}.svg",
                mime="image/svg+xml",
            )
        with col_mm2:
            png_bytes = svg_to_png(svg)
            if png_bytes:
                st.download_button(
                    "🖼️ Download as Image (PNG)",
                    data=png_bytes,
                    file_name=f"mindmap_{uploaded_file.name.replace('.pdf','')}.png",
                    mime="image/png",
                )
            else:
                st.caption("PNG export unavailable (install cairosvg for PNG support)")

# ── Q&A PAIRS ──────────────────────────────────────────────────────────────────
elif "Q&A" in output_type:
    st.markdown("### 💬 Q&A Pairs")
    st.markdown(result)
    st.divider()
    st.download_button(
        "⬇️ Download as .txt",
        data=result,
        file_name=f"qa_{uploaded_file.name.replace('.pdf','')}.txt",
        mime="text/plain",
    )

# ── INTERACTIVE QUIZ ───────────────────────────────────────────────────────────
elif "Quiz" in output_type:
    questions = st.session_state.quiz_questions
    if not questions:
        st.stop()

    # ── Countdown timer ──────────────────────────────────────────────────────
    if not st.session_state.quiz_submitted and not st.session_state.quiz_expired:
        elapsed = time.time() - (st.session_state.quiz_start_time or time.time())
        remaining = max(0, int(st.session_state.quiz_time_limit - elapsed))

        timer_col, _ = st.columns([1, 3])
        with timer_col:
            mins, secs = divmod(remaining, 60)
            color = "#ef4444" if remaining < 30 else "#f59e0b" if remaining < 60 else "#10b981"
            st.markdown(
                f'<div style="background:{color}15;border:2px solid {color};border-radius:10px;'
                f'padding:10px;text-align:center;">'
                f'<span style="font-size:1.6rem;font-weight:800;color:{color}">⏱ {mins:02d}:{secs:02d}</span>'
                f'</div>', unsafe_allow_html=True
            )
        if remaining == 0:
            st.session_state.quiz_expired = True
            st.rerun()

    if st.session_state.quiz_expired and not st.session_state.quiz_submitted:
        st.error("⏰ Time's up! Auto-submitting your quiz…")
        st.session_state.quiz_submitted = True

    st.markdown("### 🧠 Quiz")

    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}.** {q['question']}")
        opts = q.get("options", {})
        key = f"q_{i}"

        if st.session_state.quiz_submitted:
            chosen = st.session_state.quiz_answers.get(key)
            correct = q.get("answer", "")
            for letter, text in opts.items():
                if letter == correct:
                    st.markdown(f'<div class="correct-answer">✅ {letter}) {text}</div>',
                                unsafe_allow_html=True)
                elif letter == chosen and chosen != correct:
                    st.markdown(f'<div class="wrong-answer">❌ {letter}) {text}</div>',
                                unsafe_allow_html=True)
                else:
                    st.markdown(f"&nbsp;&nbsp;{letter}) {text}")
            exp = q.get("explanation", "")
            if exp:
                st.caption(f"💡 {exp}")
        else:
            option_labels = [f"{k}) {v}" for k, v in opts.items()]
            choice = st.radio(
                f"q{i+1}",
                option_labels,
                key=key,
                label_visibility="collapsed",
                index=None,
            )
            if choice:
                st.session_state.quiz_answers[key] = choice[0]  # first char = letter

        st.markdown("---")

    # ── Submit / Score ──────────────────────────────────────────────────────
    if not st.session_state.quiz_submitted:
        _, sub_col, _ = st.columns([2, 1.5, 2])
        with sub_col:
            if st.button("📊 Submit Quiz", type="primary", use_container_width=True):
                st.session_state.quiz_submitted = True
                st.rerun()
        # Auto-refresh every 5 s for the timer
        time.sleep(0.1)
        st.rerun()

    else:
        # Calculate score
        score = sum(
            1 for i, q in enumerate(questions)
            if st.session_state.quiz_answers.get(f"q_{i}") == q.get("answer", "")
        )
        total = len(questions)
        pct = int(score / total * 100) if total else 0

        emoji = "🏆" if pct >= 80 else "👍" if pct >= 60 else "📚"
        msg   = "Excellent!" if pct >= 80 else "Good job!" if pct >= 60 else "Keep studying!"

        st.markdown(
            f'<div class="score-box">{emoji} {msg}<br>'
            f'Your Score: {score} / {total} &nbsp;({pct}%)</div>',
            unsafe_allow_html=True,
        )

        time_taken = int(time.time() - (st.session_state.quiz_start_time or time.time()))
        mins, secs = divmod(min(time_taken, st.session_state.quiz_time_limit), 60)
        st.caption(f"⏱ Time taken: {mins}m {secs}s")

        if st.button("🔄 Retake Quiz"):
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
            st.session_state.quiz_expired = False
            st.session_state.quiz_start_time = time.time()
            st.rerun()

import streamlit as st

st.set_page_config(page_title="BMI Calculator | OIBSIP", page_icon="⚖️", layout="centered")

# ── Styling ─────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #1a1a2e; }
    .block-container { padding-top: 2rem; }
    .result-card {
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        margin-top: 20px;
    }
    .bmi-number { font-size: 64px; font-weight: 800; color: white; margin: 0; }
    .bmi-cat    { font-size: 22px; font-weight: 600; color: white; margin: 6px 0; }
    .bmi-tip    { font-size: 14px; color: rgba(255,255,255,0.85); margin-top: 8px; }
    .badge      { display:inline-block; padding:4px 14px; border-radius:20px;
                  font-size:13px; font-weight:600; color:white; }
</style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────
st.markdown("## ⚖️ BMI Calculator")
st.markdown("*Oasis Infobyte Internship | OIBSIP*")
st.divider()

# ── Inputs ──────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=500.0,
                              value=70.0, step=0.5)

with col2:
    unit = st.radio("Height unit", ["Meters (m)", "Centimeters (cm)"], horizontal=True)
    if unit == "Meters (m)":
        height = st.number_input("Height (m)", min_value=0.5, max_value=3.0,
                                  value=1.75, step=0.01)
    else:
        height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=300.0,
                                     value=175.0, step=1.0)
        height = height_cm / 100

# ── Calculate ───────────────────────────────
if st.button("Calculate BMI", type="primary", use_container_width=True):
    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        cat, color, tip, emoji = "Underweight",   "#3498db", "Consider a nutritious diet and consult a doctor.", "⚠️"
    elif bmi < 25.0:
        cat, color, tip, emoji = "Normal Weight", "#2ecc71", "Great! Keep maintaining your healthy lifestyle.",  "✅"
    elif bmi < 30.0:
        cat, color, tip, emoji = "Overweight",    "#f39c12", "Try a balanced diet and increase physical activity.", "⚠️"
    elif bmi < 35.0:
        cat, color, tip, emoji = "Obese Class I", "#e67e22", "Consult a healthcare provider for guidance.", "❌"
    elif bmi < 40.0:
        cat, color, tip, emoji = "Obese Class II","#e74c3c", "Please seek medical advice for your health.", "❌"
    else:
        cat, color, tip, emoji = "Obese Class III","#c0392b","Immediate medical attention is recommended.", "❌"

    # Result card
    st.markdown(f"""
    <div class="result-card" style="background:{color};">
        <p class="bmi-number">{bmi}</p>
        <p class="bmi-cat">{emoji} {cat}</p>
        <p class="bmi-tip">{tip}</p>
    </div>
    """, unsafe_allow_html=True)

    # BMI Scale
    st.markdown("#### 📊 BMI Scale")
    scale_pct = min(max((bmi - 10) / 30, 0), 1)
    st.progress(scale_pct)

    cols = st.columns(4)
    badges = [("< 18.5  Underweight","#3498db"), ("18.5–25  Normal","#2ecc71"),
              ("25–30  Overweight","#f39c12"),    ("> 30  Obese","#e74c3c")]
    for col, (label, bg) in zip(cols, badges):
        col.markdown(f'<span class="badge" style="background:{bg}">{label}</span>', unsafe_allow_html=True)

    # Details
    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Weight", f"{weight} kg")
    c2.metric("Height", f"{round(height, 2)} m")
    c3.metric("BMI", bmi)

# ── Reference Table ──────────────────────────
with st.expander("📋 BMI Reference Chart"):
    st.table({
        "Category":  ["Underweight","Normal Weight","Overweight","Obese Class I","Obese Class II","Obese Class III"],
        "BMI Range": ["< 18.5","18.5 – 24.9","25.0 – 29.9","30.0 – 34.9","35.0 – 39.9","≥ 40.0"],
    })

st.markdown("---")
st.caption("Patel Rudra | AICTE OIB-SIP May 2026 | Python Programming Internship")

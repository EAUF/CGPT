import streamlit as st

# Title and Introduction
st.title("Interactive AI Persona Selection")
st.markdown("🚀 Find the best AI personas for your investment evaluation.")

# Step 1: Investment Focus
focus = st.radio(
    "Step 1: What is your primary investment focus?",
    [
        "Disruptive Startup",
        "Deep Financial Analysis",
        "Market Trends and Competition",
        "Regulatory Risks",
        "Scalability and Execution",
        "Risk Mitigation Strategies"
    ]
)

# Step 2: AI Persona Recommendations
persona_map = {
    "Disruptive Startup": "Muse + Brainstormer + Visionary",
    "Deep Financial Analysis": "Realist + Oracle + Brainstormer",
    "Market Trends and Competition": "Investigator + Visionary + Negotiator",
    "Regulatory Risks": "Legal Advisor + Critic + Operator",
    "Scalability and Execution": "Operator + Negotiator + Conductor",
    "Risk Mitigation Strategies": "Critic + Brainstormer + Operator"
}

st.success(f"✅ Recommended Personas: {persona_map[focus]}")

# Explanation
st.subheader("Why these personas?")
explanations = {
    "Disruptive Startup": "🚀 Supports innovation, strategic pivots, and trend forecasting.",
    "Deep Financial Analysis": "💰 Provides financial stress-testing and feasibility insights.",
    "Market Trends and Competition": "📊 Helps with market intelligence and competitor benchmarking.",
    "Regulatory Risks": "⚖️ Ensures risk compliance and legal assessment.",
    "Scalability and Execution": "📈 Evaluates execution feasibility and scaling potential.",
    "Risk Mitigation Strategies": "⚠️ Focuses on risk evaluation and mitigation strategies."
}
st.write(explanations[focus])

# Next Steps
st.subheader("Next Steps")
st.markdown(
    """
    - **Activate Personas** in the AI platform to begin evaluation.
    - Use **Scenario Planning Mode** for dynamic stress-testing.
    - Review AI-generated insights for actionable recommendations.
    """
)

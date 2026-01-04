import streamlit as st

st.set_page_config(page_title="Mindfulness Self-Check", layout="centered")

# ---------------------------
# Data
# ---------------------------
questions = [
   "I notice how foods and drinks affect my thoughts, bodily sensations, and emotions.",
   "I pay attention to sensations, such as the wind in my hair or the sun on my face.",
   "I notice visual elements in the environment, such as colors or shapes.",
   "I am good at finding words to describe my feelings.",
   "I can easily put my beliefs, opinions, and expectations into words.",
   "Even when I am upset, I can find words to describe how I am feeling.",
   "I find myself doing things without paying attention.",
   "I rush through activities without being really attentive to them.",
   "I do jobs or tasks automatically, without being aware of what I am doing.",
   "I tell myself that I shouldn’t be feeling the way I’m feeling.",
   "I make judgments about whether my thoughts are good or bad.",
   "I think some of my emotions are bad or inappropriate and I shouldn’t feel them.",
   "I notice distressing thoughts or images and let them go.",
   "I watch my feelings without getting lost in them.",
   "I can step back from my thoughts and feelings and observe them without reacting."
]

reverse_items = [6, 7, 8, 9, 10, 11]  # zero-based index

scale = {
   1: "Never or very rarely",
   2: "Rarely",
   3: "Sometimes",
   4: "Often",
   5: "Very often or always"
}

# ---------------------------
# UI Flow
# ---------------------------
st.title("Mindfulness Self-Check")
st.write("A brief self-assessment to understand your current awareness and stress response.")
st.write("⏱ Takes about **2–3 minutes**")

responses = []

st.divider()

for i, q in enumerate(questions):
   st.subheader(f"Question {i+1} of 15")
   response = st.radio(
       q,
       options=list(scale.keys()),
       format_func=lambda x: f"{x} — {scale[x]}",
       key=f"q{i}"
   )
   responses.append(response)

# ---------------------------
# Scoring
# ---------------------------
if st.button("View My Results"):
   scores = []
   for i, r in enumerate(responses):
       if i in reverse_items:
           scores.append(6 - r)
       else:
           scores.append(r)

   total_score = round(sum(scores) / 15, 2)

   st.divider()
   st.header("Your Mindfulness Snapshot")

   st.metric(label="Overall Awareness Level", value=f"{total_score} / 5")

   st.write(
       "This score suggests that when life feels demanding, your attention may naturally drift "
       "away from the present moment. This is a common and very workable pattern."
   )

   st.subheader("What You’re Already Doing Well")
   st.write(
       "You show an ability to notice physical sensations and experiences. "
       "This awareness provides a strong foundation for building greater calm and clarity."
   )

   st.subheader("Areas That May Benefit From Gentle Support")
   st.write(
       "- Staying present during everyday activities\n"
       "- Being less hard on yourself emotionally"
   )

   st.subheader("Personalized Practices")

   st.markdown("**Body Awareness (2 minutes)**")
   st.write(
       "Gently bring your attention to physical sensations right now. "
       "Notice contact, temperature, or movement—without trying to change anything."
   )

   st.markdown("**Creating Space Around Thoughts**")
   st.write(
       "Imagine each thought as a leaf floating down a stream. "
       "You don’t need to follow it or stop it—just notice it pass."
   )

   st.caption(
       "This self-check is designed to support reflection and care. "
       "It does not provide a medical diagnosis."
   )

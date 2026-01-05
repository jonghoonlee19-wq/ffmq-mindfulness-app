import streamlit as st
from fpdf import FPDF
import io

st.set_page_config(page_title="Mindfulness Self-Check", layout="centered")

st.title("Mindfulness Self-Check (FFMQ-15)")

st.write("Please rate each statement from 1 (Never) to 5 (Very Often).")

# 질문 리스트
questions = {
   "Observing": [
       "1. I notice how foods and drinks affect my thoughts and body.",
       "2. I pay attention to sensations like the wind or sun on my face.",
       "3. I notice visual elements like colors and shapes in nature."
   ],
   "Describing": [
       "4. I am good at finding words to describe my feelings.",
       "5. I can easily put my beliefs and opinions into words.",
       "6. Even when upset, I can find words to express my feelings."
   ],
   "Awareness": [
       "7. I find myself doing things without paying attention. (*)",
       "8. I rush through activities without being attentive. (*)",
       "9. I do tasks automatically without being aware of them. (*)"
   ],
   "Non-Judging": [
       "10. I tell myself I shouldn’t be feeling the way I’m feeling. (*)",
       "11. I make judgments about whether my thoughts are good/bad. (*)",
       "12. I think some of my emotions are inappropriate. (*)"
   ],
   "Non-Reactivity": [
       "13. I notice distressing thoughts and just let them go.",
       "14. I watch my feelings without getting lost in them.",
       "15. I step back from thoughts and aware of them without reacting."
   ]
}

reverse_categories = ["Awareness", "Non-Judging"]  # Reverse scoring categories

# 사용자 점수 입력
user_scores = {}
for cat, qs in questions.items():
   st.subheader(cat)
   for q in qs:
       user_scores[q] = st.slider(q, 1, 5, 3)

# 점수 계산
def calculate_score(scores):
   total = 0
   for q, val in scores.items():
       for cat in reverse_categories:
           if q in questions[cat]:
               val = 6 - val  # Reverse scoring
       total += val
   avg = round(total / 15, 2)
   return avg

if st.button("Submit"):
   avg_score = calculate_score(user_scores)
   st.success(f"Your Mindfulness Average Score: {avg_score} / 5")

   # PDF 생성
   pdf = FPDF()
   pdf.add_page()
   pdf.set_font("Arial", "B", 16)
   pdf.cell(0, 10, "Mindfulness Self-Check Result", ln=True, align="C")
   pdf.ln(10)
   pdf.set_font("Arial", "", 12)
   for cat, qs in questions.items():
       pdf.cell(0, 8, cat, ln=True)
       for q in qs:
           pdf.cell(0, 8, f"{q} - {user_scores[q]}", ln=True)
       pdf.ln(2)
   pdf.cell(0, 8, f"Mindfulness Average Score: {avg_score} / 5", ln=True)

   # PDF 다운로드 버튼
   pdf_buffer = io.BytesIO()
   pdf.output(pdf_buffer)
   st.download_button("Download PDF Result", pdf_buffer, file_name="Mindfulness_Result.pdf")


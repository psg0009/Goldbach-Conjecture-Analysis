# Goldbach-Conjecture-Analysis 

Analysis of *Goldbach’s Conjecture* and *Prime Gaps* using *Cramér’s Conjecture*.

This repository contains computational research validating Goldbach’s Conjecture and analyzing Prime Gaps. We compare observed gaps to *Cramér’s bound* \((\log p)^2\) and investigate their behavior at large scales.

---

## 📂 Project Structure 📁
📂 *Goldbach-Conjecture-Analysis/*  
 ┣ 📂 data/ → Contains datasets of prime gaps.  
 ┃ ┣ 📄 Prime_Gaps_Analysis.csv  
 ┃ ┣ 📄 Processed_Prime_Gaps.csv  
 ┃  
 ┣ 📂 scripts/ → Python scripts for computational analysis.  
 ┃ ┣ 🐍 prime_gap_analysis.py → Computes prime gaps, applies Cramér's conjecture, detects anomalies.  
 ┃ ┣ 🐍 goldbach_verification.py → Analyzes prime gaps distribution, compares with expected values.  
 ┃ ┣ 🐍 interactive_prime_gaps.py → Uses Plotly for interactive visualization of prime gaps.  
 ┃  
 ┣ 📂 docs/ → Research paper and findings.  
 ┃ ┣ 📄 Goldbach_Conjecture_Paper.pdf  
 ┃ ┣ 📄 Goldbach_Conjecture_Paper.docx  
 ┃  
 ┣ 📂 images/ → Stores result images for documentation.  
 ┃ ┣ 🖼 prime_gaps_vs_cramer.png  
 ┃ ┣ 🖼 goldbach_verification.png  
 ┃ ┣ 🖼 prime_gap_distribution.png  
 ┃  
 ┣ 📄 README.md → Documentation for the project.  
 ┣ 📄 requirements.txt → List of required Python libraries.  

---

## 🚀 Setup Instructions
### *1️⃣ Clone the Repository*
bash
git clone https://github.com/YOUR-USERNAME/Goldbach-Conjecture-Analysis.git
cd Goldbach-Conjecture-Analysis


### *2️⃣ Install Dependencies*
Ensure you have *Python 3.x* installed. Then, install required libraries:
bash
pip install -r requirements.txt


### *3️⃣ Run the Analysis*
- *Compute Prime Gaps & Cramér’s Conjecture:*
  bash
  python scripts/prime_gap_analysis.py
  
- *Visualize Prime Gap Distribution:*
  bash
  python scripts/goldbach_verification.py
  
- *Run Interactive Visualization (Plotly):*
  bash
  python scripts/interactive_prime_gaps.py
  

---

## 📊 Results & Findings

### *1️⃣ Prime Gaps vs. Cramér’s Conjecture*
🔹 *Expected vs. Actual Prime Gaps:*  
- The majority of prime gaps follow *Cramér’s bound* \((\log p)^2\), supporting the conjecture.  
- No extreme anomalies where gaps exceed *twice the expected value*.  
- Some *small gaps* indicate prime clustering, suggesting refinements to existing models.  

📌 *Visualization of Prime Gaps vs. Cramér’s Bound:*  
![Prime Gaps vs. Cramér’s Bound](images/prime_gaps_vs_cramer.png)

---

### *2️⃣ Goldbach’s Conjecture Beyond \(4 × 10^{18}\)*
🔹 *Extended Validation of Goldbach's Conjecture:*  
- The research extends the *verification of Goldbach's conjecture* to numbers beyond \(4 × 10^{18}\).  
- Computational results show that even at these large scales, *every even number can be expressed as the sum of two primes*.  

📌 *Graph of Even Numbers as Sum of Two Primes:*  
![Goldbach Verification](images/goldbach_verification.png)

---

### *3️⃣ Prime Gap Distribution & Anomalies*
🔹 *Key Observations from the Data:*  
- Prime gaps exhibit a *logarithmic pattern* consistent with number theory predictions.  
- Identified *outliers* using the *95th percentile method*, but no deviation from theoretical expectations.  
- Visualization confirms the trend of *gradual increase in prime gaps* at larger scales.

📌 *Histogram of Prime Gaps Distribution:*  
![Prime Gap Distribution](images/prime_gap_distribution.png)

---

## 📌 Research Insights
- *Cramér’s conjecture* holds for large prime numbers within expected bounds.  
- *Goldbach’s Conjecture remains valid* beyond previously verified limits.  
- Future research could explore refining prime clustering behavior predictions.  

---

## 📜 Requirements
The following libraries are needed to run the analysis:
plaintext
numpy
pandas
matplotlib
scipy
plotly
sympy


Install them using:
bash
pip install -r requirements.txt


---

## 📧 Contact
For queries, reach out to *Parth Gosar*.



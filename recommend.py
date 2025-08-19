
def generate_advice(df):
    total_income = df['income'].sum()
    total_expense = df['expense'].sum()
    savings_rate = (total_income - total_expense) / total_income if total_income else 0

    tips = []

    if savings_rate < 0.1:
        tips.append("Try to save at least 10% of your monthly income.")
    if df['expense'].mean() > 100:
        tips.append("Cut down on daily spending to improve savings.")
    if (df['income'] == 0).sum() > 5:
        tips.append("Consider more consistent income sources.")

    if not tips:
        tips.append("You're doing great! Consider investing your savings.")

    return tips

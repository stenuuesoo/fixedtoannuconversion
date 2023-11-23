# create fixed to annuity function
def annual_to_monthly_annuity_rate(annual_rate):
    return (1 + annual_rate) ** (1 / 12) - 1


if __name__ == '__main__':
    # Annual interest rate
    annual_rate = 0.32  # 32%

    # Convert to monthly annuity rate
    monthly_annuity_rate = annual_to_monthly_annuity_rate(annual_rate)

    print(f"Monthly Annuity Interest Rate: {monthly_annuity_rate * 100:.2f}%")
    # create monthly to yearly function
    print(f"Annual Interest Rate: {monthly_annuity_rate * 12 * 100:.2f}%")
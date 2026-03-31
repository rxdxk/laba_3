import taxes_database as tax

def calculate_employee(base_salary, rate):
    accrued_salary = base_salary * rate

    personal_income_tax = accrued_salary * tax.PERSONAL_INCOME_TAX_RATE
    military_tax = accrued_salary * tax.MILITARY_TAX_RATE

    esv_base = max(tax.SINGLE_CONTRIBUTION_BASE_MIN,
                   min(accrued_salary, tax.SINGLE_CONTRIBUTION_BASE_MAX))

    single_contribution = esv_base * tax.SINGLE_CONTRIBUTION_RATE

    net_salary = accrued_salary - personal_income_tax - military_tax
    employee_cost = accrued_salary + single_contribution

    return {
        "accrued": accrued_salary,
        "pit": personal_income_tax,
        "military": military_tax,
        "esv": single_contribution,
        "net": net_salary,
        "cost": employee_cost
    }

def main(N):
    emp1 = calculate_employee(30000 + N * 700, 0.75 + (N % 2 + N % 3) * 0.25)
    emp2 = calculate_employee(9000 + N * 100, 0.5 - N * 0.01)
    emp3 = calculate_employee(175000 + N * 5000, 1.0)

    total_cost = emp1["cost"] + emp2["cost"] + emp3["cost"]

    print(emp1)
    print(emp2)
    print(emp3)
    print("Total:", total_cost)

if __name__ == "__main__":
    main(N=22)

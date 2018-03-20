# Cheung Man Yiu Anthony
# Chan Sau Lim
# Chong Ka Wing
mpf_reduction_rate = 0.05
mpf_allowance = 15000
married_allowance = 264000
first_net_inc = 45000
second_net_inc = 45000
third_net_inc = 45000
first_rate = 0.02
second_rate = 0.07
third_rate = 0.12
fourth_rate = 0.17
tax_reduction_rate = 0.75
tax_reduction_cap = 20000
basic_allowance = 132000

#validate income input - must be positive integer
while True:
    try:
        husband_inc = 0#input("Input Husband Income: ")
        husband_inc_int = int(husband_inc)
        if husband_inc_int < 0:
            print("Please enter a non-negative integer.")
            continue
        else:
            husband_inc = husband_inc_int

            break
    except ValueError:
       print("Not an integer! Try again.")
       continue

while True:
    try:
        wife_inc = 0#input("Input Wife Income: ")
        wife_inc_int = int(wife_inc)
        if wife_inc_int < 0:
            print("Please enter a non-negative integer.")
            continue
        else:
            wife_inc = wife_inc_int
            break
    except ValueError:
       print("Not an integer! Try again.")
       continue
print("\n")





def joint_assessment(husband_inc,wife_inc):
    #husband mpf net income:
    husband_mpf_list = []
    del husband_mpf_list[:]
    husband_mpf_list.append(mpf_allowance)

    mpf_portion_husband_inc = husband_inc * mpf_reduction_rate
    husband_mpf_list.append(mpf_portion_husband_inc)

    husband_net_income = husband_inc - min(husband_mpf_list)


    #wife mpf net income:
    wife_mpf_list = []
    del wife_mpf_list[:]
    wife_mpf_list.append(mpf_allowance)

    mpf_portion_wife_inc = wife_inc * mpf_reduction_rate
    wife_mpf_list.append(mpf_portion_wife_inc)

    wife_net_income = wife_inc - min(wife_mpf_list)

    net_chargable_income = husband_net_income+wife_net_income-married_allowance
    if net_chargable_income > 0:
        net_chargable_income = husband_net_income + wife_net_income - married_allowance
    else:
        net_chargable_income = 0

    #Tax payable schedule:
    #1st
    first_payable_lst = []
    del first_payable_lst [:]
    first_payable_lst.append(first_net_inc)
    first_payable_lst.append(net_chargable_income)

    first_payable = min(first_payable_lst) * first_rate


    #2nd
    second_payable_lst = []
    del second_payable_lst[:]
    second_payable_lst.append(second_net_inc)
    if net_chargable_income-first_net_inc > 0:
        second_payable_lst.append(net_chargable_income-first_net_inc)
    else:
        second_payable_lst.append(0)

    second_payable = min(second_payable_lst) * second_rate


    # 3rd
    third_payable_lst = []
    del third_payable_lst[:]
    third_payable_lst.append(third_net_inc)
    if net_chargable_income - second_net_inc - first_net_inc > 0:
        third_payable_lst.append(net_chargable_income - second_net_inc - first_net_inc)
    else:
        third_payable_lst.append(0)

    third_payable = min(third_payable_lst) * third_rate


    # remainder
    fourth_payable_lst = []
    del fourth_payable_lst[:]
    if net_chargable_income - third_net_inc - second_net_inc - first_net_inc > 0:
        fourth_payable_lst.append(net_chargable_income - third_net_inc - second_net_inc - first_net_inc)
    else:
        fourth_payable_lst.append(0)

    fourth_payable = max(fourth_payable_lst) * fourth_rate


    #tax reduction:
    tax_thereon = first_payable + second_payable + third_payable + fourth_payable
    tax_reduction = 0
    if tax_thereon * tax_reduction_rate > tax_reduction_cap:
        tax_reduction = tax_reduction_cap
    else:
        tax_reduction = tax_thereon * tax_reduction_rate

    #Total tax payable:
    tax_payable = round(tax_thereon - tax_reduction,2)
    return tax_payable

def individual(husband_inc, wife_inc):
    # net income == min. of mpf allowance (15000) or 5% of income
    # mpf net income:
    mpf_portion_individual_inc = husband_inc * mpf_reduction_rate

    individual_net_income = husband_inc - min(mpf_portion_individual_inc,mpf_allowance)


    net_chargable_income = individual_net_income  - basic_allowance
    if net_chargable_income > 0:
        net_chargable_income = individual_net_income  - basic_allowance
    else:
        net_chargable_income = 0


    # Tax payable schedule:
    # 1st
    first_payable = min(net_chargable_income,first_net_inc) * first_rate


    # 2nd
    second_payable_amount = 0
    if net_chargable_income - first_net_inc > 0:
        second_payable_amount = net_chargable_income - first_net_inc
    else:
        second_payable_amount = 0

    second_payable = min(second_payable_amount,second_net_inc) * second_rate


    # 3rd
    third_payable_amount = 0
    if net_chargable_income - second_net_inc - first_net_inc > 0:
        third_payable_amount = net_chargable_income - second_net_inc - first_net_inc
    else:
        third_payable_amount = 0

    third_payable = min(third_payable_amount,third_net_inc) * third_rate


    # remainder
    fourth_payable_amount = 0
    if net_chargable_income - third_net_inc - second_net_inc - first_net_inc > 0:
        fourth_payable_amount = net_chargable_income - third_net_inc - second_net_inc - first_net_inc
    else:
        fourth_payable_amount = 0

    fourth_payable = fourth_payable_amount* fourth_rate


    # tax reduction:
    tax_thereon = first_payable + second_payable + third_payable + fourth_payable
    tax_reduction = 0
    if tax_thereon * tax_reduction_rate > tax_reduction_cap:
        tax_reduction = tax_reduction_cap
    else:
        tax_reduction = tax_thereon * tax_reduction_rate

    # Total tax payable:
    a = tax_thereon - tax_reduction



    # net income == min. of mpf allowance (15000) or 5% of income
    # mpf net income:
    mpf_portion_individual_inc = wife_inc * mpf_reduction_rate

    individual_net_income = wife_inc - min(mpf_portion_individual_inc,mpf_allowance)

    net_chargable_income = individual_net_income  - basic_allowance
    if net_chargable_income > 0:
        net_chargable_income = individual_net_income  - basic_allowance
    else:
        net_chargable_income = 0


    # Tax payable schedule:
    # 1st
    first_payable = min(net_chargable_income,first_net_inc) * first_rate

    # 2nd
    second_payable_amount = 0
    if net_chargable_income - first_net_inc > 0:
        second_payable_amount = net_chargable_income - first_net_inc
    else:
        second_payable_amount = 0

    second_payable = min(second_payable_amount,second_net_inc) * second_rate

    # 3rd
    third_payable_amount = 0
    if net_chargable_income - second_net_inc - first_net_inc > 0:
        third_payable_amount = net_chargable_income - second_net_inc - first_net_inc
    else:
        third_payable_amount = 0

    third_payable = min(third_payable_amount,third_net_inc) * third_rate

    # remainder
    fourth_payable_amount = 0
    if net_chargable_income - third_net_inc - second_net_inc - first_net_inc > 0:
        fourth_payable_amount = net_chargable_income - third_net_inc - second_net_inc - first_net_inc
    else:
        fourth_payable_amount = 0

    fourth_payable = fourth_payable_amount* fourth_rate

    # tax reduction:
    tax_thereon = first_payable + second_payable + third_payable + fourth_payable
    tax_reduction = 0
    if tax_thereon * tax_reduction_rate > tax_reduction_cap:
        tax_reduction = tax_reduction_cap
    else:
        tax_reduction = tax_thereon * tax_reduction_rate

    # Total tax payable:
    b = tax_thereon - tax_reduction
    c = a+b
    return round(c,2)

def main(husband_inc,wife_inc):
    husband_inc = int(husband_inc)
    wife_inc = int(wife_inc)

    print("Individual: "+ str(individual(husband_inc, wife_inc)))

    print("Joint Assessment: " + str(joint_assessment(husband_inc, wife_inc)))

    if (individual(husband_inc, wife_inc) < joint_assessment(husband_inc, wife_inc)):
        print("Choose Individual for lower tax payable.")
        print("----------------------------------------------" + "\n" )
        return "Choose Individual for lower tax payable."
    elif (individual(husband_inc, wife_inc) == joint_assessment(husband_inc, wife_inc)):
        print("Either Joint Assessment or Individual Assessment.")
        print("----------------------------------------------" + "\n" )
        return "Either Joint Assessment or Individual Assessment."
    else:
        print("Choose Joint Assessment for lower tax payable.")
        print("----------------------------------------------" + "\n" )
        return "Choose Joint Assessment for lower tax payable."

#Main program starts here
main(husband_inc, wife_inc)


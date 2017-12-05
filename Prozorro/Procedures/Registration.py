from Prozorro.Procedures.Tenders import init_driver


def registerUserCompany(filename):
    chrm, tp, mpg = init_driver()
    mpg.open_reg_form()
    uaid = []

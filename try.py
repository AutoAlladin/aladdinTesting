import time

from Prozorro import Utils
from Prozorro.Procedures.Tenders import init_driver

a,b,mpg = init_driver()
Utils.waitFadeIn(mpg.drv)
lf = mpg.open_login_form()
lf.login("mm@mm.mm", "123123")
time.sleep(2)
mpg.drv.execute_script("$('#butLogoutPartial').click()")

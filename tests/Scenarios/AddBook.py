from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage

import time

from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_Form(self):

        log = self.getLogger()

        log.info("Let's start the test...")
        homepage = HomePage(self.driver)

        time.sleep(1)

        loggin_in = homepage.sign_in()
        time.sleep(1)

        log.info("Logging In...")

        loggin_in.Loggin_In("carlospimart","bonpassdemot")

        time.sleep(3)

        log.info("Succesfully Logged")

        homepage.alert("dismiss")

        time.sleep(3)

        homepage.verifying_page_message("//div[@class='home_text']", "THIS IS THE HOME PAGE")

        time.sleep(1)

        admin_logging = homepage.admin_in()

        time.sleep(1)

        admin_logging.Loggin_In("Aquiescencia820338$")

        time.sleep(1)

        admin_logging.alert("dismiss")

        time.sleep(1)

        admin_logging.verifying_page_message()

        items = ["Il pendolo di Foucault", 1988, 3.5,"DeBolsillo","Used",
                 "l pendolo di Foucault è suddiviso in dieci segmenti che rappresentano le dieci Sephirot."
                 " Il romanzo è ricco di citazioni esoteriche, dalla Cabala all'alchimia e alla teoria del "
                 "complotto, così tante che il critico letterario e romanziere Anthony Burgess ha suggerito "
                 "che sarebbe stato utile un indice.",
                 "Paperback", 832]

        items_2 = ["Italian", "Umberto Eco", "For sale"]
        images_path = ["C:\\Users\domin\Desktop\Castellar\il_pendolo_di_Foucault.webp"]

        time.sleep(2)
        admin_logging.menu("items", "post", items, items_2, images_path)
        time.sleep(10)
        homepage.home_page()
        time.sleep(2)
        search = homepage.search(items[0])
        time.sleep(2)
        log.info("Let's check the book on the page: ")
        time.sleep(1)
        search.verifying_page_message("//a[@class='title']","Il pendolo di Foucault")
        log.info("Test successful")


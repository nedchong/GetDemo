from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_items()
        log.info("getting all the card titles")
        cards = checkout_page.get_card_titles()
        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            log.info(card_text)
            if card_text == "Blackberry":
                checkout_page.get_card_footer()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirm_page = checkout_page.check_out_items()
        log.info("Entering country name as ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        # time.sleep(5)
        self.verify_link_presence("India")

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        text_match = str.rstrip(self.driver.find_element_by_css_selector("[class*='alert-success']").text)
        log.info("Text received from application is " + text_match)

        # assert ("Success! Thank you!" in text_match)
        # false failure to test screenshot
        assert ("xSuccess! Thank you!" in text_match)
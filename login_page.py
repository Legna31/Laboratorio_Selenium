from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

        self.error = (
            By.CSS_SELECTOR,
            "h3[data-test='error']"
        )

    def ingresar_credenciales(self, usuario, clave):

        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(usuario)

        self.driver.find_element(
            *self.password
        ).send_keys(clave)

    def click_login(self):

        self.driver.find_element(
            *self.login_button
        ).click()

    def obtener_error(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.error)
        ).text
from selenium import webdriver

from login_page import LoginPage

def test_pom():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)

    login.ingresar_credenciales(
        "locked_out_user",
        "secret_sauce"
    )

    login.click_login()

    mensaje = login.obtener_error()

    print(mensaje)

    driver.quit()

if __name__ == "__main__":
    test_pom()
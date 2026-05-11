import pytest
from login_page import LoginPage

def test_pom(driver):

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)

    login.ingresar_credenciales(
        "locked_out_user",
        "secret_sauce"
    )

    login.click_login()

    mensaje = login.obtener_error()

    assert "locked out" in mensaje
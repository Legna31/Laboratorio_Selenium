import pytest
from selenium.webdriver.common.by import By
from login_page import LoginPage

def test_login_exitoso_practico(driver):
    """CASO 1: LOGIN EXITOSO"""
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    assert "inventory.html" in driver.current_url


def test_agregar_producto_carrito(driver):
    """CASO 2: AGREGAR AL CARRITO"""
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    boton = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    boton.click()

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"


def test_login_fallido_practico(driver):
    """CASO 3: LOGIN FALLIDO"""
    driver.delete_all_cookies()
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()

    error = login.obtener_error()
    assert "locked out" in error
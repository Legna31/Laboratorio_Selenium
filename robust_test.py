import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage


def test_login_exitoso_robust(driver):
    """LOGIN EXITOSO con esperas explícitas"""
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    assert "inventory.html" in driver.current_url


def test_agregar_producto_robust(driver):
    """AGREGAR PRODUCTO con esperas robustas"""
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    wait = WebDriverWait(driver, 10)
    
    boton = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    boton.click()

    badge = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge.text == "1"


def test_login_fallido_robust(driver):
    """LOGIN FALLIDO con usuario bloqueado"""
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()

    error = login.obtener_error()
    assert "locked out" in error
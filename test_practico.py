from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def ejecutar_pruebas():
    try:

        # CASO 1 LOGIN EXITOSO
        print("Ejecutando Login Exitoso")

        driver.get("https://www.saucedemo.com")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert "inventory.html" in driver.current_url

        print("Login exitoso completado")

        # CASO 2 AGREGAR AL CARRITO

        print("Agregando producto")

        boton = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        boton.click()

        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

        assert carrito == "1"

        print("Producto agregado correctamente")

        # CASO 3 LOGIN FALLIDO

        driver.delete_all_cookies()

        driver.get("https://www.saucedemo.com")

        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text

        assert "locked out" in error

        print("Validación de usuario bloqueado correcta")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    ejecutar_pruebas()
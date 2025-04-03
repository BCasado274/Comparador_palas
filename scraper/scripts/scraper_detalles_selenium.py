from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# URL de prueba de una pala (¡la podés cambiar!)
url = 'https://www.padelnuestro.com/adidas-metalbone-3-3-2024-110141-p'

# Configurar navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Quitar esta línea si querés ver la ventana
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Acceder a la página
driver.get(url)
time.sleep(3)  # Esperar a que cargue todo

# Extraer HTML ya renderizado por JS
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Buscar los atributos técnicos
atributos = soup.find_all("div", class_="description-attributes")
print("\n🎾 Detalles técnicos encontrados:\n")
for attr in atributos:
    clave = attr.find("span", class_="description-attributes-label").get_text(strip=True)
    valor = attr.find("span", class_="description-attributes-value").get_text(strip=True)
    print(f"{clave}: {valor}")

driver.quit()

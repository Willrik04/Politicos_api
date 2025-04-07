import requests
from bs4 import BeautifulSoup
import json
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'politicos_api.settings')
django.setup()

from scraper.models import Partido, Candidato, ResultadoElectoral

def scrape_candidatos():
    """
    Función para extraer información de candidatos políticos de sitios web.
    """
    print("Iniciando scraping de candidatos...")

    # Ejemplo: Scraping de una página ficticia de candidatos
    url = "https://www.cne.gob.ec/candidatos"

    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()

        # Parsear el HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraer información de candidatos (esto es un ejemplo, ajustar según la estructura real)
        candidatos_elements = soup.select('.candidato-card')

        for element in candidatos_elements:
            # Extraer datos del candidato
            nombre = element.select_one('.nombre').text.strip()
            cargo = element.select_one('.cargo').text.strip()
            partido_nombre = element.select_one('.partido').text.strip()
            partido_lista = element.select_one('.lista').text.strip()
            foto_url = element.select_one('img')['src']

            # Crear o actualizar partido
            partido, created = Partido.objects.get_or_create(
                nombre=partido_nombre,
                defaults={'lista': partido_lista}
            )

            # Crear o actualizar candidato
            candidato, created = Candidato.objects.get_or_create(
                nombre=nombre,
                cargo=cargo,
                partido=partido,
                defaults={
                    'foto_url': foto_url,
                    'biografia': '',
                    'propuestas': '',
                    'redes_sociales': {}
                }
            )

            print(f"Candidato {'creado' if created else 'actualizado'}: {nombre}")

        print("Scraping completado con éxito.")
        return True

    except Exception as e:
        print(f"Error durante el scraping: {str(e)}")
        return False

def scrape_resultados():
    """
    Función para extraer resultados electorales.
    """
    print("Iniciando scraping de resultados electorales...")

    # Ejemplo: Scraping de una página ficticia de resultados
    url = "https://www.cne.gob.ec/resultados"

    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()

        # Parsear el HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraer información de resultados (esto es un ejemplo, ajustar según la estructura real)
        resultados_elements = soup.select('.resultado-card')

        for element in resultados_elements:
            # Extraer datos del resultado
            candidato_nombre = element.select_one('.candidato').text.strip()
            provincia = element.select_one('.provincia').text.strip()
            votos = int(element.select_one('.votos').text.strip().replace(',', ''))
            porcentaje = float(element.select_one('.porcentaje').text.strip().replace('%', ''))

            # Buscar candidato
            try:
                candidato = Candidato.objects.get(nombre=candidato_nombre)

                # Crear o actualizar resultado
                resultado, created = ResultadoElectoral.objects.update_or_create(
                    candidato=candidato,
                    provincia=provincia,
                    defaults={
                        'votos': votos,
                        'porcentaje': porcentaje
                    }
                )

                print(f"Resultado {'creado' if created else 'actualizado'} para {candidato_nombre} en {provincia}")

            except Candidato.DoesNotExist:
                print(f"Candidato no encontrado: {candidato_nombre}")

        print("Scraping de resultados completado con éxito.")
        return True

    except Exception as e:
        print(f"Error durante el scraping de resultados: {str(e)}")
        return False

if __name__ == "__main__":
    # Ejecutar scraping
    scrape_candidatos()
    scrape_resultados()
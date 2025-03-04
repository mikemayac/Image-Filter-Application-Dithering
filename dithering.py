import streamlit as st
from PIL import Image
from io import BytesIO

# Configuración de la página en modo ancho
st.set_page_config(page_title="Aplicación Quita Marca de Agua", layout="wide")


def remove_watermark(original_image):
    """
    Función para quitar la marca de agua de la imagen.
    Aún no se implementa la lógica, por lo que se devuelve la imagen original.
    """
    # Aquí irá la lógica para quitar la marca de agua
    return original_image


def apply_dithering_filter(image, filter_type):
    """
    Aplica el filtro de dithering seleccionado.
    Por ahora, cada filtro devuelve la imagen sin modificaciones.
    La lógica de cada dithering se implementará en pasos posteriores.
    """
    if filter_type == "1. Filtro de Azar":
        # TODO: Implementar dithering por azar
        return image

    elif filter_type == "2. Ordenado y disperso (Clustered)":
        # TODO: Implementar dithering ordenado (clustered)
        return image

    elif filter_type == "3. Disperso 2x2, 4x4":
        # TODO: Implementar dithering disperso 2x2 y 4x4
        return image

    elif filter_type == "4. Floyd Steinberg":
        # TODO: Implementar dithering Floyd Steinberg
        return image

    elif filter_type == "5. Fake Floyd Steinberg":
        # TODO: Implementar dithering Fake Floyd Steinberg
        return image

    elif filter_type == "6. Jarvis, Judice, Ninken":
        # TODO: Implementar dithering Jarvis, Judice, Ninken
        return image

    else:
        # Si no se selecciona, simplemente regresamos la imagen original
        return image


def main():
    st.sidebar.title("Configuraciones")

    # Menú desplegable para seleccionar el filtro de dithering
    dithering_filter = st.sidebar.selectbox(
        "Selecciona un filtro de dithering:",
        (
            "1. Filtro de Azar",
            "2. Ordenado y disperso (Clustered)",
            "3. Disperso 2x2, 4x4",
            "4. Floyd Steinberg",
            "5. Fake Floyd Steinberg",
            "6. Jarvis, Judice, Ninken"
        )
    )

    # Uploader de imagen
    uploaded_file = st.sidebar.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    st.title("Aplicación para Quitar Marca de Agua de Imágenes (con Filtros de Dithering)")

    if uploaded_file is not None:
        # Cargar la imagen y convertirla a RGB (en caso de que tenga canal alfa)
        original_image = Image.open(uploaded_file).convert("RGB")

        # Dividir la vista en dos columnas para mostrar la imagen original y la procesada
        col1, col2 = st.columns(2)

        with col1:
            st.image(original_image, caption="Imagen Original", use_container_width=True)

        with col2:
            # Quitar marca de agua (lógica pendiente o en desarrollo)
            watermark_removed_image = remove_watermark(original_image)

            # Aplicar el filtro de dithering seleccionado (lógica pendiente en cada filtro)
            result_image = apply_dithering_filter(watermark_removed_image, dithering_filter)

            st.image(result_image, caption=f"Imagen con Filtro: {dithering_filter}", use_container_width=True)

            # Botón para descargar la imagen resultante
            buf = BytesIO()
            result_image.save(buf, format="PNG")
            st.download_button(
                label="⬇️ Descargar imagen",
                data=buf.getvalue(),
                file_name="imagen_resultante.png",
                mime="image/png"
            )
    else:
        st.info("Por favor, sube una imagen para quitar la marca de agua y/o aplicar un filtro de dithering.")


if __name__ == "__main__":
    main()

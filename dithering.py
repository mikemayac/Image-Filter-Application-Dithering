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


def main():
    st.sidebar.title("Configuraciones")

    # Aquí se podrían agregar más opciones específicas para la eliminación de marcas de agua.
    uploaded_file = st.sidebar.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    st.title("Aplicación para Quitar Marca de Agua de Imágenes")

    if uploaded_file is not None:
        # Cargar la imagen y convertirla a RGB (en caso de que tenga canal alfa)
        original_image = Image.open(uploaded_file).convert("RGB")

        # Dividir la vista en dos columnas para mostrar la imagen original y la procesada
        col1, col2 = st.columns(2)
        with col1:
            st.image(original_image, caption="Imagen Original", use_container_width=True)

        with col2:
            # Procesar la imagen para quitar la marca de agua (lógica pendiente)
            result_image = remove_watermark(original_image)
            st.image(result_image, caption="Imagen sin Marca de Agua", use_container_width=True)

            # Botón para descargar la imagen resultante
            buf = BytesIO()
            result_image.save(buf, format="PNG")
            st.download_button(
                label="⬇️ Descargar imagen",
                data=buf.getvalue(),
                file_name="imagen_sin_marca.png",
                mime="image/png"
            )
    else:
        st.info("Por favor, sube una imagen para quitar la marca de agua.")


if __name__ == "__main__":
    main()

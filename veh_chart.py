import pandas as pd
import plotly.express as px
import streamlit as st


st.header('Ventas de Vehículos')

st.write('Esta aplicación aún no es funcional. En construcción.')

ruta_archivo =   "vehicles_us.csv"       
car_data = pd.read_csv(ruta_archivo)
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button("Construir gráfico de dispersión") 
      
if hist_button: # al hacer clic en el botón
                    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
                    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
                    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
if scatter_button: # al hacer click en el botón
                    # Escribir un mensaje
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches") 
                    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x= "odometer", y="price")
                    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig,)              
# Librerias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Curvas Tipo app')
st.sidebar.title('Parámetros')

with st.sidebar.beta_expander('Curva tipo exponecial'):
	qi_exp = st.number_input('Input qi exp',min_value=0.00, max_value=None, value=50.00, step=1.00 )
	b_exp = st.number_input('Input b exp',min_value=0.0000, max_value=None, value=0.0005,  step=0.0100 )
	Di_exp = st.number_input('Input Di exp',min_value=0.00, max_value=None, value=0.50,  step=1.00 )

with st.sidebar.beta_expander('Curva tipo armónica'):
	qi_arm = st.number_input('Input qi arm',min_value=0.00, max_value=None, value=50.00, step=1.00 )
	b_arm = st.number_input('Input b arm',min_value=0.0000, max_value=None, value=1.0000,  step=0.0100 )
	Di_arm = st.number_input('Input Di arm',min_value=0.00, max_value=None, value=0.50,  step=1.00 )

with st.sidebar.beta_expander('Curva tipo hiperbólica'):
	qi_hip = st.number_input('Input qi hip',min_value=0.00, max_value=None, value=50.00, step=1.00 )
	b_hip= st.number_input('Input b hip',min_value=0.0000, max_value=None, value=0.5000,  step=0.0100 )
	Di_hip = st.number_input('Input Di hip',min_value=0.00, max_value=None, value=0.50,  step=1.00 )

cantidad_meses = st.number_input('Ingrese la cantidad de meses a analizar',min_value=0.00, max_value=None, value=22.00, step=1.00 )

lista_meses = list(range(0,int(cantidad_meses)))
data_mes = {'Mes':lista_meses}
df = pd.DataFrame(data_mes)
df['Exponencial']= qi_exp/((1+Di_exp*b_exp*df.Mes)**(1/b_exp))
df['Armonica']= qi_arm/((1+Di_arm*b_arm*df.Mes)**(1/b_arm))
df['Hiperbolica']= qi_hip/((1+Di_hip*b_hip*df.Mes)**(1/b_hip))
df['Sum'] = df.Exponencial+df.Armonica+df.Hiperbolica
df['Acum'] = df.Sum*0.365/12

with st.beta_expander('WOR & GOR'):
	cola,colb = st.beta_columns(2)
	with cola:
		wor = st.number_input('Ingrese WOR',min_value=0.00, max_value=None, value=0.40, step=1.00 )
	with colb:
		gor = st.number_input('Ingrese GOR',min_value=0.00, max_value=None, value=500.00, step=1.00 )

df['Oil'] = df.Sum*365/12
df['Water'] = df.Oil*wor
df['Gas'] = df.Oil*gor/1000

st.write(df)



col1 , col2 = st.beta_columns(2)
with col1:

	fig1, ax = plt.subplots()
	ax.plot(df['Mes'], df['Exponencial'],marker = 'x',label="exp")
	ax.plot(df['Mes'], df['Armonica'],marker = '^',label="arm")
	ax.plot(df['Mes'], df['Hiperbolica'], marker = 'o',label="hip")
	ax.set_title('Gráfico escala normal')
	ax.legend(loc="best")
	ax.set_xlabel('Mes')
	ax.set_ylim(ymin=0)
	plt.grid(True, which="both", ls="-")
	st.pyplot(fig1)
with col2:
	fig2, ax = plt.subplots()
	ax.plot(df['Mes'], df['Exponencial'],marker = 'x',label="exp")
	ax.plot(df['Mes'], df['Armonica'],marker = '^',label="arm")
	ax.plot(df['Mes'], df['Hiperbolica'], marker = 'o',label="hip")
	ax.set_title('Gráfico escala logarítmica')
	ax.legend(loc="best")
	ax.set_xlabel('Mes')
	plt.yscale('log')
	plt.grid(True, which="minor", ls="-")
	st.pyplot(fig2)

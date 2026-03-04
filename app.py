import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime
from financial_engine import FinancialMathEngine


st.set_page_config(page_title="Calculadora Financiera", layout="wide", page_icon="🧮")
engine = FinancialMathEngine()

# --- CSS Personalizado ---
st.markdown("""
<style>
    .main-title { font-size: 36px; font-weight: bold; color: #1E3A8A; text-align: center;}
    .section-header { font-size: 24px; font-weight: bold; color: #1F2937; margin-top: 20px;}
    .formula-box { background-color: #F3F4F6; padding: 15px; border-radius: 8px; border-left: 5px solid #3B82F6; }
</style>
""", unsafe_allow_html=True)

# --- NAVEGACIÓN PRINCIPAL ---
opcion = st.sidebar.radio("Módulos Disponibles", [
    "0. Portada e Índice",
    "1. Tasas de Interés",
    "2. Valor del Dinero",
    "3. Rentas y Anualidades",
    "4. Tabla de Amortización",
    "5. Valuación de Bonos",
    "6. Valuación de Acciones",
    "7. Portafolios Eficientes",
    "8. Forwards (Derivados)",
    "9. Opciones (Derivados)", 
    "10. Formulario"
])

if opcion != "0. Portada e Índice":
    st.markdown('<div class="main-title">Calculadora Financiera y Actuarial</div>', unsafe_allow_html=True)

# =============================================================================
# 0. PORTADA E ÍNDICE
# =============================================================================
if opcion == "0. Portada e Índice":
    # Título principal
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Calculadora Financiera y Actuarial</h1>", unsafe_allow_html=True)
    
    st.write("---")
    
    # Créditos
    # =============================================================================
    st.markdown("#### Desarrollado por:")
    st.markdown("- **<a href='https://www.linkedin.com/in/owen-conde-a731b9249/' target='_blank' style='text-decoration: none; color: #2563EB;'>Owen Paredes Conde</a>**", unsafe_allow_html=True)
    
    st.write("---")
    
    # Descripción de la herramienta
    st.markdown("""
    Bienvenido a la Calculadora Financiera y Actuarial. Esta herramienta interactiva fue desarrollada en Python utilizando `Streamlit` 
    para automatizar y visualizar los cálculos más rigurosos de las matemáticas financieras, desde el valor del dinero en el tiempo 
    hasta la valuación de derivados con el modelo de y Árboles Binomiales y Black-Scholes-Merton.
    
    *Aviso: Esta herramienta tiene fines netamente académicos y de demostración.*
    """)
    
    st.write("---")
    
    # Índice Visual
    st.markdown("### Mapa de la Calculadora (Usa el menú lateral para navegar)")
    
    idx1, idx2 = st.columns(2)
    with idx1:
        st.info("**1. Tasas de Interés**\n\nTasas nominales, efectivas, continuas.")
        st.info("**2. Valor del Dinero**\n\nCálculos de Interés Compuesto y Tasas continuas, Valor presente y futuro.")
        st.info("**3. Rentas y Anualidades**\n\nRentas vencidas, anticipadas, diferidas y crecientes aritméticos y geométricos.")
        st.info("**4. Tabla de Amortización**\n\nTablas dinámicas para créditos y fondos de amortización.")
        st.info("**5. Valuación de Bonos**\n\nCálculo de precio limpio, sucio y Yield to Maturity.")
        
    with idx2:
        st.success("**6. Valuación de Acciones**\n\nModelo de Gordon-Shapiro y valuación relativa por múltiplos de mercado.")
        st.success("**7. Portafolios Eficientes**\n\nOptimización de carteras con el modelo de Markowitz.")
        st.success("**8. Forwards y Futuros**\n\nDeterminación de precios teóricos y valuación de contratos.")
        st.success("**9. Opciones (Derivados)**\n\nPrimas y Griegas con Black-Scholes-Merton y Árboles Binomiales (CRR).")
        st.success("**10. Formulario Oficial**\n\nCheat-sheet descargable en HTML con todas las ecuaciones matemáticas utilizadas.")


    # =============================================================================
    # Pie de página: Comentarios, Sugerencias y Uso Local
    # =============================================================================
    st.write("---")
    
    # Sección de Uso Local (GitHub)
    st.info(" **Recomendación para uso sin límites:** Si experimentas lentitud por saturación del servidor, te recomendamos descargar el código fuente y ejecutar la calculadora de forma local en tu computadora.")
    st.markdown("<p style='text-align: center; font-size: 1.1em;'> <b><a href='https://github.com/Walls16/calculadora-actuarial' target='_blank' style='text-decoration: none; color: #1E3A8A;'>Descargar desde GitHub</a></b></p>", unsafe_allow_html=True)
    
    st.write("---")
    
    # Sección de Contacto
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 1.1em;'>¿Tienes comentarios, dudas o sugerencias para mejorar esta calculadora?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'> <b><a href='https://www.linkedin.com/in/owen-conde-a731b9249/' target='_blank' style='text-decoration: none; color: #2563EB;'>Contáctame en LinkedIn (Owen Paredes Conde)</a></b></p>", unsafe_allow_html=True)
# =============================================================================
# 1. TASAS DE INTERÉS
# =============================================================================
if opcion == "1. Tasas de Interés":
    st.markdown('<div class="section-header">1. Conversión de Tasas</div>', unsafe_allow_html=True)
    
    tabs = st.tabs([
        "Triple Igualdad", 
        "De i^(m) a i, δ", 
        "De δ a i", 
        "De δ a i^(m)", 
        "De i^(m) a i^(p)", 
        "Reinversión"
    ])
    
    # TAB 0: Triple igualdad
    with tabs[0]:
        st.markdown("### La triple igualdad de tasas de interés")
        st.info("Esta ecuación relaciona la tasa efectiva anual ($i$), la tasa nominal capitalizable $m$ veces al año ($i^{(m)}$) y la tasa instantánea o fuerza de interés ($\delta$).")
        st.latex(r"1 + i = \left(1 + \frac{i^{(m)}}{m}\right)^m = e^\delta")
        
        st.write("---")
        with st.expander("Ver Explicación de la Triple Igualdad"):
            st.markdown(r"""
            **Concepto Clave:**
            El objetivo de las finanzas es que, sin importar con qué frecuencia se reinviertan los intereses (mensual, diario o en cada milisegundo), un inversionista gane exactamente el mismo rendimiento a final de año.
            
            * Si inviertes **$1$** y te pagan el interés solo una vez al final del año, terminas con **$(1 + i)$**.
            * Si te lo pagan en $m$ pedacitos al año, terminas con **$(1 + \frac{i^{(m)}}{m})^m$**.
            * Si la capitalización es continua (infinita), terminas con **$e^\delta$**.
            
            Como el rendimiento real anual (la tasa efectiva $i$) debe ser el mismo para que no haya arbitraje, estas tres expresiones son matemáticamente idénticas.
            """)
        
    # TAB 1: De tasas nominales i(m) a tasas efectivas i e instantáneas d
    with tabs[1]:
        st.markdown("### De tasas nominales $i^{(m)}$ a tasas efectivas $i$ e instantáneas $\delta$")
        c1, c2 = st.columns(2)
        
        with c1:
            j = st.number_input("Tasa Nominal $i^{(m)}$ %", value=20.0, step=0.1, key="t1_j") / 100
            m = st.number_input("Frecuencia (m)", min_value=0.0001, value=12.0, step=0.5, format="%.2f", key="t1_m")
            
        with c2:
            i_eff = engine.tasa_nominal_a_efectiva(j, m)
            delta = engine.tasa_nominal_a_instantanea(j, m)
            
            st.metric("Tasa Efectiva Anual (i)", f"{i_eff*100:.2f}%")
            st.metric("Tasa Instantánea (\delta)", f"{delta*100:.2f}%")

        st.write("---")
        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**1. Cálculo a Tasa Efectiva ($i$):**")
            st.latex(r"i = \left(1 + \frac{i^{(m)}}{m}\right)^m - 1")
            # Desarrollo dinámico
            st.latex(rf"i = \left(1 + \frac{{{j:.4f}}}{{{m:g}}}\right)^{{{m:g}}} - 1")
            st.latex(rf"i = (1 + {j/m:.6f})^{{{m:g}}} - 1")
            st.latex(rf"i = {(1+j/m)**m:.6f} - 1 = {i_eff:.6f}")
            st.success(f"**$i = {i_eff*100:.4f}\%$**")
            
            st.info("**2. Cálculo a Fuerza de Interés ($\delta$):**")
            st.latex(r"\delta = m \ln\left(1 + \frac{i^{(m)}}{m}\right)")
            # Desarrollo dinámico
            st.latex(rf"\delta = {m:g} \ln\left(1 + \frac{{{j:.4f}}}{{{m:g}}}\right)")
            st.latex(rf"\delta = {m:g} \ln(1 + {j/m:.6f}) = {m:g} \times {np.log(1+j/m):.6f}")
            st.latex(rf"\delta = {delta:.6f}")
            st.success(f"**$\delta = {delta*100:.4f}\%$**")

    # TAB 2: De tasas instantáneas d a tasa efectiva i
    with tabs[2]:
        st.markdown("### De tasas instantáneas $\delta$ a tasa efectiva $i$")
        c1, c2 = st.columns(2)
        
        with c1:
            d_tab2 = st.number_input("Tasa Instantánea $\delta$ %", value=18.0, step=0.1, key="t2_d") / 100
            
        with c2:
            i_eff_tab2 = engine.tasa_instantanea_a_efectiva(d_tab2)
            st.metric("Tasa Efectiva Anual (i)", f"{i_eff_tab2*100:.2f}%")

        st.write("---")
        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**Sustitución y Desarrollo:**")
            st.latex(r"i = e^\delta - 1")
            # Desarrollo dinámico
            st.latex(rf"i = e^{{{d_tab2:.4f}}} - 1")
            st.latex(rf"i = {np.exp(d_tab2):.6f} - 1")
            st.latex(rf"i = {i_eff_tab2:.6f}")
            st.success(f"**$i = {i_eff_tab2*100:.4f}\%$**")

    # TAB 3: De tasas instantáneas d a tasas nominales i(m)
    with tabs[3]:
        st.markdown("### De tasas instantáneas $\delta$ a tasas nominales $i^{(m)}$")
        c1, c2 = st.columns(2)
        
        with c1:
            d_tab3 = st.number_input("Tasa Instantánea $\delta$ %", value=18.0, step=0.1, key="t3_d") / 100
            m_tab3 = st.number_input("Frecuencia deseada (m)", min_value=0.0001, value=12.0, step=0.5, format="%.4f", key="t3_m")
            
        with c2:
            i_nom_tab3 = engine.tasa_instantanea_a_nominal(d_tab3, m_tab3)
            st.metric("Tasa Nominal $i^{(m)}$", f"{i_nom_tab3*100:.3f}%")

        st.write("---")
        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**Sustitución y Desarrollo:**")
            st.latex(r"i^{(m)} = m \left(e^{\delta/m} - 1\right)")
            # Desarrollo dinámico
            st.latex(rf"i^{{({m_tab3:g})}} = {m_tab3:g} \left(e^{{\frac{{{d_tab3:.4f}}}{{{m_tab3:g}}}}} - 1\right)")
            st.latex(rf"i^{{({m_tab3:g})}} = {m_tab3:g} \left(e^{{{d_tab3/m_tab3:.6f}}} - 1\right)")
            st.latex(rf"i^{{({m_tab3:g})}} = {m_tab3:g} ({np.exp(d_tab3/m_tab3):.6f} - 1)")
            st.latex(rf"i^{{({m_tab3:g})}} = {m_tab3:g} ({np.exp(d_tab3/m_tab3) - 1:.6f}) = {i_nom_tab3:.6f}")
            st.success(f"**$i^{{({m_tab3:g})}} = {i_nom_tab3*100:.4f}\%$**")

    # TAB 4: De tasas tasas nominales i(m) a tasas nominales i(p)
    with tabs[4]:
        st.markdown("### De tasas nominales $i^{(m)}$ a tasas nominales $i^{(p)}$")
        c1, c2 = st.columns(2)
        
        with c1:
            i_orig = st.number_input("Tasa Nominal Origen $i^{(m)}$ %", value=10.0, step=0.1, key="t4_i") / 100
            m_orig = st.number_input("Frecuencia Origen (m)", min_value=0.0001, value=2.0, step=0.5, format="%.2f", key="t4_m")
            p_dest = st.number_input("Frecuencia Destino (p)", min_value=0.0001, value=3.0, step=0.5, format="%.2f", key="t4_p")
            
        with c2:
            i_p = engine.tasa_nominal_m_a_nominal_p(i_orig, m_orig, p_dest)
            st.metric(f"Tasa Nominal $i^{{({p_dest:g})}}$", f"{i_p*100:.4f}%")
            st.latex(r"i^{(p)} = p \left[ \left(1 + \frac{i^{(m)}}{m}\right)^{\frac{m}{p}} - 1 \right]")

        st.write("---")
        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**Igualación de factores de acumulación:**")
            st.latex(r"\left(1 + \frac{i^{(p)}}{p}\right)^p = \left(1 + \frac{i^{(m)}}{m}\right)^m")
            st.latex(r"\frac{i^{(p)}}{p} = \left(1 + \frac{i^{(m)}}{m}\right)^{\frac{m}{p}} - 1")
            
            # Desarrollo dinámico
            frac_m_p = m_orig/p_dest
            tasa_per_orig = i_orig/m_orig
            st.latex(rf"\frac{{i^{{({p_dest:g})}}}}{{{p_dest:g}}} = \left(1 + \frac{{{i_orig:.4f}}}{{{m_orig:g}}}\right)^{{\frac{{{m_orig:g}}}{{{p_dest:g}}}}} - 1")
            st.latex(rf"\frac{{i^{{({p_dest:g})}}}}{{{p_dest:g}}} = (1 + {tasa_per_orig:.6f})^{{{frac_m_p:.4f}}} - 1")
            st.latex(rf"\frac{{i^{{({p_dest:g})}}}}{{{p_dest:g}}} = {(1+tasa_per_orig)**frac_m_p:.6f} - 1 = {((1+tasa_per_orig)**frac_m_p) - 1:.6f}")
            
            st.info("**Despejando la tasa nominal anual:**")
            st.latex(rf"i^{{({p_dest:g})}} = {p_dest:g} \times {((1+tasa_per_orig)**frac_m_p) - 1:.6f}")
            st.latex(rf"i^{{({p_dest:g})}} = {i_p:.6f}")
            st.success(f"**$i^{{({p_dest:g})}} = {i_p*100:.4f}\%$**")

    # TAB 5: Ilustración de la reinversión
    with tabs[5]:
        st.markdown("### Ilustración de la reinversión de los intereses a tasas efectivas, nominales e instantáneas")
        
        c1, c2, c3 = st.columns(3)
        C0 = c1.number_input("Capital Inicial ($C_0$)", min_value=0.0, value=100000.0, step=1000.0, key="t5_c0")
        tasa_ref = c2.number_input("Tasa Nominal ($i$) %", value=10.0, step=0.1, key="t5_ref") / 100
        n_anios = c3.number_input("Periodos ($n$)", min_value=0.1, value=1.0, step=1.0, key="t5_n")
        
        # --- 1. MOSTRAR LA TABLA DEL EXCEL ---
        st.subheader("Tabla de Acumulación")
        df_reinversion = engine.generar_tabla_reinversion(C0, tasa_ref, n_anios)
        
        st.dataframe(
            df_reinversion.style.format({
                "Monto acumulado": "${:,.2f}",
                "Rendimiento Acumulado": "{:.4f}%"
            }), 
            use_container_width=True,
            hide_index=True
        )

        # --- 2. GRÁFICA CON BOLITAS DE COLORES ---
        st.subheader("Gráfica de Convergencia")
        
        import plotly.graph_objects as go
        import plotly.express as px
        
        fig = px.scatter(df_reinversion, 
                         x="Periodo de reinversión", 
                         y="Monto acumulado", 
                         color="Periodo de reinversión",
                         title="Monto Acumulado vs. Frecuencia de Reinversión",
                         labels={
                             "Periodo de reinversión": "Frecuencia de Capitalización", 
                             "Monto acumulado": "Monto Acumulado ($)"
                         })
                         
        fig.update_traces(marker=dict(size=14), selector=dict(mode='markers'))

        fig.add_trace(go.Scatter(
            x=df_reinversion["Periodo de reinversión"], 
            y=df_reinversion["Monto acumulado"],
            mode="lines", 
            line=dict(color="#cbd5e1", width=2), 
            showlegend=False,
            hoverinfo="skip"
        ))
        
        fig.data = fig.data[::-1]
        fig.update_layout(yaxis=dict(tickformat="$.2f"))
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("---")
        with st.expander("¿Cómo interpretar esta gráfica?"):
            st.info("""
            **La magia del límite matemático ($e$)**
            
            Observa cómo, al inicio, aumentar la frecuencia de capitalización (de anual a mensual) da un gran salto en el monto acumulado. 
            Sin embargo, conforme la frecuencia sigue aumentando (diaria, por hora, por minuto...), la curva se aplana. 
            
            Llega un punto donde no importa cuántas veces más dividas el año, el dinero choca contra un **"techo invisible"**. Ese techo matemático es la capitalización continua, gobernada por el número de Euler ($e$). El interés compuesto tiene un límite máximo de crecimiento.
            """)
# =============================================================================
# 2. VALOR DEL DINERO EN EL TIEMPO
# =============================================================================
elif opcion == "2. Valor del Dinero":
    import numpy as np
    st.markdown('<div class="section-header">2. Valor del Dinero en el Tiempo</div>', unsafe_allow_html=True)
    
    t1, t2, t3, t4 = st.tabs(["Valor Futuro", "Valor Presente", "Número de Periodos", "Tasa de Rendimiento"])
    
    # ---------------------------------------------------------
    # TAB 1: VALOR FUTURO
    # ---------------------------------------------------------
    with t1:
        st.markdown("### Valor futuro de una inversión inicial $C_0$")
        
        escenario_vf = st.radio("Tipo de tasa:", [
            "Tasa efectiva",
            "Tasa nominal",
            "Tasa instantánea"
        ], horizontal=True, key="radio_vf")
        
        st.write("---")
        
        c1, c2 = st.columns(2)
        with c1:
            if escenario_vf == "Tasa efectiva":
                C0_vf = st.number_input("Capital Inicial ($C_0$)", min_value=0.0, value=20000.0, step=1000.0, key="vf_c0_1")
                i_vf = st.number_input("Tasa efectiva anual ($i$) %", value=6.8, step=0.1, key="vf_i") / 100
                n_vf = st.number_input("Años ($n$)", min_value=0.0, value=6.0, step=1.0, key="vf_n")
                
                vf_res = engine.valor_futuro(C0_vf, i_vf, n_vf)
                formula_vf = r"VF = C_0 (1+i)^n"
                
            elif escenario_vf == "Tasa nominal":
                C0_vf = st.number_input("Capital Inicial ($C_0$)", min_value=0.0, value=54000.0, step=1000.0, key="vf_c0_2")
                i_nom_vf = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=11.25, step=0.1, key="vf_inom") / 100
                n_vf2 = st.number_input("Años ($n$)", min_value=0.0, value=8.0, step=1.0, key="vf_n2")
                m_vf = st.number_input("Periodos por año ($m$)", min_value=1.0, value=4.0, step=1.0, key="vf_m")
                
                im_vf = i_nom_vf / m_vf
                vf_res = engine.valor_futuro(C0_vf, im_vf, n_vf2 * m_vf)
                formula_vf = r"VF = C_0 \left(1+\frac{i^{(m)}}{m}\right)^{nm}"
                
            else: # Tasa instantánea
                C0_vf = st.number_input("Capital Inicial ($C_0$)", min_value=0.0, value=20000.0, step=1000.0, key="vf_c0_3")
                d_vf = st.number_input("Tasa instantánea ($\delta$) %", value=5.0, step=0.1, key="vf_d") / 100
                n_vf3 = st.number_input("Años ($n$)", min_value=0.0, value=10.0, step=1.0, key="vf_n3")
                
                vf_res = engine.valor_futuro_continuo(C0_vf, d_vf, n_vf3)
                formula_vf = r"VF = C_0 e^{\delta n}"
                
        with c2:
            st.metric("Valor Futuro ($C_n$)", f"${vf_res:,.2f}")
            st.latex(formula_vf)

        st.write("---")
        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**Sustitución y Desarrollo:**")
            if escenario_vf == "Tasa efectiva":
                st.latex(r"VF = C_0 (1+i)^n")
                st.latex(rf"VF = {C0_vf:,.2f} \times (1 + {i_vf:.4f})^{{{n_vf:g}}}")
                st.latex(rf"VF = {C0_vf:,.2f} \times {(1+i_vf)**n_vf:.6f}")
                st.latex(rf"VF = {vf_res:,.2f}")
            elif escenario_vf == "Tasa nominal":
                st.latex(r"VF = C_0 \left(1+\frac{i^{(m)}}{m}\right)^{nm}")
                st.latex(rf"VF = {C0_vf:,.2f} \left(1 + \frac{{{i_nom_vf:.4f}}}{{{m_vf:g}}}\right)^{{{n_vf2:g} \times {m_vf:g}}}")
                st.latex(rf"VF = {C0_vf:,.2f} \left(1 + {im_vf:.6f}\right)^{{{n_vf2*m_vf:g}}}")
                st.latex(rf"VF = {C0_vf:,.2f} \times {(1+im_vf)**(n_vf2*m_vf):.6f}")
                st.latex(rf"VF = {vf_res:,.2f}")
            else:
                st.latex(r"VF = C_0 e^{\delta n}")
                st.latex(rf"VF = {C0_vf:,.2f} \times e^{{({d_vf:.4f} \times {n_vf3:g})}}")
                st.latex(rf"VF = {C0_vf:,.2f} \times e^{{{d_vf*n_vf3:.6f}}}")
                st.latex(rf"VF = {C0_vf:,.2f} \times {np.exp(d_vf*n_vf3):.6f}")
                st.latex(rf"VF = {vf_res:,.2f}")
            st.success(f"**Resultado Final: ${vf_res:,.2f}**")

    # ---------------------------------------------------------
    # TAB 2: VALOR PRESENTE
    # ---------------------------------------------------------
    with t2:
        st.markdown("### Valor presente de una cantidad de dinero futura $C_n$")
        
        escenario_vp = st.radio("Tipo de tasa:", [
            "Tasa efectiva",
            "Tasa nominal",
            "Tasa instantánea"
        ], horizontal=True, key="radio_vp")
        
        st.write("---")
        
        c1, c2 = st.columns(2)
        with c1:
            if escenario_vp == "Tasa efectiva":
                Cn_vp = st.number_input("Valor Futuro ($C_n$)", min_value=0.0, value=245000.0, step=1000.0, key="vp_cn_1")
                i_vp = st.number_input("Tasa efectiva anual ($i$) %", value=11.2, step=0.1, key="vp_i") / 100
                n_vp = st.number_input("Años ($n$)", min_value=0.0, value=9.0, step=1.0, key="vp_n")
                
                vp_res = engine.valor_presente(Cn_vp, i_vp, n_vp)
                formula_vp = r"VP = C_n (1+i)^{-n}"
                
            elif escenario_vp == "Tasa nominal":
                Cn_vp = st.number_input("Valor Futuro ($C_n$)", min_value=0.0, value=1000.0, step=100.0, key="vp_cn_2")
                i_nom_vp = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=10.0, step=0.1, key="vp_inom") / 100
                n_vp2 = st.number_input("Años ($n$)", min_value=0.0, value=10.0, step=1.0, key="vp_n2")
                m_vp = st.number_input("Periodos por año ($m$)", min_value=1.0, value=2.0, step=1.0, key="vp_m")
                
                im_vp = i_nom_vp / m_vp
                vp_res = engine.valor_presente(Cn_vp, im_vp, n_vp2 * m_vp)
                formula_vp = r"VP = C_n \left(1+\frac{i^{(m)}}{m}\right)^{-nm}"
                
            else: # Tasa instantánea
                Cn_vp = st.number_input("Valor Futuro ($C_n$)", min_value=0.0, value=1000.0, step=1000.0, key="vp_cn_3")
                d_vp = st.number_input("Tasa instantánea ($\delta$) %", value=5.0, step=0.1, key="vp_d") / 100
                n_vp3 = st.number_input("Años ($n$)", min_value=0.0, value=10.0, step=1.0, key="vp_n3")
                
                vp_res = engine.valor_presente_continuo(Cn_vp, d_vp, n_vp3)
                formula_vp = r"VP = C_n e^{-\delta n}"
                
        with c2:
            st.metric("Valor Presente ($C_0$)", f"${vp_res:,.2f}")
            st.latex(formula_vp)

        st.write("---")
        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**Sustitución y Desarrollo (Descuento):**")
            if escenario_vp == "Tasa efectiva":
                st.latex(r"VP = C_n (1+i)^{-n}")
                st.latex(rf"VP = {Cn_vp:,.2f} \times (1 + {i_vp:.4f})^{{-{n_vp:g}}}")
                st.latex(rf"VP = {Cn_vp:,.2f} \times {(1+i_vp)**(-n_vp):.6f}")
                st.latex(rf"VP = {vp_res:,.2f}")
            elif escenario_vp == "Tasa nominal":
                st.latex(r"VP = C_n \left(1+\frac{i^{(m)}}{m}\right)^{-nm}")
                st.latex(rf"VP = {Cn_vp:,.2f} \left(1 + \frac{{{i_nom_vp:.4f}}}{{{m_vp:g}}}\right)^{{-({n_vp2:g} \times {m_vp:g})}}")
                st.latex(rf"VP = {Cn_vp:,.2f} \left(1 + {im_vp:.6f}\right)^{{-{n_vp2*m_vp:g}}}")
                st.latex(rf"VP = {Cn_vp:,.2f} \times {(1+im_vp)**(-n_vp2*m_vp):.6f}")
                st.latex(rf"VP = {vp_res:,.2f}")
            else:
                st.latex(r"VP = C_n e^{-\delta n}")
                st.latex(rf"VP = {Cn_vp:,.2f} \times e^{{-({d_vp:.4f} \times {n_vp3:g})}}")
                st.latex(rf"VP = {Cn_vp:,.2f} \times e^{{-{d_vp*n_vp3:.6f}}}")
                st.latex(rf"VP = {Cn_vp:,.2f} \times {np.exp(-d_vp*n_vp3):.6f}")
                st.latex(rf"VP = {vp_res:,.2f}")
            st.success(f"**Resultado Final: ${vp_res:,.2f}**")

    # ---------------------------------------------------------
    # TAB 3: NÚMERO DE PERIODOS
    # ---------------------------------------------------------
    with t3:
        st.markdown("### Determinación del número de periodos de una inversión")
        c1, c2 = st.columns(2)
        
        with c1:
            va_nper = st.number_input("Valor Inicial ($C_0$)", min_value=0.01, value=50000.0, step=1000.0, key="nper_va")
            vf_nper = st.number_input("Valor Final ($C_n$)", min_value=0.01, value=245000.0, step=1000.0, key="nper_vf")
            i_nper = st.number_input("Tasa Efectiva ($i$) %", min_value=0.0001, value=4.3, step=0.1, key="nper_i") / 100
            
        with c2:
            n_res = engine.numero_periodos(va_nper, vf_nper, i_nper)
            st.metric("Número de Periodos ($n$)", f"{n_res:.5f}")
            st.latex(r"n = \frac{\ln(C_n/C_0)}{\ln(1+i)}")
            
        st.write("---")
        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**Propiedades de los Logaritmos:**")
            st.latex(r"C_n = C_0(1+i)^n \implies \frac{C_n}{C_0} = (1+i)^n")
            st.latex(r"\ln\left(\frac{C_n}{C_0}\right) = n \cdot \ln(1+i) \implies n = \frac{\ln(C_n/C_0)}{\ln(1+i)}")
            st.info("**Sustitución:**")
            st.latex(rf"n = \frac{{\ln({vf_nper:,.2f} / {va_nper:,.2f})}}{{\ln(1 + {i_nper:.4f})}}")
            ratio = vf_nper / va_nper
            st.latex(rf"n = \frac{{\ln({ratio:.6f})}}{{\ln({1+i_nper:.4f})}}")
            num = np.log(ratio)
            den = np.log(1+i_nper)
            st.latex(rf"n = \frac{{{num:.6f}}}{{{den:.6f}}} = {n_res:.5f}")
            st.success(f"**Resultado: Se requieren {n_res:.5f} periodos.**")

        st.markdown("#### Desglose del Tiempo Exacto")
        
        df_desglose = engine.desglosar_periodos(n_res)
        
        st.dataframe(
            df_desglose.style.set_properties(**{
                'background-color': '#F3F4F6',
                'color': '#1E3A8A',
                'font-weight': 'bold',
                'text-align': 'center'
            }), 
            use_container_width=True, 
            hide_index=True
        )

    # ---------------------------------------------------------
    # TAB 4: TASA DE RENDIMIENTO
    # ---------------------------------------------------------
    with t4:
        st.markdown("### Tasa de rendimiento efectivo anual o tasa de crecimiento geométrico")
        c1, c2 = st.columns(2)
        with c1:
            va_rate = st.number_input("Valor Inicial ($C_0$)", min_value=0.01, value=4582500.0, step=1000.0, key="rate_va")
            vf_rate = st.number_input("Valor Final ($C_n$)", min_value=0.01, value=9360000.0, step=1000.0, key="rate_vf")
            n_rate = st.number_input("Periodos ($n$)", min_value=0.1, value=10.0, step=1.0, key="rate_n")
            
        with c2:
            i_res = engine.tasa_rendimiento(va_rate, vf_rate, n_rate)
            st.metric("Tasa de Rendimiento ($i$)", f"{i_res*100:.4f}%")
            st.latex(r"i = \left(\frac{C_n}{C_0}\right)^{\frac{1}{n}} - 1")

        st.write("---")
        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**Despejando la tasa mediante raíz n-ésima:**")
            st.latex(r"C_n = C_0(1+i)^n \implies \frac{C_n}{C_0} = (1+i)^n")
            st.latex(r"1+i = \sqrt[n]{\frac{C_n}{C_0}} \implies i = \left(\frac{C_n}{C_0}\right)^{\frac{1}{n}} - 1")
            st.info("**Sustitución:**")
            st.latex(rf"i = \left(\frac{{{vf_rate:,.2f}}}{{{va_rate:,.2f}}}\right)^{{\frac{{1}}{{{n_rate:g}}}}} - 1")
            ratio = vf_rate / va_rate
            exp_val = 1 / n_rate
            st.latex(rf"i = ({ratio:.6f})^{{{exp_val:.6f}}} - 1")
            st.latex(rf"i = {ratio**exp_val:.6f} - 1 = {i_res:.6f}")
            st.success(f"**Resultado: La tasa de rendimiento es {i_res*100:.4f}\% por periodo.**")
# =============================================================================
# 3. RENTAS Y ANUALIDADES (Fusionado con Gradientes)
# =============================================================================
elif opcion == "3. Rentas y Anualidades":
    import numpy as np
    st.markdown('<div class="section-header">3. Valuación de Rentas y Anualidades</div>', unsafe_allow_html=True)
    
    tab_vf, tab_vp, tab_n = st.tabs(["Valor Futuro de Rentas", "Valor Presente de Rentas", "Número de Periodos (n)"])
    
    # =========================================================
    # TAB 1: VALOR FUTURO
    # =========================================================
    with tab_vf:
        tipo_renta_vf = st.radio("Tipo de Renta:", [
            "Rentas Constantes Periódicas",
            "Rentas Crecientes Geométricas",
            "Rentas Crecientes Aritméticas"
        ], horizontal=True, key="radio_tipo_vf")
        
        st.write("---")
        
        # -----------------------------------------------------
        # CONSTANTES PERIÓDICAS (VF)
        # -----------------------------------------------------
        if tipo_renta_vf == "Rentas Constantes Periódicas":
            
            escenario_const_vf = st.selectbox("Seleccione el escenario:", [
                "Vencidas a una tasa efectiva im",
                "Anticipadas a una tasa efectiva im",
                "Vencidas pagaderas p veces al año a tasa nominal i(m)",
                "Continuas a una tasa instantánea δ"
            ], key="sel_const_vf")
            
            c1, c2 = st.columns(2)
            
            with c1:
                if escenario_const_vf == "Vencidas a una tasa efectiva im":
                    R_vf = st.number_input("Pago periódico ($R$)", min_value=0.0, value=1000.0, step=100.0, key="vf_rc_1")
                    i_nom_vf = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=12.0, step=0.1, key="vf_rc_i1") / 100
                    n_vf = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vf_rc_n1")
                    m_vf = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vf_rc_m1")
                    
                    im_vf = i_nom_vf / m_vf
                    vf_res = engine.vf_anualidad_efectiva(R_vf, im_vf, n_vf * m_vf, anticipada=False)
                    formula_latex = r"VF = R \left[ \frac{\left(1+\frac{i^{(m)}}{m}\right)^{nm} - 1}{\frac{i^{(m)}}{m}} \right]"
                
                elif escenario_const_vf == "Anticipadas a una tasa efectiva im":
                    R_vf = st.number_input("Pago periódico ($R$)", min_value=0.0, value=1000.0, step=100.0, key="vf_rc_2")
                    i_nom_vf = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=12.0, step=0.1, key="vf_rc_i2") / 100
                    n_vf = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vf_rc_n2")
                    m_vf = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vf_rc_m2")
                    
                    im_vf = i_nom_vf / m_vf
                    vf_res = engine.vf_anualidad_efectiva(R_vf, im_vf, n_vf * m_vf, anticipada=True)
                    formula_latex = r"VF = R \left[ \frac{\left(1+\frac{i^{(m)}}{m}\right)^{nm} - 1}{\frac{i^{(m)}}{m}} \right] \left(1+\frac{i^{(m)}}{m}\right)"
                
                elif escenario_const_vf == "Vencidas pagaderas p veces al año a tasa nominal i(m)":
                    R_vf = st.number_input("Pago periódico ($R$)", min_value=0.0, value=1000.0, step=100.0, key="vf_rc_3")
                    i_nom_vf = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=12.0, step=0.1, key="vf_rc_inom") / 100
                    m_vf = st.number_input("Capitalizaciones por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vf_rc_m3")
                    p_vf = st.number_input("Pagos por año ($p$)", min_value=1.0, value=4.0, step=1.0, key="vf_rc_p")
                    n_vf = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vf_rc_n3")
                    
                    vf_res = engine.vf_anualidad_nominal(R_vf, i_nom_vf, m_vf, p_vf, n_vf)
                    formula_latex = r"VF = R \left[ \frac{\left(1+\frac{i^{(p)}}{p}\right)^{np} - 1}{\frac{i^{(p)}}{p}} \right]"
                
                elif escenario_const_vf == "Continuas a una tasa instantánea δ": 
                    R_anual_vf = st.number_input(r"Flujo Anual Total ($\bar{R}$)", min_value=0.0, value=12000.0, step=1000.0, key="vf_rc_4")
                    tipo_tasa_continua = st.radio("Ingresar tasa como:", ["Tasa instantánea ($\delta$)", "Tasa efectiva anual ($i$)"], horizontal=True, key="tipo_t_cont_vf")
                    n_vf = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vf_rc_n4")
                    
                    if tipo_tasa_continua == "Tasa instantánea ($\delta$)":
                        d_vf = st.number_input(r"Tasa instantánea ($\delta$) %", value=10.0, step=0.1, key="vf_rc_d") / 100
                        vf_res = engine.vf_anualidad_continua(R_anual_vf, d_vf, n_vf)
                        formula_latex = r"VF = \bar{R} \left[ \frac{e^{\delta n} - 1}{\delta} \right]"
                    else:
                        i_eff_vf = st.number_input("Tasa efectiva anual ($i$) %", value=10.51, step=0.1, key="vf_rc_ieff") / 100
                        d_vf = np.log(1 + i_eff_vf) 
                        vf_res = engine.vf_anualidad_continua(R_anual_vf, d_vf, n_vf)
                        formula_latex = r"VF = \bar{R} \left[ \frac{(1+i)^n - 1}{\ln(1+i)} \right]"
            
            with c2:
                st.metric("Valor Futuro Acumulado ($VF$)", f"${vf_res:,.3f}")
                st.latex(formula_latex)

            st.write("---")
            with st.expander("Ver desarrollo paso a paso del cálculo actual"):
                st.info("**Sustitución y Desarrollo:**")
                if escenario_const_vf == "Vencidas a una tasa efectiva im":
                    st.latex(rf"VF = {R_vf:,.2f} \left[ \frac{{\left(1 + \frac{{{i_nom_vf:.4f}}}{{{m_vf:g}}}\right)^{{{n_vf*m_vf:g}}} - 1}}{{\frac{{{i_nom_vf:.4f}}}{{{m_vf:g}}}}} \right]")
                    st.latex(rf"VF = {R_vf:,.2f} \left[ \frac{{(1 + {im_vf:.6f})^{{{n_vf*m_vf:g}}} - 1}}{{{im_vf:.6f}}} \right]")
                    factor = ((1 + im_vf)**(n_vf * m_vf) - 1) / im_vf
                    st.latex(rf"VF = {R_vf:,.2f} \times [{factor:.6f}] = {vf_res:,.2f}")
                elif escenario_const_vf == "Anticipadas a una tasa efectiva im":
                    st.latex(rf"VF = {R_vf:,.2f} \left[ \frac{{(1 + {im_vf:.6f})^{{{n_vf*m_vf:g}}} - 1}}{{{im_vf:.6f}}} \right] (1 + {im_vf:.6f})")
                    factor = ((1 + im_vf)**(n_vf * m_vf) - 1) / im_vf
                    st.latex(rf"VF = {R_vf:,.2f} \times [{factor:.6f}] \times {(1 + im_vf):.6f} = {vf_res:,.2f}")
                elif escenario_const_vf == "Vencidas pagaderas p veces al año a tasa nominal i(m)":
                    i_p = engine.tasa_nominal_m_a_nominal_p(i_nom_vf, m_vf, p_vf)
                    ip_p = i_p / p_vf
                    st.latex(rf"\text{{1. Tasa equivalente: }} i^{{({p_vf:g})}} = {i_p:.6f} \implies \frac{{i^{{({p_vf:g})}}}}{{{p_vf:g}}} = {ip_p:.6f}")
                    st.latex(rf"\text{{2. Sustitución: }} VF = {R_vf:,.2f} \left[ \frac{{(1 + {ip_p:.6f})^{{{n_vf*p_vf:g}}} - 1}}{{{ip_p:.6f}}} \right]")
                    factor = ((1 + ip_p)**(n_vf * p_vf) - 1) / ip_p
                    st.latex(rf"VF = {R_vf:,.2f} \times [{factor:.6f}] = {vf_res:,.2f}")
                elif escenario_const_vf == "Continuas a una tasa instantánea δ":
                    if tipo_tasa_continua == "Tasa instantánea ($\delta$)":
                        st.latex(rf"VF = {R_anual_vf:,.2f} \left[ \frac{{e^{{({d_vf:.4f} \times {n_vf:g})}} - 1}}{{{d_vf:.4f}}} \right]")
                        factor = (np.exp(d_vf * n_vf) - 1) / d_vf
                        st.latex(rf"VF = {R_anual_vf:,.2f} \times [{factor:.6f}] = {vf_res:,.2f}")
                    else:
                        st.latex(rf"\text{{1. Tasa Continua: }} \delta = \ln(1 + {i_eff_vf:.4f}) = {d_vf:.6f}")
                        st.latex(rf"\text{{2. Sustitución: }} VF = {R_anual_vf:,.2f} \left[ \frac{{(1 + {i_eff_vf:.4f})^{{{n_vf:g}}} - 1}}{{{d_vf:.6f}}} \right]")
                        factor = ((1 + i_eff_vf)**n_vf - 1) / d_vf
                        st.latex(rf"VF = {R_anual_vf:,.2f} \times [{factor:.6f}] = {vf_res:,.2f}")
                st.success(f"**Resultado Final: ${vf_res:,.2f}**")
                
        # -----------------------------------------------------
        # CRECIENTES GEOMÉTRICAS (VF)
        # -----------------------------------------------------
        elif tipo_renta_vf == "Rentas Crecientes Geométricas":
            st.markdown("#### Rentas geométricas (el pago crece a una tasa $q$)")
            
            tipo_tasa_geo_vf = st.radio("Ingresar tasas como:", ["Tasa efectiva periódica", "Tasa nominal anual"], horizontal=True, key="tipo_t_geo_vf")
            st.write("---")
            
            c1, c2 = st.columns(2)
            
            with c1:
                R1_vf = st.number_input("Monto del Primer Pago ($R_1$)", min_value=0.0, value=1000.0, step=100.0, key="vf_geo_r1")
                
                if tipo_tasa_geo_vf == "Tasa efectiva periódica":
                    im_geo = st.number_input("Tasa efectiva periódica de interés ($i_m$) %", value=1.0, step=0.1, key="vf_geo_im_eff") / 100
                    qm_geo = st.number_input("Tasa efectiva periódica de crecimiento ($q_m$) %", value=0.5, step=0.1, key="vf_geo_qm_eff") / 100
                    n_geo = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vf_geo_n_eff")
                    m_geo = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vf_geo_m_eff")
                    
                    nm_geo = n_geo * m_geo
                    vf_res_geo = engine.vf_gradiente_geo(R1_vf, im_geo, qm_geo, nm_geo)
                    str_i = rf"{im_geo:.4f}"
                    str_q = rf"{qm_geo:.4f}"
                    
                    if im_geo != qm_geo:
                        formula_geo_vf = r"VF = R_1 \left[ \frac{(1+i_m)^{nm} - (1+q_m)^{nm}}{i_m - q_m} \right]"
                    else:
                        formula_geo_vf = r"VF = nm \cdot R_1 (1+i_m)^{nm-1}"
                        
                else: # Tasa nominal anual
                    i_nom_geo = st.number_input("Tasa nominal anual de interés ($i^{(m)}$) %", value=12.0, step=0.1, key="vf_geo_i_nom") / 100
                    q_nom_geo = st.number_input("Tasa nominal anual de crecimiento ($q^{(m)}$) %", value=5.0, step=0.1, key="vf_geo_q_nom") / 100
                    n_geo = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vf_geo_n_nom")
                    m_geo = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vf_geo_m_nom")
                    
                    im_geo = i_nom_geo / m_geo
                    qm_geo = q_nom_geo / m_geo
                    nm_geo = n_geo * m_geo
                    str_i = rf"{im_geo:.6f}"
                    str_q = rf"{qm_geo:.6f}"
                    
                    vf_res_geo = engine.vf_gradiente_geo(R1_vf, im_geo, qm_geo, nm_geo)
                    
                    if im_geo != qm_geo:
                        formula_geo_vf = r"VF = R_1 \left[ \frac{\left(1+\frac{i^{(m)}}{m}\right)^{nm} - \left(1+\frac{q^{(m)}}{m}\right)^{nm}}{\frac{i^{(m)}}{m} - \frac{q^{(m)}}{m}} \right]"
                    else:
                        formula_geo_vf = r"VF = nm \cdot R_1 \left(1+\frac{i^{(m)}}{m}\right)^{nm-1}"
                
            with c2:
                st.metric("Valor Futuro Acumulado ($VF$)", f"${vf_res_geo:,.2f}")
                st.latex(formula_geo_vf)

            st.write("---")
            with st.expander("Ver desarrollo paso a paso del cálculo actual"):
                st.info("**Sustitución y Desarrollo:**")
                if im_geo != qm_geo:
                    st.latex(rf"VF = {R1_vf:,.2f} \left[ \frac{{(1+{str_i})^{{{nm_geo:g}}} - (1+{str_q})^{{{nm_geo:g}}}}}{{{str_i} - {str_q}}} \right]")
                    num1 = (1 + im_geo)**nm_geo
                    num2 = (1 + qm_geo)**nm_geo
                    den = im_geo - qm_geo
                    st.latex(rf"VF = {R1_vf:,.2f} \left[ \frac{{{num1:.6f} - {num2:.6f}}}{{{den:.6f}}} \right]")
                    st.latex(rf"VF = {R1_vf:,.2f} \left[ \frac{{{num1-num2:.6f}}}{{{den:.6f}}} \right] = {R1_vf:,.2f} \times {((num1-num2)/den):.6f}")
                else:
                    st.latex(rf"VF = {nm_geo:g} \times {R1_vf:,.2f} \times (1 + {str_i})^{{{nm_geo:g}-1}}")
                    st.latex(rf"VF = {nm_geo * R1_vf:,.2f} \times {(1 + im_geo)**(nm_geo - 1):.6f}")
                st.success(f"**Resultado Final: ${vf_res_geo:,.2f}**")

        # -----------------------------------------------------
        # CRECIENTES ARITMÉTICAS (VF)
        # -----------------------------------------------------
        elif tipo_renta_vf == "Rentas Crecientes Aritméticas":
            st.markdown("#### Rentas aritméticas (el pago suma/resta una cantidad fija $G$)")
            
            tipo_tasa_vf = st.radio("Ingresar tasa de interés como:", ["Tasa efectiva periódica", "Tasa nominal anual"], horizontal=True, key="tasa_arit_vf")
            st.write("---")
            
            c1, c2 = st.columns(2)
            
            with c1:
                R1_arit_vf = st.number_input("Primer Pago ($R_1$)", min_value=0.0, value=1000.0, step=100.0, key="vf_arit_r1")
                G_vf = st.number_input("Gradiente Aritmético ($G$)", value=100.0, step=50.0, help="Cantidad fija que se suma o resta a cada pago", key="vf_arit_g")
                
                if tipo_tasa_vf == "Tasa efectiva periódica":
                    im_arit_vf = st.number_input("Tasa efectiva periódica ($i_m$) %", value=1.0, step=0.1, key="vf_arit_ieff") / 100
                    n_arit_vf = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vf_arit_n_eff")
                    m_arit_vf = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vf_arit_m_eff")
                    str_i_arit_vf = r"i_m" 
                    str_val_i = rf"{im_arit_vf:.4f}"
                else:
                    i_nom_arit_vf = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=12.0, step=0.1, key="vf_arit_inom") / 100
                    n_arit_vf = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vf_arit_n_nom")
                    m_arit_vf = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vf_arit_m_nom")
                    im_arit_vf = i_nom_arit_vf / m_arit_vf
                    str_i_arit_vf = r"\frac{i^{(m)}}{m}" 
                    str_val_i = rf"{im_arit_vf:.6f}"
                    
                nm_arit_vf = n_arit_vf * m_arit_vf
                
            with c2:
                vf_res_arit = engine.vf_gradiente_aritmetico(R1_arit_vf, G_vf, im_arit_vf, nm_arit_vf)
                st.metric("Valor Futuro Acumulado ($VF$)", f"${vf_res_arit:,.2f}")
                
                formula_arit_vf = r"VF = R_1 \left[ \frac{(1+" + str_i_arit_vf + r")^{nm} - 1}{" + str_i_arit_vf + r"} \right] + \frac{G}{" + str_i_arit_vf + r"} \left[ \frac{(1+" + str_i_arit_vf + r")^{nm} - 1}{" + str_i_arit_vf + r"} - nm \right]"
                st.latex(formula_arit_vf)

            st.write("---")
            with st.expander("Ver desarrollo paso a paso del cálculo actual"):
                st.info("**Sustitución y Desarrollo:**")
                st.latex(rf"VF = {R1_arit_vf:,.2f} \left[ \frac{{(1+{str_val_i})^{{{nm_arit_vf:g}}} - 1}}{{{str_val_i}}} \right] + \frac{{{G_vf:,.2f}}}{{{str_val_i}}} \left[ \frac{{(1+{str_val_i})^{{{nm_arit_vf:g}}} - 1}}{{{str_val_i}}} - {nm_arit_vf:g} \right]")
                
                factor_s = ((1 + im_arit_vf)**nm_arit_vf - 1) / im_arit_vf
                termino_R = R1_arit_vf * factor_s
                termino_G = (G_vf / im_arit_vf) * (factor_s - nm_arit_vf)
                
                st.latex(rf"VF = {R1_arit_vf:,.2f} \times [{factor_s:.6f}] + {G_vf/im_arit_vf:,.2f} \times [{factor_s:.6f} - {nm_arit_vf:g}]")
                st.latex(rf"VF = {termino_R:,.2f} + {termino_G:,.2f}")
                st.success(f"**Resultado Final: ${vf_res_arit:,.2f}**")

    # =========================================================
    # TAB 2: VALOR PRESENTE
    # =========================================================
    with tab_vp:
        tipo_renta_vp = st.radio("Tipo de Renta (Valor Presente):", [
            "Rentas Constantes Periódicas",
            "Rentas Crecientes Geométricas", 
            "Rentas Crecientes Aritméticas"
        ], horizontal=True, key="radio_tipo_vp")
        
        st.write("---")
        
        # -----------------------------------------------------
        # CONSTANTES PERIÓDICAS (VP)
        # -----------------------------------------------------
        if tipo_renta_vp == "Rentas Constantes Periódicas":
            
            escenario_const_vp = st.selectbox("Seleccione el escenario:", [
                "Vencidas a una tasa efectiva im",
                "Anticipadas a una tasa efectiva im",
                "Perpetuas a una tasa efectiva im",
                "Vencidas pagaderas p veces al año a tasa nominal i(m)",
                "Continuas a una tasa instantánea δ o efectiva i"
            ], key="sel_const_vp")
            
            c1, c2 = st.columns(2)
            
            with c1:
                if escenario_const_vp == "Vencidas a una tasa efectiva im":
                    R_vp = st.number_input("Pago periódico ($R$)", min_value=0.0, value=1000.0, step=100.0, key="vp_rc_1")
                    i_nom_vp = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=12.0, step=0.1, key="vp_rc_i1") / 100
                    n_vp = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vp_rc_n1")
                    m_vp = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vp_rc_m1")
                    
                    im_vp = i_nom_vp / m_vp
                    vp_res = engine.vp_anualidad_efectiva(R_vp, im_vp, n_vp * m_vp, anticipada=False)
                    formula_latex = r"VP = R \left[ \frac{1 - \left(1+\frac{i^{(m)}}{m}\right)^{-nm}}{\frac{i^{(m)}}{m}} \right]"
                
                elif escenario_const_vp == "Anticipadas a una tasa efectiva im":
                    R_vp = st.number_input("Pago periódico ($R$)", min_value=0.0, value=1000.0, step=100.0, key="vp_rc_2")
                    i_nom_vp = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=12.0, step=0.1, key="vp_rc_i2") / 100
                    n_vp = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vp_rc_n2")
                    m_vp = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vp_rc_m2")
                    
                    im_vp = i_nom_vp / m_vp
                    vp_res = engine.vp_anualidad_efectiva(R_vp, im_vp, n_vp * m_vp, anticipada=True)
                    formula_latex = r"VP = R \left[ \frac{1 - \left(1+\frac{i^{(m)}}{m}\right)^{-nm}}{\frac{i^{(m)}}{m}} \right] \left(1+\frac{i^{(m)}}{m}\right)"
                
                elif escenario_const_vp == "Perpetuas a una tasa efectiva im":
                    R_vp = st.number_input("Pago periódico ($R$)", min_value=0.0, value=1000.0, step=100.0, key="vp_rc_perp")
                    i_nom_vp = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=12.0, step=0.1, key="vp_rc_i_perp") / 100
                    m_vp = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vp_rc_m_perp")
                    
                    im_vp = i_nom_vp / m_vp
                    vp_res = engine.vp_perpetuidad(R_vp, im_vp)
                    formula_latex = r"VP = \frac{R}{\frac{i^{(m)}}{m}}"

                elif escenario_const_vp == "Vencidas pagaderas p veces al año a tasa nominal i(m)":
                    R_vp = st.number_input("Pago periódico ($R$)", min_value=0.0, value=1000.0, step=100.0, key="vp_rc_3")
                    i_nom_vp = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=12.0, step=0.1, key="vp_rc_inom") / 100
                    m_vp = st.number_input("Capitalizaciones por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vp_rc_m3")
                    p_vp = st.number_input("Pagos por año ($p$)", min_value=1.0, value=4.0, step=1.0, key="vp_rc_p")
                    n_vp = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vp_rc_n3")
                    
                    vp_res = engine.vp_anualidad_nominal(R_vp, i_nom_vp, m_vp, p_vp, n_vp)
                    formula_latex = r"VP = R \left[ \frac{1 - \left(1+\frac{i^{(p)}}{p}\right)^{-np}}{\frac{i^{(p)}}{p}} \right]"
                
                elif escenario_const_vp == "Continuas a una tasa instantánea δ o efectiva i": 
                    R_anual_vp = st.number_input(r"Flujo Anual Total ($\bar{R}$)", min_value=0.0, value=12000.0, step=1000.0, key="vp_rc_4")
                    
                    tipo_tasa_continua_vp = st.radio("Ingresar tasa como:", ["Tasa instantánea ($\delta$)", "Tasa efectiva anual ($i$)"], horizontal=True, key="tipo_t_cont_vp")
                    n_vp = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vp_rc_n4")
                    
                    if tipo_tasa_continua_vp == "Tasa instantánea ($\delta$)":
                        d_vp = st.number_input(r"Tasa instantánea ($\delta$) %", value=10.0, step=0.1, key="vp_rc_d") / 100
                        vp_res = engine.vp_anualidad_continua(R_anual_vp, d_vp, n_vp)
                        formula_latex = r"VP = \bar{R} \left[ \frac{1 - e^{-\delta n}}{\delta} \right]"
                    else:
                        i_eff_vp = st.number_input("Tasa efectiva anual ($i$) %", value=10.51, step=0.1, key="vp_rc_ieff") / 100
                        d_vp = np.log(1 + i_eff_vp) 
                        vp_res = engine.vp_anualidad_continua(R_anual_vp, d_vp, n_vp)
                        formula_latex = r"VP = \bar{R} \left[ \frac{1 - (1+i)^{-n}}{\ln(1+i)} \right]"
                    
            with c2:
                st.metric("Valor Presente ($VP$)", f"${vp_res:,.2f}")
                st.latex(formula_latex)

            st.write("---")
            with st.expander("Ver desarrollo paso a paso del cálculo actual"):
                st.info("**Sustitución y Desarrollo (Descuento):**")
                if escenario_const_vp == "Vencidas a una tasa efectiva im":
                    st.latex(rf"VP = {R_vp:,.2f} \left[ \frac{{1 - \left(1 + \frac{{{i_nom_vp:.4f}}}{{{m_vp:g}}}\right)^{{-{n_vp*m_vp:g}}}}}{{\frac{{{i_nom_vp:.4f}}}{{{m_vp:g}}}}} \right]")
                    st.latex(rf"VP = {R_vp:,.2f} \left[ \frac{{1 - (1 + {im_vp:.6f})^{{-{n_vp*m_vp:g}}}}}{{{im_vp:.6f}}} \right]")
                    factor = (1 - (1 + im_vp)**(-n_vp * m_vp)) / im_vp
                    st.latex(rf"VP = {R_vp:,.2f} \times [{factor:.6f}] = {vp_res:,.2f}")
                elif escenario_const_vp == "Anticipadas a una tasa efectiva im":
                    st.latex(rf"VP = {R_vp:,.2f} \left[ \frac{{1 - (1 + {im_vp:.6f})^{{-{n_vp*m_vp:g}}}}}{{{im_vp:.6f}}} \right] (1 + {im_vp:.6f})")
                    factor = (1 - (1 + im_vp)**(-n_vp * m_vp)) / im_vp
                    st.latex(rf"VP = {R_vp:,.2f} \times [{factor:.6f}] \times {(1 + im_vp):.6f} = {vp_res:,.2f}")
                elif escenario_const_vp == "Perpetuas a una tasa efectiva im":
                    st.latex(rf"VP = \frac{{{R_vp:,.2f}}}{{{im_vp:.6f}}} = {vp_res:,.2f}")
                elif escenario_const_vp == "Vencidas pagaderas p veces al año a tasa nominal i(m)":
                    i_p = engine.tasa_nominal_m_a_nominal_p(i_nom_vp, m_vp, p_vp)
                    ip_p = i_p / p_vp
                    st.latex(rf"\text{{1. Tasa equivalente: }} i^{{({p_vp:g})}} = {i_p:.6f} \implies \frac{{i^{{({p_vp:g})}}}}{{{p_vp:g}}} = {ip_p:.6f}")
                    st.latex(rf"\text{{2. Sustitución: }} VP = {R_vp:,.2f} \left[ \frac{{1 - (1 + {ip_p:.6f})^{{-{n_vp*p_vp:g}}}}}{{{ip_p:.6f}}} \right]")
                    factor = (1 - (1 + ip_p)**(-n_vp * p_vp)) / ip_p
                    st.latex(rf"VP = {R_vp:,.2f} \times [{factor:.6f}] = {vp_res:,.2f}")
                elif escenario_const_vp == "Continuas a una tasa instantánea δ o efectiva i":
                    if tipo_tasa_continua_vp == "Tasa instantánea ($\delta$)":
                        st.latex(rf"VP = {R_anual_vp:,.2f} \left[ \frac{{1 - e^{{-({d_vp:.4f} \times {n_vp:g})}}}}{{{d_vp:.4f}}} \right]")
                        factor = (1 - np.exp(-d_vp * n_vp)) / d_vp
                        st.latex(rf"VP = {R_anual_vp:,.2f} \times [{factor:.6f}] = {vp_res:,.2f}")
                    else:
                        st.latex(rf"\text{{1. Tasa Continua: }} \delta = \ln(1 + {i_eff_vp:.4f}) = {d_vp:.6f}")
                        st.latex(rf"\text{{2. Sustitución: }} VP = {R_anual_vp:,.2f} \left[ \frac{{1 - (1 + {i_eff_vp:.4f})^{{-{n_vp:g}}}}}{{\ln(1 + {i_eff_vp:.4f})}} \right]")
                        factor = (1 - (1 + i_eff_vp)**-n_vp) / d_vp
                        st.latex(rf"VP = {R_anual_vp:,.2f} \times [{factor:.6f}] = {vp_res:,.2f}")
                st.success(f"**Resultado Final: ${vp_res:,.2f}**")
                
        # -----------------------------------------------------
        # CRECIENTES GEOMÉTRICAS (VP)
        # -----------------------------------------------------
        elif tipo_renta_vp == "Rentas Crecientes Geométricas":
            st.markdown("#### Rentas geométricas (el pago crece a una tasa $q$)")
            
            tipo_tasa_geo_vp = st.radio("Ingresar tasas como:", ["Tasa efectiva periódica", "Tasa nominal anual"], horizontal=True, key="tipo_t_geo_vp")
            st.write("---")
            
            c1, c2 = st.columns(2)
            
            with c1:
                R1_vp = st.number_input("Monto del Primer Pago ($R_1$)", min_value=0.0, value=1000.0, step=100.0, key="vp_geo_r1")
                
                if tipo_tasa_geo_vp == "Tasa efectiva periódica":
                    im_geo_vp = st.number_input("Tasa efectiva periódica de interés ($i_m$) %", value=1.0, step=0.1, key="vp_geo_im_eff") / 100
                    qm_geo_vp = st.number_input("Tasa efectiva periódica de crecimiento ($q_m$) %", value=0.5, step=0.1, key="vp_geo_qm_eff") / 100
                    n_geo_vp = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vp_geo_n_eff")
                    m_geo_vp = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vp_geo_m_eff")
                    
                    nm_geo_vp = n_geo_vp * m_geo_vp
                    vp_res_geo = engine.vp_gradiente_geo(R1_vp, im_geo_vp, qm_geo_vp, nm_geo_vp)
                    str_i = rf"{im_geo_vp:.4f}"
                    str_q = rf"{qm_geo_vp:.4f}"
                    
                    if im_geo_vp != qm_geo_vp:
                        formula_geo_vp = r"VP = R_1 \left[ \frac{1 - \left( \frac{1+q_m}{1+i_m} \right)^{nm}}{i_m - q_m} \right]"
                    else:
                        formula_geo_vp = r"VP = \frac{nm \cdot R_1}{1+i_m}"

                else: 
                    i_nom_geo_vp = st.number_input("Tasa nominal anual de interés ($i^{(m)}$) %", value=12.0, step=0.1, key="vp_geo_i_nom") / 100
                    q_nom_geo_vp = st.number_input("Tasa nominal anual de crecimiento ($q^{(m)}$) %", value=5.0, step=0.1, key="vp_geo_q_nom") / 100
                    n_geo_vp = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vp_geo_n_nom")
                    m_geo_vp = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vp_geo_m_nom")
                    
                    im_geo_vp = i_nom_geo_vp / m_geo_vp
                    qm_geo_vp = q_nom_geo_vp / m_geo_vp
                    nm_geo_vp = n_geo_vp * m_geo_vp
                    str_i = rf"{im_geo_vp:.6f}"
                    str_q = rf"{qm_geo_vp:.6f}"
                    
                    vp_res_geo = engine.vp_gradiente_geo(R1_vp, im_geo_vp, qm_geo_vp, nm_geo_vp)
                    
                    if im_geo_vp != qm_geo_vp:
                        formula_geo_vp = r"VP = R_1 \left[ \frac{1 - \left( \frac{1+\frac{q^{(m)}}{m}}{1+\frac{i^{(m)}}{m}} \right)^{nm}}{\frac{i^{(m)}}{m} - \frac{q^{(m)}}{m}} \right]"
                    else:
                        formula_geo_vp = r"VP = \frac{nm \cdot R_1}{1+\frac{i^{(m)}}{m}}"
                
            with c2:
                st.metric("Valor Presente ($VP$)", f"${vp_res_geo:,.2f}")
                st.latex(formula_geo_vp)

            st.write("---")
            with st.expander("Ver desarrollo paso a paso del cálculo actual"):
                st.info("**Sustitución y Desarrollo (Descuento):**")
                if im_geo_vp != qm_geo_vp:
                    st.latex(rf"VP = {R1_vp:,.2f} \left[ \frac{{1 - \left( \frac{{1+{str_q}}}{{1+{str_i}}} \right)^{{{nm_geo_vp:g}}}}}{{{str_i} - {str_q}}} \right]")
                    frac = (1 + qm_geo_vp) / (1 + im_geo_vp)
                    den = im_geo_vp - qm_geo_vp
                    st.latex(rf"VP = {R1_vp:,.2f} \left[ \frac{{1 - ({frac:.6f})^{{{nm_geo_vp:g}}}}}{{{den:.6f}}} \right]")
                    st.latex(rf"VP = {R1_vp:,.2f} \left[ \frac{{1 - {frac**nm_geo_vp:.6f}}}{{{den:.6f}}} \right] = {R1_vp:,.2f} \times {((1 - frac**nm_geo_vp)/den):.6f}")
                else:
                    st.latex(rf"VP = \frac{{{nm_geo_vp:g} \times {R1_vp:,.2f}}}{{1 + {str_i}}}")
                    st.latex(rf"VP = \frac{{{nm_geo_vp * R1_vp:,.2f}}}{{1 + {im_geo_vp:.6f}}}")
                st.success(f"**Resultado Final: ${vp_res_geo:,.2f}**")

        # -----------------------------------------------------
        # CRECIENTES ARITMÉTICAS (VP)
        # -----------------------------------------------------
        elif tipo_renta_vp == "Rentas Crecientes Aritméticas":
            st.markdown("#### Rentas aritméticas (el pago suma/resta una cantidad fija $G$)")
            
            tipo_tasa_vp = st.radio("Ingresar tasa de interés como:", ["Tasa efectiva periódica", "Tasa nominal anual"], horizontal=True, key="tasa_arit_vp")
            st.write("---")
            
            c1, c2 = st.columns(2)
            
            with c1:
                R1_arit_vp = st.number_input("Primer Pago ($R_1$)", min_value=0.0, value=1000.0, step=100.0, key="vp_arit_r1")
                G_vp = st.number_input("Gradiente Aritmético ($G$)", value=100.0, step=50.0, key="vp_arit_g")
                
                if tipo_tasa_vp == "Tasa efectiva periódica":
                    im_arit_vp = st.number_input("Tasa efectiva periódica ($i_m$) %", value=1.0, step=0.1, key="vp_arit_ieff") / 100
                    n_arit_vp = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vp_arit_n_eff")
                    m_arit_vp = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vp_arit_m_eff")
                    str_i_arit_vp = r"i_m" 
                    str_val_i = rf"{im_arit_vp:.4f}"
                else:
                    i_nom_arit_vp = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=12.0, step=0.1, key="vp_arit_inom") / 100
                    n_arit_vp = st.number_input("Años ($n$)", min_value=0.0, value=5.0, step=1.0, key="vp_arit_n_nom")
                    m_arit_vp = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="vp_arit_m_nom")
                    im_arit_vp = i_nom_arit_vp / m_arit_vp
                    str_i_arit_vp = r"\frac{i^{(m)}}{m}" 
                    str_val_i = rf"{im_arit_vp:.6f}"
                    
                nm_arit_vp = n_arit_vp * m_arit_vp
                
            with c2:
                vp_res_arit = engine.vp_gradiente_aritmetico(R1_arit_vp, G_vp, im_arit_vp, nm_arit_vp)
                st.metric("Valor Presente ($VP$)", f"${vp_res_arit:,.2f}")
                
                formula_arit_vp = r"VP = R_1 \left[ \frac{1 - (1+" + str_i_arit_vp + r")^{-nm}}{" + str_i_arit_vp + r"} \right] + \frac{G}{" + str_i_arit_vp + r"} \left[ \frac{1 - (1+" + str_i_arit_vp + r")^{-nm}}{" + str_i_arit_vp + r"} - nm(1+" + str_i_arit_vp + r")^{-nm} \right]"
                st.latex(formula_arit_vp)

            st.write("---")
            with st.expander("Ver desarrollo paso a paso del cálculo actual"):
                st.info("**Sustitución y Desarrollo (Descuento):**")
                st.latex(rf"VP = {R1_arit_vp:,.2f} \left[ \frac{{1 - (1+{str_val_i})^{{-{nm_arit_vp:g}}}}}{{{str_val_i}}} \right] + \frac{{{G_vp:,.2f}}}{{{str_val_i}}} \left[ \frac{{1 - (1+{str_val_i})^{{-{nm_arit_vp:g}}}}}{{{str_val_i}}} - {nm_arit_vp:g}(1+{str_val_i})^{{-{nm_arit_vp:g}}} \right]")
                
                factor_a = (1 - (1 + im_arit_vp)**-nm_arit_vp) / im_arit_vp
                desc_nm = nm_arit_vp * (1 + im_arit_vp)**-nm_arit_vp
                termino_R = R1_arit_vp * factor_a
                termino_G = (G_vp / im_arit_vp) * (factor_a - desc_nm)
                
                st.latex(rf"VP = {R1_arit_vp:,.2f} \times [{factor_a:.6f}] + {G_vp/im_arit_vp:,.2f} \times [{factor_a:.6f} - {desc_nm:.6f}]")
                st.latex(rf"VP = {termino_R:,.2f} + {termino_G:,.2f}")
                st.success(f"**Resultado Final: ${vp_res_arit:,.2f}**")

    # =========================================================
    # TAB 3: NÚMERO DE PERIODOS (n)
    # =========================================================
    with tab_n:
        st.markdown("### Determinación del número de periodos ($n$) en Rentas")
        
        c1, c2 = st.columns([1, 1])
        with c1:
            base_n = st.selectbox("Calcular n basado en:", ["Valor Futuro (Monto Acumulado)", "Valor Presente (Capital Inicial)"], key="sel_base_n")
        with c2:
            tipo_renta_n = st.selectbox("Tipo de Renta:", ["Constante Periódica", "Creciente Geométrica", "Creciente Aritmética"], key="sel_tipo_n")
            
        st.write("---")
        
        tipo_tasa_n = st.radio("Ingresar tasas como:", ["Tasa efectiva periódica", "Tasa nominal anual"], horizontal=True, key="tipo_tasa_n")
        st.write("---")
        
        c3, c4 = st.columns(2)
        
        with c3:
            if base_n == "Valor Futuro (Monto Acumulado)":
                Meta = st.number_input("Valor Futuro Objetivo ($VF$)", min_value=0.01, value=50000.0, step=1000.0, key="n_meta_vf")
            else:
                Meta = st.number_input("Valor Presente ($VP$)", min_value=0.01, value=25000.0, step=1000.0, key="n_meta_vp")
                
            R_n = st.number_input("Primer pago ($R_1$)", min_value=0.01, value=1000.0, step=100.0, key="n_pago")
            
            if tipo_tasa_n == "Tasa efectiva periódica":
                im_n = st.number_input("Tasa efectiva periódica de interés ($i_m$) %", value=1.0, step=0.1, key="n_im_eff") / 100
                m_n = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, help="Necesario para convertir el total de periodos a años exactos", key="n_m_eff")
                str_i_n = rf"{im_n:.4f}"
                
                if tipo_renta_n == "Creciente Geométrica":
                    qm_n = st.number_input("Tasa efectiva periódica de crecimiento ($q_m$) %", value=0.5, step=0.1, key="n_qm_eff") / 100
                    
            else:
                i_nom_n = st.number_input("Tasa nominal anual de interés ($i^{(m)}$) %", value=12.0, step=0.1, key="n_inom") / 100
                m_n = st.number_input("Periodos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="n_m_nom")
                im_n = i_nom_n / m_n
                str_i_n = rf"{im_n:.6f}"
                
                if tipo_renta_n == "Creciente Geométrica":
                    q_nom_n = st.number_input("Tasa nominal anual de crecimiento ($q^{(m)}$) %", value=5.0, step=0.1, key="n_qnom") / 100
                    qm_n = q_nom_n / m_n

            if tipo_renta_n == "Creciente Aritmética":
                G_n = st.number_input("Gradiente Aritmético ($G$)", value=50.0, step=10.0, help="Suma o resta fija por periodo", key="n_g")
            
        with c4:
            st.markdown("#### Resultados")
            
            n_res_total = np.nan
            usa_metodo_numerico = False
            
            if tipo_renta_n == "Constante Periódica":
                if base_n == "Valor Futuro (Monto Acumulado)":
                    n_res_total = engine.nper_anualidad_vf(Meta, R_n, im_n)
                    formula_latex = r"nm = \frac{\ln\left(\frac{VF \cdot i_m}{R} + 1\right)}{\ln(1+i_m)}"
                else:
                    n_res_total = engine.nper_anualidad_vp(Meta, R_n, im_n)
                    formula_latex = r"nm = \frac{-\ln\left(1 - \frac{VP \cdot i_m}{R}\right)}{\ln(1+i_m)}"
                    
            elif tipo_renta_n == "Creciente Geométrica":
                usa_metodo_numerico = True
                if base_n == "Valor Futuro (Monto Acumulado)":
                    n_res_total = engine.nper_gradiente_geo_vf(Meta, R_n, im_n, qm_n)
                    formula_latex = r"VF = R_1 \left[ \frac{(1+i_m)^{nm} - (1+q_m)^{nm}}{i_m - q_m} \right]"
                else:
                    n_res_total = engine.nper_gradiente_geo_vp(Meta, R_n, im_n, qm_n)
                    formula_latex = r"VP = R_1 \left[ \frac{1 - \left( \frac{1+q_m}{1+i_m} \right)^{nm}}{i_m - q_m} \right]"
                    
            elif tipo_renta_n == "Creciente Aritmética":
                usa_metodo_numerico = True
                if base_n == "Valor Futuro (Monto Acumulado)":
                    n_res_total = engine.nper_gradiente_arit_vf(Meta, R_n, G_n, im_n)
                    formula_latex = r"VF = R_1 \left[ \frac{(1+i_m)^{nm} - 1}{i_m} \right] + \frac{G}{i_m} \left[ \dots \right]"
                else:
                    n_res_total = engine.nper_gradiente_arit_vp(Meta, R_n, G_n, im_n)
                    formula_latex = r"VP = R_1 \left[ \frac{1 - (1+i_m)^{-nm}}{i_m} \right] + \frac{G}{i_m} \left[ \dots \right]"
                    
            if np.isnan(n_res_total):
                st.error("El monto objetivo es inalcanzable con estos parámetros.")
            else:
                st.metric("Total de Periodos ($nm$)", f"{n_res_total:.4f}")
                
                anios_decimal = n_res_total / m_n
                st.metric("Años totales ($n$)", f"{anios_decimal:.4f} años")
                st.latex(formula_latex)
                
                st.write("---")
                with st.expander("Ver desarrollo paso a paso del cálculo actual"):
                    if not usa_metodo_numerico:
                        st.info("**Propiedades de los Logaritmos (Despeje Analítico):**")
                        if base_n == "Valor Futuro (Monto Acumulado)":
                            st.latex(rf"nm = \frac{{\ln\left(\frac{{{Meta:,.2f} \times {str_i_n}}}{{{R_n:,.2f}}} + 1\right)}}{{\ln(1+{str_i_n})}}")
                            num_val = (Meta * im_n / R_n) + 1
                            st.latex(rf"nm = \frac{{\ln({num_val:.6f})}}{{\ln({1+im_n:.6f})}} = \frac{{{np.log(num_val):.6f}}}{{{np.log(1+im_n):.6f}}}")
                        else:
                            st.latex(rf"nm = \frac{{-\ln\left(1 - \frac{{{Meta:,.2f} \times {str_i_n}}}{{{R_n:,.2f}}}\right)}}{{\ln(1+{str_i_n})}}")
                            num_val = 1 - (Meta * im_n / R_n)
                            st.latex(rf"nm = \frac{{-\ln({num_val:.6f})}}{{\ln({1+im_n:.6f})}} = \frac{{-{np.log(num_val):.6f}}}{{{np.log(1+im_n):.6f}}}")
                        st.success(f"**Resultado Exacto: {n_res_total:.4f} periodos.**")
                    else:
                        st.warning("**Aviso: Cálculo mediante Métodos Numéricos (Iteración)**")
                        st.info("""
                        Al trabajar con rentas que crecen aritmética o geométricamente, la variable del tiempo ($nm$) se encuentra atrapada tanto en el exponente como multiplicando otras expresiones dentro del corchete.
                        
                        **No existe un método algebraico directo (despeje) para aislar $nm$.**
                        
                        Por lo tanto, la computadora encuentra la solución evaluando la función repetidas veces mediante métodos de búsqueda de raíces (como el método de Newton-Raphson o bisección de SciPy) hasta que el Valor de la Renta iguala a tu Monto Objetivo.
                        """)
                        st.latex(r"f(nm) = \text{Valor de la Renta}(nm) - \text{Monto Objetivo} = 0")
                        st.success(rf"**Raíz encontrada por la computadora:** $nm \approx {n_res_total:.4f}$")

                st.write("---")
                st.markdown("**Desglose exacto:**")
                df_desglose_n = engine.desglosar_periodos(anios_decimal)
                st.dataframe(
                    df_desglose_n.style.set_properties(**{
                        'background-color': '#F3F4F6', 'color': '#1E3A8A',
                        'font-weight': 'bold', 'text-align': 'center'
                    }), 
                    use_container_width=True, hide_index=True
                )
# =============================================================================
# 4. AMORTIZACIÓN
# =============================================================================
elif opcion == "4. Tabla de Amortización":
    st.markdown('<div class="section-header">4. Tabla de Amortización (Pagos Fijos)</div>', unsafe_allow_html=True)
    
    st.markdown("Genera la tabla de amortización calculando el pago fijo o el monto del préstamo inicial.")
    
    # Selectores principales
    modo_amort = st.radio("¿Qué deseas calcular?", [
        "Calcular Pago Fijo (R) conociendo el Préstamo (VP)",
        "Calcular Préstamo (VP) conociendo el Pago Fijo (R)"
    ], horizontal=True, key="modo_am")
    
    tipo_tasa_amort = st.radio("Ingresar tasa de interés como:", [
        "Tasa efectiva periódica", 
        "Tasa nominal anual"
    ], horizontal=True, key="tipo_tasa_am")
    
    st.write("---")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
            if modo_amort == "Calcular Pago Fijo (R) conociendo el Préstamo (VP)":
                vp_bruto = st.number_input("Valor Total del Bien ($VP_{bruto}$)", min_value=0.01, value=500000.0, step=10000.0, key="am_vp_bruto")
                
                tipo_enganche = st.radio("Tipo de Enganche:", ["Monto fijo ($)", "Porcentaje (%)"], horizontal=True, key="tipo_eng")
                
                if tipo_enganche == "Monto fijo ($)":
                    enganche = st.number_input("Enganche (Pago Inicial $)", min_value=0.0, value=50000.0, step=5000.0, key="am_enganche_monto")
                else:
                    pct_enganche = st.number_input("Enganche (%)", min_value=0.0, max_value=99.9, value=10.0, step=1.0, key="am_enganche_pct")
                    enganche = vp_bruto * (pct_enganche / 100)
                
                vp_am = vp_bruto - enganche
                
                if vp_am <= 0:
                    st.error("El enganche debe ser menor al valor total.")
                    vp_am = 0.01 
                else:
                    st.success(f"Monto a financiar ($VP$ neto): **${vp_am:,.2f}**")
                    
            else:
                R_am = st.number_input("Pago periódico constante ($R$)", min_value=0.01, value=15000.0, step=1000.0, key="am_r")
            
    with c2:
        if tipo_tasa_amort == "Tasa efectiva periódica":
            tasa_input = st.number_input("Tasa efectiva periódica ($i_m$) %", value=1.5, step=0.1, key="am_ieff") / 100
        else:
            tasa_input = st.number_input("Tasa nominal anual ($i^{(m)}$) %", value=18.0, step=0.1, key="am_inom") / 100
            
    with c3:
        n_am = st.number_input("Años del préstamo ($n$)", min_value=0.1, value=5.0, step=1.0, key="am_n")
        m_am = st.number_input("Pagos por año ($m$)", min_value=1.0, value=12.0, step=1.0, key="am_m")

    nm_am = int(n_am * m_am)
    
    if tipo_tasa_amort == "Tasa efectiva periódica":
        tasa_periodo = tasa_input
        str_tasa = r"i_m"
        str_val_tasa = rf"{tasa_periodo:.4f}"
    else:
        tasa_periodo = tasa_input / m_am
        str_tasa = r"\frac{i^{(m)}}{m}"
        str_val_tasa = rf"\frac{{{tasa_input:.4f}}}{{{m_am:g}}}"

    # ==========================================
    # CÁLCULOS Y FÓRMULAS
    # ==========================================
    st.write("---")
    col_form, col_res = st.columns([2, 1])
    
    if modo_amort == "Calcular Pago Fijo (R) conociendo el Préstamo (VP)":
        st.markdown("### Cálculo del Pago Fijo ($R$)")
        
        if tasa_periodo > 0:
            pago_R = vp_am * (tasa_periodo / (1 - (1 + tasa_periodo)**(-nm_am)))
        else:
            pago_R = vp_am / nm_am
            
        formula_amort = r"R = VP \left[ \frac{" + str_tasa + r"}{1 - \left(1+" + str_tasa + r"\right)^{-nm}} \right]"
        vp_final = vp_am 
        
        with col_form:
            st.latex(formula_amort)
            with st.expander("Ver desarrollo paso a paso"):
                st.info("**Sustitución y Desarrollo:**")
                st.latex(rf"R = {vp_am:,.2f} \left[ \frac{{{str_val_tasa}}}{{1 - \left(1+{str_val_tasa}\right)^{{-{nm_am:g}}}}} \right]")
                st.latex(rf"R = {vp_am:,.2f} \left[ \frac{{{tasa_periodo:.6f}}}{{1 - (1 + {tasa_periodo:.6f})^{{-{nm_am:g}}}}} \right]")
                factor_amort = tasa_periodo / (1 - (1 + tasa_periodo)**(-nm_am))
                st.latex(rf"R = {vp_am:,.2f} \times [{factor_amort:.6f}]")
                st.success(f"**Resultado: $R = {pago_R:,.2f}**")
                
        with col_res:
            st.metric("Pago Periódico ($R$)", f"${pago_R:,.2f}")
            
    else:
        st.markdown("### Cálculo del Préstamo ($VP$)")
        
        if tasa_periodo > 0:
            vp_calc = R_am * ((1 - (1 + tasa_periodo)**(-nm_am)) / tasa_periodo)
        else:
            vp_calc = R_am * nm_am
            
        formula_amort = r"VP = R \left[ \frac{1 - \left(1+" + str_tasa + r"\right)^{-nm}}{" + str_tasa + r"} \right]"
        vp_final = vp_calc 
        
        with col_form:
            st.latex(formula_amort)
            with st.expander("Ver desarrollo paso a paso"):
                st.info("**Sustitución y Desarrollo:**")
                st.latex(rf"VP = {R_am:,.2f} \left[ \frac{{1 - \left(1+{str_val_tasa}\right)^{{-{nm_am:g}}}}}{{{str_val_tasa}}} \right]")
                st.latex(rf"VP = {R_am:,.2f} \left[ \frac{{1 - (1 + {tasa_periodo:.6f})^{{-{nm_am:g}}}}}{{{tasa_periodo:.6f}}} \right]")
                factor_vp = (1 - (1 + tasa_periodo)**(-nm_am)) / tasa_periodo
                st.latex(rf"VP = {R_am:,.2f} \times [{factor_vp:.6f}]")
                st.success(f"**Resultado: $VP = {vp_calc:,.2f}**")
                
        with col_res:
            st.metric("Monto del Préstamo ($VP$)", f"${vp_calc:,.2f}")

    # ==========================================
    # GENERAR TABLA Y GRÁFICA
    # ==========================================
    st.write("---")
    st.markdown("### Tabla y Gráfica de Amortización")
    
    df_amort = engine.tabla_amortizacion(vp_final, tasa_periodo, nm_am)
    
    tab_tabla, tab_grafica = st.tabs(["Tabla Detallada", "Gráfica de Composición"])
        
    with tab_tabla:
            st.dataframe(
                df_amort.style.format({
                    "Saldo Inicial": "${:,.2f}",
                    "Interés": "${:,.2f}",
                    "Amortización": "${:,.2f}",
                    "Saldo Insoluto": "${:,.2f}"
                }), 
                use_container_width=True,
                hide_index=True
            )
            
    with tab_grafica:
            import plotly.express as px
            fig = px.bar(df_amort, 
                        x="Periodo", 
                        y=["Amortización", "Interés"], 
                        title="Composición del Pago a lo largo del tiempo",
                        labels={"value": "Monto ($)", "variable": "Componente"},
                        color_discrete_map={"Amortización": "#4ECDC4", "Interés": "#FF6B6B"})
            st.plotly_chart(fig, use_container_width=True)
            
            st.write("---")
            with st.expander("¿Cómo interpretar esta gráfica?"):
                st.info("""
                **El comportamiento clásico de un crédito:**
                
                Aunque el pago mensual que haces al banco (la suma de las barras) siempre es el mismo, su composición cambia drásticamente con el tiempo:
                
                * **Al inicio del crédito:** La mayor parte de tu pago se va al cobro de intereses (la zona roja), porque el saldo insoluto es muy grande. Se amortiza (abona a capital) muy poco.
                * **Al final del crédito:** Como el saldo de la deuda ya es pequeño, los intereses bajan muchísimo, y la gran mayoría de tu cuota (la zona verde) se va directo a liquidar el capital restante.
                """)

# =============================================================================
# 5. VALUACIÓN DE BONOS
# =============================================================================
elif opcion == "5. Valuación de Bonos":
    st.markdown('<div class="section-header">5. Valuación de Bonos y Obligaciones</div>', unsafe_allow_html=True)
    
    st.markdown("Calcula el precio justo de un bono o determina su Tasa de Rendimiento al Vencimiento (YTM) con base en su precio de mercado.")
    
    modo_bono = st.radio("¿Qué deseas calcular?", [
        "Calcular Precio del Bono (P) conociendo su Tasa de Rendimiento",
        "Calcular Tasa de Rendimiento al Vencimiento (YTM) conociendo su Precio (P)"
    ], horizontal=True, key="modo_bono")
    
    st.write("---")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("**Características del Bono**")
        F_bono = st.number_input("Valor Nominal ($F$)", min_value=0.01, value=1000.0, step=100.0, key="bono_f")
        r_nom_bono = st.number_input("Tasa Cupón Nominal Anual ($r^{(m)}$) %", value=8.0, step=0.1, key="bono_r") / 100
        
        igual_nominal = st.checkbox("Valor de Redención ($C$) igual al Nominal", value=True, key="bono_check_c")
        if igual_nominal:
            C_bono = F_bono
        else:
            C_bono = st.number_input("Valor de Redención ($C$)", min_value=0.01, value=1000.0, step=100.0, key="bono_c")

    with c2:
        st.markdown("**Condiciones de Mercado**")
        
        if modo_bono == "Calcular Precio del Bono (P) conociendo su Tasa de Rendimiento":
            tipo_tasa_bono = st.radio("Ingresar Tasa de Rendimiento como:", ["Tasa efectiva periódica", "Tasa nominal anual"], key="tipo_tasa_b")
            
            if tipo_tasa_bono == "Tasa efectiva periódica":
                i_mercado = st.number_input("Tasa de Rend. Efectiva Periódica ($i_m$) %", value=5.0, step=0.1, key="bono_ieff") / 100
                str_i_bono = r"i_m"
            else:
                i_nom_mercado = st.number_input("Tasa de Rend. Nominal Anual ($i^{(m)}$) %", value=10.0, step=0.1, key="bono_inom") / 100
                str_i_bono = r"\frac{i^{(m)}}{m}"
                
        else:
            precio_mercado = st.number_input("Precio actual en el mercado ($P$)", min_value=0.01, value=950.0, step=10.0, key="bono_p_mercado")
            
    with c3:
        st.markdown("**Plazos**")
        n_anios_bono = st.number_input("Años al vencimiento ($n$)", min_value=0.1, value=5.0, step=1.0, key="bono_n")
        m_bono = st.number_input("Cupones por año ($m$)", min_value=1.0, value=2.0, step=1.0, help="Frecuencia de pago (ej. 2 para semestral)", key="bono_m")

    # ==========================================
    # CÁLCULOS GENERALES
    # ==========================================
    n_periodos_bono = int(n_anios_bono * m_bono)
    r_periodo = r_nom_bono / m_bono
    cupon_Fr = F_bono * r_periodo

    st.write("---")
    st.markdown("### Resultados de la Valuación")

    # ==========================================
    # CASO A: CALCULAR PRECIO
    # ==========================================
    if modo_bono == "Calcular Precio del Bono (P) conociendo su Tasa de Rendimiento":
        if tipo_tasa_bono == "Tasa efectiva periódica":
            i_periodo_bono = i_mercado
            str_val_i_mercado = rf"{i_mercado:.6f}"
        else:
            i_periodo_bono = i_nom_mercado / m_bono
            str_val_i_mercado = rf"{i_periodo_bono:.6f}"

        precio_P, _, vp_cup, vp_red = engine.precio_bono(F_bono, r_periodo, C_bono, i_periodo_bono, n_periodos_bono)

        if precio_P > C_bono:
            estado_bono = "Se vende con **PRIMA** (Sobre la par)"
            color = "green"
        elif precio_P < C_bono:
            estado_bono = "Se vende con **DESCUENTO** (Bajo la par)"
            color = "red"
        else:
            estado_bono = "Se vende **A LA PAR**"
            color = "blue"

        col_res1, col_res2 = st.columns([1, 1])
        with col_res1:
            st.metric("Precio del Bono ($P$)", f"${precio_P:,.2f}")
            st.markdown(f"<span style='color:{color}; font-weight:bold;'>{estado_bono}</span>", unsafe_allow_html=True)
            st.write(f"Monto de cada cupón ($Fr$): **${cupon_Fr:,.2f}**")
        with col_res2:
            formula_bono = r"P = Fr \cdot a_{\overline{nm}|i_m} + C(1+i_m)^{-nm}"
            st.latex(formula_bono)
            formula_desarrollada = r"P = Fr \left[ \frac{1 - \left(1+" + str_i_bono + r"\right)^{-nm}}{" + str_i_bono + r"} \right] + C(1+" + str_i_bono + r")^{-nm}"
            st.latex(formula_desarrollada)

        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**1. Cálculo del Cupón Periódico ($Fr$):**")
            st.latex(rf"Fr = {F_bono:,.2f} \times \left(\frac{{{r_nom_bono:.4f}}}{{{m_bono:g}}}\right) = {F_bono:,.2f} \times {r_periodo:.4f} = {cupon_Fr:,.2f}")
            
            st.info("**2. Sustitución en la Ecuación del Precio:**")
            st.latex(rf"P = {cupon_Fr:,.2f} \left[ \frac{{1 - (1+{str_val_i_mercado})^{{-{n_periodos_bono:g}}}}}{{{str_val_i_mercado}}} \right] + {C_bono:,.2f}(1+{str_val_i_mercado})^{{-{n_periodos_bono:g}}}")
            
            factor_anualidad = (1 - (1 + i_periodo_bono)**-n_periodos_bono) / i_periodo_bono
            factor_descuento = (1 + i_periodo_bono)**-n_periodos_bono
            
            st.latex(rf"P = {cupon_Fr:,.2f} [{factor_anualidad:.6f}] + {C_bono:,.2f} ({factor_descuento:.6f})")
            st.latex(rf"P = {vp_cup:,.2f} \text{{ (VP Cupones)}} + {vp_red:,.2f} \text{{ (VP Redención)}}")
            st.success(f"**Precio Final: ${precio_P:,.2f}**")

    # ==========================================
    # CASO B: CALCULAR YTM
    # ==========================================
    else:
        i_periodo_res = engine.tasa_rendimiento_bono(precio_mercado, F_bono, r_periodo, C_bono, n_periodos_bono)
        
        if np.isnan(i_periodo_res):
            st.error("No se pudo encontrar una tasa válida para este precio.")
        else:
            i_nom_res = i_periodo_res * m_bono
            
            if precio_mercado > C_bono:
                estado_bono = "Se vende con **PRIMA** (Tasa Rendimiento < Tasa Cupón)"
                color = "green"
            elif precio_mercado < C_bono:
                estado_bono = "Se vende con **DESCUENTO** (Tasa Rendimiento > Tasa Cupón)"
                color = "red"
            else:
                estado_bono = "Se vende **A LA PAR** (Tasa Rendimiento = Tasa Cupón)"
                color = "blue"
                
            col_res1, col_res2 = st.columns([1, 1])
            with col_res1:
                st.metric("Tasa de Rendimiento Nominal Anual (YTM)", f"{i_nom_res * 100:,.4f}%")
                st.metric("Tasa Efectiva del Periodo ($i_m$)", f"{i_periodo_res * 100:,.4f}%")
                st.write(f"Monto de cada cupón ($Fr$): **${cupon_Fr:,.2f}**")
                st.markdown(f"<span style='color:{color}; font-weight:bold;'>{estado_bono}</span>", unsafe_allow_html=True)
                
            with col_res2:
                formula_ytm = r"P_{mercado} = Fr \left[ \frac{1 - (1+i_m)^{-nm}}{i_m} \right] + C(1+i_m)^{-nm}"
                st.latex(formula_ytm)
                
            with st.expander("Ver desarrollo paso a paso del cálculo actual"):
                st.info("**1. Estableciendo la Ecuación de Valor:**")
                st.latex(rf"{precio_mercado:,.2f} = {cupon_Fr:,.2f} \left[ \frac{{1 - (1+i_m)^{{-{n_periodos_bono:g}}}}}{{i_m}} \right] + {C_bono:,.2f}(1+i_m)^{{-{n_periodos_bono:g}}}")
                
                st.warning("**Aviso: Cálculo mediante Métodos Numéricos (Newton-Raphson)**")
                st.markdown("""
                En esta ecuación, la tasa periódica de rendimiento ($i_m$) se encuentra en el denominador y también en los exponentes de los factores de descuento. 
                
                **Al ser un polinomio de grado $nm$, es matemáticamente imposible despejar $i_m$ mediante álgebra tradicional.**
                
                Por lo tanto, el motor de la calculadora utiliza algoritmos iterativos de búsqueda de raíces para encontrar el valor exacto de $i_m$ que iguale el lado derecho de la ecuación con el precio de mercado.
                """)
                
                st.info("**2. Resultados de la iteración:**")
                st.latex(rf"i_m \approx {i_periodo_res:.6f} \quad ({i_periodo_res*100:.4f}\% \text{{ periódica}})")
                st.latex(rf"\text{{YTM Anualizada}} = i_m \times {m_bono:g} = {i_nom_res:.6f} \quad ({i_nom_res*100:.4f}\%)")
                st.success(f"**La tasa de rendimiento al vencimiento (YTM) es {i_nom_res*100:.4f}\% anual.**")
# =============================================================================
# 6. VALUACIÓN DE ACCIONES
# =============================================================================
elif opcion == "6. Valuación de Acciones":
    st.markdown('<div class="section-header">6. Valuación de Acciones</div>', unsafe_allow_html=True)
    
    st.markdown("Herramientas de valuación de renta variable basadas en dividendos y comparables de mercado.")
    
    tab_gordon, tab_rendimiento, tab_multiplos = st.tabs([
        "Valuación (D1, k, g)", 
        "Rendimiento Requerido", 
        "Valuación por Múltiplos"
    ])

    # --- PESTAÑA 1: GORDON-SHAPIRO (VALUACIÓN) ---
    with tab_gordon:
        st.markdown("### Modelo de Crecimiento Constante (Gordon-Shapiro)")
        c1, c2 = st.columns(2)
        with c1:
            d1 = st.number_input("Dividendo esperado el próximo año ($D_1$)", min_value=0.01, value=5.0, step=0.5, key="gs_d1")
            k_rend = st.number_input("Tasa de rendimiento requerida ($k$) %", value=12.0, step=0.1, key="gs_k") / 100
        with c2:
            g_crec = st.number_input("Tasa de crecimiento constante ($g$) %", value=4.0, step=0.1, key="gs_g") / 100
            st.info("Nota: Para que el modelo sea válido, $k$ debe ser mayor que $g$.")

        # Cálculo automático
        if k_rend > g_crec:
            precio_acc = engine.valuacion_gordon_shapiro(d1, k_rend, g_crec)
            st.write("---")
            col_res_gs, col_form_gs = st.columns([1, 1])
            with col_res_gs:
                st.metric("Precio Teórico de la Acción ($P_0$)", f"${precio_acc:,.2f}")
            with col_form_gs:
                st.latex(r"P_0 = \frac{D_1}{k - g}")
                
            with st.expander("Ver desarrollo paso a paso del cálculo actual"):
                st.info("**Sustitución y Desarrollo:**")
                st.latex(rf"P_0 = \frac{{{d1:,.2f}}}{{{k_rend:.4f} - {g_crec:.4f}}}")
                st.latex(rf"P_0 = \frac{{{d1:,.2f}}}{{{k_rend - g_crec:.4f}}}")
                st.latex(rf"P_0 = {precio_acc:,.2f}")
                st.success(f"**El precio justo estimado de la acción es ${precio_acc:,.2f}**")
        else:
            st.warning("La tasa de rendimiento ($k$) debe ser mayor a la de crecimiento ($g$) para valuar la acción.")

    # --- PESTAÑA 2: RENDIMIENTO REQUERIDO ---
    with tab_rendimiento:
        st.markdown("### Cálculo del Rendimiento Requerido")
        c1, c2 = st.columns(2)
        with c1:
            p0_mercado = st.number_input("Precio actual de la acción ($P_0$)", min_value=0.01, value=150.0, step=5.0, key="rr_p0")
            d1_rend = st.number_input("Dividendo esperado ($D_1$)", min_value=0.01, value=7.5, step=0.5, key="rr_d1")
        with c2:
            g_rend = st.number_input("Tasa de crecimiento ($g$) %", value=5.0, step=0.1, key="rr_g") / 100
        
        # Cálculo automático
        k_calc = engine.rendimiento_requerido_accion(d1_rend, p0_mercado, g_rend)
        st.write("---")
        col_res_rr, col_form_rr = st.columns([1, 1])
        with col_res_rr:
            st.metric("Rendimiento Requerido ($k$)", f"{k_calc * 100:,.2f}%")
        with col_form_rr:
            st.latex(r"k = \frac{D_1}{P_0} + g")

        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info("**Sustitución y Desarrollo:**")
            st.latex(rf"k = \frac{{{d1_rend:,.2f}}}{{{p0_mercado:,.2f}}} + {g_rend:.4f}")
            st.latex(rf"k = {d1_rend/p0_mercado:.6f} + {g_rend:.4f}")
            st.latex(rf"k = {k_calc:.6f}")
            st.success(f"**El costo de capital o rendimiento exigido es {k_calc*100:.2f}%.**")

    # --- PESTAÑA 3: MÚLTIPLOS ---
    with tab_multiplos:
        st.markdown("### Valuación Relativa por Múltiplos")
        
        metodo_final = st.selectbox("Seleccione el método de valuación:", [
            "Precio / Utilidad (P/E Ratio)",
            "Precio / Ventas (P/S Ratio)",
            "EV / EBITDA",
            "Precio / Valor en Libros (P/B Ratio)"
        ], key="sel_metodo_unico")

        st.write("---")
        c1, c2 = st.columns(2)
        
        if metodo_final == "Precio / Utilidad (P/E Ratio)":
            label_metrica = "Utilidad por Acción (UPA / EPS)"
            label_multiplo = "Múltiplo P/E Objetivo"
            formula_lat = r"P_0 = \text{UPA} \times \left( \frac{P}{E} \right)"
            es_ev = False
            var_nombre = "P_0"
            metrica_txt = r"\text{UPA}"
            mult_txt = r"\frac{P}{E}"
        elif metodo_final == "Precio / Ventas (P/S Ratio)":
            label_metrica = "Ventas por Acción (VPA)"
            label_multiplo = "Múltiplo P/S Objetivo"
            formula_lat = r"P_0 = \text{VPA} \times \left( \frac{P}{S} \right)"
            es_ev = False
            var_nombre = "P_0"
            metrica_txt = r"\text{VPA}"
            mult_txt = r"\frac{P}{S}"
        elif metodo_final == "EV / EBITDA":
            label_metrica = "EBITDA por Acción"
            label_multiplo = "Múltiplo EV/EBITDA Objetivo"
            formula_lat = r"EV = \text{EBITDA} \times \left( \frac{EV}{\text{EBITDA}} \right)"
            es_ev = True
            var_nombre = "EV"
            metrica_txt = r"\text{EBITDA}"
            mult_txt = r"\frac{EV}{\text{EBITDA}}"
        else: 
            label_metrica = "Valor en Libros por Acción (VLA)"
            label_multiplo = "Múltiplo P/B Objetivo"
            formula_lat = r"P_0 = \text{VLA} \times \left( \frac{P}{B} \right)"
            es_ev = False
            var_nombre = "P_0"
            metrica_txt = r"\text{VLA}"
            mult_txt = r"\frac{P}{B}"

        with c1:
            val_metrica = st.number_input(f"{label_metrica} ($)", min_value=0.01, value=10.0, step=1.0, key="val_met_input")
        with c2:
            val_multiplo = st.number_input(f"{label_multiplo}", min_value=0.1, value=15.0, step=0.5, key="val_mult_input")

        resultado_final = engine.valuacion_multiplos(val_metrica, val_multiplo)
        
        st.write("---")
        col_res_fin, col_form_fin = st.columns([1, 1])
        
        with col_res_fin:
            titulo_res = "Valor de la Empresa (EV)" if es_ev else "Precio Estimado ($P_0$)"
            st.metric(titulo_res, f"${resultado_final:,.2f}")
            st.caption(f"Valuación mediante {metodo_final}")
            
        with col_form_fin:
            st.markdown("**Identidad Financiera:**")
            st.latex(formula_lat)

        with st.expander("Ver desarrollo paso a paso del cálculo actual"):
            st.info(f"**Sustitución directa ({metodo_final}):**")
            st.latex(rf"{var_nombre} = {val_metrica:,.2f} \times {val_multiplo:,.2f}")
            st.latex(rf"{var_nombre} = {resultado_final:,.2f}")
            st.success(f"**Resultado: {titulo_res} = ${resultado_final:,.2f}**")

# =============================================================================
# 7. PORTAFOLIOS EFICIENTES (MARKOWITZ)
# =============================================================================
elif opcion == "7. Portafolios Eficientes":

    st.markdown('<div class="section-header">7. Teoría de Portafolios (Frontera Eficiente)</div>', unsafe_allow_html=True)
    st.markdown("Optimización matemática exacta usando programación cuadrática y datos reales de la bolsa (Yahoo Finance).")

    # --- Controles de entrada en la pantalla principal ---
    with st.expander("Configuración del Portafolio y Mercado", expanded=True):
        c_in1, c_in2, c_in3 = st.columns([2, 1, 1])
        with c_in1:
            tickers_input = st.text_input("Símbolos (separados por coma):", value="AAPL, MSFT, GOOGL, NVDA, TSLA", help="Ejemplo: AAPL (Apple), CEMEXCPO.MX (Cemex), SPY (S&P 500)")
        with c_in2:
            hoy = datetime.date.today()
            hace_3_anios = hoy - datetime.timedelta(days=365*3)
            fecha_inicio = st.date_input("Fecha de Inicio", value=hace_3_anios)
            fecha_fin = st.date_input("Fecha de Fin", value=hoy)
        with c_in3:
            tasa_libre_riesgo = st.number_input("Tasa Libre de Riesgo ($r_f$) %", value=5.0, step=0.1) / 100
            ejecutar = st.button("Optimizar Portafolio", use_container_width=True)

    if ejecutar:
        tickers = [ticker.strip().upper() for ticker in tickers_input.split(",") if ticker.strip()]
        
        if len(tickers) < 2:
            st.error("Necesitas al menos 2 activos para generar una frontera de Markowitz.")
        else:
            with st.spinner(f"Descargando datos históricos de {len(tickers)} activos y resolviendo matrices..."):
                try:
                    data, mu, S, res_sharpe, res_min, nube = engine.optimizacion_markowitz(
                        tickers, fecha_inicio, fecha_fin, tasa_libre_riesgo
                    )
                    
                    rend_s, vol_s, sharpe_ratio, pesos_sharpe = res_sharpe
                    rend_m, vol_m, sharpe_m, pesos_min = res_min
                    ret_sim, vol_sim, sharpe_sim = nube

                    st.success("¡Optimización matemática completada exitosamente!")

                    # --- MÉTRICAS VISUALES ---
                    st.markdown("### Portafolio Óptimo (Máximo Ratio de Sharpe)")
                    st.info("La combinación matemáticamente perfecta para maximizar el retorno por cada unidad de riesgo.")
                    
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Rendimiento Esperado Anual", f"{rend_s*100:.2f}%")
                    c2.metric("Volatilidad Anual ($\sigma$)", f"{vol_s*100:.2f}%")
                    c3.metric("Ratio de Sharpe", f"{sharpe_ratio:.4f}")

                    # --- GRÁFICAS Y RESULTADOS ---
                    tab_frontera, tab_pesos, tab_historico = st.tabs(["Frontera Eficiente", "Composición Óptima ($w_i$)", "Desempeño Histórico"])

                    with tab_frontera:
                        st.markdown("#### Gráfica Riesgo vs. Rendimiento")
                        fig_ef = go.Figure()

                        # Nube de puntos de simulación
                        fig_ef.add_trace(go.Scatter(
                            x=vol_sim, y=ret_sim, mode='markers',
                            marker=dict(size=4, color=sharpe_sim, colorscale='Viridis', showscale=True, 
                                        colorbar=dict(title="Sharpe Ratio")),
                            text=[f"Rendimiento: {r*100:.2f}%<br>Riesgo: {v*100:.2f}%<br>Sharpe: {s:.2f}" 
                                  for r, v, s in zip(ret_sim, vol_sim, sharpe_sim)],
                            hoverinfo='text', name='Portafolios Posibles'
                        ))

                        # Estrella Roja: Max Sharpe
                        fig_ef.add_trace(go.Scatter(
                            x=[vol_s], y=[rend_s], mode='markers',
                            marker=dict(symbol='star', size=16, color='red', line=dict(width=1, color='black')),
                            name='Máximo Sharpe (Óptimo)'
                        ))

                        # Estrella Azul: Min Vol
                        fig_ef.add_trace(go.Scatter(
                            x=[vol_m], y=[rend_m], mode='markers',
                            marker=dict(symbol='star', size=16, color='cyan', line=dict(width=1, color='black')),
                            name='Mínima Varianza Global'
                        ))

                        fig_ef.update_layout(
                            xaxis_title="Riesgo / Volatilidad Anualizada ($\sigma$)",
                            yaxis_title="Rendimiento Esperado Anualizado ($E[R]$)",
                            template="plotly_white", legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                            height=550
                        )
                        st.plotly_chart(fig_ef, use_container_width=True)

                    with tab_pesos:
                        st.markdown("#### Comparativa de Asignación de Capital ($w_i$)")
                        st.caption("Observa cómo cambia la distribución de tu dinero dependiendo de si buscas rentabilidad o seguridad.")
                        
                        # Unir los dos diccionarios en un solo DataFrame
                        df_pesos = pd.DataFrame({
                            'Máximo Sharpe (Rendimiento)': pesos_sharpe,
                            'Mínima Varianza (Seguridad)': pesos_min
                        }).fillna(0)
                        
                        # Formatear la tabla para Plotly (Melt)
                        df_melted = df_pesos.reset_index().melt(id_vars='index', var_name='Estrategia', value_name='Peso')
                        df_melted.rename(columns={'index': 'Activo'}, inplace=True)
                        
                        # Filtrar activos con peso casi nulo (menor a 0.1%) para no saturar la gráfica
                        df_melted = df_melted[df_melted['Peso'] > 0.001] 
                        
                        # Crear el gráfico de barras apiladas
                        fig_pesos = px.bar(
                            df_melted, 
                            y="Estrategia", 
                            x="Peso", 
                            color="Activo", 
                            orientation="h",
                            text_auto=".1%", # Muestra el porcentaje escrito dentro de la barra
                            color_discrete_sequence=px.colors.qualitative.Vivid, # Paleta de alto contraste
                            title="Distribución del Portafolio"
                        )
                        
                        fig_pesos.update_layout(
                            xaxis_title="Porcentaje de Inversión",
                            yaxis_title="",
                            xaxis_tickformat=".0%", # Formato de porcentaje en el eje X
                            template="plotly_white",
                            height=400,
                            legend_title="Símbolos",
                            barmode="stack"
                        )
                        
                        # Ajustar el texto dentro de las barras para que se vea claro
                        fig_pesos.update_traces(textfont_size=13, textangle=0, textposition="inside", cliponaxis=False)
                        
                        st.plotly_chart(fig_pesos, use_container_width=True)

                    with tab_historico:
                        st.markdown("#### Precios Históricos Normalizados (Base 100)")
                        st.caption("Evolución de cada activo si hubieras invertido $100 al inicio del periodo.")
                        precios_norm = (data / data.iloc[0]) * 100
                        fig_hist = px.line(precios_norm, x=precios_norm.index, y=precios_norm.columns,
                                           labels={"value": "Valor de Inversión ($)", "Date": "Fecha"})
                        fig_hist.update_layout(template="plotly_white", hovermode="x unified")
                        st.plotly_chart(fig_hist, use_container_width=True)

                except Exception as e:
                    st.error(f"Ocurrió un error al procesar los datos: {e}")
                    st.info("Verifica que los símbolos sean correctos, que haya conexión a internet y que el rango de fechas sea válido.")
# =============================================================================
# 8. FORWARDS (DERIVADOS)
# =============================================================================
elif opcion == "8. Forwards (Derivados)":
    import numpy as np
    st.markdown('<div class="section-header">8. Forwards (Precio y Valuación)</div>', unsafe_allow_html=True)
    
    tipo_cap = st.radio("Tipo de Capitalización:", ["Continua", "Discreta"], horizontal=True, key="fwd_cap_global")
    es_continua = "Continua" in tipo_cap

    tab_precio, tab_valuacion = st.tabs(["Precio Futuros (Forwards)", "Valuación del Contrato"])

    # -----------------------------------------------------
    # PESTAÑA 1: PRECIO FORWARD (PRICING)
    # -----------------------------------------------------
    with tab_precio:
        st.markdown("### Determinación del Precio Forward Teórico ($F$)")
        tipo_fwd = st.radio("Tipo de Activo Subyacente:", 
                            ["Simple", "Ingresos (Dividendos)", "Costos Discretos (Mercancías)", "Divisas / Retorno"], 
                            horizontal=True, key="radio_tipo_fwd")
        
        st.write("---")
        c1, c2 = st.columns([1.2, 0.8]) 
        
        with c1:
            S0 = st.number_input("Precio Spot Actual ($S_0$)", min_value=0.0, value=100.0, key="fwd_s0")
            r_fwd = st.number_input("Tasa libre de riesgo ($r$) %", value=5.0, step=0.1, key="fwd_r") / 100
            T_fwd = st.number_input("Tiempo total del contrato ($T$ en años)", min_value=0.01, value=1.0, key="fwd_t")
            st.write("---")
            
            if "Ingresos" in tipo_fwd:
                st.markdown("##### Configuración de Dividendos")
                modo_ing = st.radio("Frecuencia:", ["Periódicos y Constantes", "Irregulares (Personalizados)"], horizontal=True, key="modo_ing")
                
                I_ing = 0.0
                if modo_ing == "Periódicos y Constantes":
                    ci1, ci2 = st.columns(2)
                    monto_div = ci1.number_input("Monto por pago ($D$)", min_value=0.0, value=1.5, key="fwd_D")
                    freq_div = ci2.number_input("Pagos por año ($m$)", min_value=1.0, value=4.0, key="fwd_m_div")
                    
                    I_ing = engine.calcular_vp_dividendos(monto_div, freq_div, r_fwd, T_fwd, "Continua" if es_continua else "Discreta")
                    formula_I = r"I = \sum_{k=1}^{T \cdot m} D e^{-r (\frac{k}{m})}" if es_continua else r"I = \sum_{k=1}^{T \cdot m} \frac{D}{(1+r)^{k/m}}"
                
                else: 
                    n_flujos = st.number_input("Cantidad de dividendos esperados", min_value=1, max_value=24, value=4, key="n_flujos_ing")
                    montos_irr = []
                    tiempos_irr = []
                    
                    st.caption("Ingresa el monto y el **mes exacto** de pago (ej. 1, 5, 7, 12):")
                    for i in range(int(n_flujos)):
                        cx1, cx2 = st.columns(2)
                        m_val = cx1.number_input(f"Monto Div {i+1} ($)", value=10.0, step=1.0, key=f"monto_ing_{i}")
                        t_val = cx2.number_input(f"Ocurre en el Mes", min_value=0.1, value=float(i+1), step=1.0, key=f"mes_ing_{i}")
                        montos_irr.append(m_val)
                        tiempos_irr.append(t_val / 12.0) 
                        
                    I_ing = engine.calcular_vp_flujos_irregulares(montos_irr, tiempos_irr, r_fwd, "Continua" if es_continua else "Discreta")
                    formula_I = r"I = \sum_{j=1}^{n} D_j e^{-r t_j}" if es_continua else r"I = \sum_{j=1}^{n} \frac{D_j}{(1+r)^{t_j}}"

                if es_continua:
                    fwd_res = (S0 - I_ing) * np.exp(r_fwd * T_fwd)
                    formula_fwd = r"F = (S_0 - I) e^{rT}"
                else:
                    fwd_res = (S0 - I_ing) * (1 + r_fwd)**T_fwd
                    formula_fwd = r"F = (S_0 - I) (1 + r)^T"
                
                st.info(f"Valor Presente de ingresos calculado ($I$): **${I_ing:,.4f}**")
                st.latex(formula_I)

            elif "Costos" in tipo_fwd:
                st.markdown("##### Configuración de Costos (Almacenaje / Seguro)")
                modo_costo = st.radio("Frecuencia:", ["Periódicos y Constantes", "Irregulares (Personalizados)"], horizontal=True, key="modo_costo")
                
                U_costo = 0.0
                if modo_costo == "Periódicos y Constantes":
                    cc1, cc2 = st.columns(2)
                    monto_costo = cc1.number_input("Costo por periodo ($C$)", min_value=0.0, value=2.0, key="fwd_C")
                    freq_costo = cc2.number_input("Pagos al año ($m$)", min_value=1.0, value=12.0, key="fwd_m_costo")
                    
                    U_costo = engine.calcular_vp_dividendos(monto_costo, freq_costo, r_fwd, T_fwd, "Continua" if es_continua else "Discreta")
                    formula_U = r"U = \sum_{k=1}^{T \cdot m} C e^{-r (\frac{k}{m})}" if es_continua else r"U = \sum_{k=1}^{T \cdot m} \frac{C}{(1+r)^{k/m}}"
                
                else: 
                    n_flujos_c = st.number_input("Cantidad de pagos de costos", min_value=1, max_value=24, value=4, key="n_flujos_costo")
                    montos_c_irr = []
                    tiempos_c_irr = []
                    
                    st.caption("Ingresa el costo y el **mes exacto** de pago:")
                    for i in range(int(n_flujos_c)):
                        cx1, cx2 = st.columns(2)
                        c_val = cx1.number_input(f"Costo {i+1} ($)", value=5.0, step=1.0, key=f"monto_costo_{i}")
                        t_val = cx2.number_input(f"Ocurre en el Mes", min_value=0.1, value=float(i+1), step=1.0, key=f"mes_costo_{i}")
                        montos_c_irr.append(c_val)
                        tiempos_c_irr.append(t_val / 12.0)
                        
                    U_costo = engine.calcular_vp_flujos_irregulares(montos_c_irr, tiempos_c_irr, r_fwd, "Continua" if es_continua else "Discreta")
                    formula_U = r"U = \sum_{j=1}^{n} C_j e^{-r t_j}" if es_continua else r"U = \sum_{j=1}^{n} \frac{C_j}{(1+r)^{t_j}}"

                if es_continua:
                    fwd_res = (S0 + U_costo) * np.exp(r_fwd * T_fwd)
                    formula_fwd = r"F = (S_0 + U) e^{rT}"
                else:
                    fwd_res = (S0 + U_costo) * (1 + r_fwd)**T_fwd
                    formula_fwd = r"F = (S_0 + U) (1 + r)^T"
                
                st.warning(f"Valor Presente de costos calculado ($U$): **${U_costo:,.4f}**")
                st.latex(formula_U)

            elif "Divisas" in tipo_fwd:
                delta_fwd = st.number_input("Tasa Extranjera ($\delta$) %", value=2.0, step=0.1, key="fwd_delta") / 100
                fwd_res = engine.forward_calculo(S0, r_fwd, delta_fwd, T_fwd, "Continua" if es_continua else "Discreta")
                formula_fwd = r"F = S_0 e^{(r - \delta)T}" if es_continua else r"F = S_0 \frac{(1+r)^T}{(1+\delta)^T}"
            
            else:
                if es_continua:
                    fwd_res = S0 * np.exp(r_fwd * T_fwd)
                    formula_fwd = r"F = S_0 e^{rT}"
                else:
                    fwd_res = S0 * (1 + r_fwd)**T_fwd
                    formula_fwd = r"F = S_0 (1+r)^T"
                    
        with c2:
            st.metric("Precio Forward Teórico ($F$)", f"${fwd_res:,.4f}")
            st.latex(formula_fwd)
            st.caption("Recuerda: Los dividendos disminuyen el precio Forward, mientras que los costos de almacenaje lo aumentan.")

        with st.expander("Ver desarrollo paso a paso del cálculo de Precio (F)"):
            st.info("**Sustitución y Desarrollo:**")
            
            if "Ingresos" in tipo_fwd:
                base_val = S0 - I_ing
                st.latex(rf"\text{{Spot Ajustado}} = S_0 - I = {S0:,.2f} - {I_ing:,.4f} = {base_val:,.4f}")
                if es_continua:
                    st.latex(rf"F = ({base_val:,.4f}) e^{{({r_fwd:.4f} \times {T_fwd:g})}}")
                    st.latex(rf"F = ({base_val:,.4f}) e^{{{r_fwd*T_fwd:.6f}}}")
                    st.latex(rf"F = ({base_val:,.4f}) \times {np.exp(r_fwd*T_fwd):.6f}")
                else:
                    st.latex(rf"F = ({base_val:,.4f}) (1 + {r_fwd:.4f})^{{{T_fwd:g}}}")
                    st.latex(rf"F = ({base_val:,.4f}) \times {(1+r_fwd)**T_fwd:.6f}")
                    
            elif "Costos" in tipo_fwd:
                base_val = S0 + U_costo
                st.latex(rf"\text{{Spot Ajustado}} = S_0 + U = {S0:,.2f} + {U_costo:,.4f} = {base_val:,.4f}")
                if es_continua:
                    st.latex(rf"F = ({base_val:,.4f}) e^{{({r_fwd:.4f} \times {T_fwd:g})}}")
                    st.latex(rf"F = ({base_val:,.4f}) e^{{{r_fwd*T_fwd:.6f}}}")
                    st.latex(rf"F = ({base_val:,.4f}) \times {np.exp(r_fwd*T_fwd):.6f}")
                else:
                    st.latex(rf"F = ({base_val:,.4f}) (1 + {r_fwd:.4f})^{{{T_fwd:g}}}")
                    st.latex(rf"F = ({base_val:,.4f}) \times {(1+r_fwd)**T_fwd:.6f}")
                    
            elif "Divisas" in tipo_fwd:
                if es_continua:
                    st.latex(rf"F = {S0:,.2f} e^{{({r_fwd:.4f} - {delta_fwd:.4f}) \times {T_fwd:g}}}")
                    st.latex(rf"F = {S0:,.2f} e^{{{(r_fwd-delta_fwd)*T_fwd:.6f}}}")
                    st.latex(rf"F = {S0:,.2f} \times {np.exp((r_fwd-delta_fwd)*T_fwd):.6f}")
                else:
                    st.latex(rf"F = {S0:,.2f} \left[ \frac{{(1 + {r_fwd:.4f})^{{{T_fwd:g}}}}}{{(1 + {delta_fwd:.4f})^{{{T_fwd:g}}}}} \right]")
                    num = (1+r_fwd)**T_fwd
                    den = (1+delta_fwd)**T_fwd
                    st.latex(rf"F = {S0:,.2f} \left[ \frac{{{num:.6f}}}{{{den:.6f}}} \right]")
                    st.latex(rf"F = {S0:,.2f} \times {(num/den):.6f}")
            else:
                if es_continua:
                    st.latex(rf"F = {S0:,.2f} e^{{({r_fwd:.4f} \times {T_fwd:g})}}")
                    st.latex(rf"F = {S0:,.2f} e^{{{r_fwd*T_fwd:.6f}}}")
                    st.latex(rf"F = {S0:,.2f} \times {np.exp(r_fwd*T_fwd):.6f}")
                else:
                    st.latex(rf"F = {S0:,.2f} (1 + {r_fwd:.4f})^{{{T_fwd:g}}}")
                    st.latex(rf"F = {S0:,.2f} \times {(1+r_fwd)**T_fwd:.6f}")
                    
            st.success(f"**Resultado Final: $F = {fwd_res:,.4f}**")

    # -----------------------------------------------------
    # PESTAÑA 2: VALUACIÓN DEL CONTRATO
    # -----------------------------------------------------
    with tab_valuacion:
        posicion = st.radio("Posición:", ["Larga (Compra)", "Corta (Venta)"], horizontal=True)
        c3, c4 = st.columns(2)
        
        with c3:
            St = st.number_input("Precio Spot actual ($S_t$)", value=105.0, key="fwd_st_val")
            K_strike = st.number_input("Precio pactado ($K$)", value=100.0, key="fwd_k_val")
            r_val = st.number_input("Tasa libre riesgo ($r$) %", value=5.0, key="fwd_r_val") / 100
            delta_val = st.number_input("Yield ($\delta$) %", value=2.0, key="fwd_delta_val") / 100
            T_val = st.number_input("Tiempo remanente ($T$)", value=0.5, key="fwd_t_val")
            
        with c4:
            valor_fwd = engine.valor_forward_calculo(St, K_strike, r_val, delta_val, T_val, posicion.split()[0], "Continua" if es_continua else "Discreta")
            st.metric("Valor del Contrato ($f$)", f"${valor_fwd:,.4f}")
            
            if es_continua:
                formula_v = r"f = S_t e^{-\delta T} - K e^{-r T}" if "Larga" in posicion else r"f = K e^{-r T} - S_t e^{-\delta T}"
            else:
                formula_v = r"f = \frac{S_t}{(1+\delta)^T} - \frac{K}{(1+r)^T}" if "Larga" in posicion else r"f = \frac{K}{(1+r)^T} - \frac{S_t}{(1+\delta)^T}"
            st.latex(formula_v)

        with st.expander("Ver desarrollo paso a paso de la Valuación (f)"):
            st.info("**Sustitución y Desarrollo:**")
            
            if es_continua:
                val_spot_desc = St * np.exp(-delta_val * T_val)
                val_strike_desc = K_strike * np.exp(-r_val * T_val)
                st.latex(rf"\text{{Spot descontado: }} S_t e^{{-\delta T}} = {St:,.2f} \times e^{{-({delta_val:.4f} \times {T_val:g})}} = {val_spot_desc:,.4f}")
                st.latex(rf"\text{{Strike descontado: }} K e^{{-r T}} = {K_strike:,.2f} \times e^{{-({r_val:.4f} \times {T_val:g})}} = {val_strike_desc:,.4f}")
                
                if "Larga" in posicion:
                    st.latex(rf"f = {val_spot_desc:,.4f} - {val_strike_desc:,.4f}")
                else:
                    st.latex(rf"f = {val_strike_desc:,.4f} - {val_spot_desc:,.4f}")
            else:
                val_spot_desc = St / ((1 + delta_val)**T_val)
                val_strike_desc = K_strike / ((1 + r_val)**T_val)
                st.latex(rf"\text{{Spot descontado: }} \frac{{{St:,.2f}}}{{(1+{delta_val:.4f})^{{{T_val:g}}}}} = \frac{{{St:,.2f}}}{{{(1+delta_val)**T_val:.6f}}} = {val_spot_desc:,.4f}")
                st.latex(rf"\text{{Strike descontado: }} \frac{{{K_strike:,.2f}}}{{(1+{r_val:.4f})^{{{T_val:g}}}}} = \frac{{{K_strike:,.2f}}}{{{(1+r_val)**T_val:.6f}}} = {val_strike_desc:,.4f}")
                
                if "Larga" in posicion:
                    st.latex(rf"f = {val_spot_desc:,.4f} - {val_strike_desc:,.4f}")
                else:
                    st.latex(rf"f = {val_strike_desc:,.4f} - {val_spot_desc:,.4f}")
                    
            st.success(f"**Valor del contrato para la posición {posicion.split()[0]}: $f = {valor_fwd:,.4f}**")
# =============================================================================
# 9. OPCIONES FINANCIERAS 
# =============================================================================
elif opcion == "9. Opciones (Derivados)":
    import numpy as np
    st.markdown('<div class="section-header">9. Valuación de Opciones Financieras</div>', unsafe_allow_html=True)
    
    st.markdown("#### Parámetros del Subyacente y Mercado")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        S_opt = st.number_input("Precio Spot Actual ($S_0$)", min_value=0.01, value=100.0, step=1.0, key="opt_s")
        K_opt = st.number_input("Precio de Ejercicio ($K$)", min_value=0.01, value=100.0, step=1.0, key="opt_k")
    with col2:
        T_opt = st.number_input("Tiempo al vencimiento ($T$ en años)", min_value=0.01, value=1.0, step=0.1, key="opt_t")
        r_opt = st.number_input("Tasa libre de riesgo continua ($r$) %", value=5.0, step=0.1, key="opt_r") / 100
    with col3:
        sigma_opt = st.number_input("Volatilidad Anual ($\sigma$) %", min_value=0.1, value=20.0, step=1.0, key="opt_sigma") / 100

    st.write("---")
    
    metodo_calculo = st.radio("Selecciona el Método de Valuación:", [
        "Fórmula Analítica (Black-Scholes-Merton)", 
        "Método Numérico (Árbol Binomial CRR)"
    ], horizontal=True)
    
    st.write("---")

    # =========================================================
    # MÉTODO 1: BLACK SCHOLES
    # =========================================================
    if metodo_calculo == "Fórmula Analítica (Black-Scholes-Merton)":
        
        tipo_bsm = st.selectbox("Ajuste del Subyacente:", [
            "1. Sin ingresos ni costos (Simple)",
            "2. Con ingresos discretos (Dividendos)",
            "3. Con costos discretos (Almacenaje/Seguro)",
            "4. Con retorno conocido (Yield continuo)",
            "5. Sobre monedas (Divisas)",
            "6. De futuros"
        ], key="sel_tipo_bsm")
        
        extra_val = 0.0
        modelo_cod = "Simple"
        
        if "2." in tipo_bsm:
            st.markdown("##### Configuración de Dividendos")
            modo_ing = st.radio("Frecuencia:", ["Periódicos y Constantes", "Irregulares (Personalizados)"], horizontal=True, key="bsm_modo_ing")
            
            if modo_ing == "Periódicos y Constantes":
                c_div1, c_div2 = st.columns(2)
                monto_d = c_div1.number_input("Monto por dividendo", min_value=0.0, value=1.5, step=0.5, key="bsm_d_monto")
                freq_d = c_div2.number_input("Pagos al año ($m$)", min_value=1.0, value=4.0, step=1.0, key="bsm_d_freq")
                extra_val = engine.calcular_vp_dividendos(monto_d, freq_d, r_opt, T_opt, "Continua")
            else:
                n_flujos = st.number_input("Cantidad de dividendos esperados", min_value=1, max_value=24, value=4, key="bsm_n_ing")
                montos_irr, tiempos_irr = [], []
                st.caption("Ingresa el monto y el **mes exacto** de pago:")
                for i in range(int(n_flujos)):
                    cx1, cx2 = st.columns(2)
                    m_val = cx1.number_input(f"Monto Div {i+1} ($)", value=1.0, step=0.5, key=f"bsm_ing_m_{i}")
                    t_val = cx2.number_input(f"Mes de pago", min_value=0.1, value=float(i+1), step=1.0, key=f"bsm_ing_t_{i}")
                    montos_irr.append(m_val)
                    tiempos_irr.append(t_val / 12.0)
                extra_val = engine.calcular_vp_flujos_irregulares(montos_irr, tiempos_irr, r_opt, "Continua")
                
            st.info(f"VP de Dividendos descontados al continuo ($D$): **${extra_val:,.4f}**")
            modelo_cod = "Ingresos"
            
        elif "3." in tipo_bsm:
            st.markdown("##### Configuración de Costos (Almacenaje / Seguro)")
            modo_costo = st.radio("Frecuencia:", ["Periódicos y Constantes", "Irregulares (Personalizados)"], horizontal=True, key="bsm_modo_costo")
            
            if modo_costo == "Periódicos y Constantes":
                cc1, cc2 = st.columns(2)
                monto_c = cc1.number_input("Costo por periodo", min_value=0.0, value=2.0, step=0.5, key="bsm_c_monto")
                freq_c = cc2.number_input("Pagos al año ($m$)", min_value=1.0, value=12.0, step=1.0, key="bsm_c_freq")
                extra_val = engine.calcular_vp_dividendos(monto_c, freq_c, r_opt, T_opt, "Continua")
            else:
                n_flujos_c = st.number_input("Cantidad de pagos de costos", min_value=1, max_value=24, value=4, key="bsm_n_costo")
                montos_c_irr, tiempos_c_irr = [], []
                st.caption("Ingresa el costo y el **mes exacto** de pago:")
                for i in range(int(n_flujos_c)):
                    cx1, cx2 = st.columns(2)
                    c_val = cx1.number_input(f"Costo {i+1} ($)", value=2.0, step=0.5, key=f"bsm_costo_m_{i}")
                    t_val = cx2.number_input(f"Mes de pago", min_value=0.1, value=float(i+1), step=1.0, key=f"bsm_costo_t_{i}")
                    montos_c_irr.append(c_val)
                    tiempos_c_irr.append(t_val / 12.0)
                extra_val = engine.calcular_vp_flujos_irregulares(montos_c_irr, tiempos_c_irr, r_opt, "Continua")
                
            st.warning(f"VP de Costos descontados al continuo ($U$): **${extra_val:,.4f}**")
            modelo_cod = "Costos"

        elif "4." in tipo_bsm:
            extra_val = st.number_input("Tasa de rendimiento continuo ($q$) %", value=2.0, step=0.1) / 100
            modelo_cod = "Yield"
        elif "5." in tipo_bsm:
            extra_val = st.number_input("Tasa libre de riesgo extranjera ($r_f$) %", value=3.0, step=0.1) / 100
            modelo_cod = "Monedas"
        elif "6." in tipo_bsm:
            modelo_cod = "Futuros"

        call_price, put_price, d1_res, d2_res = engine.opciones_bsm(modelo_cod, S_opt, K_opt, T_opt, r_opt, sigma_opt, extra_val)

        from scipy.stats import norm
        Nd1 = norm.cdf(d1_res)
        Nd2 = norm.cdf(d2_res)
        N_minus_d1 = norm.cdf(-d1_res)
        N_minus_d2 = norm.cdf(-d2_res)

        if modelo_cod == "Simple":
            f_call = r"c = S_0 N(d_1) - K e^{-rT} N(d_2)"
            f_put = r"p = K e^{-rT} N(-d_2) - S_0 N(-d_1)"
            f_d1 = r"d_1 = \frac{\ln(S_0 / K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}"
        elif modelo_cod == "Ingresos":
            f_call = r"c = (S_0 - D) N(d_1) - K e^{-rT} N(d_2)"
            f_put = r"p = K e^{-rT} N(-d_2) - (S_0 - D) N(-d_1)"
            f_d1 = r"d_1 = \frac{\ln((S_0 - D)/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}"
        elif modelo_cod == "Costos":
            f_call = r"c = (S_0 + U) N(d_1) - K e^{-rT} N(d_2)"
            f_put = r"p = K e^{-rT} N(-d_2) - (S_0 + U) N(-d_1)"
            f_d1 = r"d_1 = \frac{\ln((S_0 + U)/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}"
        elif modelo_cod == "Yield":
            f_call = r"c = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)"
            f_put = r"p = K e^{-rT} N(-d_2) - S_0 e^{-qT} N(-d_1)"
            f_d1 = r"d_1 = \frac{\ln(S_0 / K) + (r - q + \sigma^2/2)T}{\sigma \sqrt{T}}"
        elif modelo_cod == "Monedas":
            f_call = r"c = S_0 e^{-r_f T} N(d_1) - K e^{-rT} N(d_2)"
            f_put = r"p = K e^{-rT} N(-d_2) - S_0 e^{-r_f T} N(-d_1)"
            f_d1 = r"d_1 = \frac{\ln(S_0 / K) + (r - r_f + \sigma^2/2)T}{\sigma \sqrt{T}}"
        elif modelo_cod == "Futuros":
            f_call = r"c = e^{-rT} [ F_0 N(d_1) - K N(d_2) ]"
            f_put = r"p = e^{-rT} [ K N(-d_2) - F_0 N(-d_1) ]"
            f_d1 = r"d_1 = \frac{\ln(F_0 / K) + (\sigma^2/2)T}{\sigma \sqrt{T}}"

        st.write("---")
        col_res_call, col_res_put = st.columns(2)
        with col_res_call:
            st.markdown(f"<div style='background-color:#E8F5E9; padding:15px; border-radius:10px; border-left: 5px solid #2E7D32;'>"
                        f"<h3 style='color:#2E7D32; margin:0;'>Call Teórica: ${call_price:,.4f}</h3></div>", unsafe_allow_html=True)
            st.metric("Parámetro d1", f"{d1_res:.4f}")
            st.latex(f_call)
            st.latex(f_d1)
        with col_res_put:
            st.markdown(f"<div style='background-color:#FFEBEE; padding:15px; border-radius:10px; border-left: 5px solid #C62828;'>"
                        f"<h3 style='color:#C62828; margin:0;'>Put Teórica: ${put_price:,.4f}</h3></div>", unsafe_allow_html=True)
            st.metric("Parámetro d2", f"{d2_res:.4f}")
            st.latex(f_put)
            st.latex(r"d_2 = d_1 - \sigma \sqrt{T}")

        # --- DESARROLLO PASO A PASO (BSM) ---# --- DESARROLLO PASO A PASO (BSM) ---
        with st.expander("Ver desarrollo paso a paso del modelo Black-Scholes-Merton"):
            st.info("**1. Cálculo de los parámetros de probabilidad ($d_1$ y $d_2$):**")
            
            # Dinámica del Spot Base según modelo
            spot_ajustado = S_opt
            if modelo_cod == "Ingresos": spot_ajustado = S_opt - extra_val
            elif modelo_cod == "Costos": spot_ajustado = S_opt + extra_val
            
            # Dinámica de la tasa efectiva r_hat para el d1
            r_hat = r_opt
            if modelo_cod in ["Yield", "Monedas"]: r_hat = r_opt - extra_val
            elif modelo_cod == "Futuros": r_hat = 0
                
            # Corrección: Mostrar la fracción de sigma^2 / 2 explícitamente en LaTeX
            st.latex(rf"d_1 = \frac{{\ln({spot_ajustado:.2f} / {K_opt:.2f}) + \left({r_hat:.4f} + \frac{{{sigma_opt:.4f}^2}}{{2}}\right){T_opt:g}}}{{{sigma_opt:.4f} \sqrt{{{T_opt:g}}}}}")
            
            num_d1 = np.log(spot_ajustado/K_opt) + (r_hat + (sigma_opt**2)/2) * T_opt
            den_d1 = sigma_opt * np.sqrt(T_opt)
            
            st.latex(rf"d_1 = \frac{{{np.log(spot_ajustado/K_opt):.6f} + {(r_hat + (sigma_opt**2)/2)*T_opt:.6f}}}{{{den_d1:.6f}}} = {d1_res:.4f}")
            
            st.latex(rf"d_2 = {d1_res:.4f} - {sigma_opt:.4f} \sqrt{{{T_opt:g}}} = {d2_res:.4f}")
            
            st.info("**2. Probabilidades Normales Acumuladas:**")
            st.latex(rf"N(d_1) = {Nd1:.4f} \quad \text{{ (Delta de la Call) }}")
            st.latex(rf"N(d_2) = {Nd2:.4f} \quad \text{{ (Probabilidad de ejercicio) }}")
            st.latex(rf"N(-d_1) = {N_minus_d1:.4f}")
            st.latex(rf"N(-d_2) = {N_minus_d2:.4f}")
            
            st.info("**3. Precios Finales (Descuentos):**")
            desc_strike = K_opt * np.exp(-r_opt * T_opt)
            
            if modelo_cod in ["Simple", "Ingresos", "Costos"]:
                st.latex(rf"Call = {spot_ajustado:.2f}({Nd1:.4f}) - {K_opt:.2f}e^{{-{r_opt:.4f} \times {T_opt:g}}}({Nd2:.4f})")
                st.latex(rf"Call = {(spot_ajustado*Nd1):.4f} - {desc_strike:.4f}({Nd2:.4f}) = {call_price:.4f}")
            else:
                st.write("*Se aplican los ajustes correspondientes al Subyacente en la fórmula general.*")
            st.success(f"**Call: ${call_price:.4f}  |  Put: ${put_price:.4f}**")

        with st.expander("Ver Letras Griegas (Sensibilidades)"):
            delta_c, delta_p, gamma, vega, theta_c, theta_p, rho_c, rho_p = engine.griegas_bsm(
                modelo_cod, S_opt, K_opt, T_opt, r_opt, sigma_opt, extra_val)
            g1, g2, g3 = st.columns(3)
            with g1:
                st.markdown("**Posición Call**")
                st.write(f"$\Delta$: {delta_c:.4f}")
                st.write(f"$\Theta$ (día): {theta_c:.4f}")
                st.write(f"$\\rho$: {rho_c:.4f}")
            with g2:
                st.markdown("**Posición Put**")
                st.write(f"$\Delta$: {delta_p:.4f}")
                st.write(f"$\Theta$ (día): {theta_p:.4f}")
                st.write(f"$\\rho$: {rho_p:.4f}")
            with g3:
                st.markdown("**Compartidas**")
                st.write(f"$\Gamma$: {gamma:.4f}")
                st.write(f"$\\nu$: {vega:.4f}")

    # =========================================================
    # MÉTODO 2: BINOMIAL (CRR)
    # =========================================================
    else:
        import plotly.graph_objects as go
        
        st.info(" **Modelo de Árbol Binomial (Cox-Ross-Rubinstein)**. Permite valuar el ejercicio anticipado (Estilo Americano).")
        
        c_binom1, c_binom2 = st.columns(2)
        pasos = c_binom1.slider("Número de Pasos en el árbol ($n$)", min_value=2, max_value=10, value=4)
        q_binom = c_binom1.number_input("Tasa de Dividendos / Retorno ($q$) %", min_value=0.0, value=0.0, step=0.1) / 100
        
        es_americana = c_binom2.checkbox("Valuar como Opción Americana (Ejercicio Anticipado)", value=True)
        tipo_opcion_arbol = c_binom2.radio("Graficar el árbol para:", ["Call", "Put"], horizontal=True)
        
        precio_call, arbol_call = engine.binomial_tree(S_opt, K_opt, T_opt, r_opt, sigma_opt, pasos, q_binom, 'call', es_americana)
        precio_put, arbol_put = engine.binomial_tree(S_opt, K_opt, T_opt, r_opt, sigma_opt, pasos, q_binom, 'put', es_americana)
        
        if precio_call is None:
            st.error("Los parámetros introducidos rompen la estabilidad del árbol CRR (probabilidad fuera de [0,1]). Ajusta los pasos o la volatilidad.")
        else:
            col_res_call, col_res_put = st.columns(2)
            estilo = 'Americana' if es_americana else 'Europea'
            with col_res_call:
                st.markdown(f"<div style='background-color:#E8F5E9; padding:15px; border-radius:10px; border-left: 5px solid #2E7D32;'>"
                            f"<h3 style='color:#2E7D32; margin:0;'>Call {estilo}: ${precio_call:,.4f}</h3></div>", unsafe_allow_html=True)
            with col_res_put:
                st.markdown(f"<div style='background-color:#FFEBEE; padding:15px; border-radius:10px; border-left: 5px solid #C62828;'>"
                            f"<h3 style='color:#C62828; margin:0;'>Put {estilo}: ${precio_put:,.4f}</h3></div>", unsafe_allow_html=True)

            with st.expander("Ver Parámetros Clave del Árbol (CRR)"):
                st.info("**Cálculo de factores base (Cox-Ross-Rubinstein):**")
                dt = T_opt / pasos
                u = np.exp(sigma_opt * np.sqrt(dt))
                d = 1 / u
                p_prob = (np.exp((r_opt - q_binom) * dt) - d) / (u - d)
                
                st.latex(rf"\Delta t = \frac{{T}}{{n}} = \frac{{{T_opt:g}}}{{{pasos:g}}} = {dt:.4f}")
                st.latex(rf"u = e^{{\sigma \sqrt{{\Delta t}}}} = e^{{{sigma_opt:.4f} \times \sqrt{{{dt:.4f}}}}} = {u:.4f} \quad \text{{ (Factor de Alza) }}")
                st.latex(rf"d = \frac{{1}}{{u}} = {d:.4f} \quad \text{{ (Factor de Baja) }}")
                st.latex(rf"p = \frac{{e^{{(r-q)\Delta t}} - d}}{{u - d}} = \frac{{e^{{({r_opt:.4f}-{q_binom:.4f}){dt:.4f}}} - {d:.4f}}}{{{u:.4f} - {d:.4f}}} = {p_prob:.4f}")
                
                st.caption(f"Cada paso adelante, el activo puede subir a S*{u:.4f} o bajar a S*{d:.4f}. La probabilidad neutral al riesgo de que suba es del {p_prob*100:.2f}%.")

            st.write("---")
            st.markdown(f"### Visualización del Árbol Binomial ($n={pasos}$)")
            
            S_tree = arbol_call[0]
            V_tree_plot = arbol_call[1] if tipo_opcion_arbol == "Call" else arbol_put[1]
            
            x_nodes, y_nodes, text_nodes = [], [], []
            for i in range(pasos + 1):
                for j in range(i + 1):
                    x_nodes.append(i)
                    y_nodes.append(S_tree[i][j])
                    text_nodes.append(f"S: {S_tree[i][j]:.1f}<br>V: {V_tree_plot[i][j]:.2f}")

            edge_x, edge_y = [], []
            for i in range(pasos):
                for j in range(i + 1):
                    edge_x += [i, i+1, None]; edge_y += [S_tree[i][j], S_tree[i+1][j], None]
                    edge_x += [i, i+1, None]; edge_y += [S_tree[i][j], S_tree[i+1][j+1], None]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(color='#cbd5e1', width=1.5), hoverinfo='none'))
            fig.add_trace(go.Scatter(x=x_nodes, y=y_nodes, mode='markers+text', 
                                     text=text_nodes if pasos <= 10 else None, 
                                     textposition="top center", 
                                     marker=dict(size=10, color='#1E3A8A'), hovertemplate="%{text}<extra></extra>"))

            fig.update_layout(xaxis_title="Paso temporal (t)", yaxis_title="Precio del Subyacente (Spot)", 
                              showlegend=False, template="plotly_white", margin=dict(l=20, r=20, t=20, b=20), height=500)
            
            st.plotly_chart(fig, use_container_width=True)
            st.caption("Los nodos muestran el precio del subyacente (S) y el valor de la prima (V) en ese instante.")
# =============================================================================
# 10. FORMULARIO 
# =============================================================================
elif opcion == "10. Formulario":
    st.markdown('<div class="section-header">Formulario Oficial de Matemáticas Financieras</div>', unsafe_allow_html=True)
    
    st.write("Explora las fórmulas por categoría. Al final de cada pestaña encontrarás un botón para descargar únicamente el formulario de esa sección en formato HTML interactivo.")
    
    # Función auxiliar para generar la plantilla HTML con soporte para tablas
    def generar_html_formulario(titulo, contenido_cuerpo):
        return f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>{titulo}</title>
            <script>
            MathJax = {{
              tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']]
              }}
            }};
            </script>
            <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
            <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; max-width: 1000px; margin: 0 auto; padding: 20px; color: #333; }}
                h1 {{ text-align: center; color: #1E3A8A; border-bottom: 2px solid #1E3A8A; padding-bottom: 10px; }}
                h2 {{ color: #2563EB; margin-top: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 15px; margin-bottom: 20px; font-size: 0.95em; }}
                th, td {{ border: 1px solid #CBD5E1; padding: 12px; text-align: left; vertical-align: middle; }}
                th {{ background-color: #F8FAFC; color: #0F172A; font-weight: bold; }}
                td:nth-child(2) {{ text-align: center; background-color: #ffffff; }}
                .footer {{ text-align: center; margin-top: 50px; font-size: 0.8em; color: #64748B; }}
            </style>
        </head>
        <body>
            <h1>{titulo}</h1>
            {contenido_cuerpo}
            <div class="footer">Generado automáticamente por la Calculadora Actuarial. ¡Mucho éxito!</div>
        </body>
        </html>
        """

    tab_mat_fin, tab_acc_bonos, tab_derivados = st.tabs([
        "Matemáticas Financieras", "Acciones y Bonos", "Derivados Financieros"
    ])
    
    # ---------------------------------------------------------
    # TAB 1: MATEMÁTICAS FINANCIERAS
    # ---------------------------------------------------------
    with tab_mat_fin:
        st.subheader("1. Tasas de Interés")
        st.markdown(r"""
| Concepto | Fórmula | Para qué se usa |
| :--- | :---: | :--- |
| **Triple igualdad** | $1 + i = \left(1 + \frac{i^{(m)}}{m}\right)^m = e^\delta$ | Relaciona y demuestra la equivalencia entre las tasas efectiva, nominal e instantánea. |
| **Tasa Efectiva Anual ($i$)** | $i = \left(1 + \frac{i^{(m)}}{m}\right)^m - 1$ | Calcula el rendimiento real anual a partir de una tasa nominal capitalizable $m$ veces al año. |
| **Tasa Instantánea ($\delta$)** | $\delta = m \ln\left(1 + \frac{i^{(m)}}{m}\right)$ | Calcula la fuerza de interés o tasa de capitalización continua. |
| **Instantánea a Efectiva ($i$)** | $i = e^\delta - 1$ | Convierte una tasa de capitalización continua a una tasa efectiva anual. |
| **Instantánea a Nominal ($i^{(m)}$)** | $i^{(m)} = m \left(e^{\delta/m} - 1\right)$ | Convierte una tasa continua a una tasa nominal anual. |
| **Nominal a Nominal ($i^{(p)}$)** | $i^{(p)} = \left(1 + \frac{i^{(m)}}{m}\right)^{\frac{m}{p}} - 1$ | Transforma una tasa nominal con $m$ capitalizaciones a otra equivalente con $p$ capitalizaciones. |
        """)

        st.subheader("2. Valor del Dinero en el Tiempo")
        st.markdown(r"""
| Concepto | Fórmula | Para qué se usa |
| :--- | :---: | :--- |
| **Valor Futuro (Efectiva)** | $VF = C_0 (1+i)^n$ | Calcula el monto acumulado de un capital inicial con tasa efectiva anual. |
| **Valor Futuro (Nominal)** | $VF = C_0 \left(1+\frac{i^{(m)}}{m}\right)^{nm}$ | Calcula el monto acumulado usando una tasa nominal capitalizable periódicamente. |
| **Valor Futuro (Instantánea)** | $VF = C_0 e^{\delta n}$ | Calcula el monto acumulado bajo un esquema de capitalización continua. |
| **Valor Presente (Efectiva)** | $VP = C_n (1+i)^{-n}$ | Descuenta un flujo futuro para hallar su valor actual con tasa efectiva. |
| **Valor Presente (Nominal)** | $VP = C_n \left(1+\frac{i^{(m)}}{m}\right)^{-nm}$ | Descuenta un flujo futuro usando una tasa nominal periódica. |
| **Valor Presente (Instantánea)**| $VP = C_n e^{-\delta n}$ | Descuenta un flujo futuro bajo capitalización continua. |
| **Número de Periodos ($n$)** | $n = \frac{\ln(C_n/C_0)}{\ln(1+i)}$ | Determina el tiempo exacto necesario para que un capital alcance un valor futuro. |
| **Tasa de Rendimiento ($i$)** | $i = \left(\frac{C_n}{C_0}\right)^{\frac{1}{n}} - 1$ | Calcula la tasa de interés implícita de una inversión a un solo pago. |
        """)

        st.subheader("3. Valor Futuro de Rentas ($VF$)")
        st.markdown(r"""
| Concepto | Fórmula | Para qué se usa |
| :--- | :---: | :--- |
| **Vencidas (Periódicas)** | $VF = R \cdot s_{\overline{nm}\|i_m} = R \left[ \frac{\left(1+\frac{i^{(m)}}{m}\right)^{nm} - 1}{\frac{i^{(m)}}{m}} \right]$ | Monto acumulado por depósitos fijos al *final* de cada periodo. |
| **Anticipadas (Periódicas)** | $VF = R \cdot \ddot{s}_{\overline{nm}\|i_m} = R \left[ \dots \right] \left(1+\frac{i^{(m)}}{m}\right)$ | Monto acumulado por depósitos fijos al *inicio* de cada periodo. |
| **Vencidas pagaderas $p$ veces** | $VF = R \cdot s_{\overline{np}\|i_p} = R \left[ \frac{\left(1+\frac{i^{(p)}}{p}\right)^{np} - 1}{\frac{i^{(p)}}{p}} \right]$ | Cuando la frecuencia de los pagos difiere de la capitalización original. |
| **Continuas (Instantánea $\delta$)** | $VF = \bar{R} \cdot \bar{s}_{\overline{n}\|\delta} = \bar{R} \left[ \frac{e^{\delta n} - 1}{\delta} \right]$ | Acumulación de un flujo de caja continuo (dinero ingresando sin pausa). |
| **Continuas (Efectiva $i$)** | $VF = \bar{R} \cdot \bar{s}_{\overline{n}\|i} = \bar{R} \left[ \frac{(1+i)^n - 1}{\ln(1+i)} \right]$ | Acumulación de un flujo continuo expresado con tasa efectiva anual. |
| **Crecientes Geométricas ($i_m \neq q_m$)**| $VF = R_1 \left[ \frac{(1+i_m)^{nm} - (1+q_m)^{nm}}{i_m - q_m} \right]$ | Acumulación de pagos que crecen a una tasa porcentual constante $q_m$. |
| **Crecientes Geométricas ($i_m = q_m$)** | $VF = nm \cdot R_1 (1+i_m)^{nm-1}$ | Caso especial donde la tasa de crecimiento iguala a la tasa de interés. |
| **Crecientes Aritméticas** | $VF = R_1 \left[ \frac{(1+i_m)^{nm} - 1}{i_m} \right] + \frac{G}{i_m} \left[ \frac{(1+i_m)^{nm} - 1}{i_m} - nm \right]$ | Acumulación de pagos que crecen sumando una cantidad monetaria fija $G$. |
        """)

        st.subheader("4. Valor Presente de Rentas ($VP$)")
        st.markdown(r"""
| Concepto | Fórmula | Para qué se usa |
| :--- | :---: | :--- |
| **Vencidas (Periódicas)** | $VP = R \cdot a_{\overline{nm}\|i_m} = R \left[ \frac{1 - \left(1+\frac{i^{(m)}}{m}\right)^{-nm}}{\frac{i^{(m)}}{m}} \right]$ | Valor actual de pagos fijos realizados al *final* de cada periodo (ej. préstamos). |
| **Anticipadas (Periódicas)** | $VP = R \cdot \ddot{a}_{\overline{nm}\|i_m} = R \left[ \dots \right] \left(1+\frac{i^{(m)}}{m}\right)$ | Valor actual de pagos fijos realizados al *inicio* de cada periodo (ej. rentas). |
| **Perpetuas** | $VP = R \cdot a_{\overline{\infty}\|i_m} = \frac{R}{\frac{i^{(m)}}{m}}$ | Valor actual de un pago fijo que se recibirá para siempre. |
| **Vencidas pagaderas $p$ veces** | $VP = R \cdot a_{\overline{np}\|i_p} = R \left[ \frac{1 - \left(1+\frac{i^{(p)}}{p}\right)^{-np}}{\frac{i^{(p)}}{p}} \right]$ | Cuando la frecuencia de pago difiere de la frecuencia de capitalización. |
| **Continuas (Instantánea $\delta$)** | $VP = \bar{R} \cdot \bar{a}_{\overline{n}\|\delta} = \bar{R} \left[ \frac{1 - e^{-\delta n}}{\delta} \right]$ | Valor actual de un flujo de caja ininterrumpido a tasa continua. |
| **Continuas (Efectiva $i$)** | $VP = \bar{R} \cdot \bar{a}_{\overline{n}\|i} = \bar{R} \left[ \frac{1 - (1+i)^{-n}}{\ln(1+i)} \right]$ | Valor actual de un flujo continuo expresado con tasa efectiva. |
| **Crecientes Geométricas ($i_m \neq q_m$)**| $VP = R_1 \left[ \frac{1 - \left( \frac{1+q_m}{1+i_m} \right)^{nm}}{i_m - q_m} \right]$ | Valor actual de pagos crecientes porcentualmente (escalonados). |
| **Crecientes Geométricas ($i_m = q_m$)** | $VP = \frac{nm \cdot R_1}{1+i_m}$ | Caso especial del gradiente geométrico donde $i_m = q_m$. |
| **Crecientes Aritméticas** | $VP = R_1 \left[ \frac{1 - (1+i_m)^{-nm}}{i_m} \right] + \frac{G}{i_m} \left[ \dots \right]$ | Valor actual de una serie de pagos que se incrementan en monto fijo $G$. |
        """)

        st.subheader("5. Número de Periodos ($nm$) y Amortización")
        st.markdown(r"""
| Concepto | Fórmula | Para qué se usa |
| :--- | :---: | :--- |
| **Periodos ($nm$) desde $VF$** | $nm = \frac{\ln\left(\frac{VF \cdot i_m}{R} + 1\right)}{\ln(1+i_m)}$ | Tiempo requerido para alcanzar una meta de ahorro $VF$ mediante pagos de $R$. |
| **Periodos ($nm$) desde $VP$** | $nm = \frac{-\ln\left(1 - \frac{VP \cdot i_m}{R}\right)}{\ln(1+i_m)}$ | Tiempo requerido para liquidar un préstamo $VP$ pagando cuotas de $R$. |
| **Pago Fijo ($R$) (Efectiva)**| $R = VP \left[ \frac{i_m}{1 - \left(1+i_m\right)^{-nm}} \right]$ | Calcula la mensualidad o cuota fija periódica para amortizar un préstamo. |
| **Pago Fijo ($R$) (Nominal)** | $R = VP \left[ \frac{\frac{i^{(m)}}{m}}{1 - \left(1+\frac{i^{(m)}}{m}\right)^{-nm}} \right]$ | Calcula la cuota de amortización usando directamente la tasa nominal. |
| **Préstamo ($VP$) (Efectiva)**| $VP = R \left[ \frac{1 - \left(1+i_m\right)^{-nm}}{i_m} \right]$ | Estima el monto máximo de crédito que se puede obtener pagando una cuota $R$. |
        """)

        # HTML Matemáticas Financieras
        html_mat_fin = generar_html_formulario("Formulario: Matemáticas Financieras", r"""
        <h2>1. Tasas de Interés</h2>
        <table>
            <tr><th>Concepto</th><th>Fórmula</th><th>Uso</th></tr>
            <tr><td>Triple Igualdad</td><td>$$1 + i = \left(1 + \frac{i^{(m)}}{m}\right)^m = e^\delta$$</td><td>Relación de tasas.</td></tr>
            <tr><td>Efectiva Anual ($i$)</td><td>$$i = \left(1 + \frac{i^{(m)}}{m}\right)^m - 1$$</td><td>Nominal a Efectiva.</td></tr>
            <tr><td>Instantánea ($\delta$)</td><td>$$\delta = m \ln\left(1 + \frac{i^{(m)}}{m}\right)$$</td><td>Nominal a Continua.</td></tr>
            <tr><td>Efectiva desde $\delta$</td><td>$$i = e^\delta - 1$$</td><td>Continua a Efectiva.</td></tr>
            <tr><td>Nominal desde $\delta$</td><td>$$i^{(m)} = m \left(e^{\delta/m} - 1\right)$$</td><td>Continua a Nominal.</td></tr>
            <tr><td>Nominal a Nominal</td><td>$$i^{(p)} = \left(1 + \frac{i^{(m)}}{m}\right)^{\frac{m}{p}} - 1$$</td><td>Cambio de capitalización.</td></tr>
        </table>

        <h2>2. Valor del Dinero en el Tiempo (TVM)</h2>
        <table>
            <tr><th>Concepto</th><th>Fórmula</th><th>Uso</th></tr>
            <tr><td>Valor Futuro (Efectiva / Nominal / Inst.)</td><td>$$VF = C_0 (1+i)^n \quad|\quad VF = C_0 \left(1+\frac{i^{(m)}}{m}\right)^{nm} \quad|\quad VF = C_0 e^{\delta n}$$</td><td>Monto acumulado.</td></tr>
            <tr><td>Valor Presente (Efectiva / Nominal / Inst.)</td><td>$$VP = C_n (1+i)^{-n} \quad|\quad VP = C_n \left(1+\frac{i^{(m)}}{m}\right)^{-nm} \quad|\quad VP = C_n e^{-\delta n}$$</td><td>Descuento de capital.</td></tr>
            <tr><td>Periodos ($n$) y Tasa ($i$)</td><td>$$n = \frac{\ln(C_n/C_0)}{\ln(1+i)} \quad|\quad i = \left(\frac{C_n}{C_0}\right)^{\frac{1}{n}} - 1$$</td><td>Tiempo y rendimiento.</td></tr>
        </table>

        <h2>3. Rentas, Anualidades y Amortización</h2>
        <table>
            <tr><th>Concepto</th><th>Fórmula</th><th>Uso</th></tr>
            <tr><td>$VF$ Rentas Vencidas</td><td>$$VF = R \left[ \frac{\left(1+\frac{i^{(m)}}{m}\right)^{nm} - 1}{\frac{i^{(m)}}{m}} \right]$$</td><td>Acumulación periódica.</td></tr>
            <tr><td>$VP$ Rentas Vencidas</td><td>$$VP = R \left[ \frac{1 - \left(1+\frac{i^{(m)}}{m}\right)^{-nm}}{\frac{i^{(m)}}{m}} \right]$$</td><td>Valor actual flujos fijos.</td></tr>
            <tr><td>$VF$ y $VP$ Rentas Continuas</td><td>$$VF = \bar{R} \left[ \frac{e^{\delta n} - 1}{\delta} \right] \quad|\quad VP = \bar{R} \left[ \frac{1 - e^{-\delta n}}{\delta} \right]$$</td><td>Flujos ininterrumpidos.</td></tr>
            <tr>
                <td>Rentas Crec. Geométricas ($i_m \neq q_m$)</td>
                <td>
                    $$VF = R_1 \left[ \frac{(1+i_m)^{nm} - (1+q_m)^{nm}}{i_m - q_m} \right]$$<br>
                    $$VP = R_1 \left[ \frac{1 - \left( \frac{1+q_m}{1+i_m} \right)^{nm}}{i_m - q_m} \right]$$
                </td>
                <td>Crecimiento porcentual constante ($q_m$).</td>
            </tr>
            <tr>
                <td>Rentas Crec. Geométricas ($i_m = q_m$)</td>
                <td>
                    $$VF = nm \cdot R_1 (1+i_m)^{nm-1}$$<br>
                    $$VP = \frac{nm \cdot R_1}{1+i_m}$$
                </td>
                <td>Caso especial: tasa interés = tasa crecimiento.</td>
            </tr>
            <tr>
                <td>Rentas Crec. Aritméticas</td>
                <td>
                    $$VF = R_1 \left[ \frac{(1+i_m)^{nm} - 1}{i_m} \right] + \frac{G}{i_m} \left[ \frac{(1+i_m)^{nm} - 1}{i_m} - nm \right]$$<br>
                    $$VP = R_1 \left[ \frac{1 - (1+i_m)^{-nm}}{i_m} \right] + \frac{G}{i_m} \left[ \frac{1 - (1+i_m)^{-nm}}{i_m} - nm(1+i_m)^{-nm} \right]$$
                </td>
                <td>Crecimiento en monto fijo ($G$).</td>
            </tr>
            <tr><td>Amortización: Pago $R$ y Capital $VP$</td><td>$$R = VP \left[ \frac{i_m}{1 - \left(1+i_m\right)^{-nm}} \right] \quad|\quad VP = R \left[ \frac{1 - \left(1+i_m\right)^{-nm}}{i_m} \right]$$</td><td>Cálculo de cuotas y préstamos.</td></tr>
        </table>
        """)
        st.write("---")
        st.download_button("Descargar Formulario: Matemáticas Financieras (HTML)", data=html_mat_fin, file_name="Form_MatFin.html", mime="text/html")

    # ---------------------------------------------------------
    # TAB 2: ACCIONES Y BONOS
    # ---------------------------------------------------------
    with tab_acc_bonos:
        st.subheader("1. Valuación de Bonos")
        st.markdown(r"""
| Concepto | Fórmula | Para qué se usa |
| :--- | :---: | :--- |
| **Precio del Bono (Notación)** | $P = Fr \cdot a_{\overline{nm}\|i_m} + C(1+i_m)^{-nm}$ | Valuación teórica de un bono sumando el VP de los cupones y el principal. |
| **Precio del Bono (Efectiva)** | $P = Fr \left[ \frac{1 - \left(1+i_m\right)^{-nm}}{i_m} \right] + C(1+i_m)^{-nm}$ | Valuación usando la tasa de rendimiento efectiva del mercado ($i_m$). |
| **Precio del Bono (Nominal)** | $P = Fr \left[ \frac{1 - \left(1+\frac{i^{(m)}}{m}\right)^{-nm}}{\frac{i^{(m)}}{m}} \right] + C(1+\frac{i^{(m)}}{m})^{-nm}$ | Valuación usando directamente la tasa nominal cotizada en el mercado. |
| **Yield to Maturity (YTM)** | $P_{mercado} = Fr \left[ \frac{1 - (1+i_m)^{-nm}}{i_m} \right] + C(1+i_m)^{-nm}$ | Ecuación para despejar la tasa de rendimiento $i_m$ iterativamente a partir del precio. |
        """)

        st.subheader("2. Valuación de Acciones")
        st.markdown(r"""
| Concepto | Fórmula | Para qué se usa |
| :--- | :---: | :--- |
| **Precio Acción (Gordon)** | $P_0 = \frac{D_1}{k - g}$ | Modelo de Gordon-Shapiro para valuar el precio teórico con dividendos crecientes a perpetuidad. |
| **Rendimiento Requerido ($k$)**| $k = \frac{D_1}{P_0} + g$ | Despeje para calcular el costo de capital accionario o rendimiento exigido. |
| **Precio / Utilidad (P/E)** | $P_0 = \text{UPA} \times \left( \frac{P}{E} \right)$ | Valuación relativa usando el múltiplo Precio-Beneficio y la Utilidad por Acción. |
| **Precio / Ventas (P/S)** | $P_0 = \text{VPA} \times \left( \frac{P}{S} \right)$ | Valuación relativa usando el múltiplo Precio-Ventas. |
| **EV / EBITDA** | $EV = \text{EBITDA} \times \left( \frac{EV}{\text{EBITDA}} \right)$ | Valuación de la empresa completa (Enterprise Value) mediante EBITDA operativo. |
| **Precio / Valor Libros (P/B)**| $P_0 = \text{VLA} \times \left( \frac{P}{B} \right)$ | Valuación usando el múltiplo Precio-Valor en Libros. |
        """)

        # HTML Acciones y Bonos
        html_acc_bonos = generar_html_formulario("Formulario: Acciones y Bonos", r"""
        <h2>1. Valuación de Bonos</h2>
        <table>
            <tr><th>Concepto</th><th>Fórmula</th><th>Uso</th></tr>
            <tr><td>Precio del Bono</td><td>$$P = Fr \left[ \frac{1 - \left(1+i_m\right)^{-nm}}{i_m} \right] + C(1+i_m)^{-nm}$$</td><td>Precio teórico ($VP$ Cupones + $VP$ Principal).</td></tr>
            <tr><td>YTM (Tasa al vencimiento)</td><td>$$P_{mercado} = Fr \left[ \frac{1 - (1+i_m)^{-nm}}{i_m} \right] + C(1+i_m)^{-nm}$$</td><td>Tasa intrínseca a partir del precio mercado.</td></tr>
        </table>
        <h2>2. Valuación de Acciones</h2>
        <table>
            <tr><th>Concepto</th><th>Fórmula</th><th>Uso</th></tr>
            <tr><td>Gordon-Shapiro ($P_0$ y $k$)</td><td>$$P_0 = \frac{D_1}{k - g} \quad|\quad k = \frac{D_1}{P_0} + g$$</td><td>Valuación por dividendos crecientes.</td></tr>
            <tr><td>Múltiplos Financieros</td><td>$$P_0 = \text{UPA} \times \left( \frac{P}{E} \right) \quad|\quad EV = \text{EBITDA} \times \left( \frac{EV}{\text{EBITDA}} \right)$$</td><td>Valuación relativa de mercado.</td></tr>
        </table>
        """)
        st.write("---")
        st.download_button("Descargar Formulario: Acciones y Bonos (HTML)", data=html_acc_bonos, file_name="Form_AccionesBonos.html", mime="text/html")

    # ---------------------------------------------------------
    # TAB 3: DERIVADOS FINANCIEROS
    # ---------------------------------------------------------
    with tab_derivados:
        st.subheader("1. Forwards (Precio Teórico $F$ y Valuación $f$)")
        st.markdown(r"""
| Concepto | Fórmula | Para qué se usa |
| :--- | :---: | :--- |
| **Activo Simple (Continua)** | $F = S_0 e^{rT}$ | Precio de entrega teórico $F$ sin ingresos ni costos de almacenaje (capitalización continua). |
| **Activo Simple (Discreta)** | $F = S_0 (1+r)^T$ | Precio teórico $F$ con capitalización discreta anual. |
| **Con Ingresos (Continua)** | $F = (S_0 - I) e^{rT}$ | Ajuste del precio descontando el valor presente de los ingresos $I$ (dividendos). |
| **Con Ingresos (Discreta)** | $F = (S_0 - I) (1 + r)^T$ | Ajuste con ingresos en capitalización discreta. |
| **Con Costos (Continua)** | $F = (S_0 + U) e^{rT}$ | Ajuste sumando el valor presente de los costos de almacenaje $U$. |
| **Con Costos (Discreta)** | $F = (S_0 + U) (1 + r)^T$ | Ajuste sumando los costos bajo tasas discretas. |
| **Divisas / Retorno (\delta)** | $F = S_0 e^{(r - \delta)T}$ | Precio forward para monedas extranjeras (con tasa $\delta$ o $r_f$) o activos con *yield* continuo. |
| **Divisas (Discreta)** | $F = S_0 \frac{(1+r)^T}{(1+\delta)^T}$ | Paridad de tasas de interés cubierta en versión discreta. |
| **VP Ingresos Periódicos (Cont)**| $I = \sum_{k=1}^{T \cdot m} D e^{-r (\frac{k}{m})}$ | VP de dividendos $D$ constantes en múltiples periodos (continua). |
| **VP Ingresos Irregulares (Disc)**| $I = \sum_{j=1}^{n} \frac{D_j}{(1+r)^{t_j}}$ | VP de dividendos $D_j$ en fechas específicas (discreta). |
| **VP Costos Periódicos (Cont)** | $U = \sum_{k=1}^{T \cdot m} C e^{-r (\frac{k}{m})}$ | VP de costos de almacenaje $C$ fijos y periódicos. |
| **VP Costos Irregulares (Disc)**| $U = \sum_{j=1}^{n} \frac{C_j}{(1+r)^{t_j}}$ | VP de costos irregulares $C_j$ descontados (discreta). |
| **Valor Contrato Larga (Cont)**| $f = S_t e^{-\delta T} - K e^{-r T}$ | Valor de mercado $f$ en el tiempo $t$ para quien compró el forward (continua). |
| **Valor Contrato Corta (Cont)**| $f = K e^{-r T} - S_t e^{-\delta T}$ | Valor de mercado $f$ para quien vendió el forward (continua). |
| **Valor Contrato Larga (Disc)**| $f = \frac{S_t}{(1+\delta)^T} - \frac{K}{(1+r)^T}$ | Valor del contrato largo en tiempo $t$ (discreta). |
| **Valor Contrato Corta (Disc)**| $f = \frac{K}{(1+r)^T} - \frac{S_t}{(1+\delta)^T}$ | Valor del contrato corto en tiempo $t$ (discreta). |
        """)

        st.subheader("2. Opciones Europeas (Black-Scholes-Merton)")
        st.markdown(r"""
| Concepto | Fórmula | Para qué se usa |
| :--- | :---: | :--- |
| **1. Simple Call ($c$)** | $c = S_0 N(d_1) - K e^{-rT} N(d_2)$ | Prima teórica de una opción de compra sobre activo sin dividendos. |
| **1. Simple Put ($p$)** | $p = K e^{-rT} N(-d_2) - S_0 N(-d_1)$ | Prima teórica de una opción de venta sobre activo sin dividendos. |
| **1. Parámetro Simple ($d_1$)**| $d_1 = \frac{\ln(S_0 / K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}$ | Factor de probabilidad $d_1$ base. |
| **2. Con Ingresos Call ($c$)** | $c = (S_0 - D) N(d_1) - K e^{-rT} N(d_2)$ | Prima call descontando monto discreto de dividendos $D$. |
| **2. Con Ingresos Put ($p$)** | $p = K e^{-rT} N(-d_2) - (S_0 - D) N(-d_1)$ | Prima put descontando dividendos. |
| **2. Parámetro Ingresos ($d_1$)**| $d_1 = \frac{\ln((S_0 - D)/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}$ | Factor ajustado reduciendo el precio *Spot* en $D$. |
| **3. Con Costos Call ($c$)** | $c = (S_0 + U) N(d_1) - K e^{-rT} N(d_2)$ | Prima call agregando costos de almacenaje $U$ al subyacente. |
| **3. Con Costos Put ($p$)** | $p = K e^{-rT} N(-d_2) - (S_0 + U) N(-d_1)$ | Prima put agregando costos. |
| **3. Parámetro Costos ($d_1$)**| $d_1 = \frac{\ln((S_0 + U)/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}$ | Factor ajustado inflando el precio *Spot* en $U$. |
| **4. Yield Continuo Call ($c$)**| $c = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)$ | Prima call con rendimiento constante continuo $q$ (ej. índices). |
| **4. Yield Continuo Put ($p$)**| $p = K e^{-rT} N(-d_2) - S_0 e^{-qT} N(-d_1)$ | Prima put con yield $q$. |
| **4. Parámetro Yield ($d_1$)** | $d_1 = \frac{\ln(S_0 / K) + (r - q + \sigma^2/2)T}{\sigma \sqrt{T}}$ | Factor ajustado por la diferencia de tasas $r - q$. |
| **5. Monedas Call ($c$)** | $c = S_0 e^{-r_f T} N(d_1) - K e^{-rT} N(d_2)$ | Prima call sobre divisas usando tasa libre de riesgo foránea $r_f$. |
| **5. Monedas Put ($p$)** | $p = K e^{-rT} N(-d_2) - S_0 e^{-r_f T} N(-d_1)$ | Prima put sobre divisas (Garman-Kohlhagen). |
| **5. Parámetro Monedas ($d_1$)**| $d_1 = \frac{\ln(S_0 / K) + (r - r_f + \sigma^2/2)T}{\sigma \sqrt{T}}$ | Factor ajustado por diferencial cambiario. |
| **6. Futuros Call ($c$)** | $c = e^{-rT} [ F_0 N(d_1) - K N(d_2) ]$ | Prima call sobre un contrato de futuros $F_0$ (Modelo de Black). |
| **6. Futuros Put ($p$)** | $p = e^{-rT} [ K N(-d_2) - F_0 N(-d_1) ]$ | Prima put sobre futuros. |
| **6. Parámetro Futuros ($d_1$)**| $d_1 = \frac{\ln(F_0 / K) + (\sigma^2/2)T}{\sigma \sqrt{T}}$ | Factor $d_1$ adaptado para precio forward en lugar de Spot. |
| **Fórmula común ($d_2$)** | $d_2 = d_1 - \sigma \sqrt{T}$ | Parámetro complementario $d_2$ aplicable a **todos** los modelos BSM. |
        """)

        # HTML Derivados
        html_derivados = generar_html_formulario("Formulario: Derivados Financieros", r"""
        <h2>1. Forwards</h2>
        <table>
            <tr><th>Concepto</th><th>Fórmula Continua</th><th>Fórmula Discreta</th></tr>
            <tr><td>Precio Teórico ($F$) Base</td><td>$$F = S_0 e^{rT}$$</td><td>$$F = S_0 (1+r)^T$$</td></tr>
            <tr><td>$F$ Con Ingresos (D)</td><td>$$F = (S_0 - I) e^{rT}$$</td><td>$$F = (S_0 - I) (1 + r)^T$$</td></tr>
            <tr><td>$F$ Con Costos (U)</td><td>$$F = (S_0 + U) e^{rT}$$</td><td>$$F = (S_0 + U) (1 + r)^T$$</td></tr>
            <tr><td>$F$ Divisas/Yield</td><td>$$F = S_0 e^{(r - \delta)T}$$</td><td>$$F = S_0 \frac{(1+r)^T}{(1+\delta)^T}$$</td></tr>
            <tr><td>Valor Contrato Larga ($f$)</td><td>$$f = S_t e^{-\delta T} - K e^{-r T}$$</td><td>$$f = \frac{S_t}{(1+\delta)^T} - \frac{K}{(1+r)^T}$$</td></tr>
            <tr><td>Valor Contrato Corta ($f$)</td><td>$$f = K e^{-r T} - S_t e^{-\delta T}$$</td><td>$$f = \frac{K}{(1+r)^T} - \frac{S_t}{(1+\delta)^T}$$</td></tr>
        </table>
        
        <h2>2. Opciones Europeas (Black-Scholes-Merton)</h2>
        <table>
            <tr><th>Modelo</th><th>Call ($c$) y Put ($p$)</th><th>Parámetro $d_1$</th></tr>
            <tr>
                <td>1. Simple</td>
                <td>$$c = S_0 N(d_1) - K e^{-rT} N(d_2)$$ $$p = K e^{-rT} N(-d_2) - S_0 N(-d_1)$$</td>
                <td>$$d_1 = \frac{\ln(S_0 / K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}$$</td>
            </tr>
            <tr>
                <td>2. Ingresos (D)</td>
                <td>$$c = (S_0 - D) N(d_1) - K e^{-rT} N(d_2)$$ $$p = K e^{-rT} N(-d_2) - (S_0 - D) N(-d_1)$$</td>
                <td>$$d_1 = \frac{\ln((S_0 - D)/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}$$</td>
            </tr>
            <tr>
                <td>3. Costos (U)</td>
                <td>$$c = (S_0 + U) N(d_1) - K e^{-rT} N(d_2)$$ $$p = K e^{-rT} N(-d_2) - (S_0 + U) N(-d_1)$$</td>
                <td>$$d_1 = \frac{\ln((S_0 + U)/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}$$</td>
            </tr>
            <tr>
                <td>4. Yield ($q$)</td>
                <td>$$c = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)$$ $$p = K e^{-rT} N(-d_2) - S_0 e^{-qT} N(-d_1)$$</td>
                <td>$$d_1 = \frac{\ln(S_0 / K) + (r - q + \sigma^2/2)T}{\sigma \sqrt{T}}$$</td>
            </tr>
            <tr>
                <td>5. Divisas ($r_f$)</td>
                <td>$$c = S_0 e^{-r_f T} N(d_1) - K e^{-rT} N(d_2)$$ $$p = K e^{-rT} N(-d_2) - S_0 e^{-r_f T} N(-d_1)$$</td>
                <td>$$d_1 = \frac{\ln(S_0 / K) + (r - r_f + \sigma^2/2)T}{\sigma \sqrt{T}}$$</td>
            </tr>
            <tr>
                <td>6. Futuros ($F_0$)</td>
                <td>$$c = e^{-rT} [ F_0 N(d_1) - K N(d_2) ]$$ $$p = e^{-rT} [ K N(-d_2) - F_0 N(-d_1) ]$$</td>
                <td>$$d_1 = \frac{\ln(F_0 / K) + (\sigma^2/2)T}{\sigma \sqrt{T}}$$</td>
            </tr>
        </table>
        <p style="text-align:center;"><b>Nota:</b> Para todos los modelos, $$d_2 = d_1 - \sigma \sqrt{T}$$</p>
        """)
        st.write("---")
        st.download_button("Descargar Formulario: Derivados (HTML)", data=html_derivados, file_name="Form_Derivados.html", mime="text/html")
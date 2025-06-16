import pandas as pd

# Datos
sueldo_mensual = 1_423_500
ingreso_quincenal = sueldo_mensual / 2
gasto_mercado = 250_000
gasto_pasajes_semanal = 7_400
gasto_pasajes_quincenal = gasto_pasajes_semanal * 2

# Crear DataFrame quincenal
datos_quincenales = [
    {"Concepto": "Ingreso quincenal", "Monto": ingreso_quincenal},
    {"Concepto": "Gasto en mercado", "Monto": -gasto_mercado},
    {"Concepto": "Gasto en pasajes (15 días)", "Monto": -gasto_pasajes_quincenal}
]

df_quincenal = pd.DataFrame(datos_quincenales)

# Calcular total quincenal restante
total_quincenal = df_quincenal["Monto"].sum()
df_quincenal.loc[len(df_quincenal)] = ["Total restante quincenal", total_quincenal]

# Mostrar resultados de forma intuitiva
print(f"\n💼 Sueldo mensual: ${sueldo_mensual:,.2f}\n")
print("📊 Análisis de ingresos y gastos por quincena:\n")

for _, row in df_quincenal.iterrows():
    concepto = row["Concepto"]
    monto = row["Monto"]
    if concepto == "Total restante quincenal":
        print(f"➡️  {concepto}: ${monto:,.2f}")
    else:
        signo = "+" if monto > 0 else "-"
        print(f"{concepto}: {signo}${abs(monto):,.2f}")

print("\n💡 El 'Total restante quincenal' es el dinero que te queda después de restar los gastos principales de tu ingreso quincenal.\n")
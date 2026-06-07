import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt
from graph_model import Graph
from data_supplier import suppliers, weights, normalize

st.set_page_config(page_title="DSS Pemilihan Supplier", layout="wide")
st.title("📦 DSS Pemilihan Supplier Berbasis Graph")

# Sidebar untuk bobot kriteria
st.sidebar.header("⚙️ Atur Bobot Kriteria")
w_price = st.sidebar.slider("Bobot Harga (lebih murah lebih baik)", 0.0, 1.0, 0.4)
w_distance = st.sidebar.slider("Bobot Jarak (lebih dekat lebih baik)", 0.0, 1.0, 0.2)
w_quality = st.sidebar.slider("Bobot Kualitas (lebih tinggi lebih baik)", 0.0, 1.0, 0.3)
w_delivery = st.sidebar.slider("Bobot Waktu Kirim (lebih cepat lebih baik)", 0.0, 1.0, 0.1)

weights = {
    "price": w_price,
    "distance": w_distance,
    "quality": w_quality,
    "delivery_time": w_delivery
}

# Normalisasi data
df_suppliers = pd.DataFrame(suppliers).T
min_price, max_price = df_suppliers["price"].min(), df_suppliers["price"].max()
min_dist, max_dist = df_suppliers["distance"].min(), df_suppliers["distance"].max()
min_quality, max_quality = df_suppliers["quality"].min(), df_suppliers["quality"].max()
min_delivery, max_delivery = df_suppliers["delivery_time"].min(), df_suppliers["delivery_time"].max()

df_suppliers["norm_price"] = df_suppliers["price"].apply(lambda x: normalize(x, min_price, max_price, is_cost=True))
df_suppliers["norm_distance"] = df_suppliers["distance"].apply(lambda x: normalize(x, min_dist, max_dist, is_cost=True))
df_suppliers["norm_quality"] = df_suppliers["quality"].apply(lambda x: normalize(x, min_quality, max_quality, is_cost=False))
df_suppliers["norm_delivery"] = df_suppliers["delivery_time"].apply(lambda x: normalize(x, min_delivery, max_delivery, is_cost=True))

# Hitung skor akhir
df_suppliers["total_score"] = (
    weights["price"] * df_suppliers["norm_price"] +
    weights["distance"] * df_suppliers["norm_distance"] +
    weights["quality"] * df_suppliers["norm_quality"] +
    weights["delivery_time"] * df_suppliers["norm_delivery"]
)

# Tampilkan data supplier
st.subheader("📊 Data Supplier & Skor Akhir")
st.dataframe(df_suppliers[["price", "distance", "quality", "delivery_time", "total_score"]])

# Rekomendasi supplier terbaik
best_supplier = df_suppliers["total_score"].idxmax()
st.success(f"🏆 **Supplier Terbaik:** {best_supplier} dengan skor {df_suppliers.loc[best_supplier, 'total_score']:.2f}")

# ---- Graph untuk jalur dari pabrik ke supplier ----
st.subheader("🗺️ Graph Jalur Distribusi (Pabrik ke Supplier)")

# Buat graph dengan bobot (misal jarak)
G = Graph()
factory = "Pabrik Pusat"
for sup in suppliers.keys():
    G.add_edge(factory, sup, suppliers[sup]["distance"])

# Visualisasi dengan networkx + matplotlib
g_nx = nx.Graph()
g_nx.add_node(factory)
for sup in suppliers.keys():
    g_nx.add_node(sup)
    g_nx.add_edge(factory, sup, weight=suppliers[sup]["distance"])

pos = nx.spring_layout(g_nx, seed=42)
fig, ax = plt.subplots(figsize=(8, 6))
nx.draw_networkx_nodes(g_nx, pos, node_size=700, node_color="lightblue", ax=ax)
nx.draw_networkx_labels(g_nx, pos, font_size=10, ax=ax)
nx.draw_networkx_edges(g_nx, pos, width=2, alpha=0.6, edge_color="gray", ax=ax)
edge_labels = {(factory, sup): suppliers[sup]["distance"] for sup in suppliers.keys()}
nx.draw_networkx_edge_labels(g_nx, pos, edge_labels=edge_labels, font_size=8, ax=ax)
plt.title("Jalur Pabrik ke Supplier (Bobot = Jarak)")
st.pyplot(fig)

# Pencarian jalur terbaik dengan Dijkstra
st.subheader("🛣️ Pencarian Jalur Terbaik (Dijkstra)")
selected_supplier = st.selectbox("Pilih Supplier Tujuan", list(suppliers.keys()))
distance, path = G.dijkstra(factory, selected_supplier)
if distance != float('inf'):
    st.success(f"Jalur terbaik dari {factory} ke {selected_supplier}: {' → '.join(path)}")
    st.info(f"Total jarak: {distance} km")
else:
    st.error("Tidak ada jalur")

# Analisis keputusan
st.subheader("📈 Analisis Keputusan")
st.write("""
**Metode yang digunakan:** Multi-Criteria Decision Making (MCDM) dengan normalisasi min-max + bobot preferensi.
**Algoritma Graph:** Dijkstra untuk pencarian rute terpendek.
**Keunggulan:** Mempertimbangkan harga, jarak, kualitas, dan waktu kirim secara simultan.
""")
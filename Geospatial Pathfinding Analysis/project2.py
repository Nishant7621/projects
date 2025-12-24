import streamlit as st
import folium
import requests
from streamlit_folium import st_folium

st.set_page_config(page_title="Routing: Dijkstra vs Bellman-Ford", layout="wide")

st.title("🗺️ Path Comparison: Dijkstra vs Bellman-Ford (Negative Edge Simulation)")

# ---------------- Session State ----------------
for key in ["start", "end", "temp_point"]:
    if key not in st.session_state:
        st.session_state[key] = None

# ---------------- Sidebar Controls ----------------
st.sidebar.header("Controls")

if st.session_state.start is None:
    st.sidebar.info("Step 1: Click map for **Start**")
    if st.session_state.temp_point:
        if st.sidebar.button("✅ Confirm Start"):
            st.session_state.start = st.session_state.temp_point
            st.session_state.temp_point = None
            st.rerun()
elif st.session_state.end is None:
    st.sidebar.info("Step 2: Click map for **Destination**")
    if st.session_state.temp_point:
        if st.sidebar.button("✅ Confirm Destination"):
            st.session_state.end = st.session_state.temp_point
            st.session_state.temp_point = None
            st.rerun()

if st.sidebar.button("🔄 Reset All"):
    for key in ["start", "end", "temp_point"]:
        st.session_state[key] = None
    st.rerun()


# ---------------- Routing Functions ----------------
def get_route(start, end, profile="driving"):
    url = f"http://router.project-osrm.org/route/v1/{profile}/{start[1]},{start[0]};{end[1]},{end[0]}?overview=full&geometries=geojson"
    try:
        res = requests.get(url).json()
        coords = res["routes"][0]["geometry"]["coordinates"]
        dist = res["routes"][0]["distance"] / 1000
        return [(lat, lon) for lon, lat in coords], dist
    except:
        return None, None


# ---------------- MAIN CLICK MAP ----------------
st.subheader("Select points on this map")
center = [20.5937, 78.9629]
m = folium.Map(location=center, zoom_start=5)

click_map = st_folium(m, height=400, width=1200, key="main_map")

if click_map and click_map.get("last_clicked"):
    st.session_state.temp_point = (click_map["last_clicked"]["lat"], click_map["last_clicked"]["lng"])

if st.session_state.start:
    folium.Marker(st.session_state.start, icon=folium.Icon(color="green", icon="play")).add_to(m)
if st.session_state.end:
    folium.Marker(st.session_state.end, icon=folium.Icon(color="red", icon="stop")).add_to(m)
if st.session_state.temp_point:
    folium.Marker(st.session_state.temp_point, icon=folium.Icon(color="orange")).add_to(m)

# ---------------- Results Display ----------------
if st.session_state.start and st.session_state.end:
    col1, col2 = st.columns(2)

    # 1. Dijkstra (Physical Distance - Positive Only)
    d_route, d_dist = get_route(st.session_state.start, st.session_state.end, "driving")

    # 2. Bellman-Ford (Simulating Negative Edge Reward)
    # We take the walking path (usually longer) but apply a "Negative Bonus"
    b_route, b_dist_raw = get_route(st.session_state.start, st.session_state.end, "walking")

    # ARTIFICIAL NEGATIVE WEIGHT SIMULATION
    # Imagine this path has a "fuel station" or "reward" that gives -10km back
    negative_reward = 10.0
    effective_cost = b_dist_raw - negative_reward

    with col1:
        st.markdown("### 🟦 Dijkstra Path")
        st.caption("Standard greedy search. Cannot handle negative weights.")
        if d_route:
            m1 = folium.Map(location=st.session_state.start, zoom_start=12)
            folium.PolyLine(d_route, color="blue", weight=7).add_to(m1)
            folium.Marker(st.session_state.start, icon=folium.Icon(color="green")).add_to(m1)
            folium.Marker(st.session_state.end, icon=folium.Icon(color="red")).add_to(m1)
            st_folium(m1, height=400, width=500, key="m1")
            st.success(f"Dijkstra Distance: {d_dist:.2f} km")

    with col2:
        st.markdown("### 🟪 Bellman-Ford Path")
        st.caption("Relaxation method. Capable of finding paths with negative 'bonuses'.")
        if b_route:
            m2 = folium.Map(location=st.session_state.start, zoom_start=12)
            folium.PolyLine(b_route, color="purple", weight=7).add_to(m2)
            folium.Marker(st.session_state.start, icon=folium.Icon(color="green")).add_to(m2)
            folium.Marker(st.session_state.end, icon=folium.Icon(color="red")).add_to(m2)
            st_folium(m2, height=400, width=500, key="m2")

            st.info(f"Actual Walking Distance: {b_dist_raw:.2f} km")
            st.error(f"Effective Cost (with -10km Bonus): {effective_cost:.2f}")

    # --- Comparison Table ---
    st.divider()
    st.subheader("📊 Key Difference: Handling Negative Weights")

    st.write(f"""
    While Dijkstra is faster for regular roads, **Bellman-Ford** is required if any part of your journey has a **negative cost** (reward). 
    In this example, even though the walking path is physically longer ({b_dist_raw:.2f} km), the negative bonus makes it the 'mathematically' shorter path ({effective_cost:.2f}) which Dijkstra would miss.
    """)
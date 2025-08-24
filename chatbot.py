import streamlit as st
import base64

# ======================
# Page Config
# ======================
st.set_page_config(
    page_title="SmartRecycle Trash4mersBot 4.0",
    page_icon="♻",
    layout="centered"
)

# ======================
# Function to set local GIF as background
# ======================
def set_gif_background(gif_file):
    with open(gif_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    css = f"""
    <style>
    /* Import Pixel Arcade Font */
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    /* Apply font globally */
    html, body, [class*="st"], div, p, span, button, input, select, textarea {{
        font-family: 'Press Start 2P', cursive !important;
    }}

    .stApp {{
        background: url("data:image/gif;base64,{b64}") center/cover no-repeat fixed !important;
        background-color: black !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call function with new uploaded gif
set_gif_background("bgneww.gif")

# ======================
# --- Rewards dictionary (Only Paper, Plastic, E-Waste) ---
# ======================
goodies = {
    "plastic": {
        200: {"prize": "Eco Sunglasses", "tagline": "🕶 From bottles to shaders – run your style in green mode!"},
        400: {"prize": "Recycled Backpack", "tagline": "🎒 Carry data… I mean, trash → compiled into a bag!"},
        600: {"prize": "Upcycled Sneakers", "tagline": "👟 Walk.exe launched successfully → powered by plastic."},
        1000: {"prize": "Plastic Brick Kit", "tagline": "🧱 Debugging Earth’s trash, one brick at a time!"}
    },
    "paper": {
        200: {"prize": "Recycled Notebook", "tagline": "📒 Logs.txt but IRL – write your future sustainably."},
        400: {"prize": "Seed Paper Cards", "tagline": "🌱 Println('Plant Mode ON') → Cards that grow!"},
        600: {"prize": "Origami Kit", "tagline": "📄 Folding algorithms into real-world fun!"},
        1000: {"prize": "Eco Sketchpad", "tagline": "🎨 Designing Version 2.0 of Earth on recycled paper."}
    },
    "ewaste": {
        200: {"prize": "USB Drive", "tagline": "💾 Save files, save Earth → recycled memory edition!"},
        400: {"prize": "Solar Charger", "tagline": "🔋 Charging... via Sun API ☀ instead of landfills."},
        600: {"prize": "Eco Headphones", "tagline": "🎧 Stream beats on hardware patched from trash."},
        1000: {"prize": "Upcycled Desk Lamp", "tagline": "💡 Debugging darkness with recycled circuits."}
    }
}

# ======================
# Title + Subheading
# ======================
st.markdown('<div style="font-size:54px; text-align:center; color:#00FF00; text-shadow:0 0 6px #00FF00;">♻ SmartRecycle EcoBot 3000 🚀</div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:16px; text-align:center; color:#00FF00;">🖥 Transforming Trash → Cash XP ⚡ | Recycle Trashes, Level Up Like a pro gamer 🎮 🌍</div>', unsafe_allow_html=True)

# ======================
# Dropdown menu
# ======================
menu = st.selectbox(
    "Select...",
    [
        "⚡ QuickStart.exe (Tutorial)",
        "📜 Rules.config (Cheat Sheet)",
        "🕹 Controls.map (How to Play)",
        "🎯 Rewards.db (Prize Vault)",
        "💾 XP_Counter_3000.run"
    ]
)

# ======================
# Submenu Content
# ======================
if menu == "⚡ QuickStart.exe (Tutorial)":
    st.info("""
    🚀 Welcome to SmartRecycle EcoBot 3000!
    
    - Step 1: Collect waste around you.
    - Step 2: Upload images before and after cleaning.
    - Step 3: Earn XP & eco-coins 🌍.
    - Step 4: Redeem rewards in the Prize Vault.
    """)

elif menu == "📜 Rules.config (Cheat Sheet)":
    st.warning("""
    ⚠ Rules of the Game
    
    - Upload clear photos before & after cleanup.
    - Same location check ✅.
    - Time gap required ⏱.
    - No fake/AI images ❌.
    """)

elif menu == "🕹 Controls.map (How to Play)":
    st.success("""
    🎮 Controls
    
    - Use your camera as your controller.
    - Trash = Enemy 👾.
    - Recycling = Power-up ⚡.
    - Cleanup missions = Levels to beat 🏆.
    """)

elif menu == "🎯 Rewards.db (Prize Vault)":
    st.subheader("🎯 Rewards.db (Prize Vault)")
    waste_type = st.selectbox("🗂 Select Waste Type:", ["Plastic", "Paper", "E-Waste"])
    points = st.selectbox("💾 Select XP Level:", [200, 400, 600, 1000])
    
    if st.button("🔍 Query Reward"):
        waste_key = waste_type.lower().replace("-", "")
        reward_info = goodies.get(waste_key, {}).get(points)
        if reward_info:
            st.success(f"🎉 Loot Unlocked: *{reward_info['prize']}*\n\n{reward_info['tagline']}")
            st.image("bgneww.gif", width=200)
            st.balloons()
        else:
            st.error("❌ RewardNotFoundException: Try leveling up more XP!")

elif menu == "💾 XP_Counter_3000.run":
    st.subheader("💾 XP_Counter_3000.run")
    st.write("Enter collected waste → Get XP 💾")

    # User input
    paper_qty = st.number_input("📄 Paper Waste:", min_value=0, step=1)
    plastic_qty = st.number_input("🧴 Plastic Waste:", min_value=0, step=1)
    ewaste_qty = st.number_input("💻 E-Waste:", min_value=0, step=1)

    if st.button("⚡ Compute XP"):
        total_points = (paper_qty * 10) + (plastic_qty * 20) + (ewaste_qty * 30)
        st.info(f"🏆 Total XP: {total_points}")
        
        st.write("🎁 *Available Loot Tables:*")
        for waste, rewards in goodies.items():
            st.write(f"🔹 {waste.capitalize()} Rewards:")
            for r_points, info in rewards.items():
                if total_points >= r_points:
                    st.success(f"- {r_points} XP → {info['prize']} ({info['tagline']})")

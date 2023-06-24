import streamlit as st

def main():
    st.set_page_config(page_title="HIGH_pressure", layout="wide")
    st.title("Food Options for Hyperlipidemia")
    

    with st.container():
        st.subheader("Heart-Healthy Fats")
        st.subheader("These fats can help lower cholesterol levels.")
        st.write("- Avocado:Rich in monounsaturated fats, avocados can help lower cholesterol levels and promote heart health.")
        st.write("- Olive oil:Contains monounsaturated fats and antioxidants that support cardiovascular health.")
        st.write("- Nuts (almonds, walnuts):High in unsaturated fats, nuts can help reduce LDL (bad) cholesterol and support heart health.")
        st.write("- Seeds (flaxseeds, chia seeds): These seeds are a good source of omega-3 fatty acids and fiber, which can contribute to healthy cholesterol levels.")

    with st.container():
        st.subheader("High-Fiber Foods")
        st.subheader("Fiber helps lower cholesterol levels.")
        st.write("- Whole grains (oats, brown rice):These grains are rich in soluble fiber, which aids in lowering cholesterol levels.")
        st.write("- Legumes (beans, lentils):High in soluble fiber and plant-based protein, legumes can help lower cholesterol and promote heart health")
        st.write("- Fruits (apples, berries):Fruits contain soluble fiber and antioxidants that can help lower cholesterol levels.")
        st.write("- Vegetables (broccoli, spinach):These vegetables are high in fiber and plant compounds that support healthy cholesterol levels")

    with st.container():
        st.subheader("Lean Protein Sources")
        st.subheader("These proteins are low in saturated fat.")
        st.write("- Skinless poultry (chicken, turkey):: These lean proteins provide essential nutrients without excessive saturated fat.")
        st.write("- Fish (salmon, trout):Rich in omega-3 fatty acids, fish can help lower triglycerides and promote heart health.")
        st.write("- Tofu: A plant-based protein source that is low in saturated fat and can be a part of a heart-healthy diet.")
        st.write("- Greek yogurt: High in protein and lower in saturated fat compared to some other dairy products.")

    # Add more containers for the remaining food options...

if __name__ == "__main__":
    main()

import streamlit as st
import webbrowser as wb

def main():
    
    st.set_page_config(page_title="CHOLESTROL", layout="wide")
    st.title("Food Options for High Cholesterol")
    

    with st.container():
        st.subheader("Fruits and Vegetables")
        st.subheader("Fruits and vegetables are rich in fiber and antioxidants, which can help lower cholesterol levels.")
        st.write("- Apples:High in soluble fiber, apples can help lower cholesterol levels and promote heart health.")
        st.write("- Berries:Rich in antioxidants and fiber, berries can contribute to reducing bad cholesterol.")
        st.write("- Broccoli: Packed with antioxidants and fiber, broccoli is a nutritious vegetable that supports heart health")
        st.write("- Spinach:A leafy green vegetable, spinach is low in cholesterol and a good source of fiber and nutrients.")

    with st.container():
        st.subheader("Whole Grains")
        st.subheader("Whole grains are high in fiber and can help reduce bad cholesterol.")
        st.write("- Oats:Rich in soluble fiber, oats can help lower LDL (bad) cholesterol levels.")
        st.write("- Whole wheat bread:Compared to refined grains, whole wheat bread contains more fiber and nutrients beneficial for heart health.")
        st.write("- Brown rice: A whole grain alternative to white rice, brown rice contains fiber and compounds that can support healthy cholesterol levels.For Healthy Fats:")

    with st.container():
        st.subheader("Healthy Fats")
        st.subheader("Healthy fats can help raise good cholesterol levels and lower bad cholesterol.")
        st.write("- Avocado:A source of monounsaturated fats, avocados can help increase HDL (good) cholesterol and lower LDL cholesterol.")
        st.write("- Nuts (almonds, walnuts):Nuts are high in monounsaturated fats, fiber, and plant sterols that promote heart health.")
        st.write("- Olive oil: Rich in monounsaturated fats and antioxidants, olive oil is a healthy alternative to saturated fats.")

    # Add more containers for the remaining food options...

if __name__ == "__main__":
    main()

import streamlit as st

def main():
    st.set_page_config(page_title="Diabetes", layout="wide")
    st.title("Food Choices for Diabetes")

    with st.container():
        st.subheader("Whole Grains")
        st.write("Whole grains are a good source of fiber and can help regulate blood sugar levels.")
        st.write("- Brown rice: A nutritious whole grain that helps regulate blood sugar levels.")
        st.write("- Quinoa: A high-protein grain with a low glycemic index, suitable for managing diabetes.")
        st.write("- Whole wheat bread:Provides fiber and nutrients compared to refined white bread.")

    with st.container():
        st.subheader("Non-Starchy Vegetables")
        st.write("Non-starchy vegetables are low in carbohydrates and calories.")
        st.write("- Broccoli:A nutrient-dense vegetable that is low in carbohydrates and calories")
        st.write("- Spinach:Packed with vitamins and minerals, spinach is a low-carb option for diabetes.")
        st.write("- Bell peppers:Colorful and crunchy, bell peppers are low in carbs and a good source of vitamins.")

    with st.container():
        st.subheader("Lean Proteins")
        st.write("Lean proteins provide essential nutrients without excessive fat or carbohydrates.")
        st.write("- Chicken breast:A lean source of protein that is low in fat and carbohydrates..")
        st.write("- Turkey: A lean meat option with essential nutrients and low carbohydrate content.")
        st.write("- Fish:Rich in omega-3 fatty acids and protein, fish is a heart-healthy choice for diabetes.")
        st.write("- Tofu:A plant-based protein source that is low in carbs and can be included in a diabetic diet.")

    # Add more containers for the remaining food options...

if __name__ == "__main__":
    main()

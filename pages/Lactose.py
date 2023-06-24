import streamlit as st
import webbrowser as wb
def main():
    st.set_page_config(page_title="lACTOSE", layout="wide")
    st.title("[Food Options for Lactose Intolerant]")
    

    with st.container():
        st.subheader("Dairy Alternatives")
        st.write(":red[These are non-dairy alternatives to traditional dairy products.]")
        st.write("- Almond milk: A plant-based milk alternative made from almonds, suitable for lactose-intolerant individuals.")
        st.write("- Soy milk:A popular non-dairy milk made from soybeans, often fortified with nutrients like calcium.")
        st.write("- Coconut milk:A creamy milk alternative derived from coconuts, commonly used in cooking and baking.")
        st.write("- Rice milk: A thin and mild-tasting milk made from rice, suitable for those with lactose intolerance.")

    with st.container():
        st.subheader("Non-Dairy Calcium Sources")
        st.write("These foods are good sources of calcium for those avoiding dairy.")
        st.write("- Leafy greens (kale, broccoli): These vegetables are rich in calcium and provide a lactose-free option for meeting calcium needs.")
        st.write("- Tofu: A versatile soy-based product that contains calcium and can be used in various dishes.")
        st.write("- Sesame seeds: These small seeds are a good source of calcium and can be added to meals or used as a topping.")
        st.write("- Fortified orange juice  :  Some brands of orange juice are fortified with calcium, offering a non-dairy source of this essential mineral.")

    with st.container():
        st.subheader("Plant-Based Protein Sources")
        st.write("These foods provide protein without lactose.")
        st.write("- Lentils:  These legumes are high in protein and can be included in various recipes, such as soups, salads, and stews.")
        st.write("- Quinoa:  A complete protein grain that is gluten-free and can be used as a base for salads or served as a side dish.")
        st.write("- Chickpeas:  Versatile legumes that are high in protein and can be used to make hummus, salads, or roasted snacks.")
        st.write("- Hemp seeds: Nutrient-dense seeds that provide plant-based protein and can be sprinkled on salads, smoothies, or yogurt.")

    # Add more containers for the remaining food options...

if __name__ == "__main__":
    main()

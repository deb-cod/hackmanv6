import streamlit as st
import numpy as np
from PIL import Image
import streamlit.components.v1 as components


def optimize_diet(food_macronutrients, desired_macronutrients, epochs, lr):
    weights = np.zeros(shape=food_macronutrients.shape[0])

    for _ in range(epochs):
        resulted_macros = (food_macronutrients.T * weights).T
        resulted_macros = np.sum(resulted_macros, axis=0)
        f_err = desired_macronutrients - resulted_macros

        for i in range(weights.shape[0]):
            w_grad = (-2 * food_macronutrients[i].dot(f_err).sum() / food_macronutrients.shape[0])
            weights[i] -= lr * w_grad
            weights[weights < 0] = 0
            weights[3] = 0.35 if weights[3] < 0.35 else 1.55 if weights[3] > 1.55 else weights[3]

    weights *= 100
    weights = [int(x) for x in weights]
    resulted_macros = [int(x) for x in resulted_macros]

    return weights, resulted_macros, np.mean(f_err)


def main():
    st.set_page_config(page_title="DIET", page_icon="🍉", layout="wide")
    
    page_bg_img = '''
        <style>
        body {
            background-image: url("background.jpg");
            background-size: cover;
        }
        </style>
        '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title("Welcome to the Diet Chart😋🥗🍚")
    st.markdown(
        """
        <style>
        .title {
            color: #46CA00;
        }
        .result {
            color: #0000FF;
        }
        .text {
            color: #FFFF00;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
  

    # Define the macronutrients for the foods
    non_veg_food_macronutrients = np.array(
        [[7.81,6.86,11],  #Milk
        [2.7, 28, 1],     # rice
        [2.4, 20, 2.2],   # potatoes
        [15, 56, 2],      # oats
        [29, 1, 3],       # chicken meat
        [15, 2, 6],       # pork meat
        [6, 0, 5],        # eggs. 1 egg = 45
        [1, 5, 3]]        # bread
    )

    

    veg_food_macronutrients = np.array(
        [[7.81,6.86,11],  #Milk
        [2.7, 28, 1],     # rice
        [2.4, 20, 2.2],   # potatoes
        [15, 56, 2],      # oats
        [10, 6, 14],      # tofu
        [9, 40, 3],       # lentils
        [20, 49, 27],     # almonds
        [1, 5, 3]]        # bread
    )
    # User input for medical conditions
    st.subheader(":blue[Medical Conditions (Select Them and if u have 😷⚕️)]")
    st.write(":blue[Specify any medical conditions you have:]")

    medical_conditions = []
    if st.checkbox("Diabetes"):
        medical_conditions.append("Diabetes")
    if st.checkbox("Hyperlipdemia"):
        medical_conditions.append("Hyperlipdemia(High Blood  Pressure )")
    if st.checkbox("Cholesterol"):
        medical_conditions.append("Cholesterol ")
    if st.checkbox("lactose intolerant"):
        medical_conditions.append("lactose intolerant")
    
    # Add more conditions as needed

    # Display selected medical conditions
    if medical_conditions:
        st.write("Selected Medical Conditions:")
        for condition in medical_conditions:
            st.write(condition)
    else:
        st.write("No medical conditions selected.") 
    with st.container():
        st.write("-----")
        st.title("User Details")
        column_1, column_2 = st.columns(2)
        with column_1:
            st.header("Enter the Body ")
            height = st.number_input("Height:", value=0.0, format="%.2f")
            Body_Weight=st.number_input("Body_Weight:",value=0.0,format="%.2f")
            Age=st.number_input("Age:",value=0)
            hsq= height**2
            if hsq != 0:
                BMI = Body_Weight / hsq
            else:
                BMI = 0  # or assign any other appropriate value
        
            st.write("BMI of The User:",BMI)
        with column_2:
            st.header("Enter Your Desired Macronutrients")
            carb_input = st.number_input("Carbohydrates", value=0)
            protein_input = st.number_input("Protein", value=0)
            fat_input = st.number_input("Fat", value=0)
            desired_macronutrients = np.array([carb_input, protein_input, fat_input])
        
    if BMI<18.5:
        st.write("Your BMI is UnderWeight",BMI)
    elif BMI>=18.5 or BMI<=25:
        st.write("Your BMI is Normal👍🏼",BMI)
    elif BMI>=25 or BMI <=30:
        st.write("Your BMI is Overweight ",BMI)
    else:
        st.write("Your BMI is Obese",BMI)
    # User input for dietary preference
    dietary_preference = st.selectbox("Select your dietary preference", ("Non-vegetarian", "Vegetarian"))

    if dietary_preference == "Non-vegetarian":
        food_macronutrients = non_veg_food_macronutrients
    elif dietary_preference == "Vegetarian":
        food_macronutrients = veg_food_macronutrients
    else:
        pass    


    

    # Set hyperparameters
    epochs = 1000
    lr = 0.001
    
    
    # Optimize the diet
    weights, resulted_macros, mean_error = optimize_diet(food_macronutrients, desired_macronutrients, epochs, lr)

    # Display the results
    st.subheader("Diet Optimization Results")
    st.write("Desired macronutrients: ", desired_macronutrients)
    st.write("Resulted macronutrients for the new diet: ", resulted_macros)
    st.write("Mean error: ", mean_error)
    
    

    

    if np.array_equal(food_macronutrients, veg_food_macronutrients):

        food_options = ["Milk","Rice", "Potatoes", "Oats", "tofu", "lentils", "almonds", "Bread"]

        st.subheader("Food Options")
        st.write("Select the food options for your diet:")

        selected_foods = []
        for food in food_options:
            if st.checkbox(food):
                    selected_foods.append(food)
                    
        st.subheader("Macronutrient Foods")
        st.write("Here are the selected macronutrient foods:")

        food_indices = [food_options.index(food) for food in selected_foods]
        selected_food_macronutrients = food_macronutrients[food_indices]
        selected_weights = np.array(weights)[food_indices]

        col1, col2, col3 = st.beta_columns(3)

        for i, food in enumerate(selected_foods):
            if i % 3 == 0:
                col = col1
            elif i % 3 == 1:
                col = col2
            else:
                col = col3

            col.subheader(food)
            img = Image.open(food.lower().replace(" ", "_") + ".jpg")
            col.image(img, caption=food, use_column_width=True)
            col.write(f"{food}: {selected_weights[i]} grams")
    elif np.array_equal(food_macronutrients, non_veg_food_macronutrients):

        food_options = ["Milk","Rice", "Potatoes", "Oats", "Chicken Meat", "Pork Meat", "Eggs", "Bread"]
       

        st.subheader("Food Options")
        st.write("Select the food options for your diet:")

        selected_foods = []
        for  food in food_options:
            if st.checkbox(food):
                    selected_foods.append(food)
                   

        st.subheader("Macronutrient Foods")
        st.write("Here are the selected macronutrient foods:")

        food_indices = [food_options.index(food) for food in selected_foods]
        selected_food_macronutrients = food_macronutrients[food_indices]
        selected_weights = np.array(weights)[food_indices]

        col1, col2, col3 = st.beta_columns(3)

        for i, food in enumerate(selected_foods):
            if i % 3 == 0:
                col = col1
            elif i % 3 == 1:
                col = col2
            else:
                col = col3

            col.subheader(food)
            img = Image.open(food.lower().replace(" ", "_") + ".jpg")
            col.image(img, caption=food, use_column_width=True)
            col.write(f"{food}: {selected_weights[i]} grams")
    else:
        st.write("The Food has not been selected ")



    st.subheader("Learn More")
    st.write("For more detailed information about building muscles and optimizing your diet, you can refer to this article:")
    st.write("[How I Have Used Machine Learning to Build Muscles](https://bogdanandreig.medium.com/how-i-have-used-machine-learning-to-build-muscles-a8aa12334c34)")

    # Add gym symbols for points
    st.subheader("Gym Points")
    st.markdown("You can earn points by going to the gym and performing exercises. Here are some examples:")
    st.write("🏋‍♂  Bench Press: 50 points")

if __name__ == '__main__':
    main()
import streamlit as st
import requests as rq
from streamlit_lottie import st_lottie
import webbrowser as wb

def load_lottieurl(url):
    r= rq.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.set_page_config(page_title="My Webpage",page_icon="✨", layout="wide")
st.sidebar.success("Choose the option: ")

url1 = 'https://virtraa.web.app'

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_il9wfcq9.json")

excercise_1 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_l0u0rf4r.json")
excercise_2 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_bettd34d.json")
excercise_3 = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_x31bhcov.json")
excercise_4 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_mJc8o5.json")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("This is Justice Engineers")
        st.title("This is our Project")

    with right_column:
        st.write(f'''
    <a target="_self" href="https://virtraa.web.app">
        <button>
            Login/Sign Up
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)    


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we are:")
        st.write("#")
        st.write(
            """In today's fast-paced world, staying fit and healthy has become a necessity.
             However, with busy schedules and limited access to gyms, it can be challenging to maintain a consistent workout routine.
               To overcome this challenge, the concept of virtual gym trainers has gained immense popularity. 
               In this context, the use of Artificial Intelligence (AI) in fitness training has emerged as a game-changer. 
               The AI gym trainer utilizes advanced technologies such as Mediapipe, Python, Numpy, and face position tracking to provide personalized workout plans and guidance to individuals.
                 In this article, we will explore how these technologies work together to create an efficient and effective AI gym trainer."""
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

with st.container():
    st.write("-----")
    st.title("Excercises we offer:")
    column_1, column_2, column_3 = st.columns(3)
    with column_1:
        st_lottie(excercise_1, height=200, key="coding1")
        st.subheader("Bicep/Tricep")
        st.write("""The bicep muscle is responsible for flexing the elbow joint and rotating the forearm. To effectively target the biceps, it is important to perform exercises that place the muscle under tension throughout its range of motion.
Bicep curls: Hold a dumbbell in each hand with your palms facing forward. Slowly curl the weights up towards your shoulders, keeping your elbows close to your sides. Pause at the top of the movement before slowly lowering the weights back down.
When performing these exercises, it is important to maintain proper form and control throughout the entire range of motion. To maximize bicep activation, focus on keeping your elbows close to your sides and avoid swinging or using momentum to lift the weights.
Varying the angle of your arms during these exercises can also help target different areas of the biceps. For example, performing curls with your arms slightly angled outwards can place more emphasis on the outer portion of the biceps, while keeping your arms closer to your body can target the inner portion of the muscle.""")
    with column_2:
        st_lottie(excercise_2, height=200, key="coding2")
        st.subheader("Push Up")
        st.write("""To perform a push-up with proper form and angles, follow these steps:
1. Start in a plank position with your hands slightly wider than shoulder-width apart and your feet hip-width apart.
2. Keep your body in a straight line from head to heels, engage your core, and lower your body towards the ground by bending your elbows.
3. Make sure your elbows are at a 45-degree angle from your body and not flared out to the sides.
4. Lower yourself until your chest touches the ground or your arms reach a 90-degree angle.
5. Push yourself back up to the starting position by extending your arms and squeezing your chest and triceps.
6. Repeat for the desired number of reps, making sure to maintain proper form and control throughout the exercise.""") 
    with column_3:
        st_lottie(excercise_3, height=200, key="coding3")
        st.subheader("Dead Lift")
        st.write("""To perform a deadlift with proper form and angles, follow these steps:
1. Stand with your feet shoulder-width apart and the barbell on the floor in front of you.
2. Bend down and grab the barbell with an overhand grip, hands slightly wider than shoulder-width apart.
3. Keep your back straight, chest up, and shoulders back as you lift the barbell off the ground.
4. As you lift, push through your heels and engage your glutes and hamstrings.
5. Keep the barbell close to your body as you stand up, making sure not to round your back or hunch your shoulders.
6. Once you reach a standing position, pause for a moment before slowly lowering the barbell back down to the ground with control.
7. Repeat for the desired number of reps, making sure to maintain proper form and control throughout the exercise.""") 
        
with st.container():
    column_4,column_5 = st.columns(2)
    with column_4:
        st_lottie(excercise_4, height=200, key="coding4")
        st.subheader("Power Lift")
        st.write("""To perform a powerlifting deadlift with proper form and angles, follow these additional steps:
1. Set up with your feet slightly wider than shoulder-width apart and your toes pointed slightly outwards.
2. Position the barbell close to your shins, with the bar over the middle of your foot.
3. Take a deep breath and brace your core before initiating the lift.
4. As you lift the bar, drive your hips forward and keep your shoulders over the bar.
5. At the top of the lift, lock out your hips and knees and squeeze your glutes.
6. Lower the bar back down to the ground by pushing your hips back and bending your knees.
7. Repeat for the desired number of reps, making sure to maintain proper form and control throughout the exercise""")
        
    with column_5:
        st.subheader("Choice of Reps")
        st.write("""The choice of reps provided for an exercise depends on various factors such as the fitness level of the individual, the specific exercise being performed, the goals of the workout, and the overall training program.\n
For beginners, it is generally recommended to start with lower reps, around 5, to ensure proper form and technique before increasing the weight or reps. As the individual progresses and becomes more comfortable with the exercise, they can gradually increase the reps and weight to challenge their muscles.\n
For moderate level individuals, a range of 15 reps is generally recommended to build endurance and muscular strength. This can help improve overall fitness and prepare the individual for more advanced exercises or training programs.\n
For individuals who are more advanced and looking to increase muscle size and strength, higher reps such as 30 may be more appropriate. This can help create more muscle tension and fatigue, leading to greater muscle growth and strength gains.\n
However, it is important to note that these rep ranges are not set in stone and can be adjusted based on the individual's goals, preferences, and limitations. Some individuals may find that they respond better to higher or lower reps, and it's important to listen to your body and adjust accordingly.\n
Ultimately, the choice of reps should be based on the individual's fitness level, goals, and overall training program. It's important to work with a qualified fitness professional to develop a personalized training program that takes into account these factors and helps you achieve your fitness goals safely and effectively.""")


with st.container():
    st.write("---")
    st.subheader("Contacts:")
    column_1, column_2, column_3, column_4 = st.columns(4)
    with column_1:
        st.write("""Debesh Pramanick\n
        pramanickdebesh1412@gmail.com\n
        +91 7022883585""")
    with column_2:
        st.write("""Siddhanth V Jain\n
        siddhanthvjain@gmail.com\n
        +91 8073225370""")
    with column_3:    
        st.write("""Yogesh S Naik\n
        yogeshsnayak3@gmail.com\n
        +91 8123586553""")

import streamlit as st
st.title("TaylorSwift Music Recommender based on your mood :)")
st.text("")
st.write("This website would recommend Taylor Swift songs (from all her albums :) !) based on your mood in a 10-level emotional rank!")

st.text("")
st.subheader("10-level emotional scale")

st.write("    1 -  i hate this world")
st.write("    2 - im gonna cry")
st.write("    3 - Hurting/Melancholic")
st.write("    4 - calm but okay")
st.write("    5 - Peaceful but sad")
st.write(" 6 - Peaceful/gentle")
st.write(" 7 - Cheerful")
st.write(" 8 - Optimistic")
st.write(" 9 - Energetic")
st.write(" 10 - Pumped")

mood = {1: "i hate this world", 2: "im gonna cry", 3: "Hurting/Melancholic", 4: "calm but okay", 5: "Peaceful but sad", 6: "Peaceful" , 7: "Cheerful" ,
                 8: "Optimistic" , 9: "Energetic" , 10: "Pumped"}

st.text("")
selected_mood = st.selectbox("Select or type your mood based on the emotional rank", mood)


st.text("")
st.text("")
st.subheader("Click this button to recommend!")
st.text("")

st.button("Recommend!", type == "primary", icon= "👍")
st.caption("the album - the song")



def music_for_you(selected_mood: int):
        import random
        moods = {1: "i hate this world", 2: "im gonna cry", 3: "Hurting/Melancholic", 4: "calm but okay", 5: "Peaceful but sad", 6: "Peaceful/gentle" , 7: "Cheerful" ,
                 8: "Optimistic" , 9: "Energetic" , 10: "Pumped"}

        if selected_mood == 1:
            options1 = ["TTPD - I Hate it Here", "folklore - the lakes"]
            result1 = random.choice(options1)
            st.markdown(result1)
        if selected_mood == 2:
            options2 = ["folklore - exile","From the Vault - You're Losing Me", "evermore - champagne problems", "evermore - its time to go",
                        "evermore - evermore", "evermore - tolerate it", "evermore - closure", "folklore - my tears ricochet", "TTPD - So Long London",
                        "TTPD - How Did It End?", "Red(Taylor's Version) - All Too Well(10 Minute Version)","TTPD - loml", "Speak Now(Taylor's Version) - Foolish One",
                        "Fearless(Taylor's Version) - You All Over Me" ]
            result2 = random.choice(options2)
            st.markdown(result2)
        if selected_mood == 3:
            options3 = ["TTPD - The Smallest Man Who Ever Lived", "Midnights - Would've Could've Should've", "TTPD - Who's Afraid of Little Old Me?",
                        "TTPD - Peter", "evermore - long story short","folklore - illicit affairs","TTPD - I Can Fix Him(No Really I Can)", "TTPD - The Manuscript",
                        "TTPD - loml", "Midnights - Snow On The Beach", "reputation - New Year's Day", "Red(Taylor's Version) - The Last Time", 
                        "Red(Taylor's Version) - Nothing New", "Speak Now(Taylor's Version) - Last Kiss", "Speak Now(Taylor's Version) - Foolish One",
                        "evermore - champagne problems", "evermore - its time to go", "evermore - evermore", "folklore - exile","From the Vault - You're Losing Me", "evermore - champagne problems", "evermore - its time to go",
                        "evermore - evermore", "evermore - tolerate it", "evermore - closure", "folklore - my tears ricochet", "TTPD - So Long London",
                        "TTPD - How Did It End?", "Red(Taylor's Version) - All Too Well(10 Minute Version)","TTPD - loml", "Fearless(Taylor's Version) - You're Not Sorry",
                        "Fearless(Taylor's Version) - You All Over Me"  ]
            result3 = random.choice(options3)
            st.markdown(result3)
        if selected_mood == 4:
            options4 = ["TTPD - Fortnight", "TTPD - The Tortured Poets Department", "TTPD - imgonnagetyouback", "TTPD - I Look in People's Windows",
                        "TTPD - The Bolter",  "TTPD - I Look In People's Windows", "TTPD - The Prophecy",  "Midnights - Snow On The Beach",
                        "Midnights - Sweet Nothing", "Lover - It's Nice To Have A Friend", "Lover - Lover"  ]
            result4 = random.choice(options4)
            st.markdown(result4)
        if selected_mood == 5:
            options5 = ["folklore - peace","folklore - mirrorball", "folklore - illicit affairs", "evermore - coney island", "TTPD - loml",
                        "folklore - the1", "folklore - marjorie", "TTPD - I Can Fix Him(No Really I Can)", "TTPD - The Manuscript",
                         "Midnights - Snow On The Beach", "Fearless(Taylor's Version) - Breathe", "Fearless(Taylor's Version) - You're Not Sorry",
                         "Fearless(Taylor's Version) - Forever & Always(Piano Version)", "Fearless(Taylor's Version) - You All Over Me", ]
            result5 = random.choice(options5)
            st.markdown(result5)
        if selected_mood == 6:
            options6 = ["folklore - seven","folklore - august", "folklore - cardigan", "folklore - invisible string", "evermore - ivy",
                        "evermore - cowboy like me", "TTPD - Robin", "Red(Taylor's Version) - State of Grace", "Red(Taylor's Version) - State of Grace (Acoustic Version)",
                        "TTPD - Robin",  "Midnights - Snow On The Beach", "Midnights - Sweet Nothing", "Lover - Lover", "Forever & Always(Piano Version)"]
            result6 = random.choice(options6)
            st.markdown(result6)
        if selected_mood == 7:
            options7 = ["Red(Taylor's Version) - Treacherous", "Red(Taylor's Version) - Starlight", "Red(Taylor's Version) - Holy Ground",
                        "Red(Taylor's Version) - Babe", "Red(Taylor's Version) - Red", "Fearless(Taylor's Version) - Forever & Always",
                        "Fearless(Taylor's Version) - The Other Side Of The Door", "Fearless(Taylor's Version) - Today Was A Fairytale",
                        "Fearless(Taylor's Version) - That's When", "Speak Now(Taylor's Version) - Sparks Fly", "TaylorSwift - Mary's Song",
                        "Lover - ME!", "Midnights - Paris", "Lover - You Need To Calm Down", "Lover - Paper Rings", "Lover - I Think He Knows",
                        "Lover - Miss Americana & The Heartbreak Prince", "1989(Taylor's Version) - Welcome To New York", "1989(Taylor's Version) - How You Get The Girl",
                         "Red(Taylor's Version) - The Very First Night", "Fearless(Taylor's Version) - You Belong With Me",
                         "Fearless(Taylor's Version) - Love Story", "Red(Taylor's Version) - Stay Stay Stay"]
            result7 = random.choice(options7)
            st.markdown(result7)
        if selected_mood == 8:
            options8 = ["Fearless(Taylor's Version) - Fearless", "Speak Now(Taylor's Version) - Long Live", "Speak Now(Taylor's Version) - Ours",
            "Lover - ME!", "Midnights - Paris", "Lover - The Man", "reptuation - Getaway Car", "reputation - Gorgeous",
            "Fearless(Taylor's Version) - Love Story", "1989(Taylor's Version) - Welcome To New York" ]
            result8 = random.choice(options8)
            st.markdown(result8)
        if selected_mood == 9:
            options9 = ["Red(Taylor's Version) - Message in a Bottle","Speak Now(Taylor's Version) - Better Than Revenge", "Red(Taylor's Version) - 22",
            "Lover - Cruel Summer", "Lover - The Man", "reputation - Ready For It", "reptuation - Getaway Car", "reputation - Gorgeous",
            "reputation - Don't Blame Me", "reputation - Look What You Made Me Do", "1989(Taylor's Version) - Style", "1989(Taylor's Version) - Shake It Off",]
            result9 = random.choice(options9)
            st.markdown(result9)
        if selected_mood == 10:
            options10 = ["1989(Taylor's Version) - New Romantics", "Red(Taylor's Version) - 22", "reputation - Ready For It", "reputation - Look What You Made Me Do",]
            result10 = random.choice(options10)
            st.markdown(result10)
        else:
            pass
        


if selected_mood == 1:
    st.markdown(music_for_you(1))

if selected_mood == 2:
    st.markdown(music_for_you(2))

if selected_mood == 3:
    st.markdown(music_for_you(3))

if selected_mood == 4:
    st.markdown(music_for_you(4))

if selected_mood == 5:
    st.markdown(music_for_you(5))

if selected_mood == 6:
    st.markdown(music_for_you(6))

if selected_mood == 7:
    st.markdown(music_for_you(7))

if selected_mood == 8:
    st.markdown(music_for_you(8))

if selected_mood == 9:
    st.markdown(music_for_you(9))

if selected_mood == 10:
    st.markdown(music_for_you(10))




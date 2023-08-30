import streamlit as st
import streamlit.components.v1 as components
#import modal
import json
import os

def main():



    st.markdown(
        """
        <style>
       /* The main content area */
        .main .block-container {
            margin-top:25em;
            color : #fff !important;
            background-color: #206579 !important;
        }
        
        /* The background of the entire body */
        body {
           background-color: #f7ae52 !important;
        }

         /* Applying background color to the header */
        header[data-testid="stHeader"] {
        background-color: #f7ae52 !important;
        }

        .stMarkdownContainer {
            margin:15em;
        }
        /* Your identified class from inspect element */
        .css-uf99v8 {
            display: flex;
            flex-direction: column;
            width: 100%;
            overflow: auto;
            align-items: center;
            background-color: #f7ae52 !important;
        }

        /* Making the content and sidebar background completely opaque */
        div.stButton > button:first-child {
            background-color: #f7ae52 !important;

            color : #fff !important;
            border : none;
            
        }
        div[data-baseweb="select"] > div {
            background-color: #206579 ; 
            color : #fff;
           
        }

        h1{
            text-align:center;
            margin-top:1em;
            text-shadow: 1px 1px 2px #444444;
            font-family: sans-serif;
            color : #ffffff;
        }

        h2 {
            padding-top: 1em;
            color : #8ef3ff;
            text-shadow: 2px 2px 2px #444444;
            color : #f7ae52;
            
            
        }

        h3 {
            color : #9c0000
            color: #00deff !important;
        }

        p {
            color : #383838;
            text-shadow : horizontal-shadow vertical-shadow blur color;
        }
        
        /* Remove padding/margin from top element in the main section */
        .main .block-container:first-child {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }

        /* Adjust the image styling */
        stImage img {
            
        
            display: block;
            margin: 0 auto;
            border: 5em ;
            padding-top: 15em;
            
        }
        
        stHeader h2{
            padding: 5em;
        }

        .css-6qob1r.e1fqkh3o3 {
        color: #fff !important;
        background-color: #f7ae52 !important;
        }
        
        .css-6qob1r.eczjsme3{
        background-color: #588391;
        color: #fff !important;
        background-color: #ffe9ce !important;

        }
        

        .sidebar.header{
        color: #383838 !important;
        }
        
        .sidebar.text_input{
            color: #383838 !important;
        }

               
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    

    
    st.title("Welcome to Swami's Pod-igy !")
    st.image('cover2.png', use_column_width=True)
    components.html( "<br><br> ",height=50)


    available_podcast_info = create_dict_from_json_files('.')

    # Left section - Input fields
    st.sidebar.header("Podcast RSS Feeds")

    # Dropdown box
                
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox("**Select Podcast**", options=['Select a podcast']+list(available_podcast_info.keys()))
    
     # User Input box
    st.sidebar.subheader("Add and Process New Podcast Feed")
    url = st.sidebar.text_input("**Link to RSS Feed**")

    process_button = st.sidebar.button("Process Podcast Feed")
    st.sidebar.markdown("**Note**: Podcast processing can take upto 5 mins, please be patient.")
    
    if process_button:

        # Call the function to process the URLs and retrieve podcast guest information
        podcast_info = process_podcast_info(url)

        # Right section - Newsletter content
        st.header("Podcast: "+podcast_info['podcast_details']['podcast_title'])

        # Display the podcast title
        st.subheader("Episode Title")
        st.markdown(
                f"<p style='margin-bottom: 5px;color: #ededed'>{podcast_info['podcast_details']['episode_title']}</p>", unsafe_allow_html=True)


        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])

        with col1:
            # Display the podcast episode summary
            st.subheader("Podcast Episode Summary")
            st.markdown(
                f"<p style='margin-bottom: 5px;color: #ededed'>{podcast_info['podcast_summary']}</p>", unsafe_allow_html=True)
 

        with col2:
            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)
        

        # Display the podcast guest and their details in a side-by-side layout
        col3, col4 = st.columns([3, 7])

        with col3:
            st.subheader("Podcast Guest")
            st.markdown(
                f"<p style='margin-bottom: 5px;color: #ededed'>{podcast_info['podcast_guest']['name']}</p>", unsafe_allow_html=True)

        with col4:
            st.subheader("Podcast Guest Details")
            st.write(podcast_info["podcast_guest"]['summary'])
            

        # Display the five key moments
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(
                f"<p style='margin-bottom: 5px;'>{moment}</p>", unsafe_allow_html=True)
    
    elif selected_podcast in available_podcast_info.keys():

        podcast_info = available_podcast_info[selected_podcast]

        # Right section - Newsletter content
        st.header("Podcast: "+podcast_info['podcast_details']['podcast_title'])

        

        # Display the podcast title
        st.subheader("Episode Title")
        st.markdown(
                f"<p style='margin-bottom: 5px;color: #ededed'>{podcast_info['podcast_details']['episode_title']}</p>", unsafe_allow_html=True)
        #st.write(podcast_info['podcast_details']['episode_title'])

        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])

        with col1:
            # Display the podcast episode summary
            st.subheader("Podcast Episode Summary")
            st.markdown(
                f"<p style='margin-bottom: 5px;color: #ededed'>{podcast_info['podcast_summary']}</p>", unsafe_allow_html=True)
            #st.write(podcast_info['podcast_summary'])

        with col2:
            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)

        # Display the podcast guest and their details in a side-by-side layout
        col3, col4 = st.columns([3, 7])

        with col3:
            st.subheader("Podcast Guest")
            st.markdown(
                f"<p style='margin-bottom: 5px;color: #ededed'>{podcast_info['podcast_guest']['name']}</p>", unsafe_allow_html=True)
            #st.write(podcast_info['podcast_guest']['name'])

        with col4:
            st.subheader("Podcast Guest Details")
            st.markdown(
                f"<p style='margin-bottom: 5px;color: #ededed'>{podcast_info['podcast_guest']['summary']}</p>", unsafe_allow_html=True)
            #st.write(podcast_info["podcast_guest"]['summary'])

        # Display the five key moments
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(
                f"<p style='margin-bottom: 5px;color: #ededed'>{moment}</p>", unsafe_allow_html=True)
   

def create_dict_from_json_files(folder_path):
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    data_dict = {}

    for file_name in json_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            podcast_info = json.load(file)
            podcast_name = podcast_info['podcast_details']['podcast_title']
            # Process the file data as needed
            data_dict[podcast_name] = podcast_info

    return data_dict

def process_podcast_info(url):
    #f = modal.Function.lookup("corise-podcast-project", "process_podcast")
    #output = f.call(url, '/content/podcast/')
    output='Swaminathan'
    return output

if __name__ == '__main__':
    main()


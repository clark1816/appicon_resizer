import streamlit as st 
import cv2
import os

st.title('Free Web App for Creating your own AppIcon')
option = st.sidebar.selectbox('Choose your option', ['Home','Create iOS App Icon', 'iPhone 6.7 Display', 'iPhone 5.5 Display', 'iPhone 5.5 Display', 'iPad Pro 12.9'])
if option == 'Create iOS App Icon':
    picture = st.file_uploader('Upload your picture here', type=['png', 'jpg', 'jpeg'])

    if picture:
        #download picture
        with open(picture.name, 'wb') as f:
            f.write(picture.getbuffer())
            #resize image to 1240x1240
            image = cv2.imread(picture.name)
            print(picture.name)
            image = cv2.resize(image, (1024, 1024))
            cv2.imwrite('image.png', image)
            st.image(image)
            
            st.success('Your image has been successfully uploaded')
            #create a button to download the image
            download = st.download_button('Download image', data=open('image.png', 'rb').read(), file_name='image.png', mime='image/png')
        
                    
    delete = st.button('Delete image')
    if delete:
        #print all the files in current directory 
        for file in os.listdir():
            print(file)
            #if file ends with .jpg .png .jpeg delete it
            if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                os.remove(file)

if option == 'iPhone 6.7 Display':
    picture = st.file_uploader('Upload your picture here', type=['png', 'jpg', 'jpeg'])

    if picture:
        #download picture
        with open(picture.name, 'wb') as f:
            f.write(picture.getbuffer())
            #resize image to 1240x1240
            image = cv2.imread(picture.name)
            print(picture.name)
            image = cv2.resize(image, (1290, 2796))
            cv2.imwrite('image.png', image)
            st.image(image)
            
            st.success('Your image has been successfully uploaded')
            #create a button to download the image
            download = st.download_button('Download image', data=open('image.png', 'rb').read(), file_name='image.png', mime='image/png')
        
                    
    delete = st.button('Delete image')
    if delete:
        #print all the files in current directory 
        for file in os.listdir():
            print(file)
            #if file ends with .jpg .png .jpeg delete it
            if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                os.remove(file)
                
if option == 'iPhone 6.5 Display':
    picture = st.file_uploader('Upload your picture here', type=['png', 'jpg', 'jpeg'])

    if picture:
        #download picture
        with open(picture.name, 'wb') as f:
            f.write(picture.getbuffer())
            #resize image to 1240x1240
            image = cv2.imread(picture.name)
            print(picture.name)
            image = cv2.resize(image, (1242, 2688))
            cv2.imwrite('image.png', image)
            st.image(image)
            
            st.success('Your image has been successfully uploaded')
            #create a button to download the image
            download = st.download_button('Download image', data=open('image.png', 'rb').read(), file_name='image.png', mime='image/png')
        
                    
    delete = st.button('Delete image')
    if delete:
        #print all the files in current directory 
        for file in os.listdir():
            print(file)
            #if file ends with .jpg .png .jpeg delete it
            if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                os.remove(file)
                
if option == 'iPhone 5.5 Display':
    picture = st.file_uploader('Upload your picture here', type=['png', 'jpg', 'jpeg'])

    if picture:
        #download picture
        with open(picture.name, 'wb') as f:
            f.write(picture.getbuffer())
            #resize image to 1240x1240
            image = cv2.imread(picture.name)
            print(picture.name)
            image = cv2.resize(image, (1242, 2208))
            cv2.imwrite('image.png', image)
            st.image(image)
            
            st.success('Your image has been successfully uploaded')
            #create a button to download the image
            download = st.download_button('Download image', data=open('image.png', 'rb').read(), file_name='image.png', mime='image/png')
        
                    
    delete = st.button('Delete image')
    if delete:
        #print all the files in current directory 
        for file in os.listdir():
            print(file)
            #if file ends with .jpg .png .jpeg delete it
            if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                os.remove(file)
                
if option == 'iPad Pro 12.9':
    picture = st.file_uploader('Upload your picture here', type=['png', 'jpg', 'jpeg'])

    if picture:
        #download picture
        with open(picture.name, 'wb') as f:
            f.write(picture.getbuffer())
            #resize image to 1240x1240
            image = cv2.imread(picture.name)
            print(picture.name)
            image = cv2.resize(image, (2048, 2732))
            cv2.imwrite('image.png', image)
            st.image(image)
            
            st.success('Your image has been successfully uploaded')
            #create a button to download the image
            download = st.download_button('Download image', data=open('image.png', 'rb').read(), file_name='image.png', mime='image/png')
        
                    
    delete = st.button('Delete image')
    if delete:
        #print all the files in current directory 
        for file in os.listdir():
            print(file)
            #if file ends with .jpg .png .jpeg delete it
            if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                os.remove(file)
import face_recognition

image = face_recognition.load_image_file('./img/groups/team2.jpg')
face_location = face_recognition.face_locations(image)


#Array of coords of each face
print(face_location)
print(f'There are {len(face_location)} people in this image')
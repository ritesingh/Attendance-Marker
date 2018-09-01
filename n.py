import face_recognition
import cv2
import pandas as pd
import datetime

video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

ritesh_image = face_recognition.load_image_file("ritesh.jpg")
ritesh_face_encoding = face_recognition.face_encodings(ritesh_image)[0]

akash_image = face_recognition.load_image_file("akash.png")
akash_face_encoding = face_recognition.face_encodings(akash_image)[0]


soumyajit_image = face_recognition.load_image_file("soumyajit.png")
soumyajit_face_encoding = face_recognition.face_encodings(soumyajit_image)[0]


debasish_image = face_recognition.load_image_file("debasish.png")
debasish_face_encoding = face_recognition.face_encodings(debasish_image)[0]

biswarup_image = face_recognition.load_image_file("biswarup.png")
biswarup_face_encoding = face_recognition.face_encodings(biswarup_image)[0]

kamal_image = face_recognition.load_image_file("kamal.png")
kamal_face_encoding = face_recognition.face_encodings(kamal_image)[0]

amit_image = face_recognition.load_image_file("amit.png")
amit_face_encoding = face_recognition.face_encodings(amit_image)[0]

ajitesh_image = face_recognition.load_image_file("ajitesh.png")
ajitesh_face_encoding = face_recognition.face_encodings(ajitesh_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding ,ritesh_face_encoding
    ,akash_face_encoding,soumyajit_face_encoding,debasish_face_encoding,biswarup_face_encoding,
    kamal_face_encoding,amit_face_encoding,ajitesh_face_encoding,
]
known_face_names = [
    "Barack Obama",
    "Joe Biden","Ritesh","Akash","Soumyajit",
    "Debasish","Biswarup","kamal","Amit","Ajitesh"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
d={ "Barack Obama":"A",
    "Joe Biden":"A","Ritesh Singh":"A","Akash Singh":"A","Soumyajit Dutta":"A",
    "Debasish Mondal":"A","Biswarup Bannerji":"A","Kamal Yadav":"A","Amit Sansoya":"A",
    "Sachin Bhandari":"A","Rajesh Chauhan":"A","Piyush Kumar":"A","Taranjot Kaur":"A",
}

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                d[name]="P"


            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

now = datetime.datetime.now()
name=now.strftime("%Y-%m-%d at %H")
df=pd.Series(d)
df.to_csv(name+".csv")

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

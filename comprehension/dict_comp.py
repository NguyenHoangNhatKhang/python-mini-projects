# #new_dict = {new_key:keyvalue for item in list}
# import random
# names = ["alex","beth","caroline","dave","eleanaor","freddies"]
# scores = [1,5,6,8,9,10]
# # student_scores = {student:scores[i] for i,student in enumerate(names) }
# student_scores = {student:score for student,score in zip(names,scores)}
# # student_scores = {names[i]:scores[i] for i in range(len(names))}
# # print(student_scores)

# passed_students = {passed_student:passed_score for passed_student,passed_score in student_scores.items() if passed_score > 3}
# print(passed_students)
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# # print(words)
# result = {word:len(word) for word in words}


# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {day:int(temp_c) *9/5 + 32 for day,temp_c in weather_c.items()}

# print(weather_f)


student_dict = {
    "student":["angela","james","lily"],
    "score":[56,76,98]
}

# for key,value in student_dict.items(): 
#     print({key:value})
import pandas 
student_df = pandas.DataFrame(student_dict)
# for key,value in student_df.items():
    # print(value.student) duyệt theo cột 
# duyệt theo dòng
for index,row in student_df.iterrows():
    print(row.student)
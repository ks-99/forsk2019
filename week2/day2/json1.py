"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json

faculty="""
[{
		"fac1": {
			"First Name": "kunal",
			"Last Name": "Srivastava",
			"Photo": "https://www.pexels.com/photo/nature-red-love-romantic-67636/",
			"Department": "Computer Science",
			"Research Area": ["cs", "ml", "ai"],
			"contact_details": {
				"Phone_no": "9782496329",
				"Email": "kunalsrivastava365@gmail.com"
			}
		}
	},
	{
		"fac2": {
			"First Name": "abhi",
			"Last Name": "Srivastava",
			"Photo": "https://www.pexels.com/photo/nature-red-love-romantic-67636/",
			"Department": "Computer Science",
			"Research Area": ["cs", "ml", "ai"],
			"contact_details": {
				"Phone_no": "9783796329",
				"Email": "kunalsjksastava365@gmail.com"
			}
		}
	}
] 
"""
student="""
[{
		"stu1": {
			"First Name": "kunal_s",
			"Last Name": "Srivastava",
			"Photo": "https://www.pexels.com/photo/nature-red-love-romantic-67636/",
			"Department": "Computer Science",
			"Research Area": ["cs", "ml", "ai"],
			"contact_details": {
				"Phone_no": "97845496329",
				"Email": "kunalsrivastava365@gmail.com"
			}
		}
	},
	{
		"stu2": {
			"First Name": "abcd",
			"Last Name": "Srivastava",
			"Photo": "https://www.pexels.com/photo/nature-red-love-romantic-67636/",
			"Department": "Computer Science",
			"Research Area": ["cs", "ml", "ai"],
			"contact_details": {
				"Phone_no": "92323796329",
				"Email": "kunalsjksastava365@gmail.com"
			}
		}
	}
]
 """
faculty1=json.loads(faculty)
student1=json.loads(student)

new_fac=json.dumps(faculty1)
new_stu=json.dumps(student1)

with open("faculty.json", "w") as write_file:
    json.dump(faculty1, write_file)
with open("student.json", "w") as write_file:
    json.dump(student1, write_file)
  
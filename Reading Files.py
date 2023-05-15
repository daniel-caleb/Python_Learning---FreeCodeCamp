# employee_file = open("names.txt", "r")
#
# for employee in employee_file.readlines():
#     print(employee)
# # print(employee_file.readline())
# #
# # print(employee_file.readlines())
# # print(employee_file.readlines()[1])
# employee_file.close()


# How to open and read / append files
employee_file = open("names.txt", "a")

employee_file.write("Toby - Human Resource")

employee_file.close()
# REMEMBER THAT APPENDING ADDS FILES EVERY TIME YOU RUN. ONE MUST SHOULD BE CAREFUL!!

# How to write into files
employee_file = open("names.txt", "w")

employee_file.write("\n Kelly - Customer Service")

employee_file.close()
# REMEMBER THAT WRITE "W" OVERWRITES A FILE --DELETES ALL THE ENTIRE FILE AND CAN ALSO CREATE A NEW FILE!!


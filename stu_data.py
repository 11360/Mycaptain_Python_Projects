import csv
def write_to_csv(split_stu_info):
    csv_file=open("stu_info.csv","w")
    writer=csv.writer(csv_file)
    if csv_file.tell()==0:
        writer.writerow(["Name","Roll_no","Contact_info","Email_Id"])
        writer.writerow(split_stu_info)
condition=True
stu_num=1
while(condition):
    stu_info=input("Enter student data for student #{} in format(Name Roll_no Contact_number Email_Id): ".format(stu_num))
    print("The inputted info is: "+stu_info)
    split_stu_info=stu_info.split(" ")
    print("\nThe splitted informtion is-\nName:{}\nRoll_no:{}\nContact_info:{}\nEmail_Id:{}\n".format(split_stu_info[0],split_stu_info[1],split_stu_info[2],split_stu_info[3]))
    choice_check=input("Is the entered data right or not (Yes/No): ")
    if choice_check=="Yes":
        write_to_csv(split_stu_info)
        condition_check=input("Print (Yes/No) to add further data: " )
        if condition_check=="Yes":
            condition=True
            stu_num+=1
        elif condition_check=="No":
            condition=False
    elif choice_check=="No":
        print("\nPlease re-enter the values")
          

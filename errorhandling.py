def split_bill(total_amount,num_people):

    try :

       total = float(total_amount)
       people = int(num_people)

       calculate_share = total/people


    except ZeroDivisionError :
        return "Error: Number of people cannot be zero"



    except ValueError :
        return "Error : please provide vaild numeric amounts"

    except TypeError:
        return "Error: Unsupported input type provided."

    
    else :
        return f"Each person owes: ${calculate_share :.2f}"

print(split_bill("120.50","4"))


print(split_bill(100,0))
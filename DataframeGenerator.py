import random

class DataGenerator:
    def __init__(self, num_rows):
        self.num_rows=num_rows
        self.data=[]
    
    def get_id(self):
        if len(self.data):
            l = [x[0] for x in self.data]
            return max(l)+1
        else:
            return 1 # return one if the data is empty
        
    def check_duplicate(self):
        #cannot use recursion as there is no base case and will return NoneType if it cannot reach on unique id
        name, city = self.get_names(), self.get_city()
        unique_id = name + city
        existing_ids = {x[1] + x[2] for x in self.data} #set gets distinct values
        while unique_id in existing_ids:
            name, city = self.get_names(), self.get_city()
            unique_id = name + city
        return (name, city)
        
    def get_names(self):
        first_names=['Rohit', 'Virat', 'Rishabh', 'Hardik', 'Surya', 'Mithali', 'Harmanpreet']
        last_names=['Yadav', 'Bumrah', 'Chahal', 'Jadeja', 'Patel', 'Mandhana', 'Goswami']
        full_name = str(first_names[random.randint(0,len(first_names)-1)] + " " + last_names[random.randint(0,len(last_names)-1)])
        return full_name
        
    def get_city(self):
        city=["Chennai", "Mumbai", "Delhi" , "Hyderabad", "Pune", "Kolkata", "Bangalore"]
        return city[random.randint(0, len(city)-1)]
    
    def get_salary(self):
        return random.randint(100000,1000000)
    
    def get_data(self):
        for i in range(0,self.num_rows):
            name, city = self.check_duplicate()
            salary=self.get_salary()
            id=self.get_id()
            list1=[id, name, city, salary]
            self.data.append(list1)
        return self.data
    
    def __str__(self):
        return(f"Data generator with {self.num_rows} rows")
    
    
class Shark:
    def __init__(self, name, eaten):
        self.name = name
        self.eaten = eaten + 5
        self.eaten = str(eaten)
        with open('class.py') as f:
            read_data = f.read()
            print(read_data)
            f.close()
            
        

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")

    def has_eaten(self):
        print(self.name + ' ate ' + self.eaten + ' swimmers.')

    def len_name(self):
        print(self.name + ' length is ' + str(len(self.name)))

    def get_test(self):
        print(self.name + ' ' + str(testInt()))
        print(self.name + ' ' + str(testString()))
        
def testInt():
    return 3;

def testString():
    return 'three'

def main():
    # Set name of Shark object
    sammy = Shark("Sammy", 5)
    sammy.swim()
    sammy.be_awesome()

    dennis = Shark("Dennis", 5)
    dennis.swim()
    dennis.be_awesome()
    dennis.has_eaten()
    dennis.len_name()
  
    bruce = Shark("Bruce", 3)
    bruce.has_eaten()
    bruce.eaten = '12'
    bruce.has_eaten()
    bruce.len_name()
    bruce.get_test()



    inString='|ABC|123|rpm=123.33|'
    startPos=(inString.find('='))
    print(startPos)
    print(inString[startPos + 1:startPos + 6])
    print(inString.split('|',))
    a=(inString.split('|',))
    print('length of a is: ' + str(len((a[2]))))
    print(a[3])
    print(inString.split('|',)[1])
    

if __name__ == "__main__":
    main()

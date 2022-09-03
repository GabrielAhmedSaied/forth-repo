


class game:
    
    def __init__(self,name) :
        while True:
            print(f'''welcome {name}
            1- even_odd_number
            2- no_dub_words
            3- ent_num
            4- devision_chart
            5- devision
            ''')
            choice =int(input('choose 1 or 2 or 3 or 4 or 5 :')) 
            if choice==1:
                start=int(input('enter start num :'))
                end=int(input('enter end num :'))
                self.even_odd_methods(start,end)
            elif choice==2   :
                sentence=input('enter the sentence')
                self.no_dub_words(sentence)     
            elif choice==3  :  
                self.ent_num()    
            elif choice==4 : 
                self.division_chart()
            elif choice==5:
                self.division()
            play_again=input('enter yes or no ')
            if play_again=='no':
                print('goodbye')
                break
                
            elif play_again == 'yes':
                continue
                        
    def even_odd_methods(self,start,end):
        nums=range(start,end)
        even_nums = []
        odd_nums = []
        for num in nums:
            if num % 2 == 0 :
                even_nums.append(num)
            else :
                odd_nums.append(num)   
            print(even_nums)
            print(odd_nums)      
    def no_dub_words(self,sentence):
        sentence=sentence.split(' ')
        clear_sentence = []
        for word in sentence:
            if word not in clear_sentence:
                clear_sentence.append(word)
        print(clear_sentence)
        print(len(sentence)-len(clear_sentence))  
          
    def ent_num(self):
        number=int(input('enter number:'))
        x=0
        while x<= number:
            print(x)
            x +=1
        else:
            print('all numbers is printed')
        
    def division_chart():
        fNum = int(input('insert the first number:'))
        sNum = int(input('insert the second number:'))
        for num in range(0,fNum):
            if num % sNum ==0:
                print(num)    
    
    def division():
        firstNum = int(input('insert the first number:'))
        secondNum = int(input('insert the second number:'))
        for y in range(0,100):
            if y % firstNum ==0 or y % secondNum ==0 :
                print(y)    
        

u1=game('gabriel')
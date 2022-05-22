
def numbers():
    
    
   while True : 
       arr=[]
       try:
            
            a = int(input("A ədədini daxil edin : "))
            b = int(input("B ədədini daxil edin : ")) 
            
            if a>b:
                print('Daxil edilən dəyərlər tələblərə uyğun deyil')
                
            if a<b:        
                for i in range(a,b):
                    if i%5==0 and i%7!=0:
                        arr.append(i)
                        print(arr) 
                                         
       except ValueError:
            print("Düzgün dəyər daxil edilməyib!")                 
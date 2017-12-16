logo = """

              |
            '.'.'
           -= o =-
            .'.'.
              |
              ,
             / \		
           .'. o'.			
          / 6 s ^.\			
         /.-.o *.-.\			
         `/. '.'9  \`	
        .'6. *  s o '.			
       /.--.s .6 .--.\ 	
       `/ s '. .' * .\`	  
      .' o 6 .` .^ 6 s'.	
     /.---. * ^ o .----.\		
     `/s * `.^ s.' ^ * \`
    .' o , 6 `.' ^ o  6 '.			
   /,-^--,  o ^ * s ,----,\			
   `'-._s.;-,_6_^,-;._o.-'
            |   |
            '---'						
"""

import string, time, console
time.sleep(2)
word = "Merry Christmas!"
amt = len(word)
console.set_font("Menlo",10)
console.set_color(1,0,0)
print logo
time.sleep(2)
print word
time.sleep(4)
console.clear()
banner = """
             _____
           .'~ ~ ~`.
           |  a a  |
           `.  ~  .'
       .----'(>o<)`----.
      ( S             S )
       `---.   o   .---'
            ;  o   :
            ;  o   :
           /        \				
          /    /\    \			
       .-' ~~ /  \ ~~ `-.		
       `.___.'    `.___.'				
"""
time.sleep(2)
print banner
time.sleep(3)
console.set_font("Arial Rounded MT Bold",40)
print "Happy Holidays!"

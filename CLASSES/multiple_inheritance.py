class Grand():
     

    def Moves(self):
      print("Dragon punches huh huh!")

class Master():
    def Mental_moves(self):
       print("I am now big")
  


class GrandMaster(Grand, Master):
   pass


GM = GrandMaster()
GM.Moves()
GM.Mental_moves()
   
 
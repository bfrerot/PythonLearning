class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Middle, Top): # Logicall inheritance path is Bottom==> Middle ==> Top, so should be class Bottom(Middle, Top)
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

    
        
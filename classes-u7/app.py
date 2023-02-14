class TrackableList(list):
    def append(self, __object) -> None:
        print("Append called")
        return super().append(__object)
    
list = TrackableList()

list.append("1")
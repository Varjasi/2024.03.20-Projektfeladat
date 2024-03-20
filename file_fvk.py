def beolvas(filename:str)->list[str]:
    file= open(filename)
    sorok= file.readlines()
    file.close()
    return sorok


def stringSzetszedoToIntList(
        szoveg:str,
        separator=" "):
    
    egysor=szoveg.split(separator)
    return(egysor)
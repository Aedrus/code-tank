# App Entrypoint
import gc

def main():
    var1 = "I"
    var2 = "am"
    var3 = "a"
    var4 = "programmer"
    
    del var1, var2, var3, var4
    gc.collect()
    print(var4)

if __name__ == "__main__":
    main()
# Resten av koden finns på Martins dator

def tabell(gissningar):
    print("Drag #       Drag        Feedback")
    print("----------------------------------")
    for i in range(12, 0, -1):
        print("")
        
        if len(gissningar) >= i:
            print(f"{i}           {gissningar[i][0]}        {gissningar[i][1]}")
        else:
            print(i)

# Test-värden
gissningar = {
    1: ["4623", "feedback"],
    2: ["1230", "feedback"]
}
tabell(gissningar)
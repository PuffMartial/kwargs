def hello(*kwargs):
    print("HALLO", end="")
    for key,value in kwargs.item():
        print(value, end="")

hello(title="Mr", first="puff", middle="psalms" last="marshal" )
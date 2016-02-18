def combine(paramType, end):
    out = open("alldata-"+paramType+".csv", "w")
    header_written = False
    for batch in range(1,end+1):
        for pe in range(4):
            f = open("slimfly7-min-"+paramType+"-10/"+paramType+str(pow(2,batch))+"-"+str(pe)+".txt", "r")
            for line in f:
                if line.startswith("Forced") and not header_written:
                    header_written = True
                    out.write(paramType+",")
                    tokens = line.split(",")
                    del tokens[0]
                    del tokens[4]
                    del tokens[5]
                    del tokens[6]
                    del tokens[6]
                    out.write(",".join(tokens))
                elif not line.startswith("Forced"):
                    tokens = line.split(",")
                    del tokens[0]
                    del tokens[4]
                    del tokens[5]
                    del tokens[6]
                    del tokens[6]
                    out.write(str(pow(2,batch))+",")
                    out.write(",".join(tokens))
            f.close()

    out.close()

combine("batch",7)
combine("gvt",10)

data = "06:30:30"
data = list(map(int, data.split(":")))
hr = data[0]
mm = data[1] // 5
ss = data[2] // 5
lst = []

for a in range(8):
    com = ""
    hrr = 0
    mmm = 0
    sss = 0
    ah = 0
    am = 0
    aas = 0
    match a:
        case 0:
            com += "r"
            ah = 1
                
        case 1:
            com += "g"
            am = 1
                
        case 2:
            com += "b"
            aas = 1
                
        case 3:
            com += "y"
            ah = 1
            am = 1
                
        case 4:
            com += "c"
            am = 1
            aas = 1
                
        case 5:
            com += "m"
            ah = 1
            aas = 1
                
        case 6:
            com += "w"
            ah = 1
            am = 1
            aas = 1
                
        case 7:
            com += "k"
    
    hrr += ah
    mmm += am
    sss += aas
    if hrr > hr or mmm > mm or sss > ss:
        com = com[:-1]
        hrr -= ah
        mmm -= am
        sss -= aas
        continue

    for b in range(8):
        bh = 0
        bm = 0
        bs = 0
        match b:
            case 0:
                com += "r"
                bh = 1
                    
            case 1:
                com += "g"
                bm = 1
                    
            case 2:
                com += "b"
                bs = 1
                    
            case 3:
                com += "y"
                bh = 1
                bm = 1
                    
            case 4:
                com += "c"
                bm = 1
                bs = 1
                    
            case 5:
                com += "m"
                bh = 1
                bs = 1
                    
            case 6:
                com += "w"
                bh = 1
                bm = 1
                bs = 1
                    
            case 7:
                com += "k"
        
        hrr += bh
        mmm += bm
        sss += bs
        if hrr > hr or mmm > mm or sss > ss:
            com = com[:-1]
            hrr -= bh
            mmm -= bm
            sss -= bs
            continue
        
        for c in range(8):
            ch = 0
            cm = 0
            cs = 0
            match c:
                case 0:
                    com += "r"
                    ch = 2
                        
                case 1:
                    com += "g"
                    cm = 2
                        
                case 2:
                    com += "b"
                    cs = 2
                        
                case 3:
                    com += "y"
                    ch = 2
                    cm = 2
                        
                case 4:
                    com += "c"
                    cm = 2
                    cs = 2
                        
                case 5:
                    com += "m"
                    ch = 2
                    cs = 2
                        
                case 6:
                    com += "w"
                    ch = 2
                    cm = 2
                    cs = 2
                        
                case 7:
                    com += "k"
            
            hrr += ch
            mmm += cm
            sss += cs
            if hrr > hr or mmm > mm or sss > ss:
                com = com[:-1]
                hrr -= ch
                mmm -= cm
                sss -= cs
                continue

            for d in range(8):
                dh = 0
                dm = 0
                ds = 0
                match d:
                    case 0:
                        com += "r"
                        dh = 3
                            
                    case 1:
                        com += "g"
                        dm = 3
                            
                    case 2:
                        com += "b"
                        ds = 3
                            
                    case 3:
                        com += "y"
                        dh = 3
                        dm = 3
                            
                    case 4:
                        com += "c"
                        dm = 3
                        ds = 3
                            
                    case 5:
                        com += "m"
                        dh = 3
                        ds = 3
                            
                    case 6:
                        com += "w"
                        dh = 3
                        dm = 3
                        ds = 3
                            
                    case 7:
                        com += "k"
                
                hrr += dh
                mmm += dm
                sss += ds
                if hrr > hr or mmm > mm or sss > ss:
                    com = com[:-1]
                    hrr -= dh
                    mmm -= dm
                    sss -= ds
                    continue
                
                for e in range(8):
                    h = 0
                    m = 0
                    s = 0
                    match e:
                        case 0:
                            com += "r"
                            h = 5
                             
                        case 1:
                            com += "g"
                            m = 5
                             
                        case 2:
                            com += "b"
                            s = 5
                             
                        case 3:
                            com += "y"
                            h = 5
                            m = 5
                             
                        case 4:
                            com += "c"
                            m = 5
                            s = 5
                             
                        case 5:
                            com += "m"
                            h = 5
                            s = 5
                             
                        case 6:
                            com += "w"
                            h = 5
                            m = 5
                            s = 5
                             
                        case 7:
                            com += "k"
                    
                    hrr += h
                    mmm += m
                    sss += s
                    if hrr > hr or mmm > mm or sss > ss:
                        com = com[:-1]
                        hrr -= h
                        mmm -= m
                        sss -= s
                        continue
                    if hrr == hr and mmm == mm and sss == ss:
                        lst.append(com)
                    com = com[:-1]
                    hrr -= h
                    mmm -= m
                    sss -= s
                com = com[:-1]
                hrr -= dh
                mmm -= dm
                sss -= ds
            com = com[:-1]
            hrr -= ch
            mmm -= cm
            sss -= cs
        com = com[:-1]
        hrr -= bh
        mmm -= bm
        sss -= bs
    com = com[:-1]
    hrr -= ah
    mmm -= am
    sss -= aas

lst.sort()
final = " ".join(lst)
print(final)
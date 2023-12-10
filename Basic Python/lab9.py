import doctest

# represents a country population as (number of people, country name)
# number of people > 0
PopulationInfo = tuple[int, str]

#country_info_tuple = (str,int,int)

def count_evens_odds(filename: str) -> dict[str, int]:
    """ returns a dictionary with exactly two key:value pairs
    {'Even': count of even numbers, 'Odd': count of odd numbers}
    >>> count_evens_odds('empty.txt')
    {'Even': 0, 'Odd': 0}
    >>> count_evens_odds('numbers_small.txt')
    {'Even': 6, 'Odd': 8}
    >>> count_evens_odds('numbers.txt')
    {'Even': 50056, 'Odd': 49944}
    """
    #TODO: complete this function
    nums = {'Even': 0,'Odd' : 0}
    file = open(filename, 'r')
    line = file.readline()
    while line != '':
        if int(line) % 2 == 0:
            nums['Even'] +=1
        else:
            nums['Odd'] += 1
        line = file.readline()
    file.close()
    return nums

def get_number_frequencies(filename: str) -> dict[int, int]:
    """ returns a dictionary with counts of all unique numbers found in filename
    and the frequency they occur within filename:
    - Dict[unique number: number of occurances in filename]
    >>> get_number_frequencies('empty.txt')
    {}
    
    >>> get_number_frequencies('numbers_small.txt')
    {865: 2, 771: 5, 633: 1, 200: 5, 866: 1}
    
    >>> get_number_frequencies('numbers.txt')
    {865: 87, 633: 80, 798: 114, 905: 125, 866: 94, 842: 112, 793: 98, 771: 96, 200: 90, 701: 100, 861: 123, 510: 100, 158: 95, 985: 97, 573: 104, 575: 86, 435: 95, 645: 104, 478: 104, 403: 114, 227: 112, 122: 103, 294: 103, 914: 96, 368: 112, 605: 105, 163: 92, 297: 88, 770: 112, 111: 117, 363: 94, 105: 105, 713: 94, 57: 86, 12: 91, 306: 96, 582: 106, 869: 99, 494: 106, 930: 109, 524: 96, 355: 110, 38: 92, 378: 97, 653: 95, 891: 100, 509: 90, 523: 104, 452: 104, 253: 108, 339: 93, 941: 115, 67: 96, 391: 95, 99: 99, 958: 90, 920: 99, 347: 108, 323: 108, 949: 121, 169: 80, 706: 110, 858: 81, 704: 95, 727: 95, 116: 98, 448: 112, 991: 94, 796: 114, 789: 109, 192: 105, 970: 88, 20: 101, 724: 88, 142: 118, 173: 118, 50: 100, 763: 105, 370: 116, 975: 110, 287: 95, 386: 96, 69: 93, 89: 109, 245: 96, 304: 90, 656: 117, 167: 98, 1000: 105, 174: 113, 230: 102, 367: 106, 520: 88, 774: 114, 951: 91, 820: 107, 71: 117, 613: 85, 778: 95, 94: 114, 74: 97, 296: 111, 799: 100, 879: 99, 170: 115, 251: 95, 258: 112, 224: 109, 271: 90, 604: 99, 480: 69, 358: 106, 97: 99, 92: 92, 691: 107, 332: 88, 1: 102, 447: 108, 649: 95, 537: 97, 16: 89, 697: 90, 683: 111, 936: 106, 9: 86, 779: 92, 84: 119, 402: 106, 617: 98, 628: 116, 759: 111, 927: 107, 441: 91, 629: 100, 880: 94, 345: 105, 45: 105, 154: 76, 551: 109, 232: 109, 564: 94, 204: 99, 4: 105, 114: 98, 851: 92, 654: 112, 657: 104, 968: 92, 95: 102, 658: 100, 599: 88, 850: 88, 288: 109, 938: 93, 91: 106, 203: 109, 752: 91, 966: 96, 885: 113, 516: 118, 333: 101, 963: 91, 285: 110, 453: 100, 517: 77, 146: 99, 58: 115, 109: 112, 214: 105, 609: 102, 147: 90, 606: 84, 263: 102, 295: 111, 73: 107, 823: 102, 372: 109, 196: 107, 33: 87, 25: 96, 767: 94, 898: 104, 948: 97, 533: 96, 504: 114, 426: 104, 115: 107, 901: 117, 775: 104, 871: 87, 160: 108, 627: 108, 438: 116, 758: 106, 900: 93, 950: 92, 804: 96, 351: 99, 133: 93, 455: 104, 856: 103, 707: 95, 317: 108, 470: 96, 572: 103, 104: 96, 54: 96, 637: 108, 128: 82, 195: 103, 640: 129, 268: 103, 342: 102, 928: 99, 878: 76, 847: 103, 616: 83, 837: 103, 838: 92, 693: 121, 36: 111, 626: 118, 139: 100, 984: 99, 303: 88, 780: 92, 15: 102, 239: 96, 477: 118, 688: 101, 877: 88, 300: 110, 335: 97, 423: 119, 979: 103, 409: 107, 886: 92, 559: 103, 893: 108, 560: 96, 17: 102, 954: 89, 385: 100, 353: 94, 310: 93, 548: 100, 792: 91, 916: 101, 277: 121, 957: 120, 555: 84, 60: 106, 157: 91, 165: 104, 10: 104, 207: 101, 721: 101, 666: 102, 590: 106, 689: 82, 694: 106, 406: 91, 149: 102, 59: 102, 791: 103, 569: 117, 825: 101, 515: 104, 622: 103, 318: 99, 863: 104, 280: 101, 545: 92, 868: 103, 744: 94, 567: 95, 944: 91, 603: 83, 508: 93, 327: 111, 266: 93, 561: 103, 236: 112, 574: 91, 379: 112, 246: 107, 874: 83, 6: 96, 28: 95, 641: 110, 276: 111, 264: 106, 395: 114, 731: 105, 47: 95, 772: 84, 790: 96, 708: 91, 924: 95, 981: 110, 762: 105, 357: 100, 437: 97, 462: 94, 369: 81, 32: 109, 241: 110, 915: 103, 126: 102, 876: 94, 375: 86, 746: 101, 684: 87, 40: 112, 747: 112, 206: 108, 434: 121, 737: 81, 238: 108, 902: 104, 855: 94, 557: 93, 741: 99, 715: 80, 359: 96, 887: 85, 812: 97, 63: 122, 857: 120, 211: 92, 352: 90, 624: 101, 250: 90, 79: 119, 286: 114, 278: 98, 646: 103, 907: 113, 316: 97, 986: 103, 179: 97, 912: 100, 996: 90, 217: 113, 308: 105, 185: 96, 42: 103, 558: 85, 929: 96, 81: 114, 735: 109, 695: 122, 487: 107, 389: 93, 425: 105, 983: 100, 321: 107, 733: 108, 144: 100, 53: 100, 870: 106, 639: 102, 484: 122, 670: 100, 699: 95, 749: 106, 845: 101, 7: 96, 233: 91, 361: 96, 186: 107, 151: 118, 655: 87, 593: 113, 408: 109, 98: 120, 382: 118, 446: 98, 14: 94, 800: 99, 680: 114, 322: 108, 189: 111, 311: 105, 465: 114, 110: 123, 919: 101, 23: 103, 718: 97, 117: 121, 743: 88, 797: 106, 166: 112, 665: 85, 685: 116, 648: 108, 400: 100, 281: 96, 168: 86, 910: 110, 30: 112, 143: 113, 601: 92, 882: 91, 298: 110, 130: 116, 782: 98, 420: 93, 589: 111, 305: 102, 895: 84, 101: 112, 77: 98, 507: 74, 765: 105, 760: 89, 894: 99, 538: 120, 570: 107, 283: 103, 859: 112, 751: 99, 314: 95, 940: 122, 90: 108, 982: 108, 344: 86, 155: 107, 501: 108, 785: 102, 191: 102, 973: 105, 911: 111, 598: 114, 457: 97, 993: 104, 897: 94, 786: 100, 489: 89, 292: 109, 220: 103, 615: 98, 324: 98, 612: 103, 265: 94, 55: 95, 275: 115, 781: 99, 223: 93, 836: 100, 644: 109, 376: 104, 808: 104, 953: 116, 676: 113, 315: 109, 784: 93, 675: 117, 460: 102, 814: 105, 137: 112, 267: 116, 674: 100, 807: 97, 407: 106, 215: 106, 202: 97, 580: 106, 662: 93, 248: 95, 841: 104, 862: 90, 829: 116, 410: 113, 769: 113, 925: 97, 884: 103, 86: 106, 594: 75, 933: 81, 530: 112, 738: 98, 243: 110, 716: 92, 396: 85, 208: 84, 832: 94, 209: 89, 634: 89, 795: 110, 413: 114, 709: 85, 125: 94, 103: 104, 661: 100, 788: 104, 720: 109, 750: 90, 908: 113, 302: 106, 132: 107, 974: 88, 343: 95, 571: 119, 123: 113, 87: 130, 822: 100, 272: 102, 566: 103, 183: 82, 947: 100, 608: 103, 18: 94, 997: 118, 56: 109, 62: 99, 621: 90, 964: 103, 138: 91, 282: 90, 164: 98, 906: 99, 68: 109, 422: 110, 182: 99, 565: 101, 987: 92, 764: 100, 307: 88, 134: 113, 150: 104, 980: 108, 889: 81, 969: 103, 394: 95, 499: 111, 398: 111, 835: 88, 816: 118, 135: 90, 112: 100, 505: 98, 412: 95, 525: 95, 810: 111, 430: 84, 190: 97, 881: 90, 26: 90, 888: 90, 194: 106, 692: 108, 48: 90, 923: 91, 469: 114, 44: 92, 817: 97, 776: 95, 249: 97, 140: 108, 257: 105, 393: 90, 630: 103, 261: 93, 492: 119, 496: 117, 931: 104, 131: 84, 710: 101, 839: 89, 219: 103, 371: 92, 172: 106, 801: 93, 120: 81, 988: 98, 729: 99, 424: 86, 212: 94, 890: 92, 864: 106, 549: 83, 11: 98, 592: 105, 935: 98, 473: 108, 100: 90, 811: 108, 390: 99, 338: 96, 711: 109, 348: 87, 228: 97, 643: 90, 591: 99, 754: 93, 222: 95, 917: 101, 959: 91, 442: 111, 113: 113, 436: 101, 726: 99, 892: 111, 635: 105, 419: 94, 583: 104, 22: 114, 768: 105, 539: 98, 34: 90, 381: 90, 75: 105, 85: 109, 831: 107, 631: 90, 429: 99, 490: 111, 596: 105, 990: 95, 512: 109, 8: 117, 529: 96, 918: 102, 677: 75, 610: 99, 96: 94, 328: 105, 840: 118, 301: 101, 416: 113, 171: 96, 360: 96, 454: 96, 198: 91, 755: 108, 458: 92, 552: 94, 313: 100, 581: 91, 377: 98, 921: 87, 899: 100, 384: 101, 531: 95, 118: 101, 904: 90, 440: 101, 244: 97, 72: 97, 349: 96, 826: 119, 210: 104, 734: 81, 226: 113, 614: 106, 88: 125, 740: 106, 242: 108, 225: 85, 698: 100, 896: 103, 218: 107, 290: 81, 415: 101, 459: 93, 563: 101, 943: 104, 503: 92, 961: 91, 284: 120, 161: 102, 651: 119, 76: 102, 262: 94, 270: 89, 474: 99, 625: 96, 577: 89, 414: 92, 19: 105, 875: 107, 745: 111, 872: 94, 13: 89, 254: 92, 37: 95, 471: 92, 719: 100, 756: 116, 650: 99, 255: 106, 586: 97, 205: 91, 989: 102, 51: 97, 31: 113, 942: 95, 331: 110, 544: 90, 291: 81, 802: 107, 748: 104, 46: 96, 175: 97, 356: 108, 972: 95, 860: 79, 761: 90, 777: 103, 497: 100, 136: 92, 830: 98, 237: 121, 757: 94, 362: 96, 145: 109, 334: 88, 678: 78, 669: 101, 652: 100, 550: 99, 805: 105, 439: 103, 229: 99, 451: 102, 240: 94, 526: 93, 485: 105, 703: 91, 702: 103, 330: 111, 29: 100, 159: 100, 668: 76, 231: 88, 588: 90, 49: 98, 443: 97, 197: 107, 690: 96, 27: 103, 513: 98, 483: 91, 148: 68, 421: 110, 528: 101, 815: 96, 636: 98, 346: 98, 542: 82, 844: 79, 742: 93, 937: 79, 482: 109, 647: 107, 998: 115, 388: 92, 466: 108, 976: 97, 642: 130, 65: 103, 506: 98, 722: 113, 184: 105, 500: 96, 93: 102, 803: 111, 554: 107, 401: 104, 849: 100, 461: 103, 411: 101, 127: 121, 833: 94, 518: 103, 821: 101, 909: 82, 35: 103, 999: 85, 730: 101, 329: 110, 632: 96, 221: 113, 498: 108, 679: 114, 962: 113, 611: 89, 433: 96, 687: 102, 843: 97, 216: 103, 467: 95, 374: 91, 106: 94, 867: 92, 108: 94, 809: 108, 269: 96, 725: 102, 623: 94, 24: 86, 52: 102, 320: 94, 956: 96, 794: 98, 945: 92, 312: 86, 5: 87, 846: 89, 978: 97, 671: 94, 834: 99, 193: 104, 827: 106, 405: 101, 992: 98, 783: 95, 80: 93, 955: 106, 602: 93, 934: 96, 366: 90, 325: 88, 960: 101, 536: 101, 540: 111, 39: 97, 156: 94, 279: 112, 519: 101, 556: 122, 994: 95, 476: 82, 187: 104, 995: 88, 336: 103, 107: 83, 495: 102, 201: 102, 199: 95, 3: 88, 82: 95, 21: 98, 464: 90, 511: 121, 522: 102, 578: 97, 773: 106, 686: 101, 234: 86, 119: 97, 256: 99, 819: 134, 828: 96, 488: 102, 579: 92, 162: 107, 41: 97, 712: 89, 682: 116, 527: 110, 129: 105, 502: 103, 259: 93, 427: 96, 491: 107, 659: 95, 638: 97, 562: 97, 486: 99, 965: 91, 883: 106, 66: 99, 952: 94, 853: 77, 607: 105, 913: 99, 78: 93, 364: 94, 180: 111, 354: 110, 380: 94, 600: 108, 584: 98, 181: 101, 663: 96, 319: 88, 736: 93, 340: 89, 597: 85, 326: 106, 121: 92, 178: 101, 418: 112, 428: 104, 595: 108, 543: 117, 534: 95, 824: 97, 723: 115, 576: 93, 493: 101, 213: 95, 673: 101, 141: 90, 449: 88, 667: 101, 787: 105, 532: 93, 373: 88, 681: 95, 399: 88, 177: 93, 341: 97, 299: 70, 43: 100, 618: 98, 922: 104, 397: 94, 337: 102, 587: 103, 432: 91, 365: 100, 387: 86, 383: 88, 188: 106, 456: 111, 124: 91, 468: 110, 521: 107, 450: 98, 753: 105, 971: 101, 514: 90, 541: 105, 289: 95, 404: 104, 535: 98, 696: 90, 463: 87, 70: 108, 547: 100, 2: 102, 417: 96, 705: 77, 444: 93, 176: 107, 848: 116, 732: 94, 932: 81, 873: 76, 64: 95, 83: 98, 293: 88, 620: 87, 619: 99, 967: 102, 903: 82, 806: 84, 672: 92, 813: 105, 700: 103, 714: 91, 568: 102, 481: 87, 431: 85, 766: 80, 728: 110, 445: 80, 102: 92, 274: 88, 479: 97, 660: 119, 585: 79, 946: 107, 235: 84, 475: 99, 852: 93, 252: 107, 739: 102, 61: 86, 818: 113, 664: 102, 977: 117, 717: 95, 309: 111, 273: 107, 153: 96, 926: 107, 260: 90, 553: 84, 350: 97, 546: 100, 152: 78, 392: 118, 472: 89, 854: 92, 247: 102, 939: 90}
    """    
    #TODO: complete this function
    nums = {}
    file = open(filename, 'r')
    line = file.readline()
    while line != '':
        line = line.strip()
        line = int(line)
        if line not in nums:
            nums[line] = 0
        nums[line] +=1
        line = file.readline()
    file.close()
    return nums    

def most_freq_number(filename: str) -> list[int]:
    """ returns a sorted list of the numbers in filename 
    that have the highest frequency. 
    >>> most_freq_number('empty.txt')
    []
    >>> most_freq_number('numbers_small.txt')
    [200, 771]
    >>> most_freq_number('numbers.txt')
    [819]
    """
    #TODO: complete this function
    # NOTE: you can call the previous function to create a dictionary of 
    # numbers to frequencies but...
    # to solve this problem you need to find the highest frequency number
    # requiring you to consider ALL key: value pairs in the dictionary.
    # The exercise demonstrates that dictionary lookups won't solve all problems.
    nums = get_number_frequencies(filename)
    unique_nums = []
    num_frequency = []
    items = nums.items()
    most_frequent = []
    biggest = 0
    result_list = []
    if nums != {}:
        for index in items:
            unique_nums.append(index[0]), num_frequency.append(index[1]) 
        for index in range(1,len(num_frequency)):
            if num_frequency[index] > num_frequency[biggest]:
                biggest = index       
        most_frequent.append(biggest)
        for index in range(len(num_frequency)):
            if num_frequency[index] == num_frequency[biggest] and index not in most_frequent:
                most_frequent.append(index) 
        most_frequent.sort()
        for index in range(len(most_frequent)):
            spot = most_frequent[index]
            result_list.append(unique_nums[spot])
        result_list.sort()
    return result_list      
def create_population_dictionaries(filename: str, granularity: int) -> (dict[str, int], dict[int, list[str]]):
    """ read population counts from filename into dictionaries:
    - Dict[country name: population]
    - Dict[population granularity: country names with this population granularity]
    Returns the 2 dictionaries as a tuple.
    
    Precondition: assumes filename contains only one entry for each country
    >>> create_population_dictionaries('empty.txt', 10000)
    ({}, {})
    >>> create_population_dictionaries('populations_small.csv', 10000)
    ({'St. Martin (French part)': 31949, 'Nauru': 13049, 'Palau': 21503, 'British Virgin Islands': 30661, 'San Marino': 33203, 'Gibraltar': 34408, 'Monaco': 38499, 'Turks and Caicos Islands': 34900, 'Liechtenstein': 37666}, {3: ['St. Martin (French part)', 'British Virgin Islands', 'San Marino', 'Gibraltar', 'Monaco', 'Turks and Caicos Islands', 'Liechtenstein'], 1: ['Nauru'], 2: ['Palau']})
    >>> create_population_dictionaries('populations_small.csv', 1000)
    ({'St. Martin (French part)': 31949, 'Nauru': 13049, 'Palau': 21503, 'British Virgin Islands': 30661, 'San Marino': 33203, 'Gibraltar': 34408, 'Monaco': 38499, 'Turks and Caicos Islands': 34900, 'Liechtenstein': 37666}, {31: ['St. Martin (French part)'], 13: ['Nauru'], 21: ['Palau'], 30: ['British Virgin Islands'], 33: ['San Marino'], 34: ['Gibraltar', 'Turks and Caicos Islands'], 38: ['Monaco'], 37: ['Liechtenstein']})
    """
    #TODO: complete this function
    # See the Lab PDF for tips on implementing this function
    name_pop_info = {}
    name_pop_gran_info = {}
    country_info = []
    result_list = []
    file= open(filename,'r')
    for index in file:
        info = index.split(',')
        info[-1] = int(info[-1].rstrip('\n'))
        info.append(info[1]//granularity)
        country_info.append(tuple(info))
    for country_info_tuple in country_info:
        name_pop_info[country_info_tuple[0]] = country_info_tuple[1]     
        if country_info_tuple[2] not in name_pop_gran_info:
            name_pop_gran_info[country_info_tuple[2]] = [country_info_tuple[0]]
        else:
            name_pop_gran_info[country_info_tuple[2]].append(country_info_tuple[0])
    file.close()
    result_list.append(name_pop_info)
    result_list.append(name_pop_gran_info) 
    return tuple(result_list)

    
def population_analysis(filename: str, country: str, granularity: int) -> list[PopulationInfo]:
    """  given the population counts in filename, calculates
    the population bin of the given country using the given granularity. 
    Creates a returns a sorted list of PopulationInfo for all countries 
    in the same population bin as the given country.
    
    Precondition: coutry must be in english with correct capitalization
    >>> population_analysis('empty.txt', 'Canada', 1000)
    []
    >>> population_analysis('populations_small.csv', 'Canada', 1000)
    []
    >>> population_analysis('populations_small.csv', 'monaco', 1000)
    []
    >>> population_analysis('populations_small.csv', 'San Marino', 1000)
    [(33203, 'San Marino')]
    >>> population_analysis('populations_small.csv', 'Monaco', 10000)
    [(30661, 'British Virgin Islands'), (31949, 'St. Martin (French part)'), (33203, 'San Marino'), (34408, 'Gibraltar'), (34900, 'Turks and Caicos Islands'), (37666, 'Liechtenstein'), (38499, 'Monaco')]
    >>> population_analysis('populations.csv', 'Canada', 1000000)
    [(36286425, 'Canada')]
    >>> population_analysis('populations.csv', 'Jamaica', 1000000)
    [(2064845, 'Slovenia'), (2203821, 'Lesotho'), (2250260, 'Botswana'), (2479713, 'Namibia'), (2569804, 'Qatar'), (2872298, 'Lithuania'), (2876101, 'Albania'), (2881355, 'Jamaica'), (2924816, 'Armenia')]
    """
    #TODO: complete this function
    # See the Lab PDF for tips on implementing this function
    info = create_population_dictionaries(filename, granularity)
    result_list = []
    desired_countries= []
    result_format = []
    if info != []:          
        info_tuple_list = list(info[1].items())
        for index in range(len(info_tuple_list)):
            if country in info_tuple_list[index][1]:
                for num in range(len(info_tuple_list[index][1])):
                    desired_countries.append(info_tuple_list[index][1][num])
        country_pop_list = list(info[0].items())
        for index in range(len(desired_countries)):
            for num in range(len(country_pop_list)):
                if desired_countries[index] == country_pop_list[num][0] and country_pop_list[num][0] not in result_format:
                    result_format.append(country_pop_list[num][1])
                    result_format.append(country_pop_list[num][0]) 
            result_list.append(tuple(result_format))
            result_format.clear()
        result_list.sort()
    return result_list
def repeat(s, exclaim): 
    s = s*3
    if exclaim: 
        s=s+"!"
    return s
def main(): 
    print repeat("Yay", False)
    print repeat("Woo", True)
if __name__ == '__main__':
    main()
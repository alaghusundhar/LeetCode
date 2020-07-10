

def SubstringSearch():
    # Hashmap to store all substrings
    S = dict()

    # Iterate over all the substrings 
    for i in range(len(P)):

        # Boolean array to maintain all 
        # characters encountered so far 
        freq = [False] * 26
        # Variable to maintain the
        # subtill current position 
        s = ""
        for j in range(i, len(P)):

            # Get the position of the 
            # character in the string
            pos = ord(P[j]) - ord('a')
            # Check if the character is
            # encountred 
            if (freq[pos] == True):
                break

            freq[pos] = True
            # Add the current character
            # to the substring 
            s += P[j]
            print (s)
            # Insert subin Hashmap 
            S[s] = 1
            print(S)

    return len(S)


def SubstringSearchSecondApproach(string):
    j=1
    a=set()
    while True:
        for i in range(len(string)-j+1):
            a.add(string[i:i+j])
        if j==len(string):
            break
        j+=1
        #string=string[1:]
    return a



# Driver code
S = "bcada"

#print(distinctSubstring(S))
print(substr(S))

# This code is contributed by mohit kumar 29    
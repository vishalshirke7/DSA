def encode(arr):
    start_ptr = 0
    encoded_str = ""
    for i in range(len(arr)):
        if arr[i] == arr[start_ptr]:
            pass
        else:
            encoded_str += arr[start_ptr] + str(i - start_ptr)
            start_ptr = i
    encoded_str += arr[start_ptr] + str(i - start_ptr + 1) 
    return encoded_str

encode(list('hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcac'))
Output = 'h1n1w1n1k1u1e1w1h1s1q1m1g1b2u1q1c1l1j2i1v1s1w1m1d1k1q1t1b1x1i1x1m1v1t1r2b1l1j1p1t1n1s1n1f1w1z1q1f1j1m1a1f1a1d1r2w1s1o1f1s1b1c1n1u1v1q1h1f2b1s1a1q1x1w1p1q1c1a1c1'